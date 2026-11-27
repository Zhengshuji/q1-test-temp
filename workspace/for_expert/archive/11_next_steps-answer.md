# Overall assessment

This is a substantial improvement over the previous report. In particular, the report now has three results that fit together into a credible paper architecture:

1. An unconditional counting identity that gives an exact geometric description of Type I.
2. A fixed-candidate spectral test reducing (5b) to observability of a \\(q\\)-dimensional pair.
3. A whole-family counterexample showing that counting feasibility and spectral feasibility are genuinely different, now with an explicit order-four witness establishing \\(q\_{\min}=4\\).

My recommendation is to begin writing the paper now, with II.2 and II.5 as the main results and II.3 as a central structural theorem. I would not make a hardness reduction or a general tractability theorem a prerequisite.

There is, however, one point in II.4 that I would not yet present as a theorem: the incidence construction excludes the cases \\(L_0x=0\\) and \\((\lambda I-A)x=0\\). Those are not automatically harmless. I explain this below, because it affects the proposed whole-family covering criterion.

## 1. The main results: what I would retain

### II.2 — the counting identity is strong and ready for the main text

The identity

\\[ h=s_0+q-\dim(R\cap S) \\]

is correct under the stated assumptions. The proof is short and unconditional: \\(C\oplus R=\mathcal Z^\perp\\), \\(L_0\subseteq R\\), and therefore

\\[ (C\oplus R)+S=(C\oplus R)+W. \\]

The intersection identity

\\[ (C\oplus R)\cap S=C\oplus(R\cap S) \\]

then gives the result. The equivalences

\\[ \text{Type I}\iff R\cap W=\\{0\\} \\]

and

\\[ \text{Type I}\iff s_0=r_1+r,\qquad R\cap S=\operatorname{row}L_0 \\]

also follow correctly.&#x20;

11_next_steps.md



I would promote this to a numbered theorem, not leave it as a preparatory observation. It gives both an arithmetic formula and a clean geometric interpretation:

\\[ h=q+r_1-\dim(\pi R\cap\pi W). \\]

The quotient formulation is especially useful because it removes the measured-output subspace \\(C\\) from the intersection calculation.

One wording correction: in II.2, replace “no augmentation at that order, at any order of the instance” with “no augmentation at any admissible order.” The value \\(s_0\\) is fixed for the instance, so the statement is stronger and simpler than the current wording suggests.

### II.3 — the observability reduction is a central result

I checked the argument. Under (5a), choose

\\[ \mathcal LA=\Lambda\mathcal L+G_0C+G_1CA, \qquad H=\begin{pmatrix}\mathcal L\\\CA\\\C\end{pmatrix}. \\]

Then \\(Q\_{\mathcal L}(\lambda)=D(\lambda)H\\), and

\\[ \ker D(\lambda) =\\{(u,0,0):(\lambda I-\Lambda)u=0\\}. \\]

Thus a rank drop occurs exactly when there is \\(x\in V\\) such that

\\[ \mathcal Lx\ne0,\qquad \Lambda\mathcal Lx=\lambda\mathcal Lx. \\]

Consequently, with \\(U=\mathcal L(V)\\) and \\(\ker E=U\\),

\\[ \boxed{ (5b)\iff (E,\Lambda)\text{ is observable} \iff \operatorname{rank} \begin{pmatrix} E\\\E\Lambda\\\ \vdots\\\E\Lambda^{q-1} \end{pmatrix}=q. } \\]

This is more than a computational shortcut. It changes the way one should formulate the spectral part of the problem: instead of treating it as a universal rank condition over \\(\lambda\\), it becomes an ordinary finite-dimensional observability condition.

I would make this a theorem in the main text, immediately after the counting theorem. State explicitly that the choice of \\(\Lambda,G_0,G_1\\) is not canonical, but the truth value of the observability test is independent of the choice because each such test is equivalent to the same condition (5b).

One important qualification: this is a fixed-candidate reduction. It does not by itself solve the global search over \\(\mathcal L\\), since \\(\Lambda\\), \\(E\\), and \\(\mathcal L\\) are coupled design variables.

### II.5 — the counterexample is now much more convincing

