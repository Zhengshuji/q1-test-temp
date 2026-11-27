# Image-Space Reduction and Polynomial-Time Feasibility for Functional Observers with a Two-Dimensional Compressed Kernel

**Draft for LaTeX conversion.** Companion to the papers on decision complexity, on minimum order, and on
the one-dimensional (hyperplane) kernel layer. All statements are for the $K_0$-split problem unless marked
**U** (unrestricted). Numbering is fixed; environment labels in brackets for cross-referencing.

---

## Abstract

For a linear system $(A,C)$ and a prescribed observer row block $L_0$, feasibility of a functional observer
of order $q$ is governed by two rank conditions on the pencil $\lambda H-H_A$, where $H=LN$, $H_A=LAN$ and
$N$ spans the unobservable subspace $K_0=\ker[C;CA]$. The layer index of a design is
$c=k-\rank H$, $k=\dim K_0$; the case $c=1$ was settled in earlier work, where the admissible kernel
directions are the real eigenvectors of the compression $M=\pi_{K_0}A|_{K_0}$.

This paper treats $c=2$. Our main result is a **reduction of the fibre variable**: for a fixed kernel
direction $D$ the pencil depends on the fibre $W$ only through its image
$\Phi(W)\subseteq D^\circ$, a subspace of $D^\circ$ of dimension at most $c=2$. Consequently the search over
a Grassmannian of arbitrary dimension collapses to a search over subspaces of the image $\varphi(T_D)$, whose
dimension is at most the codimension of $K_0$ (hence at most $2p$). We give the
exact realizability conditions for a prescribed $\Phi$, the resulting reduced feasibility criterion, a
classification of the invariant-plane base for simple spectrum — with the real and the conjugate-complex
branches treated separately — a two-valued decision algorithm, and a $\mathrm{poly}(n,\tau)$ bit-complexity
bound under simple spectrum. We also show that the layer index is **not monotone** at fixed order: there are
instances where the $c=2$ layer is feasible while the $c=1$ layer is not. All structural claims are stated
for the split problem; the unrestricted problem is left open.

**Index Terms** — functional observers, minimum order, compressed pencil, invariant subspaces, Grassmann
bundles, subresultants, bit complexity.

---

## I. Introduction

**Setting.** The pair $(A,C)$ is given, together with a prescribed row block $L_0$. A design of order $q$ is a
row block $\mathcal L=[L_0;R]$ with $q$ rows; its row space $V$ has dimension $q$. Write
$K_0=\ker[C;CA]$, $k=\dim K_0$, fix a basis $N$ of $K_0$, and put $H=LN$, $H_A=LAN$. The design is
*feasible* when

$$(5a)\ \operatorname{row}H_A\subseteq\operatorname{row}H,\qquad
(5b)\ \rank(\lambda H-H_A)=\omega\ \ \text{for all }\lambda\in\mathbb C,$$

with $\omega=\rank H$. Condition $(5b)$ is equivalent to the vanishing of the gcd of all $\omega\times\omega$
maximal minors of the pencil (a standard polarity/resultant fact; see Section II).

**Prior work and what is new.** The existence question, the order spectrum and the minimum-order
characterisation were settled in [1], [2] (see also [4], [5]): for every order $q$ there is an exact
criterion, and the feasible orders are monotone and saturate. The *complexity* of the general decision
problem remains open. In [3] the case $c=1$ was solved structurally: the admissible kernel directions are the
real eigenvectors of the compression $M=\pi_{K_0}A|_{K_0}$, restricted by a prescribed-row orthogonality
condition; the design family is a finite union of relative Grassmann bundles; and one function-field gcd per
chart decides the whole chart.

This paper treats $c=2$. The contributions are:

1. **Layer bookkeeping (Section II).** The layer index is $c=k-\omega$ and the "ambient row excess" is
   $t=q-\omega$; the identity $c-t=k-q$ shows that $c$ and $t$ move together when $q$ is fixed. A previous,
   ambiguous identification of $\omega$ with $\dim(V\cap K_0)$ is corrected. We separate the unrestricted
   problem **U** from the $K_0$-split problem **S** and show by a counterexample that the split hypothesis
   cannot be derived from $(5a)$.
2. **The two fixed-kernel fibres (Section III).** For fixed $D=\ker H$ we give the exact fibre in both
   problems, including the exactness condition $K_0\cap(D+AD)=D$ in **U**, and the *two independent*
   prescribed-row conditions in **S** — one on the base ($P_{K_0}(V_0)\subseteq D^{\perp_{K_0}}$) and one on
   the fibre ($W_0\subseteq W$).
3. **Image-space reduction (Section IV).** The pencil's row space equals the row space of its
   $D$-part plus $\Phi(W)\subseteq D^\circ$, so the fibre acts only through a subspace of a $c$-dimensional
   space. We give the general proof, the exact realizability inequalities for a prescribed $\Phi$, and the
   reduced feasibility criterion.
4. **A two-valued algorithm at $c=2$ (Sections V–VI).** For simple spectrum the invariant-plane base is
   finite, of $O(k^2)$ points, split into a real-real and a conjugate-complex branch. The image space has at
   most one projective-line component, and on an image-line chart every real point is admissible, so the
   generic-gcd criterion is sharp in both directions and the algorithm decides exactly.
5. **Bit complexity (Section VII).** Under simple spectrum the decision runs in $\mathrm{poly}(n,\tau)$ bit
   operations, with arithmetic in number fields of degree at most $k^2$.
