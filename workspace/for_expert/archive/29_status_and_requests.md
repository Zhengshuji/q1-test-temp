# Project status, gaps, and requests

This note states the problem, the results obtained so far with their verification level,
the present obstacles, and the two approaches we are considering. It ends with specific questions.

---

# Part I. Problem and standard forms

## I.1 The original problem

Given $A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$ and a row block $L_0\in\mathbb C^{r\times n}$,
for $q\ge r$ set $\mathcal L=\begin{bmatrix}L_0\\R\end{bmatrix}\in\mathbb C^{q\times n}$ with $R$ free, and require

$$(5a)\quad \operatorname{rank}\begin{bmatrix}\mathcal LA\\ \mathcal L\\ CA\\ C\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}\mathcal L\\ CA\\ C\end{bmatrix},
\qquad
(5b)\quad \operatorname{rank}\bigl[\lambda\mathcal L-\mathcal LA;\ CA;\ C\bigr]=h
\ \ \text{for all }\lambda\in\mathbb C,$$

where $h:=\operatorname{rank}\begin{bmatrix}\mathcal L\\CA\\C\end{bmatrix}$ is the normal rank. Define

$$q_{\min}:=\min\{q:\ \exists R\ \text{satisfying }(5a)\text{ and }(5b)\}.$$

**Question $q1$.** Is computing $q_{\min}$ NP-hard?

The characterisation of $q_{\min}$ is settled in the literature: arXiv:2609.33615 and arXiv:2609.37992
(Fernando, 2026) give the order spectrum $\Sigma_{FO}\subseteq[q_0,\,n_0-p]$, a necessary and sufficient
condition for each order (the $\exists Z$ criterion of Thm 5, and the chart form $Z_I(\Theta)$ of Thm 6),
$\nu_{\min}=\min\Sigma_{FO}$, and an explicit construction; $q_0=\sum_j\eta_j$ is polynomial as well.
What remains open is the complexity of the chart-by-semialgebraic existence problem

$$\exists\,\text{chart } I\ \ \exists\,\Theta\in\mathbb R^{d(m_L-d)}:\ (5b)\ \text{holds},$$

and this is $q1$: if it is polynomial then $q1$ is false; if it is $\exists\mathbb R$-hard then $q1$ is hard.

## I.2 Notation

* $\mathcal J:=\operatorname{row}[C;CA]$, with $j:=\operatorname{rank}C$ and $r_1:=\operatorname{rank}[CA;C]$;
* $\mathcal V:=\operatorname{row}[\mathcal L;C]\le\mathbb C^n$, $d:=\dim\mathcal V$; $\mathcal Z:=\ker[C;\mathcal L]$;
  when $\mathcal L$ has full row rank, $\mathcal V=\mathcal Z^{\perp}$;
* $S:=\mathcal V\cap\mathcal Z$, $c:=\dim S$; $\rho:=\dim\pi(\mathcal V)$, where $\pi$ is the quotient map modulo $\mathcal J$;
* $K:=\ker[C;CA]$, $k:=\dim K$; $W:=\mathcal LV\le\mathbb C^q$;
* the pencil $Q_{\mathcal L}(\lambda):=\begin{bmatrix}\lambda\mathcal L-\mathcal LA\\CA\\C\end{bmatrix}\in\mathbb C^{(q+2p)\times n}$;
* $\delta:=\dim\bigl(\operatorname{row}(CA)/(\operatorname{row}(CA)\cap\mathcal V)\bigr)=h-(q+p)$;
* $d_{\rm fin}$ and $d_\infty$: total degrees of the finite and infinite elementary divisors;
* $r(\lambda):=\dim\pi\bigl(\mathbb C^n(\lambda I-A)\bigr)=\operatorname{rank}[\lambda I-A;\,C;\,CA]-j$.

## I.3 Three equivalent forms

