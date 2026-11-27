# The dimension question restated on the admissible locus, and an inventory of open recommendations

This report does three things: it records a failed attempt at a dimension bound, restates the question correctly,
and asks one question. It also lists which of the earlier recommendations remain open.

---

# Part I. Setting

$K=\ker[C;CA]$, $k=\dim K$, $N_K$ a basis; $H(R)=\mathcal L(R)N_K$, $H_A(R)=\mathcal LA(R)N_K$; $\omega$ fixed;
$\mathscr R$ the reachable linear space of lower-block pairs, of dimension
$$\dim\mathscr R=m\bigl(2k-\dim\ker T\bigr),\qquad m=q-r,$$
where $T(v,w)=v+Aw$ and $\ker T\cong\{w\in K:Aw\in K\}$; the top blocks are fixed by $L_0$.

---

# Part II. A failed attempt, and what it teaches

## II.1 The attempt

Write the bad set as $\phi^{-1}(Z)$, with $\phi(R)=\lambda H(R)-H_A(R)$ linear in $R$ and
$Z=\{M:\operatorname{rank}M<\omega\}$. Pulling back a variety under a linear map does not lower the codimension, so
$$\operatorname{codim}\phi^{-1}(Z)\ \ge\ \operatorname{codim}Z=(q-\omega+1)(k-\omega+1).$$
If $q>\omega$ and $k\ge\omega$, this would put $\dim(\text{bad})<\dim\mathscr R$ and hence prove feasibility
whenever $q>\omega$.

## II.2 It is false

The twelve-instance batch computed earlier has $k=q=2$, $r=1$, $\omega=1$ (so $q>\omega$), and
$(q-\omega+1)(k-\omega+1)=4$, yet every instance is infeasible: on the rank-one chart, $(5a)$ forces one parameter
to vanish and the non-invariance determinant is then identically zero.

## II.3 Why

The codimension bound is about the whole reachable space $\mathscr R$. But feasibility is defined only on the
subset where $(5a)$ holds, and $(5a)$ is an additional condition that can cut $\mathscr R$ down drastically — in
the example, to a hyperplane. The bad set can fill that smaller set completely while being a proper subset of
$\mathscr R$.

## II.4 The corrected question

$$\dim\bigl(\text{bad}\cap\{(5a)\}\bigr)\ <\ \dim\{(5a)\}\ ?$$

Everything turns on this. We know the answer can be negative on particular charts (the twelve instances), so the
question is whether it can be *uniformly* negative, or whether (as we now suspect) the two cases
"bad fills the admissible locus" and "bad is proper" both occur in a way that is decidable by ranks.

**Question 1.** Is there a usable description of the admissible locus
$$\{R:(5a)\ \text{holds},\ \operatorname{rank}H(R)=\omega\}$$
as a union of finitely many **affine-linear** pieces? If it is affine-linear, the codimension argument above
applies to it directly and settles the dimension question. If it is not, we would like to know what replaces it.

---

# Part III. Inventory of open recommendations

| Recommendation | Status |
|---|---|
| reduced criterion (L7), independently verified | done |
| closedness of the bad locus | done |
| reduced Bézout system with the correct count $2\omega$ | done |
| fixed-row image, corrected to $\ker(A|_K)=0$ and $K\cap AK=0$ | done |
| decision problem $=$ rank-stratified target, including $\omega=0$ | done |
| left-inverse and generalized-inverse certificates | done |
| central theorem with (B') quadratic | done |
| Stage 1: characterisation of attainable pairs | done |
| Stage 2: minimal hard subfamily | **attempted, not found** (three probes, all negative) |
| Stage 3: encode quadratic constraints | **not started** |
| Stage 4: polynomial many-one reduction | **not started** |
| Lean formalisation of the reduced criterion | **not done** |
| comparison table with seven columns for the paper | **not done** |

**Question 2.** Given that Stage 2 has produced only negative results, is it still the right order to attempt
Stage 3, or should the negative evidence be consolidated into a conjecture (for instance: feasibility is decidable
by rank computations on the admissible locus) and stated as such?

---

# Part IV. What we believe, and what would change our mind

The negative evidence is now of three kinds: the free regime is trivially feasible; the smallest constrained
regime is rigid and easy; and the reachable space is never thin. Together they suggest that the difficulty of
$q1$ is not of the "rare feasible set" kind that NP-hard reductions usually exploit.

What would change our mind: a determinantal family in which the bad set fills the admissible locus for a
*nontrivial* range of $\omega$, forcing infeasibility for reasons that are not visible from ranks alone. The
twelve-instance batch shows this happens at $k=q=2$; we do not know whether it can be made to encode a hard
problem at larger $k$.

**Question 3.** Is the phenomenon in the twelve instances (bad filling the admissible locus because $(5a)$
collapses it) the mechanism behind infeasibility in general? If so, infeasibility would be a rank condition, and
$q1$ would be decidable by ranks — which is the outcome our evidence points to.
