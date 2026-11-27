# Review of `04_two_obstructions.md`

This report contains a genuine advance: Conjecture T is refuted by an exact Type III counterexample. The counterexample is particularly valuable because it separates the two mechanisms that had previously been conflated:

- the integer obstruction, where \\(h\ge q+r_1\\);
- a genuinely spectral obstruction, where \\(h\<q+r_1\\), but a finite elementary divisor remains.

I independently checked the displayed \\(n=6\\) example using exact rational arithmetic. The checks give

\\[ \begin{aligned} \operatorname{rank}[C;L_0]&=4,\\\ \operatorname{rank}\mathcal L&=3,\\\ r_1&=4,\\\ h&=6, \end{aligned} \\]

and the algebraic rank equality (5a) holds. The gcd of the \\(6\times6\\) minors of the pencil is

\\[ \boxed{\lambda^2-5\lambda+7}. \\]

Its discriminant is \\(-3\\), so its roots are nonreal. This confirms the reported spectral failure and explains why checking only real values of \\(\lambda\\) would miss it.

There is, however, one important mathematical error in Section II.3, and one substantial opportunity to strengthen Section II.5. The error is in the inference that \\(q+r_1=n\\) forces \\(h=n\\). It does not. I explain this below because it affects the claimed structural explanation of the published example.

My overall assessment: the counterexample and the nullspace geometry are strong results; the two-obstruction framework is the right way to organise the problem, provided the dimension arguments are corrected.

## 1. The counterexample refuting Conjecture T

Your example has

\\[ q=q_0=3,\qquad r_1=4,\qquad h=6,\qquad s=3. \\]

Thus

\\[ k=q_0+r_1-h=1\le s=3. \\]

The integer obstruction disappears, but

\\[ d\_{\rm fin}=2>0, \\]

so (5b) fails.

This is exactly the counterexample needed to refute

\\[ (5b)\iff h\<q_0+r_1 \quad\text{at }q=q_0. \\]

The pencil's maximal-minor gcd gives a particularly concise exact certificate:

\\[ g(\lambda)=\lambda^2-5\lambda+7. \\]

Since this is nonconstant, the pencil loses rank at its complex roots. It is useful to include this polynomial explicitly in the report, rather than only reporting \\(d\_{\rm fin}=2\\).

The example also illustrates an important point about the two obstructions:

\\[ \begin{array}{c|c} \text{Integer obstruction} & h\ge q+r_1\\\ \text{Spectral obstruction} & h\<q+r_1,\quad d\_{\rm fin}>0 \end{array} \\]

The second row is no longer hypothetical. It has an exact rational witness.&#x20;

04_two_obstructions.md



One wording qualification: the report says Type III failures are common once \\(A\\) has repeated eigenvalues or Jordan structure. The 17/45 experiment supports the observation that they occur in the tested structured family. It does not yet establish that repeated eigenvalues or Jordan structure cause them, or that they are necessary. I would say “frequently observed in the tested structured families” rather than “common once \\(A\\) has…”.

## 2. Q1 — Is this phenomenon known in the literature?

There is a very relevant result in the 2026 preprint by Tyrone Fernando, Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger.

That paper gives a complete order-by-order characterization and explicitly exhibits an example with

\\[ q_0=3,\qquad q\_{\min}=5. \\]

It proves by covering all four Grassmann charts at \\(q=3\\), and all six charts at \\(q=4\\), that no admissible augmentation at either order satisfies the spectral condition. It then constructs a feasible augmentation at \\(q=5\\).&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1



So the general phenomenon

\\[ \text{algebraically minimum-order augmentation exists, but every such augmentation fails spectrally} \\]

is already present in the literature.

However, that does not settle the more specific question raised by your new example:

\\[ \boxed{h\<q_0+r_1,\qquad d\_{\rm fin}>0.} \\]

The preprint establishes spectral infeasibility over the complete families at \\(q_0\\) and \\(q_0+1\\), and describes a rank-related mechanism for its example. But it does not, in the discussion I checked, classify that mechanism using your particular invariant

\\[ h=\operatorname{rank}[\mathcal L;CA;C]. \\]

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1

