# The experimental programme: method, results, and what we got wrong

This report records how we ran the computations, what they returned, and the three methodological failures we
committed. It closes with four questions about the experiments and the next move.

---

# Part I. Setting

$K=\ker[C;CA]$, $k=\dim K$, $N_K$ a basis; $H(R)=\mathcal L(R)N_K$, $H_A(R)=\mathcal LA(R)N_K$; $\omega$ fixed;
admissible locus $\mathcal X_\omega=\{\operatorname{rank}H=\omega,\ \operatorname{rank}[H;H_A]=\omega\}$;
spectral bad locus $\mathcal B_\omega$ = those $R\in\mathcal X_\omega$ for which the pencil drops rank at some finite
$\lambda$. A single pencil is tested by a univariate gcd. The general question, as established earlier, is
$\mathcal X_\omega\setminus\mathcal B_\omega\ne\varnothing$.

The reachable pairs are characterised by the linear compatibility space
$$\{(B_1,B_2):\ B_1Z_1+B_2Z_2=0\},\qquad Z=\begin{bmatrix}Z_1\\Z_2\end{bmatrix}\ \text{a basis of}\ \ker T,$$
with $T(v,w)=v+Aw$ and $\ker T\cong\{w\in K:Aw\in K\}$.

---

# Part II. The experimental programme

## II.1 What we were looking for

Following the suggestion we received, we looked for an observer instance with $k>\omega$ that has a nonempty
admissible locus with at least one component on which the generic gcd is **nonconstant** (a "bad component"),
since such a component would be the natural target for a hardness reduction; and conversely, instances where all
admissible points are good would support a tractability conjecture.

## II.2 Experiment 1: random sampling at $k=2$, $\omega=1$ — succeeded

$n=4$, $p=1$, $q=2$, $r=1$; $C=e_1^{\mathsf T}$; the first row of $A$ equal to $e_4^{\mathsf T}$ (so
$K=\langle e_2,e_3\rangle$); remaining rows random; $R$ enumerated over $\{-1,0,1\}^4$. At $\omega=1$ the spectral
test is the rank criterion $\operatorname{rank}[H\ H_A]=2$.

Over 32 instances: admissible locus empty in 16; **admissible but all bad in 12**; admissible and all good in 2;
**both good and bad points in the same instance in 2**. So bad admissible components do occur, and the
componentwise picture is real rather than formal.

## II.3 Experiment 2: random sampling at $k=3$, $\omega=2$ — failed, and why

Same style at $n=5$, $p=1$, $q=3$, $r=1$, 600 random $R$ per instance: every instance returned **zero admissible
points**. Diagnosis: $H$ is $3\times3$, so $\operatorname{rank}H=2$ is a codimension-one condition, and the kernel
inclusion is a further closed condition; random points in a small integer box essentially never land on them.

**Lesson 1: do not sample a set of positive codimension.** This was already recorded in the project's discipline
notes and we still repeated it.

## II.4 Experiment 3: structured construction at $n=6$, $p=2$ — failed on the wrong region

We switched to constructing points: choose $H=UV$, $H_A=GV$ with $U$ of full column rank and $V$ of full row rank,
then solve for $R$. But the computation showed $\operatorname{rank}[C;CA]=4$, $\dim K=2$, not the intended value.
The reason is structural: $CA$ uses only the first $p$ rows of $A$, so those rows must carry the whole rank
increase; consequently $A(K)\subseteq\ker C$, and since $K\subseteq\ker C$ one gets
$$\dim(AK\cap K)\ \ge\ 2k-(n-p).$$
So the free regime $K\cap AK=0$ requires $n-p\ge2k$. At $k=3$ this forces $n\ge9$ and $p\ge3$.

**Lesson 2: check the dimension condition before constructing.**

## II.5 Experiment 4: structured construction at $n=9$, $p=3$ — succeeded

With $C=[I_3\ 0]$ and $A$ having columns $e_1,e_2,e_3$ in positions $4,5,6$ and $e_4,e_5,e_6$ in positions
$7,8,9$, one has $\operatorname{rank}[C;CA]=6$, $k=3$, $K=\langle e_7,e_8,e_9\rangle$, $K\cap AK=0$: the free
regime. Random full-column-rank $U$ and $G$ with top blocks matched to $L_0$, then solving for $R$ (always
solvable here): of 200 constructions, **125 good and 75 bad**. So this layer has feasible points and the bad locus
is a proper closed subset — consistent with the closedness theorem.

