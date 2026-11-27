# **Report 109 — Review of the&#x20;**\\(c=2\\)**&#x20;package**

**Overall assessment:** Report 109 makes substantial progress over Report 108. In particular, the elimination of the ambient fibre variable \\(W\\) is a promising structural reduction, and the revised real generic-point criterion addresses an important gap in the earlier argument. The correction to the prescribed-row condition is also properly incorporated.

However, I would not yet regard the package as a complete proof of the \\(c=2\\) polynomial-time theorem. There are two important mathematical issues to resolve:

1. The realizability criterion for \\(\Phi\\) needs an explicit dimension condition, and the resulting parameter space is more restricted than the report's shorthand suggests.
2. The rational primary-component parametrization in II.5 does not cover all real invariant two-planes in the general nonsimple-spectrum case. In particular, it does not justify the claimed general rational chart construction.

The good news is that these issues do not destroy the central elimination idea. The fixed-\\(c=2\\), simple-spectrum result in II.6 appears structurally sound, although its bit-complexity proof still needs to be made explicit.

I will distinguish below between results that I consider correct, results that need qualification, and results that should be revised before being used in a paper.

## **1. The fixed-direction fibre: the correction is now correct**

The revised formulation in II.1(b) is an improvement over Report 108.

Write

\\[ V=D^{\perp\_{K_0}}\oplus W,\qquad W\subseteq K_0^\perp. \\]

The condition \\(V_0\subseteq V\\) splits into two independent conditions:

\\[ P\_{K_0}(V_0)\subseteq D^{\perp\_{K_0}}, \qquad W_0:=P\_{K_0^\perp}(V_0)\subseteq W. \\]

The first is a condition on the base \\(D\\); the second is a condition on the fibre \\(W\\). Thus the prescribed-row-compatible base

\\[ \mathcal B\_{\rm pres} = \left\\{ D\in\mathcal I_c(M): P\_{K_0}(V_0)\subseteq D^{\perp\_{K_0}} \right\\} \\]

is necessary. The additional condition

\\[ W_0\subseteq T_D \\]

is also necessary for the fibre to exist.

For a fixed \\(D\\), the fibre is indeed

\\[ \mathcal F_D^{\rm split} \simeq \operatorname{Gr}(t-w_0,T_D/W_0), \\]

provided all the stated compatibility and dimension conditions hold. In particular,

\\[ w_0\le t\le \dim T_D=(n-k)-r(D). \\]

The dimension formula

\\[ \dim\mathcal F_D^{\rm split} =(t-w_0)\bigl((n-k)-r(D)-t\bigr) \\]

is consistent with the Grassmannian dimension formula.

**Recommendation:** Retain II.1(b), but make the logical dependencies explicit in the theorem statement. I would state the complete equivalence first, then derive the Grassmannian description as a corollary. This makes it harder for a reader to overlook one of the prescribed-row conditions.

## **2. The new elimination theorem: the central idea is correct**

This is the most important new result in Report 109.

Define

\\[ \varphi_w(u)=\langle w,A\_{21}u\rangle, \qquad w\in T_D,\quad u\in K_0, \\]

and

\\[ \Phi(W)=\\{\varphi_w:w\in W\\}. \\]

Since \\(w\in T_D\\) means \\(w\perp A\_{21}D\\), we have

\\[ \varphi_w(d)=0 \qquad(d\in D). \\]

Therefore

\\[ \boxed{\Phi(W)\subseteq D^\circ.} \\]

This part is correct.

### **2.1 Checking the row-space identity and its sign**

The convention in the report is that the rows of \\(H\\) are \\(v^{\mathsf T}N\\), and those of \\(H_A\\) are \\(v^{\mathsf T}AN\\), for row vectors \\(v^{\mathsf T}\\) spanning \\(V\\).

For \\(w\in W\subseteq K_0^\perp\\),

\\[ w^{\mathsf T}N=0. \\]

Thus the \\(W\\)-rows contribute nothing to \\(H\\).