Therefore I would make the following distinction in your report:

- Known: spectral infeasibility can persist at the minimum algebraic order, and can persist for more than one order.
- New in your current example: an exact minimum-order spectral failure for which the integer obstruction \\(h\ge q_0+r_1\\) is absent.
- Still to compare: whether the preprint's example also has this latter property, or whether its failures are explained by the integer obstruction in your notation.

This last comparison is worth doing. If the preprint's example is Type I at \\(q_0\\), your example supplies a genuinely different mechanism, not merely another example of a known gap.

## 3. Q2 — The identity for \\(h\\)

Your identity is correct:

\\[ \boxed{ h=\dim(\mathcal Z^\perp+W). } \\]

The proof is immediate from

\\[ \mathcal Z^\perp=\operatorname{row}[C;\mathcal L] =\operatorname{row}C+\operatorname{row}\mathcal L \\]

and \\(\operatorname{row}C\subseteq W\\). Thus

\\[ \mathcal Z^\perp+W =\operatorname{row}\mathcal L+W. \\]

It is elementary, but it is conceptually useful because it removes the choice of a particular row basis \\(\mathcal L\\). The value of \\(h\\) is determined by the subspace \\(\mathcal Z\\), once the order and the prescribed functional are fixed.&#x20;

04_two_obstructions.md



I would go one step further. There is a useful interpretation of \\(\delta\\) as the dimension of a kernel of a restriction map. This leads directly to Q4.

Let

\\[ K=\ker C,\qquad N=\dim K=n-p,\qquad U=W/\operatorname{row}C. \\]

Then

\\[ \dim U=a:=r_1-p. \\]

Since \\(\mathcal Z\subseteq K\\), restriction of row functionals gives a linear map

\\[ \rho\_{\mathcal Z}:U\longrightarrow\mathcal Z^\*, \qquad [w]\longmapsto w|\_{\mathcal Z}. \\]

Its kernel consists exactly of those classes represented by vectors in \\(W\cap\mathcal Z^\perp\\). Hence

\\[ \boxed{ \delta=\dim\ker\rho\_{\mathcal Z} =a-\operatorname{rank}\rho\_{\mathcal Z}. } \\]

This is the most useful geometric form of your dimension identity.

It also gives

\\[ h=q+r_1-\delta. \\]

I recommend including this restriction-map formulation in the next report. It makes the integer obstruction a standard rank-deficiency condition.

## 4. Q3 — Is the two-obstruction dichotomy the right organisation?

Yes—with one clarification.

For any fixed full-row-rank algebraically admissible augmentation, there are two possibilities:

Type I:

\\[ \delta=0 \quad\Longleftrightarrow\quad h=q+r_1. \\]

Then the zero-index counting obstruction applies, and (5b) necessarily fails.

Type II:

\\[ \delta\ge1 \quad\Longleftrightarrow\quad h\<q+r_1. \\]

The integer obstruction disappears, but the spectral condition may either hold or fail.

Thus the failure classification is

\\[ \boxed{ \begin{aligned} \text{failure} &= \underbrace{\\{\delta=0\\}}\_{\text{integer obstruction}}\\\ &\quad\cup \underbrace{\\{\delta\ge1,\ d\_{\rm fin}>0\\}}\_{\text{genuine spectral obstruction}}. \end{aligned} } \\]

These sets are disjoint and cover all failures, assuming the stated minimal-index identity.

Your counterexample belongs to the second set:

\\[ \delta=q+r_1-h=7-6=1,\qquad d\_{\rm fin}=2. \\]

This is a good classification because it separates a dimension-counting obstruction from the remaining polynomial-pencil obstruction.

But do not write that \\(\delta\ge1\\) is itself a spectral obstruction. It merely says that the integer obstruction is absent. A candidate with \\(\delta\ge1\\) can be spectrally feasible or spectrally infeasible.

The more informative object is therefore not just the set of \\(\mathcal Z\\) with \\(\delta\ge1\\), but the pair of loci

