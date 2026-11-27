# The corrected fixed-row image, a self-audit of the chain, and a request on the input model

This report does three things: it corrects the fixed-row lemma that the last audit refuted, it records a
self-audit of every statement in the chain, and it asks for advice on the input model needed before any
complexity statement about the rank strata can be made.

---

# Part I. The corrected fixed-row image

Throughout, $m=q-r$, $K=\ker[C;CA]$, $N_K$ a basis of $K$ (columns), $T:K\oplus K\to\mathbb C^n$ defined by
$$T(v,w)=v+Aw,$$
and $\Theta(R)=(RN_K,\,RAN_K)$ for $R\in\mathbb C^{m\times n}$.

## I.1 The previous statement was false

We claimed $\operatorname{im}\Theta=\operatorname{Hom}(K,\mathbb C^m)^2$ iff $K\cap AK=0$. This is false:
with $A=0$ and $K\ne0$ one has $AK=0$ and $K\cap AK=0$, yet $AN_K=0$, so $RAN_K=0$ for every $R$ and the image
cannot be everything.

## I.2 The correct criterion

**Proposition 1.** $\Theta$ is surjective iff $T$ is injective iff
$$\ker(A|_K)=0\quad\text{and}\quad K\cap AK=0.$$

*Proof.* If $T(v,w)=0$ then $Aw=-v\in K$. Under the two conditions, $Aw\in K\cap AK$ forces $Aw=0$, and
injectivity of $A|_K$ gives $w=0$, hence $v=0$. Conversely, if $T$ is injective, then $Aw=0$ with $w\in K$ gives
$T(0,w)=0$, so $w=0$ and $A|_K$ is injective; and if $v=Aw\in K$ with $w\in K$ then $T(-v,w)=0$, so $v=w=0$.
$\square$

## I.3 The exact image, without hypotheses

**Proposition 2.** For arbitrary $A$ and $K$,
$$\operatorname{im}\Theta=\bigl\{(B_1,B_2):\ B_1v+B_2w=0\ \text{whenever}\ v+Aw=0\bigr\}.$$

*Proof.* If $(B_1,B_2)=\Theta(R)$ then $B_1v+B_2w=R(v+Aw)$, so the condition is necessary. Conversely, the
condition says $\ker T\subseteq\ker B$ for $B(v,w)=B_1v+B_2w$; then $\widetilde R(T(v,w)):=B_1v+B_2w$ is a
well-defined linear map on $\operatorname{im}T=K+AK$, and any linear extension to $\mathbb C^n$ gives an $R$ with
$R|_K=B_1$ and $R\circ A_K=B_2$. $\square$

## I.4 Two quantitative consequences

$$\ker T\cong\{w\in K:\ Aw\in K\},\qquad \dim\ker T=\dim(K\cap A^{-1}K),$$
where $A^{-1}K$ is the preimage; this is **not** $\dim(K\cap AK)$ — the difference is $\ker A\cap K$. Hence the
number of independent compatibility conditions is $m\dim(K\cap A^{-1}K)$, and
$$\dim\operatorname{im}\Theta=m\bigl(2k-\dim(K\cap A^{-1}K)\bigr).$$

**Consequence for the earlier construction.** The explicit example from an earlier report used
$A:e_1\mapsto e_5$, $e_2\mapsto e_6$ on $K=\langle e_1,e_2\rangle$, which **is** injective on $K$; that
construction therefore remains valid, only the stated criterion needed the extra hypothesis.

---

# Part II. Self-audit of the chain

We classify the errors found so far into three kinds, since each has occurred at least once:

1. **counting**: the Bézout system has $2\omega$ equations, not $2\omega-1$;
2. **missing hypothesis**: the fixed-row image needs $\ker(A|_K)=0$ in addition to $K\cap AK=0$;
3. **square-versus-rectangular confusion**: charts by columns, not rows; the criterion is the gcd of all
   $\omega$-minors, not a single determinant; one vanishing minor does not imply a rank drop.

| Statement | Hypotheses | Status | Residual risk |
|---|---|---|---|
| $(5a)\iff\ker H\subseteq\ker H_A$ | $K=\ker(C,CA)$ | machine-checked | none |
| kernel identity (set level) | $(5a)$; $D\subseteq\ker Q(\lambda)$ | machine-checked | low |
| kernel identity (additive form) | — | rank–nullity | low |
| reduced criterion | $\ker H\subseteq\ker H_A$; $\mathbb C$ algebraically closed | verified | none |
| closedness | algebraic dependence of $H,H_A$ on $R$; constant rank | verified | keep the hypothesis in the statement |
| elimination trichotomy | localisation at the chart | verified | localisation details |
| reduced Bézout system | fixed column chart; $U,G$ affine; entries of degree $\omega$ | verified | none |
| fixed-row image | $\ker(A|_K)=0$ and $K\cap AK=0$ | corrected here | awaiting check |
| exact image | none | verified | none |
| decision problem $=$ rank-stratified target | $\omega=0$ included | verified | none |
| real density | nonsingular real point on each component | criterion + one instance | general case unchecked |
| per-layer complexity | input model not fixed | open | high |

Two further points that should be stated explicitly and were not:

1. the identity $\operatorname{rank}P=\operatorname{rank}P_{\mathrm{red}}$ uses $V^{\mathsf T}_{[:,S]}=I_\omega$,
   which presupposes that $U=H_{[:,S]}$ has full column rank; the rank-stratified target must therefore fix $S$
   and state this, otherwise "the gcd" is ambiguous;
2. the claim $\min_R\operatorname{rank}(\mathcal L|_K)=\operatorname{rank}(L_0N_K)$ requires $R$ to range over
   all matrices (in particular $RN_K=0$), and it is only a lower bound, unrelated to feasibility.

---

# Part III. Request: the input model for the stratum-level complexity statements

We have two statements in mind and do not know how to phrase either without an input model:

* on the $\omega=0$ stratum the target pair is the single point $(0,0)$, so membership seems decidable by
  inspection — but the preimage in $R$-space need not be a single point, so "decidable by inspection" is a
  statement about one point and not about the decision problem;
* on the $\omega=1$ stratum the bad condition is a system of quadratic equations in $R$; deciding whether it
  vanishes identically on the stratum looks like linear algebra, but we do not know which decision problem we
  are then solving.

**Question 1.** What is the right input model? We propose: $A,C,L_0$ with rational entries in binary, $q$ in
unary (so that the matrix dimensions are bounded by the input length), $R$ existentially quantified over
$\mathbb Q^{(q-r)\times n}$, the spectral condition required for all $\lambda\in\mathbb C$. Is unary encoding of
$q$ appropriate, or does it distort the problem that the literature studies?

**Question 2.** Under that model, what are the smallest strata-level statements that are both true and
meaningful? We would like to avoid asserting a complexity boundary at $\omega=2$ and equally to avoid stating
trivialities.

**Question 3.** Is there a formulation of the stratum-level question that makes the fixed-row compatibility
conditions (Proposition 2) part of the input rather than an implicit constraint? That is, can the decision
problem be stated as "given the compatibility relations $\ker T\subseteq\ker B$, is there a member of the
compatible family with no finite rank drop?", which would remove the fixed-row discussion from the complexity
statement altogether?

---

# Part IV. Status of the verification list

| Item | Status |
|---|---|
| reduced criterion | verified |
| closedness | verified |
| reduced Bézout system | verified |
| fixed-row image | corrected here, for review |
| decision problem $=$ stratified target | verified |
| per-layer complexity | blocked on the input model |