* $(5a)\iff\pi(\mathcal VA)\subseteq\pi(\mathcal V)$;
* $(5b)\iff\operatorname{rank}Q_{\mathcal V}(\lambda)=\rho$ for all $\lambda$, where $Q_{\mathcal V}(\lambda)=\lambda\pi(\mathcal L)-\pi(\mathcal LA)$;
* order decomposition: $q=\rho+c$, with $\rho$ the dimension modulo $\mathcal J$ and $c$ the dimension inside $\mathcal Z$.

---

# Part II. Results

Every statement below has a complete paper proof; 22 of the 29 propositions also have a machine-checked
Lean kernel (8 of them formalise the literal statement, 14 formalise the non-trivial core and record
which step remains on paper). Independent review is marked as such. Numerical experiments are reported
only as evidence of the form "n/N instances", never as proof.

## II.1 Order structure and lower bounds

**A.1 (layer decomposition and lower bound).** $q=\rho+c$, and

$$q_{\min}\ \ge\ \max\bigl\{r+\varepsilon,\ \ \rho+\max(c_0,1)\bigr\}.$$

The decomposition is definitional. Each lower bound is obtained by minimising over feasible $U$;
the additive bound uses $\min(f+g)\ge\min f+\min g$ and does not assume simultaneous attainability.

## II.2 Pencils and the spectral condition

**B.1 (quotient pencil).** $(5b)\iff\operatorname{rank}Q_{\mathcal V}(\lambda)=\rho$ for all $\lambda$.
Passing to the quotient modulo $\mathcal J$ turns the rank condition into
$\operatorname{rank}(\lambda\pi(\mathcal L)-\pi(\mathcal LA))=\dim\pi(\mathcal V)$.

**B.2 (top layer).** If $\rho=d$, then $(5b)\iff(D_W^{\mathsf T},T_W)$ is observable (PBH).

**B.3 (layer $\rho=0$).** $\rho=0\iff\mathcal V\subseteq\mathcal J$; in that case $(5b)$ holds automatically.

**B.4 (full space).** For $\mathcal V=\mathbb C^n$, the pencil has constant column rank $n$ if and only if
$A$ has no right eigenvector in $K=\ker[C;CA]$, i.e.
$$\nexists\,0\ne x:\quad Cx=0,\quad CAx=0,\quad \exists\lambda:\ (\lambda I-A)x=0 .$$

The dual form $(\nexists\,0\ne\varphi:\ \varphi C=\varphi CA=0,\ \varphi(\lambda I-A)=0)$ is a different
statement and is not equivalent to constant column rank. A check on 3962 random integer instances:
the right-eigenvector criterion agrees with the rank computation on 3962/3962 instances, while the dual
form has 117 counterexamples. An earlier Lean kernel formalised the dual form; it is retained as a
standalone lemma and no longer counts as coverage of B.4.

**F.1 (rank barrier).** If $(5b)$ holds at $\lambda_0$, then $\rho\le r(\lambda_0)$. Consequently a layer
with $\rho>\min_\lambda r(\lambda)$ is infeasible. The argument is that the row space of
$Q_{\mathcal L}(\lambda_0)$ contains the image of $\pi_{\mathcal J}\bigl((\lambda_0I-A)\mathbb C^n\bigr)$,
whose dimension is at least $\rho$. This is a necessary condition only.

**B.9 (boundary and equality).** $h\le q+r_1$, with strict inequality when $L_0\ne0$; at equality
$\mathcal V\cap W_0=0$, where $W_0=\operatorname{row}[CA;C]$.