6. **A non-monotonicity example (Section VIII).** At one and the same order, the $c=2$ layer can be feasible
   while the $c=1$ layer is not. This rules out "only small layers matter" as a complexity strategy.

**Notation.** $E=\mathbb R^n$ throughout, with the Euclidean inner product. $\pi_{K_0}$ is the orthogonal
projection; $K_0^\perp$ its kernel; $D^\circ\subseteq K_0^*$ is the annihilator of $D$ when $D\le K_0$.
$\mathrm{Gr}(d,X)$ is the Grassmannian of $d$-planes in $X$. All matrices are real; $\tau$ is the maximum bit
length of the entries of $A$ and $C$. For a subspace $X$ we write $\dim X$ for its dimension.

---

## II. The layer parameters

### A. Three quantities that must not be confused

For a design $\mathcal L$ with row space $V$ of dimension $q$, define

$$\omega:=\rank H,\qquad c:=k-\omega,\qquad t:=q-\omega .$$

**[Proposition 1] (layer identities).**
1. $\omega=\rank(LN)=\dim\pi_{K_0}(V)=k-\dim(K_0\cap V^\perp)$;
2. $q=\omega+t$ and $c-t=k-q$;
3. $\dim(V\cap K_0^\perp)=q-\omega=t$, and $\dim(V\cap K_0)$ is a third quantity, in general different from
   both $c$ and $t$.

*Proof.* For (1): $\ker(LN)=\{u:Lu=0\}\cap K_0$ as a subset of $K_0$, i.e. $K_0\cap\ker L=K_0\cap V^\perp$
(when $L$ has full row rank, $\ker L=V^\perp$); hence $\omega=k-\dim(K_0\cap V^\perp)$. On the other hand
the restriction map $V\to K_0^*$, $v\mapsto\langle v,\cdot\rangle|_{K_0}$, has kernel $V\cap K_0^\perp$ and
rank equal to the rank of its adjoint $\pi_{K_0}|_V$, so $\dim\pi_{K_0}(V)=q-\dim(V\cap K_0^\perp)$; and its
adjoint's kernel is $K_0\cap V^\perp$, so $\dim\pi_{K_0}(V)=k-\dim(K_0\cap V^\perp)$. Both coincide with
$\omega$. Part (2) is the definition of $t$ and $c-t=(k-\omega)-(q-\omega)=k-q$. Part (3) is the first
computation above. $\square$

**[Remark 1].** In the hyperplane layer $q=k$, so $c=t$ and the three quantities of Proposition 1 coincide;
this is why the distinction was invisible in [3]. For $q\ne k$ they differ, and the layer index must be
defined as $c=k-\omega$.

### B. The split hypothesis

**[Definition 1].** A design is **$K_0$-split** (problem **S**) when $\dim(V\cap K_0)=\omega$; equivalently
$V=(V\cap K_0)\oplus(V\cap K_0^\perp)$. Designs satisfying $(5a)$, $(5b)$ without this condition form the
**unrestricted** problem **U**.

**[Proposition 2] (invariant kernel under split).** Let $\mathcal L$ be split and satisfy $(5a)$, and put
$D=\ker H=K_0\cap V^\perp$, $M=\pi_{K_0}A|_{K_0}$. Then $M(D)\subseteq D$.

*Proof.* By $(5a)$, $\ker H\subseteq\ker H_A$, i.e. $AD\perp V$. Let $\varphi_d(u)=\langle u,d\rangle$ and
$\varphi_{Ad}(u)=\langle u,Ad\rangle$ for $u\in K_0$. Both vanish on $V\cap K_0$: the first because
$D\subseteq V^\perp$, the second by $V\perp AD$. The annihilator of $V\cap K_0$ in $K_0^*$ has dimension
$k-\dim(V\cap K_0)=c$, and the $\varphi_d$, $d\in D$, are $c$ independent elements of it; hence
$\varphi_{Ad}\in\operatorname{span}\{\varphi_d\}$ and $\pi_{K_0}(Ad)\in D$. $\square$

**[Proposition 3] (the split hypothesis is not a normalisation).** There is a design satisfying $(5a)$, with
exact kernel and $c=2$, whose $D=\ker H$ is not $M$-invariant.

*Construction.* In $E=\mathbb{R}^8$ take $K_0=\operatorname{span}\{e_5,\dots,e_8\}$ and a compression
$M=\operatorname{diag}(1,1,2,3)$, choose $D=\operatorname{span}\{e_1+e_2,\,e_3+e_4\}\le K_0$ (not
$M$-invariant), put $U=D+AD$ and $V=U^\perp$. Then $\dim(D+AD)=3$, $K_0\cap(D+AD)=D$ (exactness),
$q=\dim V=5$, $\dim(K_0\cap V^\perp)=2=c$, $AD\perp V$ so $(5a)$ holds, and yet
$\dim(V\cap K_0)=1\ne\omega=2$, so the design is not split and $M(D)\not\subseteq D$. $\square$

---

## III. The fixed-kernel fibres

Throughout this section $D\le K_0$ with $\dim D=c$ is fixed, $U_D:=D+AD$, and $V_0=\operatorname{row}L_0$.
We write $P_{K_0}$ and $P_{K_0^\perp}$ for the two orthogonal projections, and
$M=P_{K_0}A|_{K_0}$, $A_{21}=P_{K_0^\perp}A|_{K_0}$, so that $Ax=Mx+A_{21}x$ for $x\in K_0$ (the two
summands lie in complementary subspaces).

### A. The unrestricted problem **U**

