# The hyperplane layer: what we have measured, and four conjectures

This note collects the computational record of the hyperplane layer, the structural facts that the
record suggests, and four conjectures. It is meant to let you judge whether the conjectures are
plausible, whether any of them is already known, and which one to try to prove first. As before, the
motivation is the decision complexity of the prescribed-row problem; the characterisation itself is
taken from the literature.

---

## Part I. Setting

Let $A\in\mathbb Q^{n\times n}$, $C\in\mathbb Q^{p\times n}$ ($\operatorname{rank}C=p$),
$L_0\in\mathbb Q^{r_0\times n}$, and let $q$ be a candidate order with $\mathcal L=[L_0;R]$. Put
$K_0=\ker[C;CA]$, $k=\dim K_0$, $N$ a basis of $K_0$, $H=LN$, $H_A=LAN$, $\omega=\operatorname{rank}H$.
The two conditions are
$$
(5a)\ \operatorname{row}H_A\subseteq\operatorname{row}H,\qquad
(5b)\ \operatorname{rank}(\lambda H-H_A)=\omega\ \ \forall\lambda\in\mathbb C .
$$
**The hyperplane layer** is $k-\omega=1$; writing $V=\operatorname{row}L$ one has
$\omega=\dim(V\cap K_0)$, so in this layer $V\cap K_0$ misses $K_0$ by one dimension, and
$\ker H$ is a line, spanned by some $v=N\sigma^{\mathsf T}$.

Two equivalent descriptions of a layer point are used below.

- **Row description.** $v\in B:=\{v\in K_0: L_0v=L_0Av=0\}$, and each row $r$ of $L$ satisfies
  $rv=rAv=0$; equivalently $\operatorname{row}L\subseteq U^\perp$ with $U:=\operatorname{span}(v,Av)$.
- **Spectral description.** $\operatorname{rank}P(\lambda)<\omega$ for some $\lambda$ if and only if
  there is $u\in K_0\setminus\operatorname{span}(v)$ with $(\lambda I-A)u\in U$, where
  $P(\lambda)=\lambda H-H_A$. (This holds with equality of the two sides when
  $\operatorname{row}L=U^\perp$; otherwise it is a sufficient condition.)

---

## Part II. What we have

### II.1 Structural facts (proved)

1. **The bad locus is closed on a component.** Homogenise, form the incidence
   $\mathcal D\subseteq Y\times\mathbb P^1$ of the vanishing of the maximal minors, and project. The
   projection is proper, and there are no bad points at infinity because $\operatorname{rank}H=\omega$.
   (This replaces an earlier, incorrect rank-inequality argument of ours; your counterexample
   $L=\binom{x}{y}$ settled it.)
2. **Components.** For $B$ the admissible projective subspace and $E_\lambda=\mathbb P(K_0\cap\ker(A-\lambda I))\cap B$,
   the lifted incidence space is $Z=Z^\circ\cup\bigcup_\lambda F_\lambda$, where $Z^\circ$ is the
   closure of the bundle over $B\setminus E$ and $F_\lambda$ is the *full fibre* over $E_\lambda$;
   the pieces are irreducible and pairwise incomparable, so there are at most $1+\delta$ components
   ($\delta=\dim(K_0\cap A^{-1}K_0)$). Each is explicitly parametrised (projective base, kernel of an
   explicit linear map).
3. **The generic-gcd criterion.** On an irreducible component, feasibility over $\overline{\mathbb Q}$
   is equivalent to the generic gcd of the maximal minors being one. (Real and rational points are a
   separate matter; a nonempty Zariski-open set need not contain them.)
4. **A fixed kernel direction.** With $Q$ a basis of $U^\perp$ (as rows), $M(\lambda)=Q(\lambda I-A)N$
   satisfies
   $$Qv=QAv=0\ \Longrightarrow\ M(\lambda)\,c_v=0\quad\text{for all }\lambda,$$
   where $c_v$ is the coordinate vector of $v$. Hence $\det M\equiv0$ identically.
   Consequently (for $\operatorname{row}L=U^\perp$, i.e. on the non-eigen stratum) badness is the
   condition $\operatorname{rank}M(\lambda)\le\omega-1$, and since the kernel always contains $c_v$,
   this is a rank condition on a pencil with one variable direction removed.

### II.2 Computational record

**E1 (one instance with $\delta=1$).** $Z$ has exactly two components. On $Z^\circ$ the gcd is
$\lambda$ (the component is entirely bad); on $F$ (the fibre over the eigen-point, where the rows are
two-dimensional) the gcd is $1$ (the component is good). Reading the base $\mathbb P^1$ alone gives a
"mixed" picture; per component there is no mixing. The product decomposition
$Z=\{b=0\}\cup\{y\propto V_0\}$ was checked on 194 random instances of the same shape.