\\[ \begin{aligned} \mathfrak D\_{\rm int} &=\\{\mathcal Z:\delta(\mathcal Z)=0\\},\\\ \mathfrak D\_{\rm spec} &=\\{\mathcal Z:\delta(\mathcal Z)\ge1,\ d\_{\rm fin}(\mathcal Z)>0\\}, \end{aligned} \\]

restricted to the algebraically admissible family.

That is the natural geometric framework for the rest of the project.

## 5. Q4 — Is the condition \\(\delta\ge1\\) Schubert-type?

Yes. In fact, it can be described as a standard Schubert incidence condition, and this gives a useful codimension formula.

Recall

\\[ K=\ker C,\qquad \dim K=N=n-p, \\]

and let

\\[ U=W/\operatorname{row}C\subseteq K^\*, \qquad \dim U=a=r_1-p. \\]

The annihilator of \\(\mathcal Z\\) inside \\(K^\*\\) is

\\[ T=\mathcal Z^\perp\cap K^\*. \\]

Because \\(\dim\mathcal Z=N-q\\), we have

\\[ \dim T=q. \\]

The restriction-map formula above gives

\\[ \delta=\dim(U\cap T). \\]

Therefore

\\[ \boxed{ \delta\ge1 \iff T\cap U\ne\\{0\\}. } \\]

Now \\(T\\) varies over the Grassmannian

\\[ \operatorname{Gr}(q,K^\*)=\operatorname{Gr}(q,N), \\]

while \\(U\\) is a fixed \\(a\\)-dimensional subspace of \\(K^\*\\).

Thus the set

\\[ \Omega_U = \\{T\in\operatorname{Gr}(q,N):\dim(T\cap U)\ge1\\} \\]

is a Schubert variety: it is the locus of \\(q\\)-planes meeting a fixed \\(a\\)-plane nontrivially.

### Codimension

There are two cases.

If \\(q+a>N\\), the dimension formula for subspaces forces every \\(q\\)-plane \\(T\\) to intersect \\(U\\) nontrivially. Thus

\\[ \delta\ge1 \\]

for every candidate \\(\mathcal Z\\).

If \\(q+a\le N\\), the Schubert variety has codimension

\\[ N-q-a+1. \\]

Substituting \\(N=n-p\\) and \\(a=r_1-p\\), this becomes

\\[ \boxed{ \operatorname{codim}\Omega_U =n-q-r_1+1. } \\]

Equivalently, in terms of

\\[ d=\dim\mathcal Z=n-p-q, \qquad a=r_1-p, \\]

the codimension is

\\[ \boxed{d-a+1.} \\]

The Schubert class, with the usual Grassmannian convention for \\(q\\)-planes in an \\(N\\)-space, is the special Schubert class

\\[ \sigma\_{N-q-a+1}. \\]

This is a genuine structural result, not just an analogy.

### Consequences for your experiments

- If \\(q+r_1>n\\), then \\(\delta\ge1\\) automatically. The integer obstruction is impossible for dimensional reasons.
- If \\(q+r_1=n\\), the integer-obstruction-free locus is a Schubert divisor: it has codimension one in the full Grassmannian.
- If \\(q+r_1\<n\\), the integer-obstruction-free locus has higher codimension and is correspondingly thinner in the full Grassmannian.

This gives a geometric explanation for why the integer obstruction becomes less relevant as \\(q\\) increases.

It also provides a useful baseline for interpreting your sampling results. The algebraically admissible family may be much smaller than the full Grassmannian, so the Schubert codimension alone does not predict the fraction of admissible candidates with \\(\delta\ge1\\). But it tells you what the ambient geometry looks like before imposing (5a).

## 6. Q5 — How should complex eigenvalues be handled?

Your current approach—the gcd of the maximal minors—is the right exact method for the all-complex-\\(\lambda\\) condition.

For a fixed candidate, let

\\[ Q(\lambda)= \begin{bmatrix} \lambda\mathcal L-\mathcal LA\\\CA\\\C \end{bmatrix}, \\]

and let \\(h\\) be its normal rank. Let \\(f_1(\lambda),\ldots,f_t(\lambda)\\) be all its nonzero \\(h\times h\\) minors. Then

\\[ \boxed{ (5b)\iff \gcd(f_1,\ldots,f_t)=1. } \\]