**[Theorem 4] (unrestricted fibre).** Let $D\le K_0$ with $\dim D=c$.
1. A $q$-dimensional $V$ satisfies $V_0\subseteq V$, $V\subseteq U_D^\perp$ and $K_0\cap V^\perp=D$ if and only
   if
   $$V_0\subseteq V\subseteq U_D^\perp,\qquad \dim V=q,\qquad K_0\cap(D+AD)=D .$$
2. The condition $K_0\cap(D+AD)=D$ is **equivalent** to exactness of the kernel, i.e. to
   $K_0\cap V^\perp=D$ for every $V$ with $V_0\subseteq V\subseteq U_D^\perp$.

*Proof.* (1) If $K_0\cap V^\perp=D$ and $(5a)$ holds then $U_D\subseteq V^\perp$ and hence
$K_0\cap(D+AD)\subseteq K_0\cap V^\perp=D$, while $D\subseteq D+AD$ gives the reverse inclusion. Conversely
if $K_0\cap(D+AD)=D$, then any $V$ with $V_0\subseteq V\subseteq U_D^\perp$ satisfies
$D\subseteq K_0\cap V^\perp\subseteq K_0\cap(D+AD)=D$. (2) is the same two lines. $\square$

**[Remark 2].** For $c=2$ the fibre of **U** is thus $\{V\in\mathrm{Gr}(q,U_D^\perp):V_0\subseteq V,\
K_0\cap V^\perp=D\}$, which is an open subset of a Grassmannian once the exactness condition holds. We do
not eliminate the fibre variable in **U**.

### B. The split problem **S**

**[Theorem 5] (split fibre).** Let $D\in\mathcal I_c(M)$ and assume the design is split. Put
$$T_D:=K_0^\perp\cap(A_{21}D)^\perp,\qquad W_0:=P_{K_0^\perp}(V_0),\quad w_0=\dim W_0,\quad
r(D)=\rank(A_{21}|_D).$$
If $P_{K_0}(V_0)\subseteq D^{\perp_{K_0}}$ and $W_0\subseteq T_D$, then the admissible row spaces are
$$V=D^{\perp_{K_0}}\oplus W,\qquad W_0\subseteq W\subseteq T_D,\quad \dim W=t,$$
and the fibre is
$$\mathcal F_D^{\rm split}\cong\mathrm{Gr}\bigl(t-w_0,\ T_D/W_0\bigr),$$
of dimension $(t-w_0)\bigl((n-k)-r(D)-t\bigr)$, non-empty if and only if
$$w_0\le t\le (n-k)-r(D).$$
Conversely every admissible row space arises this way.

*Proof.* (i) $V\cap K_0=\{x\in K_0:x\perp V\}^\perp$ intersected with $K_0$; since $V$ is split, this equals
$K_0\cap V^\perp$'s orthocomplement in $K_0$, i.e. $D^{\perp_{K_0}}$. (ii) For $d\in D$,
$\langle d,V\rangle=0$ and $\langle Ad,V\rangle=0$; writing $Ad=Md+A_{21}d$ with $Md\in D$,
$\langle Md,V\rangle=0$ automatically, so $V\perp AD\iff W\subseteq(A_{21}D)^\perp$. Since
$W\le K_0^\perp$, this is $W\subseteq T_D$. (iii) $V_0\subseteq V$ splits into $P_{K_0}(V_0)\subseteq
D^{\perp_{K_0}}$ and $W_0\subseteq W$, and the former is a condition on $D$ alone. (iv) The free part of $W$
modulo $W_0$ inside $T_D$ is a Grassmannian of the stated dimension. $\square$

**[Remark 3] (the prescribed rows are two conditions).** The condition on the base,
$$\mathcal B_{\rm pres}:=\bigl\{D\in\mathcal I_c(M):\ P_{K_0}(V_0)\subseteq D^{\perp_{K_0}}\bigr\}
=\bigl\{D\in\mathcal I_c(M):\ D\perp P_{K_0}(V_0)\bigr\},$$
is not implied by $W_0\subseteq W$; omitting it produces "designs" that cannot be completed to a legal
observer. It also removes entire components of the base: if $P_{K_0}(V_0)$ contains a vector with non-zero
inner product with every element of a given invariant $D$, that $D$ is excluded regardless of the fibre.

---

## IV. Image-space reduction

Fix $D\in\mathcal B_{\rm pres}$ and a split design $V=D^{\perp_{K_0}}\oplus W$ with $W_0\subseteq W\subseteq
T_D$.

### A. The reduction

For $w\in K_0^\perp$ define $\varphi_w\in K_0^*$ by $\varphi_w(u)=\langle w,A_{21}u\rangle$, and
$$\Phi(W):=\{\varphi_w:\ w\in W\}\subseteq D^\circ .$$
(The inclusion holds because $W\subseteq T_D$ means $W\perp A_{21}D$.)

**[Theorem 6] (image-space reduction).** For every $\lambda$,
$$\operatorname{row}\bigl(\lambda H-H_A\bigr)=\operatorname{row}\bigl(\lambda H_K-(H_A)_K\bigr)+\Phi(W),$$
where $H_K,(H_A)_K$ denote the rows carried by $D^{\perp_{K_0}}$. Consequently the pencil condition depends on
$W$ only through $\Phi(W)$, and $\dim\Phi(W)\le\dim\varphi(T_D)\le\dim T_D=(n-k)-r(D)$. Moreover:

