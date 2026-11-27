# The hyperplane layer of the prescribed-row problem: a deterministic criterion, and the question of its cost

This note reports one structural step and asks three questions. The step removes a sub-goal that we
now believe was unnecessary; the questions are about the cost of what remains, and about whether a
known structural theorem can replace it. As before, the motivation is the decision complexity of the
chart-times-semialgebraic feasibility problem, not the characterisation, which the literature already
provides.

---

## Part I. Setting, compressed to what the questions need

Let $A\in\mathbb Q^{n\times n}$, $C\in\mathbb Q^{p\times n}$ ($\operatorname{rank}C=p$),
$L_0\in\mathbb Q^{r_0\times n}$, and $q$ a candidate order. Put
$$
K_0=\ker[C;CA],\quad k=\dim K_0,\quad H=LN,\quad H_A=LAN,\quad \omega=\operatorname{rank}H,
$$
with $N$ a basis of $K_0$. Then $(5a)\iff\operatorname{row}H_A\subseteq\operatorname{row}H$ and
$(5b)\iff\operatorname{rank}(\lambda H-H_A)=\omega$ for all $\lambda\in\mathbb C$.

A candidate row space $\mathcal V=\operatorname{row}\mathcal L$ has invariants
$\rho=\dim\pi(\mathcal V)$, $c=\dim(\mathcal V\cap\mathcal J)$ ($\mathcal J=\operatorname{row}[C;CA]$),
with $q=\rho+c$. The **hyperplane case** is the layer $k-\omega=1$: the base is $\mathbb P(K_0)$, and
for $v=N\sigma^{\mathsf T}$ the constraint on the $m=q-r_0$ free rows $R$ is linear,
$$Rv=0,\qquad RAv=0 .$$
For fixed $v$ this leaves a linear space of rows, and the "lifted incidence space" is
$$
Z=\bigl\{(v,R):\ \sigma\in\mathbb P(K_0),\ Rv=RAv=0,\ \operatorname{rank}H=\omega,\
\operatorname{rank}[L_0;R]=q\bigr\}.
$$
On each irreducible component $Y$ of $Z$ the last two conditions are open, and feasibility of the
layer means: some point of $Z$ satisfies the spectral condition, i.e. the $\omega\times\omega$ maximal
minors $m_I$ of $\lambda H-H_A$ have no common root.

**Why the layer matters.** If every layer is decidable in polynomial time, the minimum order is
computable and the unrestricted problem is tractable. The hyperplane case is the first layer that is
not trivial, so its cost is a genuine test of the whole programme.

---

## Part II. The step: per-component generic gcd, and no drop-locus recursion

### II.1 The bad set is closed on a component, with a three-line proof

Let $Y$ be an irreducible component of $Z$ (so the normal rank is $\omega$). For each $D\ge0$ let
$L_D(y)$ be the coefficient matrix of
$$
(u_I)\longmapsto\sum_I u_I\,m_I(y;\cdot),\qquad \deg u_I\le D,
$$
whose entries are polynomials in $y$. Then
$$
\gcd_I m_I(y;\cdot)\ne1\iff 1\notin(m_I)\iff\forall D:\ 1\notin\operatorname{im}L_D(y).
$$
Each condition "$1\notin\operatorname{im}L_D$" is the rank condition
$\operatorname{rank}L_D<\operatorname{rank}[L_D\mid e_0]$, hence closed, so
$\{\gcd\ne1\}$ is an intersection of closed sets. No properness or homogenisation is needed.

### II.2 Consequence: the generic point decides

On an irreducible $Y$, either the bad set is all of $Y$, or its complement is a nonempty open dense
set. Therefore
$$
Y\ \text{contains a feasible point}\iff
\gcd_I m_I(y;\cdot)=1\ \text{in}\ \mathbb C(Y)[\lambda],
$$
i.e. the **generic gcd** over the function field of the component decides the component. This is a
deterministic criterion; a random point is only a *specialisation* of the generic point, which is why
the previously used test was one-sided rather than two-sided.

### II.3 Why the "exceptional locus" was a red herring

We previously tried to complete the locus on which the gcd degree jumps, and had to admit that the
candidate list was incomplete. The reason is now clear: the phenomenon "generic point bad, exceptional
point good" **cannot happen on a component** (II.2). It happens when one takes a generic point of a
*base* or of a *chart*, which may meet several components.

A concrete instance: with $\sigma=(a,-4b,b)$, the constraints of the layer give
$$
a y_1-4b y_2+b y_3=0,\quad y_1=0\ \Longrightarrow\ b\,(-4y_2+y_3)=0,
$$
a product. Hence the total space splits,
$$
Z=\underbrace{\{b=0\}}_{Z_1}\ \cup\ \underbrace{\{y\propto V_0\}}_{Z_2},
$$
and: on $Z_2$ (which dominates the whole base $\mathbb P^1$) the gcd is $\lambda$, so the component is
entirely bad; on $Z_1$ (the fibre over one base point, where $y$ is two-dimensional) the generic gcd is
$1$, so the component is good. Neither branch is mixed. Reading the base $\mathbb P^1$ alone mixes
them, and that mixing is what made the exceptional locus look necessary.

### II.4 What remains, and the shape of the gap

Two things remain, and neither is geometric:

1. **Enumerate the components of $Z$** (not of the base). The base decomposition gives at most
   $\delta+1$ pieces, but the total space refines it, as II.3 shows; the refinement is by fibre
   dimension / compatibility rank.
2. **Pay for the generic gcd.** By II.1 it is enough to decide whether some maximal minor of
   $L_D(y)$ is a nonzero function on $Y$ — a polynomial identity test for an explicit family of
   determinants. A grid of evaluation points gives certainty only if the grid is larger than the degree
   in every parameter, and the number of parameters grows with $k$.

---

## Part III. Questions

**Q1 (cost).** Is the test of II.2 — "is the generic gcd of the maximal minors of a *linear* pencil,
parameterised by a linear space of row data, equal to 1?" — decidable in polynomial time? Equivalently,
is the relevant structured PIT (nonzeroness of a maximal minor of the Bézout matrix of the maximal
minors) known to be tractable for this family, or is it as hard as general PIT? Any reference on
"generic gcd over the function field of a parameterised family" would settle whether the hyperplane
layer is in $\mathrm P$.

**Q2 (bypass).** We observe two mechanisms by which a component is entirely bad: (i) there is a single
$\lambda_0$ at which the rank drops identically, because all rows of $\lambda_0H-H_A$ lie in one fixed
line; (ii) a spectral mechanism, where the minors share exactly one root without such a line. Is there
a known structural characterisation of "entirely bad" components that would replace the identity test by
linear algebra — for instance in terms of the pair $(\iota|_W,A|_W)$, or of the Kronecker data of the
restricted pencil? If such a characterisation exists, the cost question disappears.

**Q3 (recursion).** Our earlier plan, and one of your suggestions, was to compute the generic gcd on a
component, then recursively decompose the locus where its degree rises. With II.1–II.2, that recursion
is unnecessary whenever the component decomposition is complete. Do you agree, or is there a case we
are missing — for instance over the reals, where the complement of a closed set need not be dense in the
real topology, or when the component is not normal?

**Q4 (what may be claimed).** With II.1–II.3, may we state that the hyperplane layer is decidable
(deterministically, in exact arithmetic) subject only to the enumeration of components and the cost of
the identity test? Or do you regard the enumeration of components of $Z$ as the harder half, which
would make the current statement premature?

A short answer to Q1 and Q4 would already tell us whether to invest the next phase in derandomising the
identity test or in the component enumeration.
