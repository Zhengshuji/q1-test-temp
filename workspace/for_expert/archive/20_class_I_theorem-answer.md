# Referee review of `20_class_I_theorem.md`



Main theorem correct

Class I minimum order resolved



This is a substantial advance. The two-case argument in B.27 is mathematically sound. It closes the Class I conjecture for every \\(1\le q\le n-2\\), without needing the canonical-coordinate recursion or an incidence-variety calculation.

The key insight is exactly the one your report identifies: when \\(p=1\\), the row space \\(\mathcal V\\) has only one possible new direction contributed by \\(CA\\). Consequently, there are only two cases:

- \\(cA\notin\mathcal V\\): the equality obstruction B.22 applies.
- \\(cA\in\mathcal V\\): admissibility condition (5a) forces \\(\mathcal V\\) to be \\(A\\)-invariant, contradicting observability unless \\(\mathcal V\\) is the entire row space.

This is a clean structural proof. I would promote B.27 to a main theorem, subject to a small clarification of its hypotheses concerning terminal-order feasibility. I also see a useful generalization that should be extracted before moving to the next cases.&#x20;

20_class_I_theorem.md



## 1. Q1: checking B.26 and B.27

### 1.1 B.26(1): correct

You define

\\[ \mathcal Z=\ker\begin{bmatrix}C\\\\\mathcal L\end{bmatrix}, \qquad \mathcal V=\mathcal Z^\perp. \\]

By the standard row-space/nullspace identity,

\\[ \mathcal V =\operatorname{row}\begin{bmatrix}\mathcal L\\\c\end{bmatrix}. \\]

The admissibility condition

\\[ \operatorname{rank}\begin{bmatrix}C\\\\\mathcal L\end{bmatrix}=q+1 \\]

then gives

\\[ \boxed{\dim\mathcal V=q+1.} \\]

There is no hidden assumption here beyond the stated rank condition.

One notational recommendation: since the argument is over \\(\mathbb C\\), specify whether \\(\mathcal Z^\perp\\) means the Hermitian orthogonal complement or the algebraic annihilator. The row-space identity is most naturally expressed using the algebraic annihilator. Either convention gives the intended dimension and row-space identification when used consistently.

### 1.2 B.26(2): correct

For \\(p=1\\),

\\[ \operatorname{row}\begin{bmatrix}CA\\\C\end{bmatrix} =\operatorname{span}\\{cA,c\\}. \\]

Since \\(c\in\mathcal V\\),

\\[ \begin{aligned} h &=\operatorname{rank}\begin{bmatrix}\mathcal L\\\CA\\\C\end{bmatrix}\\\ &=\dim\bigl(\mathcal V+\operatorname{span}\\{cA\\}\bigr). \end{aligned} \\]

Therefore

\\[ \boxed{ h= \begin{cases} q+1,&cA\in\mathcal V,\\\ q+2,&cA\notin\mathcal V. \end{cases}} \\]

This is exactly the dichotomy needed for B.27.

Importantly, you do not need \\((\ell,A)\\) to be observable here. You only use the observability of \\((c,A)\\), and even that is not needed until the second case of B.27.

### 1.3 B.26(3): correct, with a simpler proof available

You want to establish

\\[ (5a)\iff \mathcal VA\subseteq\mathcal V+\operatorname{span}\\{cA\\}. \tag{1} \\]

First observe that

\\[ \mathcal V=\operatorname{row}\mathcal L+\operatorname{span}\\{c\\}. \\]

In fact, the sum is direct, because admissibility gives

\\[ \operatorname{rank}\begin{bmatrix}\mathcal L\\\c\end{bmatrix}=q+1. \\]

Consequently,

\\[ \mathcal VA =\operatorname{row}(\mathcal LA)+\operatorname{span}\\{cA\\}. \\]

On the other hand, (5a) is equivalent to

\\[ \operatorname{row}(\mathcal LA) \subseteq \mathcal V+\operatorname{span}\\{cA\\}. \\]

Combining these two identities gives (1) immediately.

This is slightly cleaner than the proof in the report and makes the equivalence transparent.

### 1.4 B.26(4): correct

If \\(cA\in\mathcal V\\), then