3. $\operatorname{row}(\lambda H-H_A)\subseteq D^\circ$ for every $\lambda$, and $\dim D^\circ=k-c=\omega$;
4. hence $\rank(\lambda H-H_A)\le\omega$ automatically, and $(5b)$ is equivalent to
   $$\operatorname{row}\bigl(\lambda H-H_A\bigr)=D^\circ\quad\text{for all }\lambda,\qquad\text{i.e.}\qquad
   R_\lambda+\Phi(W)=D^\circ\ \ \forall\lambda,$$
   where $R_\lambda:=\operatorname{row}P_D(\lambda)$.

*Proof.* Regard the rows as functionals on $K_0$: for $v\in E$ put $h_v(x)=\langle v,x\rangle$ and
$h^A_v(x)=\langle v,Ax\rangle$, and $\Psi_\lambda(v)=\lambda h_v-h^A_v$; the rows of $\lambda H-H_A$ are the
$\Psi_\lambda(v)$ for $v$ ranging over a basis of $V$, transported to $\mathbb R^k$ by the basis $N$ (this
transport is the only place where the coordinate identification $K_0^*\simeq\mathbb R^k$ is used).
1. For $w\in W\le K_0^\perp$: $h_w(x)=\langle w,x\rangle=0$ since $x\in K_0$, and
$h^A_w(x)=\langle w,Ax\rangle=\langle w,Mx\rangle+\langle w,A_{21}x\rangle=0+\varphi_w(x)$; hence
$\Psi_\lambda(w)=-\varphi_w$, independently of $\lambda$.
2. For any linear $\Psi$ and any direct sum $V=P\oplus W$, $\Psi(V)=\Psi(P)+\Psi(W)$.
Combining, $\Psi_\lambda(V)=\Psi_\lambda(P)+\operatorname{span}\{\varphi_w\}$, and the sign is immaterial
because a subspace equals its negative.
3. For $v\in P=D^{\perp_{K_0}}$ and $d\in D$: $\langle v,d\rangle=0$, and
$\langle v,Ad\rangle=\langle v,Md\rangle+\langle v,A_{21}d\rangle=0+0$ because $Md\in D$ and
$A_{21}d\in K_0^\perp$; hence every $\Psi_\lambda(v)$ annihilates $D$, i.e. lies in $D^\circ$. Since
$\dim D^\circ=k-c=\omega$, the rank bound follows.
4. A subspace of the $\omega$-dimensional $D^\circ$ has dimension $\omega$ if and only if it is $D^\circ$. $\square$

**[Remark 4] (what the reduction says).** The spectral condition does not see $W$, only $\Phi(W)$: if
$\Phi(W_1)=\Phi(W_2)$ then the two designs have identical pencils up to row operations. The design space is
therefore quotiented by the fibres of $\Phi$, and the relevant parameter lives in a space of dimension at most
$c$. For $c=2$ this is decisive (Section VI).

### B. Exact realizability

**[Theorem 7] (realizability of a prescribed image).** Let $\varphi=\varphi|_{T_D}:T_D\to D^\circ$,
$\Phi_0=\varphi(W_0)$, and let $\bar\varphi:T_D/W_0\to D^\circ/\Phi_0$ be the induced map. A subspace $\Phi\le
D^\circ$ is realised by some $W$ with $W_0\subseteq W\subseteq T_D$ and $\dim W=t$ if and only if
$$\Phi_0\subseteq\Phi\subseteq\varphi(T_D),\qquad
\dim\Phi-\dim\Phi_0\ \le\ t-w_0\ \le\ \dim\ker\bar\varphi+\dim\Phi-\dim\Phi_0 .$$

*Proof.* Put $S=W/W_0\le T_D/W_0$; then $\dim S=t-w_0$ and $\bar\varphi(S)=\Phi/\Phi_0$. If such $S$ exists
then $\Phi/\Phi_0\subseteq\bar\varphi(T_D/W_0)$ and
$\dim(\Phi/\Phi_0)=\dim\bar\varphi(S)\le\dim S\le\dim\bar\varphi^{-1}(\Phi/\Phi_0)=\dim\ker\bar\varphi+
\dim(\Phi/\Phi_0)$. Conversely choose $S_0\subseteq\bar\varphi^{-1}(\Phi/\Phi_0)$ with
$\bar\varphi(S_0)=\Phi/\Phi_0$ and $\dim S_0=\dim(\Phi/\Phi_0)$, and extend it inside the same preimage to
dimension $t-w_0$; the upper inequality makes this possible. $\square$

### C. The reduced criterion

**[Theorem 8].** Write $P_D(\lambda)=\lambda H_K-(H_A)_K$ and $r_D(\lambda)=\dim\operatorname{row}P_D(\lambda)$.
Then
$$\exists W\ (W_0\subseteq W\subseteq T_D,\ \dim W=t)\ \text{satisfying }(5b)$$
$$\iff\ \exists\Phi\ \text{satisfying Theorem 7 such that}\
\dim\bigl(\operatorname{row}P_D(\lambda)+\Phi\bigr)=\omega\ \ \forall\lambda,$$
and the latter is equivalent to
$$\dim\Phi-\dim\bigl(\Phi\cap\operatorname{row}P_D(\lambda)\bigr)=\omega-r_D(\lambda)\quad\forall\lambda .$$

*Proof.* Immediate from Theorem 6 and $\dim(X+Y)=\dim X+\dim Y-\dim(X\cap Y)$. $\square$