The order-four witness fills the gap that previously prevented the conclusion \\(q\_{\min}=4\\). The logic is now complete, provided the three all-parameter certificates are included with enough detail to be independently checked:

- every admissible order-three augmentation fails (5b);
- the displayed order-four augmentation satisfies both (5a) and (5b);
- hence \\(q\_{\min}=4\\).

The fact that the witness has

\\[ h=6\<q+r_1=8 \\]

is particularly important. It demonstrates that the spectral obstruction is not simply the counting obstruction in disguise.&#x20;

11_next_steps.md



I would give the explicit witness in the main text and move the chart-by-chart elimination and Bézout certificates to an appendix or supplementary verification file. The main text should explain what each certificate proves and why the parameter charts cover the entire admissible family.

## 2. A serious qualification needed in II.4

The proportionality idea is promising, but the current covering criterion is not yet justified as written.

There are two separate issues.

### Issue A: the image \\(S\\) need not be projectively closed

You define the incidence set using

\\[ L_0x\ne0,\qquad z=(\lambda I-A)x\ne0, \\]

and then take its image in \\(\mathbb P(K)\\). This makes the domain an open subset of a projective incidence variety. Its image is generally only constructible; it need not be closed.

The projective dimension theorem applies to a projective closed subvariety. It does not say that an arbitrary constructible set \\(S\\) of dimension at least \\(q-r\\) intersects every \\(\mathbb P^{d-1}\\).

For example, a dense open subset of a projective line has dimension one but can miss a specified point. Thus even if

\\[ \dim\overline S\ge q-r, \\]

a particular \\(\mathbb P^{d-1}\\) could meet \\(\overline S\\) only in the boundary \\(\overline S\setminus S\\). Such an intersection does not supply an actual bad line.

Required repair: either prove that the relevant image is closed, or prove that every boundary point introduced by taking the closure also corresponds to a genuine finite-\\(\lambda\\) obstruction. Merely replacing \\(S\\) by \\(\overline S\\) does not repair the covering argument.

### Issue B: the excluded cases need separate treatment

The graph description is valid on the locus \\(u=L_0x\ne0\\), because

\\[ v=L_0Ax=\lambda u \\]

then determines \\(\lambda\\) uniquely. But the incidence construction omits:

1. \\(u\ne0\\) and \\(z=0\\);
2. \\(u=0\\), including the possibility \\(v=0\\).

The first case is not innocuous. If

\\[ x\in V\setminus\\{0\\},\quad Ax=\lambda x,\quad L_0x\ne0, \\]

then \\(x\notin K\\), and hence \\(x\notin\mathcal Z\\) for every admissible \\(\mathcal Z\subseteq K\\). It is a spectral obstruction for every candidate, even though \\(z=0\\) has no projective line \\([z]\\).

The second case is different: if \\(L_0x=0\\), the equation \\(L_0(\lambda I-A)x=0\\) no longer determines \\(\lambda\\). In particular, if also \\(L_0Ax=0\\), it holds for every \\(\lambda\\), and the one-parameter family of possible \\(z\\)'s must be accounted for separately.

These cases may be ruled out by additional hypotheses, or handled by adding separate incidence components. But they cannot simply be discarded from the dimension count.&#x20;

11_next_steps.md



### What I would claim at this stage

I would keep the proportionality locus

\\[ P=\\{x\in V:v\wedge u=0\\} \\]

and the estimate

\\[ \dim(\text{proportionality locus})=\dim V-\varepsilon \\]

as a useful algebraic observation. But I would label the proposed covering criterion conditional until both issues above have been resolved.

This is also consistent with your own caution in II.5: a rational map defined only on an open subset does not automatically give the properness needed for a projective surjectivity argument. The same discipline should be applied to II.4.

## 3. Answers to the six questions

### Q1. Which should come first?

My ranking is:

1. (c) Write up II.2 and II.5 now.
2. Develop II.3 into a complete theorem and include it in the paper.
3. Continue II.4 as a separate geometric investigation.
4. Defer a general \\(\exists\mathbb R\\)-hardness reduction until the structure of the feasible Type III family is better understood.