The reason is that the rank drops below \\(h\\) at a complex value \\(\lambda_0\\) exactly when every maximal minor vanishes at \\(\lambda_0\\). Over \\(\mathbb C\\), this is equivalent to the minors having a common nonconstant factor.

For your example,

\\[ g(\lambda)=\lambda^2-5\lambda+7, \\]

whose roots are

\\[ \lambda=\frac{5\pm i\sqrt3}{2}. \\]

So the spectral failure is invisible to a test that only scans real \\(\lambda\\).

The general matrix-pencil framework treats finite eigenvalues over \\(\mathbb C\\), and the relevant literature explicitly defines the spectral condition over the complex field.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1



### Practical recommendation

Keep the gcd test as the primary exact test. It is:

- root-free;
- exact over rational input;
- independent of numerical eigenvalue approximations;
- naturally compatible with your Toeplitz nullity test.

For real rational input, the gcd can be computed in \\(\mathbb Q[\lambda]\\). A nonconstant polynomial over \\(\mathbb Q\\) has a complex root, whether or not it has a real root. Thus there is no need to compute the roots to decide (5b).

If the problem later changes to a restricted spectral region—for example, requiring rank constancy only in the closed right half-plane—then the gcd alone will detect common roots but will not determine whether they lie in the forbidden region. That is a different problem requiring a root-location test.

## 7. Q6 — What should be the main research line now?

I would make the main objective:

\\[ \boxed{ \text{Characterise the smallest }k\ge0 \text{ for which an order-}(q_0+k)\text{ augmentation satisfies (5b).} } \\]

The two-obstruction framework should become the main structural tool for this objective, rather than replacing it.

There are good reasons for this choice.

First, the algebraic minimum \\(q_0\\) is already well understood through functional observability indices. The 2026 preprint establishes the algebraically feasible order interval

\\[ q_0\le q\le n_0-p \\]

under functional observability, and gives a complete fixed-order nullspace characterisation.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv+1



Second, the joint algebraic-spectral feasible orders need not form an interval. The preprint explicitly warns that algebraic feasibility at consecutive orders does not imply corresponding monotonicity of joint feasibility.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



Third, your new invariant \\(\delta\\) provides a useful first-stage filter:

\\[ \delta=0\quad\Longrightarrow\quad\text{spectral failure}. \\]

But the counterexample proves that the surviving candidates still require a genuine spectral test.

I suggest organising the problem at each order \\(q\\) as follows:

1. Determine the algebraically admissible nullspaces \\(\mathcal Z\\).
2. Compute \\(\delta(\mathcal Z)\\).
3. Discard every candidate with \\(\delta=0\\).
4. On the remaining candidates, test the spectral condition.
5. Determine the first order for which at least one candidate passes.

This creates a clean separation between a geometric pre-filter and the spectral feasibility problem.

A potentially important question is whether the spectral-degeneracy locus inside the algebraically admissible family has a describable dimension or algebraic structure. Your Type III example shows that this locus is not simply contained in the integer-obstructed stratum.

I would therefore keep the order-gap problem as the headline research objective, and use the \\(\delta\\)-geometry to explain and accelerate it.

## 8. Q7 — Which results are publishable, and in what order?

Here is my assessment, distinguishing the mathematical strength of a result from its likely novelty.

| Result                             | Assessment                  | What would strengthen it                                                          |
| ---------------------------------- | --------------------------- | --------------------------------------------------------------------------------- |
| Exact Type III counterexample      | Strongest immediate result  | Full exact verification and comparison with the published example                 |
| \\(h=\dim(\mathcal Z^\perp+W)\\)   | Correct but elementary      | Derive the restriction-map and Schubert formulations                              |
| \\(h=n\Rightarrow(5a)\\) automatic | Correct but elementary      | Present as a corollary of the nullspace formulation                               |
| Fixed-candidate Toeplitz criterion | Useful computational result | State the exact construction and prove its equivalence to the gcd test            |
| Reproduced two-order-gap example   | Useful validation           | Prove the structural explanation over the complete admissible family              |
| Two-obstruction classification     | Potentially substantial     | Develop the geometry and quantify the spectral locus within the admissible family |

