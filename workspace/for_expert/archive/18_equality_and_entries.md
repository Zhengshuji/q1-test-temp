# The equality boundary, the Kronecker bookkeeping, and a request for direction

This note reports what we did after your referee report: the equality case $h=q+r_1$ (your Direction A), the
Kronecker bookkeeping you asked to be made explicit, and three corrections that came out of it. It ends with
questions, the first of which is exactly the one we cannot settle ourselves.

Levels: **L1** paper proof, **L2** exact verification on finitely many instances, **L3** machine-checked.
We now label a statement **[Lean-conditional]** when Lean checks only the inference and the mathematical content
enters as a hypothesis — your recommended convention, adopted.

---

# Part I. What changed since the last report

## 1. B.8 split, and the index identity made conditional

As you pointed out, $h=\sum\varepsilon_j+d_{\rm fin}$ is **not** a general identity. We now state:

**B.8a (Smith criterion).** $Q_{\mathcal L}(\lambda)$ has constant rank $h$ on $\mathbb C$ iff $d_{\rm fin}=0$, where
$d_{\rm fin}$ is the total degree of the nonzero invariant factors. That half is correct and we keep it.

**B.8b (observer-specific, conditional).** $h=\sum_i\varepsilon_i+d_{\rm fin}$ **provided** the Kronecker form has
no right minimal indices and no infinite elementary divisors. The correct general bookkeeping is
$$h=\sum_i\varepsilon_i+\sum_j\eta_j+d_{\rm fin}+d_\infty,\qquad
m=\sum_i\varepsilon_i+\sum_j(\eta_j+1)+d_{\rm fin}+d_\infty,\qquad
n=\sum_i(\varepsilon_i+1)+\sum_j\eta_j+d_{\rm fin}+d_\infty .$$
Whether the observer pencil automatically has no right indices and no infinite divisors **is not proved by us**,
and your report is right that B.9 and B.10 rest on it.

## 2. Two short results that constrain the equality regime

**B.19 (top stratum and equality are mutually exclusive).** If $V\subseteq\mathcal Z$ then $h<q+r_1$.
*Proof.* $V\subseteq\mathcal Z$ means $\mathcal L$ vanishes on $V$, so $R=\operatorname{row}\mathcal L\subseteq V^\perp
=\operatorname{row}[C;CA]=W$; hence $R\cap W=R\ne0$ (as $\operatorname{rank}\mathcal L=q\ge1$). By the Type I criterion
(B.11c) $h\ge q+r_1\iff R\cap W=0$, so $h<q+r_1$. $\square$

This matters because $V\subseteq\mathcal Z$ is the one way $(5b)$ holds automatically ($V/S=0$). So the equality
case cannot be settled "for free"; but the converse — that equality forces failure — is also not what we can prove.

**B.20 (bookkeeping at equality).** At $h=q+r_1$: the constant right nullspace of $Q_{\mathcal L}$ is exactly
$S=V\cap\mathcal Z$; and $W\cap\mathcal Z^\perp=C$.

## 3. B.21: the right nullspace is $S[\lambda]$, and $s=n-h$

**B.21.** With $s=\dim(V\cap\mathcal Z)$ and $h=\operatorname{rank}[\mathcal L;CA;C]$:

1. $s=n-h$. *Proof.* $S=W^\perp\cap\mathcal Z$, so $S^\perp=W+\mathcal Z^\perp$ and
   $s=n-\dim(W+\mathcal Z^\perp)=n-h$. (exact verification 650/650)
2. The right nullspace of $Q_{\mathcal L}$ in $\mathbb C[\lambda]^n$ is $S[\lambda]$. *Proof.* The $C$- and
   $CA$-blocks force every coefficient of $x(\lambda)$ into $V$; on $V$ the first block equals
   $(\lambda I-\Lambda)\mathcal Lx(\lambda)$, and $\lambda I-\Lambda$ is invertible over $\mathbb C(\lambda)$, so
   $\mathcal Lx(\lambda)=0$, i.e. every coefficient lies in $V\cap\ker\mathcal L=S$. The converse uses
   $A(S)\subseteq\mathcal Z$.
3. Consequently $Q_{\mathcal L}$ has $n-h=s$ right minimal indices, all of degree zero, so $\sum_j\eta_j=0$.