The reason is strategic. You already have a coherent mathematical story:

- a clean counting identity;
- an independent spectral obstruction;
- a fixed-candidate observability characterization;
- an exact example where all algebraic-minimum-order candidates fail spectrally, but a higher-order candidate succeeds.

That is a paper-sized contribution if the all-parameter proof in II.5 is fully documented. A hardness result would be valuable, but it is not needed to make this contribution mathematically meaningful.

I would not delay writing for a general formula for \\(\varepsilon\\). It is a separate geometric problem, and the current incidence argument needs repair before it can support the claimed covering theorem.

### Q2. Is “no Type III” the right tractability hypothesis?

Yes. I prefer the explicit hypothesis

> Counting-spectral separation: At every admissible order \\(q\\), every augmentation satisfying (5a) and \\(h\<q+r_1\\) also satisfies (5b).

This is exactly “there is no Type III point on the admissible locus,” but it says directly what is needed for the algorithmic consequence.

Under this hypothesis, for each \\(q\\),

\\[ \begin{aligned} &\exists\\,\mathcal L\text{ satisfying (5a) and (5b)}\\\ &\qquad\Longleftrightarrow \exists\\,\mathcal L\text{ satisfying (5a) and }h\<q+r_1. \end{aligned} \\]

The forward implication follows because (5b) requires \\(h\<q+r_1\\); the reverse implication is precisely the hypothesis.

This is a useful proposition, but the polynomial-time conclusion needs an additional qualification. You must show that the existence of an algebraically admissible augmentation with \\(h\<q+r_1\\) can be decided in polynomial time for the input class under consideration. That is not automatic when (5a) restricts the admissible row spaces.

I would therefore separate the statements:

- Proposition: Under counting-spectral separation, the joint feasibility question at each order reduces to the existence of a non-Type-I algebraic augmentation.
- Corollary: If that latter existence question is polynomial-time decidable on a specified input class, then \\(q\_{\min}\\) is polynomial-time computable on that class.

Then give a concrete sufficient structural condition for the second statement. For example, if (5a) is automatic throughout the candidate family, the remaining question is a Grassmannian intersection/extension question and may be decidable by rank calculations. State the exact conditions under which your proposed rank test handles it.

This is stronger mathematically than simply saying “no Type III implies polynomial time,” because it makes the algorithmic assumption visible rather than hiding it inside the hypothesis.

### Q3. Is \\(\varepsilon\\) a familiar invariant? Can it be read from Kronecker data?

I would not expect a standard Kronecker invariant to give \\(\varepsilon\\) by itself.

Let

\\[ U_0=L_0|\_V,\qquad U_1=L_0A|\_V. \\]

For each \\(x\in V\\), form the \\(2\times r\\) matrix

\\[ \Phi(x)= \begin{pmatrix} U_0x\\\ U_1x \end{pmatrix}. \\]

Then

\\[ P=\\{x\in V:\operatorname{rank}\Phi(x)\le1\\}. \\]

Thus \\(P\\) is a determinantal locus, defined by the \\(2\times2\\) minors of a \\(2\times r\\) matrix of linear forms. Equivalently, it is the inverse image of the rank-at-most-one determinantal variety under the linear map

\\[ V\longrightarrow \mathbb C^r\oplus\mathbb C^r, \qquad x\longmapsto (U_0x,U_1x). \\]

So \\(\varepsilon\\) is the codimension of this particular linear section of a determinantal variety. For \\(r=1\\), the minors are absent and \\(\varepsilon=0\\), as your report observes.

This gives a concrete computational route:

1. Construct the ideal\
   \\[\
   I=(v_i u_j-v_j u_i:1\le i\<j\le r)\
   \\]\
   in the coordinate ring of \\(V\\).
2. Compute its dimension, for example using a Gröbner basis or Hilbert polynomial.
3. Obtain \\(\varepsilon=\dim V-\dim P\\), with the convention for the empty projective locus handled explicitly.

But I would distinguish two questions:

- Can \\(\varepsilon\\) be computed from the actual matrices? Yes, by determinantal algebra.
- Can it be read off from the Kronecker data of a restricted pencil? Not from the usual Kronecker data alone, without showing that those data retain the relative position of the two maps \\(U_0,U_1\\).