For the corresponding rows of \\(H_A\\),

\\[ w^{\mathsf T}AN = w^{\mathsf T}MN+w^{\mathsf T}A\_{21}N. \\]

The first term vanishes because \\(MN\\) has columns in \\(K_0\\), whereas \\(w\perp K_0\\). The second term is exactly the coordinate row of \\(\varphi_w\\). Hence

\\[ w^{\mathsf T}AN=\varphi_w N. \\]

Consequently, the \\(W\\)-rows of \\(\lambda H-H_A\\) are

\\[ -\varphi_w. \\]

The minus sign does not change the row space, so

\\[ \boxed{ \operatorname{row}(\lambda H-H_A) = \operatorname{row}\bigl(\lambda H_K-(H_A)\_K\bigr) +\Phi(W). } \\]

Thus **II.4(ii) is correct under the stated row convention**, provided the notation \\(\Phi(W)\\) means the coordinate representation of the image subspace in the same \\(K_0^\*\\) coordinates as the rows of \\(H\\) and \\(H_A\\).

I recommend adding one sentence explicitly identifying the coordinate identification \\(K_0^\*\simeq\mathbb R^k\\). That will prevent a possible confusion between a functional and its coordinate row.

### **2.2 The important qualification: realizability needs an exact dimension condition**

The report says that realizability of a prescribed \\(\Phi\\) is a linear condition, namely

\\[ \varphi(W_0)\subseteq\Phi\subseteq\varphi(T_D), \\]

together with dimension bookkeeping.

This is essentially right, but the dimension bookkeeping should be stated explicitly. Otherwise, the corollary is not a complete equivalence.

Let

\\[ T=T_D,\qquad \varphi:T\longrightarrow D^\circ, \qquad K=\ker\varphi, \\]

and let

\\[ \Phi_0=\varphi(W_0). \\]

Assume \\(W_0\subseteq T\\), as required by the fixed-direction fibre.

For a candidate subspace \\(\Phi\\), we seek \\(W\\) satisfying

\\[ W_0\subseteq W\subseteq T,\qquad \dim W=t,\qquad \varphi(W)=\Phi. \\]

The correct criterion is

\\[ \boxed{ \begin{aligned} &\Phi_0\subseteq\Phi\subseteq\varphi(T),\\\ &\dim\Phi-\dim\Phi_0 \le t-w_0\\\ &\hspace{30mm}\le \dim\ker\bar\varphi+\dim\Phi-\dim\Phi_0, \end{aligned}} \\]

where

\\[ \bar\varphi:T/W_0\longrightarrow D^\circ/\Phi_0 \\]

is the induced map.

The reason is simple. We need a subspace

\\[ S=W/W_0\subseteq T/W_0 \\]

of dimension \\(t-w_0\\) whose image under \\(\bar\varphi\\) is exactly

\\[ \Phi/\Phi_0. \\]

Such a subspace exists precisely when its dimension is at least the dimension of the required image and at most the dimension of the full preimage of that image. The latter dimension is

\\[ \dim\ker\bar\varphi+\dim(\Phi/\Phi_0). \\]

This is a linear-algebraic realizability test, so it is algorithmically manageable.

**This condition should be added to the report.** It is not merely cosmetic: it determines which \\(\Phi\\)'s are actually attainable by a \\(t\\)-dimensional \\(W\\).

### **2.3 Does&#x20;**\\(c=2\\)**&#x20;really reduce the fibre to at most one projective line?**

Yes, with an important qualification.

Since

\\[ \dim D^\circ=2, \\]

the possible image dimensions are \\(0,1,2\\). The parameter spaces of subspaces of \\(D^\circ\\) are:

- dimension zero: one point, \\(\Phi=\\{0\\}\\);
- dimension one: \\(\mathbb P(D^\circ)\simeq\mathbb P^1\\);
- dimension two: one point, \\(\Phi=D^\circ\\).

So the unrestricted collection of possible image subspaces has at most one projective-line component.