## II.6 Experiments 5–6: the constrained region — not completed

$n=5$, $p=1$, $q=3$, $r=1$ gives $k=3$ and $\dim(K+AK)=4<6$, the constrained region. Two attempts:

* with $L_0=e_2^{\mathsf T}$ the top blocks are $(1,0,0)$ and $(0,1,0)$; rank two together with
  $\operatorname{row}H_A\subseteq\operatorname{row}H$ forces $\operatorname{row}H=\operatorname{span}\{e_1,e_2\}$,
  hence $H_A$ has zero third column, but the compatibility relation $B_2e_3=B_1e_2$ forces that column to equal
  $B_1e_2$; the two are incompatible unless $\operatorname{rank}H\le1$. So **the stratum is empty for that
  $L_0$** — a genuine structural statement, not an experimental failure;
* with $L_0=e_4^{\mathsf T}$ the top blocks are compatible, but the script crashed twice inside a symbolic
  linear-algebra routine (a non-square-matrix error), and replacing our own rank routine with exact Gaussian
  elimination did not remove the crash. The cause was not identified.

**Lesson 3: check that the top blocks are compatible, since otherwise the stratum is empty and the experiment is
meaningless.**

## II.7 What we think the experiments do and do not show

* A constructed admissible point that tests good is a proof that the stratum has feasible points — this is a
  sound one-sided conclusion, and it is what Experiments 1 and 4 provide.
* "Zero admissible points found" is **not** evidence of emptiness: it may mean the layer is empty, the region is
  wrong, or the sampling misses a positive-codimension set (Experiments 2, 3, 5).
* Every "no" conclusion we have accepted came with a structural argument, not from sampling.

---

# Part III. Consolidated structural position

Verified and recorded earlier: the reduced criterion; closedness of the bad locus and the open-or-empty
dichotomy; the reduced Bézout system; the exact fixed-row image and the linear compatibility space; the equality
of the decision problem with the rank-stratified target; the left-inverse and generalized-inverse certificates;
and the central theorem that real feasibility is equivalent to a real system of polynomial size and degree two.

Regions decided:
* fixed $R$: univariate gcd;
* $\omega=0$: trivially feasible;
* $\omega=1$: feasibility is $\operatorname{rank}[H\ H_A]=2$, a rank condition (and this is why the bad components
  of Experiment 1 do not threaten tractability);
* $k=\omega$: an affine family, for which the generic algebraic test applies;
* rank-only criteria fail at $\omega=2$, so genuine algebraic content persists there.

---

# Part IV. Questions

**Question 1.** Are Experiments 1 and 4 methodologically sound as evidence? We regard them as one-sided
certificates only. In particular, in Experiment 1 the twelve "all bad" instances — are they enough to assert the
existence of a bad admissible **component**, or must we further check that the all-bad set contains an open
subset of an irreducible component (rather than being a lower-dimensional closed subset)?

**Question 2.** In Experiment 5 the emptiness of the stratum for $L_0=e_2^{\mathsf T}$ was shown by a short
argument. Is there a general criterion — in terms of $L_0N_K$, $L_0AN_K$ and the compatibility space — for which
$L_0$ make the rank-$\omega$ stratum empty? That would let us choose $L_0$ systematically instead of discovering
emptiness by computation.

**Question 3.** For the constrained region, is the following a sound experimental protocol: (i) test top-block
compatibility first; (ii) parameterise the compatibility space by its linear equations; (iii) construct points
with $\operatorname{rank}H=\omega$ by a rank factorisation; (iv) test the spectral condition by an exact
univariate gcd implemented without any computer-algebra system? We would prefer to hear whether you would add a
step.

**Question 4.** Given that both successful experiments found a proper bad locus and no instance has yet produced an
"all bad with positive-dimensional admissible locus" case at $\omega\ge2$, would you (a) push the constrained
region experiment, (b) move to the componentwise symbolic computation of the generic gcd on each component, or
(c) something we have not considered? We have limited appetite for more failed computations and would rather spend
the next round on whatever you judge most informative.