**[Remark 5].** Theorems 6–8 reduce the fibre problem to a quantifier over subspaces of $D^\circ$. Two
spaces matter and they must not be confused: $D^\circ$ has dimension $\omega$, which grows with $k$, while
the image $\varphi(T_D)$ has dimension at most $\dim T_D=(n-k)-r(D)\le n-k\le 2p$, where $p$ is the number of
output rows. So the effective parameter ranges over
$$\bigcup_{j\le\min(t,\,2p)}\mathrm{Gr}\bigl(j,\ \varphi(T_D)\bigr),$$
a family of dimension at most $\lfloor\min(t,2p)^2/4\rfloor\le p^2$, **independent of $c$**. In particular the
image parameter is a point, a projective line, or a plane only when $\dim\varphi(T_D)\le2$; for larger output
counts the parameter is a higher-dimensional Grassmannian. A necessary condition for feasibility follows at
once: $\max_\lambda(\omega-r_D(\lambda))\le\dim\Phi\le n-k$, i.e. the rank deficiency of $P_D(\lambda)$ can
never exceed the codimension of $K_0$.

---

## V. The two-dimensional kernel: the base at $c=2$

Write $\mathcal I_2(M)=\{D\in\mathrm{Gr}(2,K_0):M(D)\subseteq D\}$.

**[Theorem 9] (base, simple spectrum).** Suppose $M$ has simple spectrum, i.e. its minimal polynomial over
$\mathbb Q$ has pairwise distinct irreducible factors and no repeated roots. Then $\mathcal I_2(M)$ is finite,
and every element is one of:
1. **(branch R)** $\operatorname{span}\{v_\alpha,v_\beta\}$ for two real eigenvalues $\alpha\ne\beta$ with
   eigenvectors $v_\alpha,v_\beta$;
2. **(branch C)** the real two-plane attached to a complex-conjugate pair: for a real eigenvector
   decomposition $z=u+iw$ of an eigenvalue $\mu=a+ib$ with $b\ne0$, the plane $\operatorname{span}\{u,w\}$,
   equivalently $\ker f(M)$ where $f$ is the irreducible quadratic factor.
The total number of planes is $\binom{k_{\mathbb R}}{2}+\#\{\text{conjugate pairs}\}\le k^2$, where
$k_{\mathbb R}$ is the number of real eigenvalues.

*Proof.* For a simple spectrum $M$ is diagonalisable over $\mathbb C$ and each complex eigenspace is a line. An
invariant real two-plane either contains two real eigenvectors (branch R), or is spanned by the real and
imaginary parts of a complex eigenvector (branch C), or is $\mathbb R^2$ for a two-dimensional $M$ with a
non-real pair, which is the case $k=2$ of branch C. Nothing else is invariant, because the restriction of $M$
to $D$ has a characteristic polynomial of degree two dividing the minimal polynomial. The count is immediate.
$\square$

**[Remark 6] (what is *not* claimed).** For non-simple spectra $\mathcal I_2(M)$ can be positive-dimensional
(the families $\mathrm{Gr}(2,K_\lambda)$ inside a repeated eigenspace, and products
$\mathbb P(K_\lambda)\times\mathbb P(K_\mu)$), and the planes attached to a repeated irreducible quadratic
form a $\mathbb{CP}^{g-1}$-family of real dimension $2(g-1)$, $g$ the geometric multiplicity. We make **no**
claim of a rational parametrisation of the general invariant-plane variety; the simple-spectrum statement
above is what the algorithm uses.

---

## VI. Exact decision at $c=2$

### A. Admissibility is automatic on an image-line chart

Recall from [3] that a point of a chart is *admissible* when some maximal minor of the cleared pencil keeps
its generic $\lambda$-degree at that point; the specialization lemma then shows that the generic gcd degree
is a lower bound on every admissible point, and that the generic gcd being a constant forces the chart to
contain a real feasible point whenever the real points are Zariski dense.

**[Lemma 10].** On every chart of a split design, $\rank H=\omega$ identically. In particular, on a chart
parameterising an image line, $H$ does not depend on the parameter and every real point of the chart is
admissible.

*Proof.* The $W$-rows of $H$ vanish (Theorem 6, step 1) and the $D$-rows have rank $\dim D^{\perp_{K_0}}
=k-c=\omega$; hence $\rank H=\omega$ for every choice of $W$. On an image-line chart the pencil differs from
a fixed matrix only in the single row $-\varphi(s)$, whose $\lambda$-coefficient is zero, so there is a
maximal minor whose $\lambda$-leading coefficient does not vanish and does not depend on $s$. $\square$

**[Corollary 11] (two-valued decision).** Under the hypotheses of Theorem 12 below, each real-admissible
image chart satisfies both hypotheses of the generic-gcd criterion, hence
$$\text{the generic gcd on the chart is }1\iff\text{the chart contains a real feasible design}.$$
Therefore the algorithm outputs exactly **feasible** or **infeasible**.

### B. The algorithm

**[Definition 2] (image charts).** Let $\Phi_0=\varphi(W_0)$ and $V_\varphi:=\varphi(T_D)$, of dimension
$\le\min(n-k,2p)$. The realisable image spaces are the subspaces $\Phi\le V_\varphi$ with
$\Phi_0\subseteq\Phi$, $\dim\Phi\le t$, satisfying the inequalities of Theorem 7; they are charted by the
standard affine charts of $\bigcup_{j}\mathrm{Gr}(j,V_\varphi)$, each of which carries
$j(\dim V_\varphi-j)\le p^2$ parameters. Two degenerate cases deserve names: $\Phi=\{0\}$ (possible only if
$\Phi_0=0$ and $t\ge0$ with the lower inequality satisfied) and $\Phi=D^\circ$ itself (possible only if
$V_\varphi=D^\circ$, i.e. only in the boundary case $\dim T_D=\omega$). When $\dim\Phi_0\ge1$ the
one-dimensional families disappear; the line case occurs only when $\Phi_0=0$ and $\dim V_\varphi\ge2$.