**E2 (small instance: $n=5$, $p=1$, $r_0=1$, $q=3$; $k=3$, $\omega=2$).**
With $v$ a non-eigenvector: $\operatorname{rank}H=2=k-1$, $(5a)$ holds, $\operatorname{row}L=U^\perp$
(both dimensions $3$), and
$$\gcd\big(\text{2-minors of }\lambda H-H_A\big)=\gcd\big(\text{2-minors of }M\big)=\lambda^2 .$$
With $v$ an eigenvector: $\operatorname{rank}H=2$ and $(5a)$ still hold, but
$\operatorname{row}L\subsetneq U^\perp$ ($3<4$), and the gcd is $1$ — this point is good.
Three further random row choices agreed; a degenerate choice with $\operatorname{row}L\subsetneq U^\perp$
confirmed the sufficient direction.

**E3 (varying $v$: $n=5$, $p=1$, $r_0=0$, $q=3$; hence $B=\mathbb P(K_0)=\mathbb P^2$).**
Ten random $v$ (all with $\dim U=2$, $\operatorname{rank}H=2$, $(5a)$ true):
$$\text{8 distinct monic quadratics, with 8 distinct root sets, pairwise coprime,}$$
and $\gcd_M=\gcd_{\text{pencil}}$ in all ten cases. So the common root genuinely **moves** with $v$;
there is no fixed common factor, and the "fixed-root" mechanism of E1 is not the only one.

**E4 (the degree is constant in this family).** In the setting of E3 the gcd had degree exactly $2$ for
every sampled $v$; recomputing on **six further random $A$** (not the companion-like matrix of E3) gave
$\det M\equiv0$ and degree exactly $2$ every time.

---

## Part III. Conjectures, and what we would like to know

### H1. Degree constancy
On each component, $\deg\gcd$ of the maximal minors is **constant** (in E3's family it is $2$, for
every $v$ and every $A$ tested). If this holds, "the component is entirely bad" can be certified by a
**lower bound on the degree**, rather than by exhibiting the root $\lambda(v)$ — a strictly weaker
target than the polynomial identity test of Report 94, Q1.

### H2. A dichotomy rather than a trichotomy
We can distinguish three behaviours of $\Lambda(v)=\{\lambda:\operatorname{rank}P(\lambda)<\omega\}$:
fixed root (E1), finite cover, and true movement (E3). The middle case has not been observed.
**Conjecture:** it does not occur — either a common root is fixed, or the roots genuinely move.

### H3. The reduced pencil suffices
On the non-eigen stratum, badness is decided by the $(n-2)\times k$ pencil $M(\lambda)=Q(\lambda I-A)N$
(and by the fixed kernel direction, effectively by a $(n-2)\times(k-1)$ pencil). This is a smaller
object than the $\binom{q}{\omega}$ minors of the $q\times k$ pencil; it may matter for the cost of the
algorithm in Report 94, Theorem C.

### H4. The eigen fibres are the good ones
In E1 and in E2 the eigen component was good, and the open component bad. **Conjecture:** the fibres
$F_\lambda$ are generically good whenever they are nonempty. (Two instances only; we do not trust it.)

### Questions

1. **H1**: is constant degree of the gcd of the maximal minors a known phenomenon for a family of
   pencils — e.g. is it forced by a flatness or constant-rank condition, or by the fixed kernel
   direction of II.1(4)? In E3 the degree is $2$ regardless of $A$, which suggests an invariant
   (perhaps a Kronecker-type index of the restricted pencil) rather than an accident.
2. **H2**: is a "finite cover without a fixed root" case possible? If you know a mechanism, we will
   build it; if you believe it impossible, we will try to prove the dichotomy.
3. **H3/H4**: with the fixed kernel direction of II.1(4), does the problem reduce to the rank-$\le1$
   locus of a $3\times2$ affine pencil? Is the rank-$\le1$ problem for such pencils decidable in
   polynomial time by known means (we are thinking of the minors being quadratics with a common
   root)?
4. **Priority**: H1 and H2 look cheapest; H3 is the one that would affect the algorithm's cost. Which
   would you attack first?

### Reliability

| Item | Label |
|---|---|
| closedness, components, generic-gcd criterion | proved (your corrections incorporated) |
| fixed kernel direction $M(\lambda)c_v=0$, $\det M\equiv0$ | proved (one line), checked symbolically on 7 instances |
| E1, E2, E3 | exact rational computation on the displayed instances; not a proof |
| H1–H4 | **conjectures**; E4 is evidence for H1, not a proof |
| the layer's feasibility in E2/E3 | **not decided** (E3's ten good-looking samples show the gcd is never $1$; that is evidence, not a proof) |