**B.22 (equality obstruction).** If $h=q+r_1$ and $q\ge1$, then $(5b)$ fails. More precisely,
$Q_{\mathcal L}$ is strictly equivalent to $\operatorname{diag}(\lambda I_q-K_1,\ I_{r_1})$, hence
$d_{\rm fin}=q$ and $d_\infty=r_1$. Choose $B$ with $\operatorname{row}B=\operatorname{row}[CA;C]$ and
$H_0=[\mathcal L;B]$ of full row rank; then $(5a)$ gives $\mathcal LA=KH_0$, so
$$\begin{bmatrix}\lambda\mathcal L-\mathcal LA\\B\end{bmatrix}
=\begin{bmatrix}\lambda I_q-K_1&-K_2\\0&I_{r_1}\end{bmatrix}H_0,$$
and the block determinant $\det(\lambda I_q-K_1)$ is monic of degree $q$, hence has a root, and the rank drops there.

**B.6 (right indices and infinite divisors).** Using $(5a)$ only: all right minimal indices of $Q_{\mathcal L}$
are zero (the right null module is generated by constant vectors), and all infinite elementary divisors have
degree one, so $d_\infty=h-\operatorname{rank}\mathcal L$.

**B.8 (Smith/gcd criterion).** Let $Q(\lambda)$ be an $a\times b$ polynomial matrix of normal rank $h$. Then
$$\operatorname{rank}Q(\lambda)=h\ \ \forall\lambda\in\mathbb C
\iff \Delta_h(\lambda):=\gcd\{\text{all } h\times h \text{ maximal minors}\}\in\mathbb Q^{\times},$$
and $\Delta_h=d_1d_2\cdots d_h$ is the product of the invariant factors. No Smith normal form is needed:
the finite-family Bézout identity $g=\sum a_ip_i$ gives $g(\alpha)=0\iff p_i(\alpha)=0$ for all $i$,
and every non-constant polynomial over $\mathbb C$ has a root.

## II.3 Necessary condition and terminal region

**B.31 (necessary condition for feasibility).** Let $\mathcal L$ be admissible and $q+p<n$. Then
$$(5b)\ \text{holds}\ \Longrightarrow\ 1\le\delta(\mathcal V)<r_1-p .$$
If $\delta=r_1-p$ then $h=q+r_1$ and B.22 gives failure; if $\delta=0$ the invariant-subspace exclusion
of B.28(a) applies.

**B.32 (terminal region).** If $r_1\le p+1$ then $q_{\min}=n-p$. The proof combines B.31 (no sub-terminal
order is feasible) with feasibility of the terminal order.

## II.4 Unified quotient-pencil theorem

**B.17.** Let $\overline N_{\mathcal Z}(\lambda):V/S\to X/\mathcal Z$. Then:

* *permanent kernel*: the $\lambda$-independent part of $\ker\overline N_{\mathcal Z}(\lambda)$ equals $S$; this uses $(5a)$ only;
* *exact failure criterion*: $(5b)\iff\ker\overline N_{\mathcal Z}(\lambda)=S$ for all $\lambda$;
* *right null space*: $s=n-h$, the right null space is $S\otimes\mathbb C[\lambda]$, and $\sum_j\eta_j=0$;
* *stratification*: a three-layer criterion in terms of $\operatorname{rank}(J_{\mathcal Z}|_V)$; the correct
  criterion for the intermediate layer is $\exists\lambda:\ker N_Z(\lambda)\not\subseteq S$, not full column
  rank of $N_Z(\lambda)$.

## II.5 Intrinsic spectral characterisation

**B.23 (block factorisation).** $Q_{\mathcal L}(\lambda)=P(\lambda)H_0$ with
$P(\lambda)=\begin{pmatrix}\lambda I_q-K_1&-K_2\\0&I_{r_1}\end{pmatrix}$ and
$\det P(\lambda)=\det(\lambda I_q-K_1)$; only block triangularity is used.