**[Algorithm 1] (decision at $c=2$, split, simple spectrum).**
1. compute $K_0$, $N$, $M$, $A_{21}$, $\omega$, $c$, $t$;
2. enumerate $\mathcal I_2(M)$ by Theorem 9, keeping only $D\in\mathcal B_{\rm pres}$;
3. for each $D$ compute $r(D)$, $T_D$, $W_0$, $\Phi_0$, and check $W_0\subseteq T_D$;
4. enumerate the realisable image spaces $\Phi$ by Theorem 7 and Remark 5;
5. for each image chart, clear denominators and compute the gcd of the $\omega\times\omega$ maximal minors
   over $\mathbb Q(s)[\lambda]$ (or over the field of definition of $D$); if it is constant, return
   *feasible*;
6. if every chart gives a non-constant gcd, return *infeasible*.

**[Theorem 12] (correctness).** Assume $c=2$, simple spectrum of $M$, and the split condition. Then
Algorithm 1 terminates and its answer is correct.

*Proof.* Finite enumeration by Theorems 9 and 7; correctness on each chart by Corollary 11 and Theorem 8; the
chart cover is complete because every realisable $\Phi$ is one of the three kinds of Definition 2. $\square$

---

## VII. Bit complexity

Let $\tau$ be the maximum bit length of the entries of $A$ and $C$.

**[Lemma 13] (arithmetic of the enumeration).** Assume simple spectrum. Then the number of planes is $O(k^2)$,
each plane is defined over a number field $L_D$ of degree at most $k^2$, and the field data and the bases of
$D$, $D^{\perp_{K_0}}$, $T_D$, together with $\varphi$, $\Phi_0$ and the entries of the cleared pencil, have
heights $\mathrm{poly}(n,\tau)$.

*Proof.* (Sketch.) $M$ is rational, so its minimal polynomial has coefficients of polynomial bit length; its
irreducible factors over $\mathbb Q$ then have polynomial height, and the roots have height bounded by the
Mahler measure of these factors. Branch R uses $L_D=\mathbb Q(\alpha,\beta)$ with $[\mathbb Q(\alpha,\beta):
\mathbb Q]\le d_id_j\le k^2$; eigenvectors are obtained by Cramer's rule over $L_D$, with denominators
$f_i'(\alpha)\ne0$ by simplicity. Branch C uses $\ker f(M)$, which is $\mathbb Q$-defined, so the final
objects live over $\mathbb Q$ even though the intermediate eigenvector data are computed in a complex
embedding of $\mathbb Q[t]/(f)$. Orthogonal complements and kernels are again Cramer, and the pencil entries
are obtained by polynomially many field operations. $\square$

**[Lemma 14] (degrees on an image chart).** On a chart of $\mathrm{Gr}(j,V_\varphi)$ at most $j$ rows of the
pencil depend on the chart parameters, and each dependence is affine. Hence every maximal minor satisfies
$$\deg_{\text{param}}\le j\le\min(t,\,2p),\qquad \deg_\lambda\le\omega\le k .$$
In particular on a line chart ($j=1$) the parameter degree is at most one.

*Proof.* A maximal minor is multilinear in the rows; exactly the $j$ rows corresponding to a basis of $\Phi$
vary, and they vary affinely in the chart coordinates. $\square$

**[Theorem 15] (bit complexity).** Assume (i) $c=2$, (ii) simple spectrum, (iii) the split condition, and
(iv) **$p$ fixed**, so that $n-k=\rank[C;CA]\le2p$ is bounded. Then Algorithm 1 runs in
$\mathrm{poly}(n,\tau)$ bit operations, with arithmetic in number fields of degree at most $k^2$.

*Proof.* There are $O(k^2)$ planes; for each, the realisable image spaces live in $V_\varphi=\varphi(T_D)$,
whose dimension is at most $2p$ and hence bounded; so the number of charts and the number of parameters per
chart are bounded independently of $k$ (at most $O(p^2)$ parameters, by Remark 5). On such a chart the pencil
has $\deg_\lambda\le\omega$ and heights $\mathrm{poly}(n,\tau)$, and the gcd of the maximal minors over
$L_D(\text{chart})[\lambda]$ costs $\mathrm{poly}(\omega,p,[L_D:\mathbb Q],\text{heights})$ by the standard
subresultant bound [9]. Summing over the $O(k^2)$ planes gives $\mathrm{poly}(n,\tau)$. $\square$

**[Remark 7] (the two boundaries, and why $p$ must be fixed).** Hypothesis (iv) of Theorem 15 is not cosmetic.
Without a bound on $n-k=\rank[C;CA]$ the space $V_\varphi=\varphi(T_D)$ grows with $k$, the fibre parameter has
up to $p^2$-many free parameters, and the chartwise gcd is no longer a polynomial-time primitive. Note also
that $c=2$ alone gives $\omega=k-2$, so $D^\circ$ is *large*: it is the bound on $n-k$, not the smallness of
$c$, that controls the fibre. Likewise, without simplicity of the spectrum the base is positive-dimensional (a
Grassmannian of dimension $2(d_\lambda-2)=O(n)$) and the number of charts is no longer polynomial. With $c$
allowed to vary, the number of components is $\binom{k}{c}$, which is exponential. The present method
therefore gives $\mathrm{poly}(n,\tau)$ only under fixed $p$ with simple spectrum, and at best
$n^{O(cn+p^2)}$ in general.