But the prescribed-row condition imposes

\\[ \Phi_0\subseteq\Phi. \\]

This can shrink the family substantially:

- If \\(\Phi_0=0\\), the line family \\(\mathbb P^1\\) may remain, subject to the realizability inequalities.
- If \\(\dim\Phi_0=1\\), there is only one one-dimensional subspace containing \\(\Phi_0\\), namely \\(\Phi_0\\) itself. The only other possible candidate is \\(D^\circ\\).
- If \\(\dim\Phi_0=2\\), only \\(\Phi=D^\circ\\) is possible.

The image constraint

\\[ \Phi\subseteq\varphi(T_D) \\]

and the dimension inequalities can shrink the family further.

Therefore, the correct conclusion is:

\\[ \boxed{ \text{For }c=2,\text{ the effective }\Phi\text{-space is a subset of } \\{0\\}\cup\mathbb P(D^\circ)\cup\\{D^\circ\\}, } \\]

with the subset determined by \\(W_0\\), \\(t\\), and \\(\varphi(T_D)\\).

It is not necessarily a full projective line, but it has at most one projective-line component. The original Grassmannian fibre may have much larger dimension; the elimination theorem shows that its pencil-feasibility verdict depends only on this much smaller image parameter.

That is a genuinely useful reduction.

## **3. The generic gcd criterion: the Gauss argument is sound, but the hypothesis should be sharpened**

II.3 is a meaningful improvement over Report 108. The key point is to avoid the invalid inference that a nonempty Zariski-open subset automatically contains a real point.

The report now assumes that real points are Zariski dense. Under that assumption, the argument is correct in substance.

There are, however, two technical details to repair.

### **3.1 The coordinate ring need not automatically be a UFD**

The proof says:

\\[ A=F[\mathcal X],\quad\text{a UFD}. \\]

This is true if the chart is an affine space, or an appropriate localization of a polynomial ring. It is not true for an arbitrary irreducible affine variety.

The proof needs to specify the kind of chart being used. A clean version would say:

> Let \\(\mathcal X\\) be an affine rational chart with coordinate ring \\(A=F[x_1,\ldots,x_d]\_S\\), where \\(S\\) is a multiplicative set. Then \\(A\\) is a UFD.

If the actual chart is not of this form, the proof should use a suitable divisibility argument in its coordinate ring or work after passing to a polynomial parametrization.

Once \\(A\\) is a UFD, the Gauss-lemma argument is valid: a primitive gcd over \\(\operatorname{Frac}(A)[\lambda]\\) can be chosen in \\(A[\lambda]\\), and it divides every \\(m_i\\) there.

### **3.2 The full-rank hypothesis is stronger than necessary as written**

The report describes a full-rank point as one where no \\(\lambda\\)-leading coefficient of any \\(m_i\\) vanishes.

That is unnecessarily strong and potentially problematic: some maximal minors may be identically zero, and different minors can have different degrees.

What the proof actually needs is this:

\\[ \boxed{ \text{At }x,\text{ at least one maximal minor has its generic } \lambda\text{-degree.} } \\]

To see why, write

\\[ m_i=Gq_i, \\]

where \\(G\\) is the primitive generic gcd and

\\[ \deg\_\lambda G=d\_{\rm gen}. \\]

If \\(\operatorname{lc}\_\lambda(G)(x)=0\\), then

\\[ \operatorname{lc}\_\lambda(m_i)(x)=0 \\]

for every \\(i\\). Therefore, if at least one minor retains its generic degree at \\(x\\), the leading coefficient of \\(G\\) cannot vanish there. It follows that

\\[ \deg\_\lambda G(x,\lambda)=d\_{\rm gen}, \\]

and \\(G(x,\lambda)\\) divides every specialized minor.

In the pencil setting, a particularly natural sufficient condition is

\\[ \operatorname{rank}H(x)=\omega, \\]

because then at least one maximal minor of

\\[ \lambda H(x)-H_A(x) \\]