**B.24 (partial operator).** Define
$$\Phi:W\to\mathbb C^q,\qquad \Phi(x\mathcal L):=x\Lambda .$$
It is well defined using $(5a)$ alone (full row rank of $\mathcal L$ is not needed), and $\Phi=K_1|_W$. Then
$$\boxed{(5b)\ \text{fails}\iff\exists\,0\ne w\in W:\ \Phi(w)\in\mathbb C\,w .}$$
Since $\Phi$ maps into $\mathbb C^q$ and not into $W$, this is a partial eigenvector condition rather than a
statement about an operator on $W$. Equivalently, with
$\mathcal E_\Phi:=\{[w]\in\mathbb P(W):\Phi(w)\in\mathbb Cw\}$ one has $(5b)\iff\mathcal E_\Phi=\varnothing$.
The formulation does not depend on the choice of the extension $\Lambda$.

## II.6 Incidence variety and coverage criterion

**B.13a (homogeneous incidence variety).** Let $P_{\alpha,\beta}=\alpha I-\beta A$, $[\alpha:\beta]\in\mathbb P^1$,
$$\mathfrak I=\{([x],[z],[\alpha:\beta])\in\mathbb P(V)\times\mathbb P(K)\times\mathbb P^1:\ z\wedge P_{\alpha,\beta}x=0\},
\qquad
\mathcal B=\{([x],[\alpha:\beta]):P_{\alpha,\beta}x=0\}.$$
Then $\mathfrak I$ is closed; outside $\mathcal B$ the fibres have dimension at most zero (for $P_{\alpha,\beta}x\ne0$
the only possible point is $[z]=[P_{\alpha,\beta}x]$); over $\mathcal B$ the fibre is all of $\mathbb P(K)$, of
dimension $k-1$. Hence
$$\dim\mathfrak I\ \le\ \max\{v,\ \dim\mathcal B+k-1\},\qquad v=\dim V .$$

**B.13b (abstract coverage lemma).** If $\dim\mathfrak I<k-1=\dim\mathbb P(K)$, the projection
$\mathfrak I\to\mathbb P(K)$ is not surjective, so some $[z]$ satisfies $z\wedge(\alpha x-\beta Ax)\ne0$
for every non-zero $x$ and every $[\alpha:\beta]$.

**B.13c (sufficient condition).** If $\mathcal B=\varnothing$ and $v<k-1$, then $\dim\mathfrak I\le v<k-1$ and
B.13b applies. Note that $\mathcal B\ne\varnothing$ forces the projection to be surjective: a single base point
admits every $[z]$. The condition $\mathcal B=\varnothing$ is therefore essential, and B.13c is a sufficient
condition for infeasibility, not an equivalence.

## II.7 Arithmetic and complexity