---

## VIII. Examples, limitations and the general layer

### A. The layer index is not monotone at fixed order

At a fixed order $q$ the identity $c-t=k-q$ shows that $c$ and $t$ move together, so only one order allows
both layers to be compared. Take $k=4$: then $c=1$ forces $q=3+t$ and $c=2$ forces $q=2+t$, and $q=3$ is the
common value ($c=1,t=0$; $c=2,t=1$). For the instance $A,C$ of [3, §VI] with the compression replaced by
$\operatorname{diag}(1,1,2,3)$:

**[Theorem 16] (non-monotonicity).** At order $q=3$ the $c=2$ layer is feasible and the $c=1$ layer is not.

*$c=2$ side.* With $D=\operatorname{span}\{e_1+e_2,e_3\}$ and $W=\operatorname{span}\{(0,0,1,1,0,0,0,0)\}$,
the design $V=D^{\perp_{K_0}}\oplus W$ has $\dim V=3$, $\omega=2$, satisfies $(5a)$ and exactness
($\dim(K_0\cap V^\perp)=2$), and the six maximal $2\times2$ minors of the pencil are
$$-(\lambda-3)(\lambda-1),\ (\lambda-3)(\lambda-1),\ \lambda-1,\ 1-\lambda,\ \lambda-3,\ 3-\lambda,$$
whose gcd is $1$ (indeed $\tfrac12\bigl((\lambda-1)-(\lambda-3)\bigr)=1$). So $(5b)$ holds.

*$c=1$ side.* At $q=3$ and $c=1$ one has $t=q-\omega=0$, so $\dim(V\cap K_0^\perp)=0$ and the design is
automatically split; Proposition 2 therefore applies. The invariant lines are the lines of the eigenspace
$E_1=\operatorname{span}\{e_1,e_2\}$ together with $\operatorname{span}\{e_3\}$ and
$\operatorname{span}\{e_4\}$. For the family
$D=\operatorname{span}\{e_1+se_2\}$ one computes $H=\begin{pmatrix}-s&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}$,
$\rank H=3$, and the gcd of the nonzero maximal minors equals $(\lambda-1)(\lambda-2)(\lambda-3)$,
**independently of $s$**; the point at infinity $s=\infty$ gives the same gcd, and the two isolated
directions give $(\lambda-1)^2(\lambda-3)$ and $(\lambda-1)^2(\lambda-2)$. Hence no $c=1$ design of order $3$
is feasible. $\square$

**[Remark 8].** The direction of the failure is "the larger layer is easier", so no monotonicity argument can
replace the analysis of all layers.

### B. The general layer

**[Proposition 17] (verbatim generalisation).** Theorems 4–8 hold with $2$ replaced by $c$: the base is
$\mathcal B_{\rm pres}\subseteq\mathcal I_c(M)$, the fibre is $\mathrm{Gr}(t-w_0,T_D/W_0)$ with
$T_D=K_0^\perp\cap(A_{21}D)^\perp$, the image space satisfies $\Phi(W)\subseteq D^\circ$ with
$\dim D^\circ=k-c=\omega$, and the reduced criterion of Theorem 8 is unchanged. The effective image parameter
ranges over $\bigcup_{j\le\min(t,2p)}\mathrm{Gr}(j,\varphi(T_D))$, of dimension at most
$\lfloor\min(t,2p)^2/4\rfloor\le p^2$.

*Proof.* The proofs of Theorems 6–8 use only $\dim D=c$ and $M(D)\subseteq D$; the numerical value $2$ enters
only in the list of possible image dimensions. $\square$

**[Remark 9].** Note that $\dim D^\circ=\omega$, not $c$: since $c=k-\omega$, the annihilator of a
$c$-dimensional subspace of an $\omega+c$-dimensional space has dimension $\omega$. For $c=2$ and $k=4$ the
two coincide, which is why the small cases are misleading; in general $D^\circ$ is large and only the image
$\varphi(T_D)$ is small.

**[Remark 10] (what remains open).** For general $c$ three obstructions persist: the enumeration of
$\mathcal I_c(M)$ (exponential when $c$ varies), the choice of $\Phi$ (a Grassmannian of dimension up to $p^2$), and the absence of a rational parametrisation of the base in the non-simple case. Two
questions seem most promising: (a) whether the quantifier over $\Phi$ can be replaced by a rank or separation
condition on the induced maps of $T_D/W_0$; (b) whether the layer index can be traded for $\dim U$ with
$U=\pi_1(W)$, since $c=k-\dim U$. We do not know the answer to either.

### C. Limitations of this paper

1. All structural results are for the split problem **S**; the unrestricted problem **U** is only reduced to a
   fibre description (Theorem 4) and its invariant-kernel structure is lost.
2. The decision algorithm and the complexity bound require simple spectrum; the non-simple case is left open.
3. No uniformity in $c$ is claimed; the honest general bound is $n^{O(cn+p^2)}$.
4. The general invariant-plane variety is used only through its defining equations; no rational parametrisation
   is claimed.

---

## References

[1] Decision complexity of functional observer feasibility: compression, certificates and the fixed-parameter
algorithm. (Paper I.)