has degree \\(\omega\\), assuming the matrix has \\(\omega\\) rows and \\(H(x)\\) has full row rank.

I would therefore replace the current definition with:

> A point \\(x\\) is admissible if the leading coefficient matrix \\(H(x)\\) has rank \\(\omega\\). Equivalently, at least one maximal minor of the pencil has its full generic \\(\lambda\\)-degree \\(\omega\\).

This is closer to the actual mathematical requirement.

### **3.3 The generic-point criterion**

Subject to the UFD/chart condition and the rank condition just described, the theorem

\\[ d\_{\rm gen}=0 \iff \mathcal X\text{ contains a real pencil-feasible point} \\]

is correct if the real points of \\(\mathcal X\\) are Zariski dense and every real point under consideration satisfies the rank condition.

The forward direction uses the nonempty open set on which the gcd has generic degree zero. Real-point density ensures that this open set contains a real point.

The reverse direction follows from the specialization divisibility result.

One further refinement: the statement that the locus where the gcd degree is at least \\(d\\) is closed should be made on a fixed-degree locus, or formulated using homogenized polynomials. Subresultant conditions are straightforward when the degrees of the polynomials being compared are fixed; when leading coefficients vanish, degree drops can complicate the naive statement.

**My recommendation:** Keep the theorem, but separate it into three lemmas:

1. generic gcd divisibility under a UFD hypothesis;
2. specialization degree preservation at full-rank points;
3. real-point existence from Zariski density.

That separation will make the proof much more robust.

## **4. The rational-chart construction in II.5 has a substantive gap**

This is the part I would revise most carefully.

The report proposes using the rational primary decomposition

\\[ K_f=\ker f(M) \\]

for irreducible factors \\(f\in\mathbb Q[t]\\), and then lists:

- \\(\operatorname{Gr}(2,K_f)\\) for \\(\deg f=1\\);
- the image of \\([v]\mapsto\operatorname{span}\\{v,Mv\\}\\) for \\(\deg f=2\\);
- products of projective spaces for pairs of distinct factors.

This is not a complete description of the invariant two-plane variety in general.

### **4.1 The distinction between eigenspaces and generalized primary components**

For a linear factor \\(f(t)=t-a\\),

\\[ K_f=\ker(M-aI) \\]

is the eigenspace, not the full generalized eigenspace.

If \\(M\\) has a nontrivial Jordan block, invariant two-planes can contain generalized eigenvectors and need not lie in \\(K_f\\).

For example, take

\\[ M= \begin{pmatrix} a&1&0\\\ 0&a&1\\\ 0&0&a \end{pmatrix}. \\]

The plane

\\[ D=\operatorname{span}(e_1,e_2) \\]

is invariant, but

\\[ D\not\subseteq\ker(M-aI)=\operatorname{span}(e_1). \\]

Thus it is not represented by \\(\operatorname{Gr}(2,K_f)\\).

This is not a minor exceptional case. It is precisely the Jordan-block issue that II.2 correctly warns about.

If instead \\(K_f\\) is intended to denote the generalized primary component

\\[ \ker f(M)^r \\]

for sufficiently large \\(r\\), then \\(\operatorname{Gr}(2,K_f)\\) is still not the invariant-plane variety: not every two-plane in a generalized primary component is invariant.

### **4.2 Irreducible factors of degree greater than two**

There is a second issue.

Suppose \\(M\\) is rational and has an irreducible cubic factor over \\(\mathbb Q\\) with three real roots. Over \\(\mathbb R\\), the corresponding invariant subspaces include the sums of pairs of real eigenlines. Those planes need not be defined over \\(\mathbb Q\\).

Thus a decomposition over irreducible factors in \\(\mathbb Q[t]\\) does not by itself enumerate all real invariant two-planes. A rational algebraic variety may have real points that are not rational points, and a rational parametrization of some components does not imply that all real components have been covered.

This matters because the algorithm is deciding existence over \\(\mathbb R\\), not merely enumerating rational invariant subspaces.