**D.1 ($P\in\mathbf P$).** Define
$$P(A,B,S):=\min\{\dim U:\ S\le U,\ \Phi(U)\subseteq(U+B)/B\},$$
with value $+\infty$ if the family is empty. Then
$$\mathcal P(Y,C,\Phi,T)=\dim T+\mathcal P(Y/M,C',\Phi',T'),\qquad
M=T+C,\quad C'=\widehat\pi\Phi(M),\quad T'=\widehat\pi\Phi(T),$$
where $\widehat\pi:Y/C\to Y/M$ is the natural quotient map (well defined because $C\subseteq M$) and the
correction map is $\sigma=-\gamma\circ\beta$ with $\gamma:C'\to M$ and $\beta:U'\to C'$ determined by
$\widehat\pi\Phi(\gamma c)=c$ and $U'.\mathrm{mkQ}(\beta u)=U'.\mathrm{mkQ}(\widehat\pi\Phi(su))$.
Iterating $O(n)$ times with $O(n^3)$ work per step gives $O(n^4)$. Moreover $\rho_{ci}=P(T,B,U_0)$, where $T$ is
the action of $A$ on $\mathbb C^n/\mathcal J$. Note that $\rho_{ci}$ is the minimum dimension on the $(A)$ side
and is weaker than $q_{\min}$, which also involves $(5b)$.

**G.1 (DEC $\in\exists\mathbb R$).** A chart-free encoding uses $O(n^3)$ variables and equations, degree at most $n$,
and only $O(n)$ branches in $s$, with no disjunction over charts. The core lemma $\ker(CAZ)=Z\cap\mathcal V$ and
the implication "left inverse $\Rightarrow$ injective" are machine checked. This is an upper bound only.

**H.1 (Theorem Q).** If $Z\subseteq H$ and $A(S)\subseteq Z$, then
$$\operatorname{rank}[(\lambda I-A)V\mid Z]=\dim(V+Z)\iff\operatorname{rank}[U\mid P(\lambda)]=r+t,$$
with $U=Z/S$ and $P(\lambda)=(A-\lambda I)|_{V/S}$. The hypothesis $A(S)\subseteq Z$ is retained explicitly, and
$[U\mid P(\lambda)]$ need not be square; squareness corresponds to $q=t$.

**C.1 (a special family).** For the closure family with $S=\mathcal J$ the only feasible solution is the whole
space, so $q_{\min}=n$.

## II.8 Withdrawn results

Four closed-form conjectures for $q_{\min}$ (refuted by explicit counterexamples); the "controllability"
characterisation (the bridge $\beta(\mathcal H)\subseteq B$ vanishes identically, so the criterion is degenerate);
matroid, TAP and Schubert-counting routes; and conjectures of the form $\dim V+1$.

---

# Part III. Obstacles, approaches, and requests

## III.1 Obstacles

$$\text{no reduction is known (no }\exists\mathbb R\text{-hardness, no NP-hardness)},\qquad
\text{no polynomial decision procedure is known}.$$

The obstruction in our formulation is a constrained regular subpencil problem (AVOID): among the augmentations
satisfying $(5a)$, decide whether the spectral condition can be avoided. The difficulty is that the spectral
obstruction is analytic rather than combinatorial: it is the statement that a certain eigenvector exists, either
a right eigenvector of $A$ in $K$ (B.4) or a partial eigenvector of $\Phi$ in $W$ (B.24). All purely combinatorial
routes we tried fail because the obstruction does not live in the dimension or counting layer.

## III.2 Two approaches

**Approach A (hardness).** Use an infeasibility interface to build a reduction. Two interfaces are available:
the rank barrier F.1, which is a necessary condition ($\rho$ large forces infeasibility), and the coverage
criterion B.13c, which is a sufficient condition for infeasibility. A reduction would encode a real-algebraic
problem into the requirement that some $[z]$ avoids the incidence family, or into the triggering of the
rank barrier at some layer.

**Approach B (tractability).** Use the intrinsic form of B.23 and B.24 to remove chart enumeration. At present
$(5b)$ fails if and only if $\mathcal E_\Phi\ne\varnothing$. If membership in $\mathcal E_\Phi$ can be decided
by finitely many linear-algebraic tests, for instance through the minimal polynomial of $\Phi$ restricted to $W$,
the chart enumeration disappears and a polynomial algorithm follows.

## III.3 Questions

1. **Placement in the literature.** Is the complexity of DEC-Θ (existence of a chart together with a semialgebraic
   solution set) known, or closely related to known results, for instance the NP-hardness of static output feedback
   or of spectral assignment for regular subpencils? Under which standard problem should it be classified?
2. **Approach A.** Which known hard problem would you start a reduction from? Which of the two interfaces
   (rank barrier, coverage criterion) is the more likely to give an encodable negative condition? Is the
   hypothesis $\mathcal B=\varnothing$ in B.13c too strong, and if so how should it be weakened?
3. **Approach B.** Is there a polynomial test for the partial eigenvector condition on $\Phi$ that avoids chart
   enumeration? In other words, is chart enumeration the actual obstruction, or can it be made intrinsic?
4. **Structure.** Do B.17 and B.23+B.24 together constitute the unified description of the spectral obstruction
   you had in mind, or is a further piece missing, and if so which one?
5. **Scope for a paper.** Which of these results are worth stating as new, and which are reformulations of the
   $\exists Z$ criterion of Thm 5 in arXiv:2609.37992? We do not wish to claim overlap with that work.