The reason is that the invariant depends on the joint position of \\(L_0|\_V\\) and \\(L_0A|\_V\\), not merely on dimensions or eigenstructure of an operator. Also, \\(V=\ker[C;CA]\\) need not be \\(A\\)-invariant, so “the restriction of \\(A\\) to \\(V\\)” may not even be an endomorphism of \\(V\\). A compressed map or a pair of maps must be specified before asking for its Kronecker invariants.

My recommendation: call \\(\varepsilon\\) the codimension of the proportionality determinantal locus for now. That is precise and does not imply a standard name that may not exist.

### Q4. Does bilinear/rank structure suggest hardness? Which source problem?

Bilinearity and rank constraints are a reason to investigate \\(\exists\mathbb R\\)-hardness, but they are not a proof of hardness and do not by themselves establish a barrier to polynomial algorithms.

Your encoding is interesting because it has a compact form:

- variables for \\(\mathcal L,\Lambda,G_0,G_1\\);
- a rank stratum for \\(M=\mathcal LV_0\\);
- an annihilator \\(E\\);
- an observability certificate.

This gives an upper bound in \\(\exists\mathbb R\\), subject to the encoding details discussed below. It does not tell us whether the problem is \\(\exists\mathbb R\\)-hard.

I would start with quadratic feasibility / ETR-INV, rather than immediately reducing from a complicated matrix-completion problem. The reason is that your observability interface already has bilinear matrix products. A reduction from a system of quadratic equations could potentially encode multiplication constraints directly into the observer-design variables.

A useful research plan would be:

1. Start with a bounded quadratic feasibility problem, with variables \\(x_i\\) and equations built from \\(x_ix_j\\), linear terms, and constants.
2. Encode the variables as entries of one or more structured matrices.
3. Use bilinear products in the observer equations to represent multiplication gates.
4. Force the required rank and observability properties so that the construction works in both directions.
5. Prove that every feasible observer yields a solution to the original quadratic system, not merely that every original solution produces some feasible observer.

The last point is usually the difficult one. It is easy to embed a multiplication gadget into a matrix equation; it is much harder to prevent unintended observer solutions.

A rank-constrained matrix completion problem is a possible alternative source, especially if you discover that the essential design freedom is the choice of a low-rank factorization. But I would first test the quadratic-feasibility route because it aligns more directly with your bilinear encoding.

### Q5. Has the observability formulation appeared in observer-design literature?

There is substantial overlap in the surrounding theory, but I did not find an exact match for your particular \\(E,\Lambda\\) formulation in the targeted search.

A relevant recent paper is Darouach and Fernando, On functional observability and functional observer design, Automatica 173 (2025), article 112115. It develops functional-observability conditions and observer-design methods, and its discussion includes the familiar algebraic and spectral rank conditions for functional observers.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.sciencedirect.com\&sz=32)

ScienceDirect+1



More importantly, there is a very recent preprint by Tyrone Fernando, Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger (29 September 2026). It studies the same order-by-order problem, including the algebraic and spectral conditions, and gives a nullspace matrix-pencil characterization of the spectral condition. Its Theorem 4 uses the pencil

\\[ \operatorname{rank}\big((\lambda I-A)V\mid Z\big) =\operatorname{rank}(V\mid Z). \\]

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv

That is a significant literature-overlap warning. Before claiming novelty for the overall order-by-order nullspace characterization, you should compare your paper carefully with this preprint. In particular, the report's II.3 is not the first reduction of the spectral condition to a nullspace/pencil test.

However, the observability representation

\\[ \ker E=\mathcal L(V),\qquad (E,\Lambda)\text{ observable} \\]

is a different and potentially useful reformulation. The targeted search found the standard functional-observer and pencil literature, but did not establish that this exact representation has already been published. I would therefore make a restrained novelty claim:

> We derive an equivalent finite-dimensional observability test for the spectral condition of a fixed algebraically admissible augmentation.

Do not claim that the PBH criterion itself is new. PBH observability is classical. The potentially new part is the derivation of the specific pair \\((E,\Lambda)\\) from the augmented functional-observer equations, and the resulting compact existential-real certificate.