### **4.3 What I recommend instead**

Separate two different objectives:

**Objective A: a complete geometric description.** Work with the real invariant-subspace variety

\\[ \mathcal I_2(M) = \\{D\in\operatorname{Gr}(2,K_0):M(D)\subseteq D\\}. \\]

It is defined by polynomial equations over \\(\mathbb Q\\), since \\(M\\) is rational. This gives a rational algebraic model of the whole problem without claiming that each real component is individually rationally parametrized.

**Objective B: an effective algorithm.** Stratify this variety according to the possible real Jordan forms of \\(M|\_D\\), or use exact real-algebraic methods on the defining equations. If you want a polynomial-time theorem, you must exploit additional spectral assumptions that make this variety finite or otherwise very simple.

For the current \\(c=2\\) theorem, the second route is preferable: impose simple spectrum and use the finite invariant-plane classification. There is no need to solve the full nonsimple-spectrum parametrization in order to establish the simple-spectrum result.

**Verdict on II.5:** The claim that the primary decomposition gives rational charts for the general invariant two-plane family is not established. The final sentence identifying one remaining open point is too optimistic: the coverage of generalized eigenspaces and of real planes arising from higher-degree irreducible rational factors also needs to be addressed.

## **5. The&#x20;**\\(c=2\\)**, simple-spectrum complexity theorem: plausible and promising**

I agree with the central architecture of II.6.

Under simple spectrum, \\(M\\) is diagonalizable over \\(\mathbb C\\), and the real invariant two-planes are finite in number:

1. spans of two real eigenvectors;
2. real planes associated with a complex-conjugate eigenvalue pair.

The number of such planes is