Hence at equality (where also $\sum_i\varepsilon_i=0$, by the left-index count) the Kronecker identity reduces to
$$d_{\rm fin}+d_\infty=h=q+r_1,$$
so that **equality forces failure iff $d_\infty<h$**, i.e. iff the pencil has a non-trivial *finite* elementary
divisor.

## 4. One route we had to discard

We tried $d_\infty=h-\operatorname{rank}(A_1)$ where $A_1$ is the leading coefficient. **It is false.** The pencil
$\begin{pmatrix}1&\lambda\\0&1\end{pmatrix}$ has $h=2$, $\operatorname{rank}A_1=1$, but $\det\equiv1$, hence
$d_\infty=2$. A literature search (Gantmacher; Van Dooren's Kronecker algorithm; the survey material on singular
pencils) did not give us a usable formula for $d_\infty$ in terms of the coefficients alone, which is where we are
stuck.

## 5. Evidence

The equality boundary is never feasible in our samples: 26 822 admissible candidates with $h=q+r_1$, and $(5b)$
fails in all of them. $h>q+r_1$ never occurs at all (the row count forbids it). This is exact verification, not
proof.

---

# Part II. Corrections to the paper layer already made

* **B.13f**: the sentence "the pencil determinant vanishes identically" was wrong; the object that vanishes
  identically is the three-vector product $\det[Av,v,k]$ (three vectors in a two-dimensional space). The scalar
  quotient pencil is a nonzero affine polynomial and has a root. Withdrawn and corrected.
* **B.18c** is now stated with the restriction $z\notin V$ explicitly (if $z\in V$ then $S=\mathcal Z$ and the
  quotient domain is zero, so the image criterion does not apply).
* **B.18e** is now worded as "every admissible candidate at $d=1$ violates $(5b)$", not "every line in $K$".
* **B.11d** now carries the restriction $h\ne q+r_1$, with the equality case listed as open.

---

# Part III. Questions

**Q1 (the formula we need).** For a matrix pencil $P(\lambda)=A_0+\lambda A_1$ of normal rank $h$, is there a
usable expression for $d_\infty$, the total size of the infinite elementary divisors, in terms of
$\operatorname{rank}A_1$, $\operatorname{rank}A_0$ and $h$? We know $d_\infty=h-\operatorname{rank}A_1$ is false
(counterexample above) and that for regular square pencils $d_\infty=n-\deg\det$. Is there a correct general
statement, or is $d_\infty$ genuinely a Kronecker-form datum that cannot be computed from a few ranks? If the
latter, is there another route to $d_\infty<h$ in our setting, where the leading coefficient is
$[\mathcal L;0;0]$ of rank exactly $q$?

**Q2 (is the equality case even needed?).** Since B.8a already gives $(5b)\iff d_{\rm fin}=0$, and B.19/B.21 tell us
that at equality $\sum\varepsilon=\sum\eta=0$, would you advise proving $d_\infty<h$ directly, or re-forming the
dichotomy so that the equality case is absorbed (for instance by strengthening CSS as you suggested, and stating
the dichotomy only for $h\ne q+r_1$)?

**Q3 (B.21's status).** $s=n-h$ and "the right nullspace is $S[\lambda]$" look like clean statements to us, and
they are exactly the kind of bookkeeping your report asked for. Do they interact with the observer-specific
identity of B.8b in a way that would let us *prove* the two missing hypotheses (no right indices — which B.21 now
gives — and no infinite divisors, which remains open)?

**Q4 (label discipline).** We adopted your five labels. Two declarations in `Logic.lean` quantify over an
arbitrary index type with the mathematical content as hypotheses; is that the right shape for a
**[Lean-conditional]** artifact, or would you prefer those to be stated as implications between explicit
propositions of the problem (so that the hypothesis is a named, checkable statement)?

**Q5 (what next).** Given that $d=1$ is now settled for Class I and $d\ge2$ is untouched, and that the equality
boundary is one inequality away, would you have us (i) finish the boundary, (ii) go to $d\ge2$, or (iii) stop the
structural work and write the paper layer up as it stands, with the three open points (B.8b's two hypotheses,
$d_\infty<h$, $d\ge2$) stated as conjectures?