### My recommended order of presentation

First: the Type III counterexample.

This is the clearest new mathematical finding in the report. It refutes a natural conjecture and demonstrates that the integer obstruction is not sufficient to characterise spectral feasibility.

Include:

- the exact matrices;
- exact verification of (5a);
- \\(h,q_0,r_1,s\\);
- the maximal-minor gcd;
- the nonreal roots;
- agreement with the Toeplitz and nullspace tests.

Second: the geometric identity and Schubert formulation.

The identity for \\(h\\) becomes more valuable when combined with

\\[ \delta=\dim(U\cap T). \\]

That gives a standard geometric interpretation and a codimension formula. This is considerably stronger than merely observing that \\(h\\) depends on \\(\mathcal Z\\).

Third: the automatic algebraic condition when \\(h=n\\).

This is a short but useful corollary:

\\[ h=n \iff \mathcal Z^\perp+W=\mathbb C^n \Longrightarrow \operatorname{row}(\mathcal LA) \subseteq\operatorname{row}(\mathcal L)+W. \\]

It can be included as part of the geometric section.

Fourth: the fixed-candidate computational framework.

The Toeplitz and gcd tests should be presented as exact verification methods, with the nullspace-pencil criterion as an independent formulation. The fact that these are established mathematical tools does not diminish the value of a carefully derived and independently validated implementation, but it does mean the novelty claim should be about the particular reduction and its usefulness, not about inventing the general theory of polynomial matrix pencils.

The two-order-gap example should be used as a benchmark, not presented as a new discovery unless your analysis proves a new structural property of its entire admissible family.

## 9. Two important corrections to the report

These are important enough that I would fix them before continuing the numerical experiments.

### Correction A: Section II.3 does not prove \\(h=n\\)

The report argues that in the published example, at \\(q=4\\),

\\[ q+r_1=n, \\]

and then concludes that

\\[ h=n,\qquad \delta=0. \\]

This implication is invalid.

From your identity,

\\[ h=q+r_1-\delta, \\]

and the fact that \\(h\le n\\), when \\(q+r_1=n\\) we get only

\\[ \delta\ge0. \\]

We do not get \\(\delta=0\\).

Indeed, Q4 shows that when \\(q+r_1=n\\), the set \\(\delta\ge1\\) is a Schubert divisor in the full Grassmannian. It is a genuine, nonempty subset of the ambient parameter space.

So the correct conclusion is:

- \\(q+r_1>n\\): \\(\delta\ge1\\) is forced for every candidate;
- \\(q+r_1=n\\): \\(\delta=0\\) is possible, but \\(\delta\ge1\\) is also possible;
- \\(q+r_1\<n\\): both possibilities are again possible.

Your 2000 random samples at \\(q=4\\) are strong empirical evidence that the admissible family in that particular example lies in the \\(\delta=0\\) stratum. But the ambient dimension argument does not prove it.&#x20;

04_two_obstructions.md



I recommend replacing the claim in II.3 with:

> Since \\(q+r_1=n\\), the integer-obstruction-free locus \\(\delta\ge1\\) is a Schubert divisor in the ambient Grassmannian. The 2000 samples suggest that the algebraically admissible family at \\(q=4\\) is contained in the complementary stratum \\(\delta=0\\). A symbolic proof of this confinement remains open.

This is both correct and mathematically more interesting: it identifies a special geometric restriction imposed by (5a).

### Correction B: Section II.5 appears to contain a stronger error

This one is more consequential.

You define

\\[ X=\mathcal Z^\perp=\operatorname{row}[C;\mathcal L] \\]

and

\\[ G\_{\mathcal Z} =\\{x\in X:xA\in X+W\\} =\ker\varphi. \\]

You correctly observe that

\\[ (5a)\iff \operatorname{row}\mathcal L\subseteq G\_{\mathcal Z}. \\]

But because

\\[ X=\operatorname{row}C+\operatorname{row}\mathcal L \\]

and

\\[ \operatorname{row}C\subseteq G\_{\mathcal Z}, \\]

this is equivalent to