[2] Minimum order and minimum-order construction for functional observers. (Paper II.)

[3] Functional-observer feasibility in the hyperplane layer. (Paper III.)

[4] A. Fernando, *Functional observer design: existence and order spectrum*, arXiv:2609.33615 (preprint).

[5] A. Fernando, *Functional observers: a chartwise characterisation*, arXiv:2609.37992 (preprint).

[6] W. Bruns and U. Vetter, *Determinantal Rings*, Lecture Notes in Mathematics 1327, Springer, 1988.

[7] W. Fulton, *Young Tableaux*, Cambridge University Press, 1997 (degeneracy loci, Ch. 14).

[8] S. Basu, R. Pollack and M.-F. Roy, *Algorithms in Real Algebraic Geometry*, 2nd ed., Springer, 2006.

[9] J. von zur Gathen and J. Gerhard, *Modern Computer Algebra*, 3rd ed., Cambridge University Press, 2013
(subresultants, gcd degree bounds).

[10] E. Emre and M. L. J. Hautus, "A polynomial characterization of (A,B)-invariant and reachability subspaces",
*SIAM J. Control Optim.*, vol. 18, no. 4, 1980.

---

## Appendix A. Proof of Lemma 13 (height propagation)

The chain is: entries of $A,C$ of bit length $\le\tau$ → entries of $M$ and $A_{21}$ (polynomial, by Cramer
and by the inverse of the Gram matrix of $N$) → coefficients of the characteristic and minimal polynomials of
$M$ (polynomial in $k$ and in the entry heights) → irreducible factors over $\mathbb Q$ (polynomial height, by
Kronecker's bound) → roots $\alpha$ of these factors (height bounded by the Mahler measure, hence polynomial)
→ eigenvectors $v_\alpha=\ker(M-\alpha I)$ over $\mathbb Q(\alpha)$ (Cramer, denominators $f'(\alpha)\ne0$) →
bases of $D$, $D^{\perp_{K_0}}$, $T_D$ (kernels and orthogonal complements, again Cramer) → entries of
$\varphi$, $\Phi_0$ and the pencil (polynomially many field operations) → subresultants and gcd (degree and
height bounds as in [9]). Each step multiplies the height by a factor that is polynomial in $n$ and in the
degrees involved; the degree of the field is at most $k^2$. This yields the stated
$\mathrm{poly}(n,\tau)$ bound. A fully explicit constant is not computed here.

## Appendix B. Notes for the LaTeX conversion (not part of the paper)

**Environment map.** 17 numbered items, numbered sequentially across types as written:
Propositions 1–3, Theorem 4, Theorem 5, Theorems 6–9, Lemma 10, Corollary 11, Theorem 12,
Lemmas 13–14, Theorem 15, Theorem 16, Proposition 17. Remarks are numbered 1–9 and are *not* part of the
sequence; Algorithm 1 is a float. If the target style insists on per-type counters, renumber and update the
cross-references in Sections IV–VII (they refer to Theorems 6–8, 12, 15 and to Proposition 17).

**Claim labels.** Every structural statement is for the split problem **S**. Statements that also hold for the
unrestricted problem are not claimed; Theorem 4 is the only **U** statement. Please keep the S/U tags in the
section headings — the reviewer explicitly asked for them.

**What must stay as stated (do not strengthen).**
1. Theorem 9 is a *simple-spectrum* classification. Remark 6 is the disclaimer for the general case; it must
   not be dropped, because no rational parametrisation of the general invariant-plane variety is claimed.
2. Theorems 12 and 15 depend on simple spectrum and on $c=2$; Remark 7 lists both boundaries and the honest
   general bound $n^{O(cn+p^2)}$.
3. The two prescribed-row conditions ($P_{K_0}(V_0)\subseteq D^{\perp_{K_0}}$ and $W_0\subseteq W$, plus
   $W_0\subseteq T_D$) are independent and both are needed; Remark 3 explains why omitting the base condition
   is a real error.
4. Lemma 10 (admissibility is automatic) is what turns the three-valued procedure into a two-valued decision;
   without it the algorithm must be described as a certified partial procedure.

**Proof status (for internal use; do not print).** Theorems 5, 6, 7, 8, 9, 12, 15, Lemma 10, Corollary 11 have
written proofs in the body (paper level). Lemma 13 is a sketch with the height chain in Appendix A; an explicit
constant is not computed and the paper says so. Theorem 16's data are exact rational computations.

**Machine-checked fragments (available on request; not in the paper).** The following are formalised and pass
an axiom audit whose only axioms are the three standard ones: $V\le D^\perp$ and
$V\ge(D+AD)^\perp\iff W\subseteq(A_{21}D)^\perp$ for split designs; $\Phi(W)\subseteq D^\circ$;
$V\cap K_0=K_0\cap D^\perp$; $\dim V=\dim(K_0\cap D^\perp)+\dim W$. The row-space identity of Theorem 6 itself
is *not* formalised (it is a matrix-level statement); Theorem 6 is proved in the body by the two-step argument
(vanishing $W$-rows of $H$, additivity of images over a direct sum).

**Recommended additions before submission.** (i) the ten-class exact test set (specification available) —
in particular a conjugate-complex instance for Theorem 9 branch C, and two instances where the inequalities of
Theorem 7 hold with equality; (ii) the explicit height chain of Appendix A with constants, or a precise reference
to each standard bound used; (iii) a paragraph in Section I relating this paper to [1]–[3] by *layer*, not as
"Paper IV" of a series.
