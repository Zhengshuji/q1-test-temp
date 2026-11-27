# Convention questions, domain of the partial map, and outstanding issues

This note records one convention problem that must be settled before any further computation,
and collects the older questions on which we would like advice. It is self-contained; the notation
is repeated where needed.

---

# Part I. Setting and status

## I.1 The problem

Given $A\in\mathbb C^{n\times n}$, $C\in\mathbb C^{p\times n}$, a row block $L_0\in\mathbb C^{r\times n}$,
and $\mathcal L=\begin{bmatrix}L_0\\R\end{bmatrix}\in\mathbb C^{q\times n}$ with $R$ free, require

$$(5a)\ \operatorname{rank}\begin{bmatrix}\mathcal LA\\ \mathcal L\\ CA\\ C\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}\mathcal L\\ CA\\ C\end{bmatrix},
\qquad
(5b)\ \operatorname{rank}\bigl[\lambda\mathcal L-\mathcal LA;\ CA;\ C\bigr]=h\ \ \forall\lambda\in\mathbb C,$$

with $h=\operatorname{rank}\begin{bmatrix}\mathcal L\\CA\\C\end{bmatrix}$, and ask whether computing
$q_{\min}=\min\{q:\exists R\}$ is NP-hard.

## I.2 Notation (column convention throughout this note)

$A$ and $\mathcal L$ act on column vectors. Let
$V:=\operatorname{row}[\mathcal L;C]^{\mathsf T}\le\mathbb C^n$,
$\mathcal J:=\operatorname{row}[C;CA]^{\mathsf T}$, $K:=\ker[C;CA]$,
$W:=\mathcal LV\le\mathbb C^q$, $V_0:=V\cap K$, $W_0:=\mathcal LV_0$,
$\rho:=\dim W$, and $Q_{\mathcal L}(\lambda):=\begin{bmatrix}\lambda\mathcal L-\mathcal LA\\CA\\C\end{bmatrix}$.

## I.3 Status

Thirty propositions are recorded, each with a complete paper proof; twenty-two also have a
machine-checked Lean kernel (eight formalise the literal statement, fourteen the non-trivial core).
Four review rounds have been completed. The unified statement now reads

$$(5b)\iff\overline N_{\mathcal Z}(\lambda)\ \text{injective}\ \forall\lambda
\iff\nexists\,0\ne w:\ \Phi(w)\in\mathbb C w
\iff\gcd\{\text{maximal minors of }\lambda\iota-\Phi\}\in\mathbb C^\times .$$

---

# Part II. The convention problem

## II.1 Two readings of $\Phi$

Our statement of the partial map was written as $\Phi(x\mathcal L):=x\Lambda$ with $x$ a row vector,
while the unified statement writes $W=\mathcal LV\subseteq\mathbb C^q$. These are transposes of each other,
and the two readings give different domains. Writing everything in the column convention:

**Definition.** Suppose $\Lambda$ satisfies
$$\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA.\qquad(\ast)$$
Set $\Phi(w):=\Lambda w$ for $w\in W$.

**Identity.** If $v\in V_0=V\cap\ker[C;CA]$, then
$$\Lambda\mathcal Lv=\mathcal LAv-G_0(Cv)-G_1(CAv)=\mathcal LAv .$$
Hence on $W_0$ one has $\Phi(\mathcal Lv)=\mathcal LAv$.

**Where $(5a)$ enters.** If instead one *defines* $\Phi(\mathcal Lv):=\mathcal LAv$ for $v\in V_0$, well-definedness requires
$$\mathcal Lv=0\ \Longrightarrow\ \mathcal LAv=0,$$
which is the transpose form of $(5a)$, namely $\ker[\mathcal L;CA;C]\subseteq\ker(\mathcal LA)$.
If one defines $\Phi(w)=\Lambda w$, well-definedness is automatic, and $(5a)$ enters only through the identity above.

Both readings give the same map on $W_0$. The failure criterion then reads
$$(5b)\ \text{fails}\iff\exists\,0\ne v\in V_0:\ \mathcal Lv\ne0,\ \mathcal LAv=\lambda\mathcal Lv
\iff\exists\,0\ne w\in W_0:\ \Phi(w)\in\mathbb C w .$$

## II.2 The question

The domain is written as $W=\mathcal LV$ in our earlier statement but is $W_0=\mathcal LV_0$ in the computation above.
These coincide when $S=V\cap\mathcal Z=0$, and differ otherwise.

**Question 1.** Which domain is the correct one for the partial-eigenvector criterion:
$W=\mathcal LV$, or $W_0=\mathcal L(V\cap\ker[C;CA])$? If the answer is $W_0$, the four-way equivalence
in Part I.3 should be restated with $W_0$ and with $\iota:W_0\hookrightarrow\mathbb C^q$.

We note that the same question affects the pencil $\lambda\iota-\Phi$ and therefore the degree of
the determinantal divisor, so we would like to settle it before computing examples.

**Question 2.** In $(\ast)$, is the existence of $(\Lambda,G_0,G_1)$ exactly equivalent to $(5a)$
(we use this in B.17/B.28(a))? If it is only sufficient, the definition of $\Phi$ weakens accordingly.

---

# Part III. Older questions we would still like advice on

## III.1 The AVOID formulation

Earlier rounds reduced the search to: among the augmentations satisfying $(5a)$, decide whether the
pencil can avoid a finite rank drop (AVOID = constrained regular subpencil). Two interfaces are available:
the rank barrier (necessary) and the incidence-coverage criterion (sufficient, with the empty base locus
hypothesis you identified as intrinsic).

**Question 3.** Is there a third interface that is both necessary and computable — for instance a
condition on the finite elementary divisors of the quotient pencil rather than on incidence dimension?

## III.2 Lower bounds

We have $q_{\min}\ge\max\{r+\varepsilon,\ \rho+\max(c_0,1)\}$ and the terminal-region theorem
$r_1\le p+1\Rightarrow q_{\min}=n-p$ (under observability, so $n_0=n$).

**Question 4.** Is there a principled way to improve the lower bound, or is the current one expected
to be optimal in general? A concrete instance family where the bound is attained would settle this.

## III.3 Degenerate cases

**Question 5.** For the write-up, which degenerate cases must be treated explicitly? We currently expect:
$K=0$ (so $\mathbb P(K)$ is empty and the coverage criterion is vacuous), $V=0$,
$\mathcal L$ of rank $<q$, and $L_0=0$. Are there others that we have not considered?

## III.4 Novelty check

Our provisional assessment is that the candidate new results are the unified four-way statement,
the equality obstruction, the partial-eigenvector characterisation, the rank barrier, the necessary
condition $\delta\in[1,r_1-p)$ and the $\exists\mathbb R$ upper bound; and that the quotient-pencil
equivalence, the gcd criterion and the quotient-equivalence theorem are likely reformulations.

**Question 6.** Do you consider this assessment correct? In particular, is the four-way unified statement
sufficiently distinct from the $\exists Z$ criterion of arXiv:2609.37992 to be presented as a contribution,
or should it be presented as a structural repackaging of it?

## III.5 Scope

**Question 7.** If the complexity question stays open, would you recommend publishing the structural
results as a paper with an explicitly stated open problem, or waiting for one side of the dichotomy?

---

# Part IV. What we would do with your answers

If Question 1 is answered in favour of $W_0$, we will restate the unified theorem with $W_0$ and
re-run the consistency checks of the machine-checked pieces. If Question 2 is answered negatively,
we will weaken the definition of $\Phi$ to the case where $(\ast)$ holds and record the obstruction.
For Questions 3–7 we will follow your priorities and report back with a worked attempt rather than a
survey.