\\[ \boxed{(5a)\iff G\_{\mathcal Z}=X\iff\varphi=0.} \\]

Here is the direct proof. If (5a) holds, then every row \\(\ell\\) of \\(\mathcal L\\) satisfies

\\[ \ell A\in X+W. \\]

For any \\(x\in X\\), write \\(x=c+\ell\\), where \\(c\in\operatorname{row}C\\) and \\(\ell\in\operatorname{row}\mathcal L\\). Then

\\[ xA=cA+\ell A\in W+(X+W)=X+W, \\]

because \\(cA\in\operatorname{row}CA\subseteq W\\). Thus every \\(x\in X\\) belongs to \\(G\_{\mathcal Z}\\), so \\(G\_{\mathcal Z}=X\\).

The converse is immediate.

Consequently,

\\[ \boxed{ (5a)\iff \operatorname{rank}\varphi=0, } \\]

not merely \\(\operatorname{rank}\varphi\le p\\).

Your dimension estimate

\\[ \dim G\_{\mathcal Z}=p+q-\operatorname{rank}\varphi \\]

is correct. But the condition

\\[ \dim G\_{\mathcal Z}\ge q \iff \operatorname{rank}\varphi\le p \\]

is only a weak necessary condition for fitting \\(q\\) rows inside \\(G\_{\mathcal Z}\\). It does not ensure that those rows, together with \\(C\\), span the whole \\((p+q)\\)-dimensional space \\(X\\).

Since the rows of \\(C\\) and \\(\mathcal L\\) must together span \\(X\\), and all of them must belong to \\(G\_{\mathcal Z}\\), the latter space must actually equal \\(X\\).

Implication for the reported experiments: if your code constructs \\(\mathcal L\\) inside \\(G\_{\mathcal Z}\\) and also enforces

\\[ \operatorname{row}[C;\mathcal L]=\mathcal Z^\perp, \\]

then it should find that every such candidate has \\(\varphi=0\\). If it finds candidates with \\(0<\operatorname{rank}\varphi\le p\\), check whether the code is enforcing the full row-space equality or only the weaker dimension condition.

This also reverses the report's conclusion that (5a) depends on the choice of complement for fixed \\(\mathcal Z\\). Under the stated full-rank assumptions, (5a) depends only on \\(\mathcal Z\\). Every complement of \\(\operatorname{row}C\\) in \\(X\\) gives the same answer: either all such complements satisfy (5a), or none do.

That is a potentially useful simplification, but it means the II.5 implementation and its statistics need to be rechecked before being relied upon.&#x20;

04_two_obstructions.md



## 10. My recommended next experiments

I would revise the immediate research plan in light of these corrections.

1. Recheck the Section II.5 code first. For every fixed \\(\mathcal Z\\), compute \\(\operatorname{rank}\varphi\\) exactly. Verify that the code accepts (5a) precisely when this rank is zero.
2. Recompute the 89-instance statistics. In particular, distinguish the number of candidate nullspaces satisfying (5a) from the number satisfying only the weak bound \\(\operatorname{rank}\varphi\le p\\).
3. Prove or disprove the published-example confinement. At \\(q=4\\), determine symbolically whether every algebraically admissible \\(\mathcal Z\\) has \\(\delta=0\\). Do not infer it from \\(q+r_1=n\\).
4. Use the new counterexample as the Type III benchmark. Its gcd\
   \\[\
   \lambda^2-5\lambda+7\
   \\]\
   is an exact certificate of spectral failure, and its \\(\delta=1\\) value is an exact certificate that the integer obstruction is absent.
5. Investigate the spectral locus within the Schubert strata. Once (5a) is correctly characterised, study the spectral condition separately on \\(\delta=0,1,2,\ldots\\).

The last item is particularly promising. It could lead to a structural classification of the spectral failures that remain after the integer obstruction has been removed.

Bottom line: the new counterexample is a real advance, and the Schubert formulation gives the integer obstruction a clean geometric interpretation. But I would not yet regard the 89-instance results or the proposed construction in II.5 as reliable until the \\(\operatorname{rank}\varphi=0\\) issue has been checked. That is the most important task before the next round of experiments.