\\[ \mathcal V+\operatorname{span}\\{cA\\}=\mathcal V. \\]

Thus (1) becomes

\\[ \boxed{(5a)\iff\mathcal VA\subseteq\mathcal V.} \\]

This is the decisive step.

### 1.5 B.27: the two cases are exhaustive and both are settled

Let \\(1\le q\le n-2\\).

Case I: \\(cA\notin\mathcal V\\).

B.26 gives

\\[ h=q+2. \\]

Since \\((c,A)\\) is observable and \\(n\ge2\\), the rows \\(c,cA\\) are linearly independent. Hence

\\[ r_1=\operatorname{rank}\begin{bmatrix}CA\\\C\end{bmatrix}=2. \\]

It follows that

\\[ h=q+r_1. \\]

Your equality theorem B.22 now gives

\\[ (5b)\text{ fails}. \\]

Case II: \\(cA\in\mathcal V\\).

B.26(4) gives

\\[ \mathcal VA\subseteq\mathcal V. \\]

Since \\(c\in\mathcal V\\), induction yields

\\[ cA^k\in\mathcal V \qquad\forall k\ge0. \\]

Observability of \\((c,A)\\) means

\\[ \operatorname{span}\\{c,cA,\ldots,cA^{n-1}\\} =\mathbb C^{1\times n}. \\]

Therefore

\\[ \mathcal V=\mathbb C^{1\times n}. \\]

But

\\[ \dim\mathcal V=q+1\le n-1, \\]

a contradiction.

Thus Case II is impossible.

We conclude

\\[ \boxed{ 1\le q\le n-2 \quad\Longrightarrow\quad (5b)\text{ fails}. } \\]

Verdict: B.27's lower-bound proof is complete. It does not require observability of \\((\ell,A)\\).

## 2. A clarification: terminal-order feasibility and the hypotheses

The lower-bound proof is complete, but I recommend making the terminal-order construction explicit in the theorem statement.

At \\(q=n-1\\), choose an \\((n-1)\\)-dimensional row space \\(\mathcal V\\) satisfying

\\[ \operatorname{span}\\{\ell\\}\subseteq\mathcal V, \qquad c\notin\mathcal V. \\]

Such a subspace exists whenever

\\[ \operatorname{rank}\begin{bmatrix}c\\\\\ell\end{bmatrix}=2. \\]

Choose \\(\mathcal L\\) whose row space is \\(\mathcal V\\). Then

\\[ \operatorname{rank}\begin{bmatrix}c\\\\\mathcal L\end{bmatrix}=n, \\]

and (5a) holds automatically because

\\[ \operatorname{row}\begin{bmatrix}\mathcal L\\\c\\\cA\end{bmatrix} =\mathbb C^{1\times n}. \\]

It remains to check (5b). Here

\\[ \mathcal Z=\\{0\\}. \\]

The quotient-pencil criterion says that failure of (5b) would require

\\[ 0\ne x\in\ker c,\qquad Ax=\lambda x \\]

for some \\(\lambda\in\mathbb C\\).

But observability of \\((c,A)\\), by the PBH criterion, excludes such an eigenvector. Hence (5b) holds.

So terminal-order feasibility uses only:

- observability of \\((c,A)\\);
- linear independence of \\(c\\) and \\(\ell\\).

It does not require observability of \\((\ell,A)\\).

The original project assumptions apparently include

\\[ \operatorname{rank}\begin{bmatrix}C\\\L_0\end{bmatrix}=p+r=2, \\]

so this condition is already available in the intended setting. Nevertheless, I would explicitly include it in B.27 or refer to the standing assumptions.

### Recommended theorem statement

> Theorem B.27 (Class I minimum augmentation order). Let \\(C=c\\) and \\(L_0=\ell\\) be row vectors, with \\((c,A)\\) observable and \\(\operatorname{rank}[c;\ell]=2\\). Under the admissibility conditions (5a) and \\(\operatorname{rank}[c;\mathcal L]=1+q\\), every candidate with \\(1\le q\le n-2\\) violates (5b). A feasible candidate exists at \\(q=n-1\\). Consequently,\
> \\[\
> \boxed