\\[ \binom{k\_{\mathbb R}}{2} + \\#\\{\text{nonreal conjugate pairs}\\} =O(k^2). \\]

For each \\(D\\), the elimination theorem reduces the effective image parameter to at most one projective line. Thus there are at most two affine charts for a genuinely variable line family, plus the zero- and two-dimensional image cases. This is a constant number of chart types per \\(D\\), not a new factor growing with \\(n\\).

### **5.1 Is&#x20;**\\(\deg_s\le1\\)**&#x20;valid on every reduced-fibre chart?**

The right answer is: **yes, for the projective-line parameterization of&#x20;**\\(\Phi\\)**, provided the row-space representation is chosen correctly.**

Suppose

\\[ \Phi(s)=\operatorname{span}(\phi_0+s\phi_1). \\]

The rows contributed by \\(\Phi(s)\\) can be represented by one row that is affine-linear in \\(s\\). The rows from \\(D^{\perp\_{K_0}}\\) are fixed. Therefore the entries of the resulting pencil matrix are affine-linear in \\(s\\), but more importantly, only one row varies with \\(s\\).

Every maximal minor is multilinear in its rows. Since only one row varies, every maximal minor has degree at most one in \\(s\\):

\\[ \boxed{\deg_s m_i\le1.} \\]

This is stronger than merely saying that every matrix entry has degree at most one; if many rows varied independently, the determinant degree could be larger.

The qualification is that the chart must parameterize the *image line* \\(\Phi\\), not an arbitrary lift \\(W\\). If one parameterizes \\(W\\) directly, several rows can vary and the degree bound need not hold.

The report should state this explicitly. It is the elimination theorem—not a generic property of the original Grassmannian fibre—that gives the degree-one bound.

### **5.2 Does the projective line need to be counted with multiplicity over rank strata?**

No additional multiplicity factor is needed in the simple-spectrum setting, but the rank strata must be handled as separate cases.

For each fixed \\(D\\), the map

\\[ \varphi:T_D\longrightarrow D^\circ \\]

has rank \\(0,1,\\) or \\(2\\). The possible \\(\Phi\\)'s depend on that rank and on \\(\Phi_0\\).

- If \\(\operatorname{rank}\varphi=0\\), only \\(\Phi=0\\) is realizable.
- If \\(\operatorname{rank}\varphi=1\\), the image is one fixed line.
- If \\(\operatorname{rank}\varphi=2\\), the full projective line may be available, subject to prescribed-row and dimension constraints.

These are not multiple copies of the projective line. They are different possibilities for the image map. A clean implementation should compute the rank and the prescribed image \\(\Phi_0\\) for each \\(D\\), then construct only the feasible image-space cases.

Thus the chart count remains

\\[ O(k^2) \\]

up to a fixed constant, provided the algorithm does not redundantly enumerate every \\(W\\) lifting the same \\(\Phi\\).

### **5.3 What is still missing from the polynomial-time proof?**

The sketch is convincing at the geometric level, but it is not yet a complete bit-complexity proof.

It needs to establish:

1. **Exact representation of each&#x20;**\\(D\\)**.** Eigenvalues and eigenvectors may be algebraic rather than rational. The proof must explain how the relevant real invariant planes are represented exactly, including irreducible quadratic factors and their real embeddings.
2. **Polynomial bit growth.** The height of the eigenvalue representations, bases of \\(D\\), bases of \\(D^\perp\\), and induced maps must be bounded polynomially in the input size.
3. **Exact computation of the image map.** The rank of \\(\varphi\\), \\(\Phi_0\\), and the realizability inequalities must be decided exactly.
4. **The one-variable gcd complexity.** For each chart, the algorithm computes a gcd over \\(\mathbb Q(s)[\lambda]\\), or over the appropriate algebraic number field. Its complexity must be bounded in terms of coefficient degrees and heights.
5. **Real-chart validity.** The chosen affine chart must contain real points satisfying the rank and prescribed-row conditions whenever the corresponding image family is feasible.

In particular, “one gcd over \\(\mathbb Q(s)[\lambda]\\)” is not by itself a bit-complexity bound. The coefficient heights and the arithmetic field degree matter.

My current conclusion is:

- The **structural reduction** in II.6 is strong.
- The **polynomial-time claim** is plausible under the stated assumptions.
- The **proof sketch** needs a proper exact-arithmetic complexity lemma before it can be presented as a theorem.

## **6. The general-**\\(c\\)**&#x20;discussion: Q-B is the best next direction**

I agree with the report's assessment that Q-B is the most natural continuation of II.4.

The elimination theorem gives

\\[ \Phi(W)\subseteq D^\circ, \qquad \dim D^\circ=c. \\]

Instead of searching over the original Grassmannian of \\(W\\)'s, one searches over

\\[ \Phi\in\operatorname{Gr}(r,D^\circ), \qquad 0\le r\le c, \\]

subject to realizability.

The maximum dimension of this image-space family is

\\[ \max\_{0\le r\le c}r(c-r) = \left\lfloor\frac{c^2}{4}\right\rfloor. \\]

This is actually a little sharper than the report's coarse \\(O(c^2)\\) bound.

However, Q-B asks for more than reducing the dimension. It asks whether the existence of some \\(\Phi\\) making the pencil full-rank can be replaced by a direct rank or separation condition on the induced map.

That is where a new structural theorem could emerge.

### **6.1 A useful reformulation for Q-B**

For fixed \\(D\\), write the fixed part of the pencil as

\\[ P_D(\lambda)=\lambda H_K-(H_A)\_K. \\]

The full pencil row space is

\\[ \operatorname{row}P_D(\lambda)+\Phi. \\]

The condition

\\[ \operatorname{rank}\bigl(\lambda H-H_A\bigr)=\omega \quad\forall\lambda \\]

is therefore equivalent to

\\[ \boxed{ \dim\bigl(\operatorname{row}P_D(\lambda)+\Phi\bigr)=\omega \quad\forall\lambda. } \\]

Equivalently, if the fixed row space has dimension \\(r_D(\lambda)\\), the image subspace \\(\Phi\\) must contribute exactly the missing dimension:

\\[ \dim\Phi- \dim\bigl(\Phi\cap\operatorname{row}P_D(\lambda)\bigr) = \omega-r_D(\lambda) \quad\forall\lambda. \\]

This formulation may be useful because it isolates the interaction between \\(\Phi\\) and a one-parameter family of fixed row spaces.

It also suggests a possible route to a separation criterion: identify the subspaces of \\(D^\circ\\) that intersect the moving row space too much, and characterize whether an admissible \\(\Phi\\) can avoid all of them.

I would not yet claim this is a rank-only criterion. The condition must hold for every \\(\lambda\\), so the spectral dependence remains essential. But it is a much better starting point than the original \\(W\\)-quantifier.

### **6.2 Suggested order of research**

I would prioritize the questions as follows:

1. **Q-B:** derive a criterion on \\(\Phi\\) using the induced maps and the moving row spaces.
2. **Q-A:** investigate whether the invariant-subspace base can be avoided or compressed after Q-B has simplified the fibre.
3. **Q-C:** investigate reindexing by \\(\dim U\\) as an algorithmic organization, but do not expect it alone to remove the hard invariant-subspace geometry.

The reason is that Q-B acts directly on the new theorem. It is the most likely to produce a genuinely new result, and it may also simplify the base search indirectly.

## **7. A further issue: the unrestricted and split problems must remain visibly separate**

Report 109 correctly distinguishes these problems at the beginning, but the new elimination theorem is specifically a theorem for the \\(K_0\\)-split layer.

That distinction should be maintained throughout the paper.

The decomposition

\\[ V=D^{\perp\_{K_0}}\oplus W \\]

is what makes the \\(W\\)-rows of \\(H\\) vanish and permits the reduction to \\(\Phi(W)\\). Without the split condition, the component of \\(V\\) outside \\(K_0\\) need not be represented by a subspace \\(W\subseteq K_0^\perp\\) independently of its \\(K_0\\)-component. Consequently, the row-space identity in II.4 cannot simply be transferred to the unrestricted problem.

I suggest explicitly labeling the new theorem:

> **Split-layer image reduction theorem.**

Then state that it does not yet eliminate the fibre variable for unrestricted designs. This is important when connecting the \\(c=2\\) paper to the broader minimum-order problem.

## **8. Recommended revisions to Report 109**

Here is how I would revise the report before using it as the basis of the next paper draft.

| Section                  | Assessment                           | Required action                                                                                                                                   |
| ------------------------ | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| II.1(a)                  | Correct                              | Retain; make the dimension and prescribed-row assumptions explicit                                                                                |
| II.1(b)                  | Correct after Report 108 correction  | Retain the base and fibre compatibility conditions                                                                                                |
| II.2                     | Broadly correct, but concise         | State the simple-spectrum case as the main algorithmic classification; avoid implying a complete classification in the multiple-Jordan-block case |
| II.3                     | Correct in principle                 | Specify a UFD chart, sharpen the full-rank hypothesis, and clarify fixed-degree subresultant arguments                                            |
| II.4(i)–(ii)             | Correct under the stated conventions | Retain; explicitly identify the coordinate representation and sign                                                                                |
| II.4 realizability       | Incomplete as written                | Add the exact dimension inequalities for \\(\bar\varphi\\)                                                                                        |
| II.4 \\(c=2\\) reduction | Correct with qualification           | Say “at most one projective-line component,” not that a full \\(\mathbb P^1\\) is always available                                                |
| II.5                     | Not established                      | Replace the claimed general rational chart construction or restrict it to suitable spectral cases                                                 |
| II.6                     | Promising                            | Prove exact arithmetic and bit-complexity bounds                                                                                                  |
| II.7                     | Structural proposal only             | Retain as a research programme, not as a proved generalization                                                                                    |

The most important immediate corrections are II.4 realizability and II.5.

## **9. A stronger theorem hierarchy for the next version**

I would organize the mathematical results around the new elimination theorem rather than around the original Grassmannian fibre.

**Theorem 1 — Split-layer fixed-direction characterization.**

For fixed \\(D\\), characterize all admissible \\(V\\) by

\\[ V=D^{\perp\_{K_0}}\oplus W, \qquad W_0\subseteq W\subseteq T_D, \\]

with the prescribed-row base condition.

**Theorem 2 — Image reduction.**

Define

\\[ \varphi:T_D\to D^\circ. \\]

Prove

\\[ \operatorname{row}(\lambda H-H_A) = \operatorname{row}P_D(\lambda)+\varphi(W). \\]

This is the central structural theorem.

**Theorem 3 — Exact image realizability.**

For a proposed \\(\Phi\\), give necessary and sufficient conditions for the existence of a \\(t\\)-dimensional lift \\(W\\). Include the inequalities involving \\(\ker\bar\varphi\\).

**Theorem 4 — Reduced feasibility criterion.**

Show that the existence of a feasible \\(W\\) is equivalent to the existence of a realizable \\(\Phi\\) satisfying

\\[ \dim\bigl(\operatorname{row}P_D(\lambda)+\Phi\bigr)=\omega \qquad\forall\lambda. \\]

**Theorem 5 — The simple-spectrum&#x20;**\\(c=2\\)**&#x20;algorithm.**

Use the finite invariant-plane base and the at-most-one-projective-line image family to obtain the polynomial-time result, after proving the exact arithmetic bounds.

This hierarchy makes the contribution much clearer: the main innovation is not simply that a Grassmannian has become smaller. It is that the pencil-feasibility condition factors through a low-dimensional linear image.

## **10. Final research priorities**

**Priority 1 — Complete the elimination theorem**

Highest

- Add the exact realizability inequalities.
- State the reduced \\(\Phi\\)-feasibility equivalence precisely.
- Prove the row-space identity in the general matrix notation, not only on a concrete chart.

  **Priority 2 — Finish the&#x20;**\\(c=2\\)**&#x20;algorithm**

  High
- Restrict the base to the simple-spectrum case.
- Give exact algebraic-number representations.
- Establish polynomial bounds for the one-variable gcd calculations.
- Verify all real-chart and rank conditions.

  **Priority 3 — Repair the general base geometry**

  Research extension
- Replace the incomplete rational primary-component parametrization.
- Treat generalized eigenspaces and real invariant planes arising from higher-degree irreducible factors.
- Separate geometric classification from algorithmic enumeration.

  **Priority 4 — Pursue Q-B**

  New theorem direction
- Study the moving row spaces \\(\operatorname{row}P_D(\lambda)\\).
- Characterize which \\(\Phi\\)'s supply the missing rank uniformly in \\(\lambda\\).
- Investigate whether the condition can be expressed through induced maps on \\(T_D/W_0\\).

## **11. Overall conclusion**

My assessment is that Report 109 is a real advance over Report 108. The image reduction

\\[ W\longmapsto\Phi(W)\subseteq D^\circ \\]

is the strongest new result. It identifies a small space through which the entire pencil-feasibility condition factors, and for \\(c=2\\) it reduces the effective fibre search to at most a projective-line family.

I would preserve this result as the centre of the project.

There are two qualifications I would insist on before treating the report as complete:

- **Do not claim that every&#x20;**\\(\Phi\\)**&#x20;satisfying only the inclusion conditions is realizable.** Add the dimension inequalities.
- **Do not use II.5 as a general rational parametrization theorem.** Its treatment of generalized eigenspaces and real invariant planes needs substantial revision.

With those changes, the simple-spectrum \\(c=2\\) algorithm becomes a focused and credible theorem target. I would not broaden its complexity claim to arbitrary multiplicities yet.

The most productive next step is to formalize Theorems 2–4 above as one self-contained result: an exact characterization of the reduced \\(\Phi\\)-feasibility problem, including necessary and sufficient lift conditions. That will establish whether the new reduction is merely a smaller search space or a genuine elimination theorem that can support further complexity results.



109_c2_package.md

109_c2_package.md