I would also include a comparison table in the introduction:

| Approach                      | Spectral condition becomes                     |
| ----------------------------- | ---------------------------------------------- |
| Original observer formulation | Rank condition for every \\(\lambda\\)         |
| Nullspace-pencil formulation  | Rank condition on \\([(\lambda I-A)V\mid Z]\\) |
| Your new formulation          | Observability of \\((E,\Lambda)\\)             |

This makes the relationship and the claimed increment clear.

### Q6. Should you write the paper now?

Yes. I would write now, with the following structure:

1. Problem formulation and order interval.
2. Counting geometry: the unconditional identity and Type I characterization.
3. Spectral geometry for a fixed candidate: the observability reduction.
4. A whole-family counterexample: all order-three algebraic candidates fail, but an order-four candidate succeeds.
5. Computational and formal verification: exact certificates, Lean inventory, and reproducibility details.
6. Open problems: incidence geometry, tractable subclasses, and complexity.

I would not put II.4's covering criterion in the main theorem section until the open-image and excluded-locus issues are repaired. It can appear as a conjectural or conditional geometric direction.

## 4. Two technical corrections to make before freezing the report

### 4.1 Make the observability ETR encoding genuinely quadratic

In II.6, the displayed matrix

\\[ \mathcal O= \begin{pmatrix} E\\\E\Lambda\\\\\vdots\\\E\Lambda^{q-1} \end{pmatrix} \\]

does not have degree at most two in the unknown entries of \\(E,\Lambda\\) if you expand the powers directly. The entries of \\(E\Lambda^k\\) have degree \\(k+1\\).

This is easy to fix, and it is worth doing because it makes the claimed quadratic encoding rigorous.

Introduce auxiliary matrices

\\[ E_0=E,\qquad E\_{j+1}=E_j\Lambda \quad (j=0,\ldots,q-2), \\]

and define

\\[ \widetilde{\mathcal O}= \begin{pmatrix} E_0\\\E_1\\\\\vdots\\\E\_{q-1} \end{pmatrix}. \\]

Now every recurrence is bilinear, and the left-inverse constraint

\\[ Y_O\widetilde{\mathcal O}=I_q \\]

is bilinear as well. All equations have degree at most two.

The number of auxiliary entries is \\(O(q^3)\\), so the polynomial-size claim remains plausible. Make this recurrence explicit in the report and in the formal encoding.

### 4.2 State the complexity model precisely

When you say “polynomial time” or “polynomial-size \\(\exists\mathbb R\\) encoding,” specify:

- whether the input matrices are rational, real algebraic, or arbitrary complex numbers;
- whether bit complexity or arithmetic-operation complexity is intended;
- how complex variables and coefficients are represented;
- whether the rank-stratum disjunction is counted as part of the formula size.

For rational input, splitting complex variables into real and imaginary parts gives a real existential formula. The rank conditions can be represented by factorization and inverse-witness equations, as you describe. But the polynomial-size claim should explicitly account for the auxiliary recurrences above.

Your conclusion that this is an upper bound rather than an algorithm is exactly right.&#x20;

11_next_steps.md



## 5. Concrete next steps

I would assign the next work in this order:

1. Freeze II.2: write the theorem and its short proof, including the quotient-space interpretation.
2. Freeze II.3: write the observability theorem, with all dimensions and the independence of the factorization choice stated explicitly.
3. Finish II.5's certificate package: publish the order-three all-parameter infeasibility proof and the exact order-four witness together.
4. Repair II.6: add the recurrence variables \\(E_j\\) and give the exact formula-size accounting.
5. Audit II.4: split off the \\(L_0x=0\\) and \\(z=0\\) loci, then address the nonclosed-image problem before using projective dimension theory.
6. Do a careful comparison with Fernando's September 2026 preprint and the 2025 functional-observability paper, so that the paper's novelty claim is precise.

The central message of the report is now strong: the counting obstruction is completely characterized by a simple subspace-intersection identity, whereas the remaining obstruction is genuinely spectral and admits a finite-dimensional observability representation. That distinction is the paper's most coherent organizing idea.