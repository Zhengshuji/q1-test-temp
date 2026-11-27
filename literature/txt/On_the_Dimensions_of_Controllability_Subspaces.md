# ON THE DIMENSIONS OF CONTROLLABILITY SUBSPACES: A CHARACTERIZATION VIA POLYNOMIAL MATRICES AND KRONECKER INVARIANTS\*

**MICHAEL E. WARREN AND ADRIAN E. ECKBERG, JR.†**

*SIAM J. CONTROL*, Vol. 13, No. 2, February 1975, pp. 434–443.

> \* Received by the editors August 31, 1973.
> † Electronic Systems Laboratory, Department of Electrical Engineering, Massachusetts Institute of Technology, Cambridge, Massachusetts. The first author is now at the Electrical Engineering Department, University of Florida, Gainesville, Florida 32603. The second author is now at Bell Laboratories, Holmdel, New Jersey 07733. This research was conducted at the Decision and Control Sciences Group of the M.I.T. Electronic Systems Laboratory, and supported by the National Science Foundation under Grant GK-25781.

---

## Abstract

The controllability subspaces of a pair $(A,B)$, instrumental in the formulation of the geometric theory of decoupling, are shown to have a natural analog in terms of the kernel of the singular pencil of matrices $(\lambda I - A; -B)$. In addition the pencil of matrices leads directly to the multivariable canonical form of Brunovsky.

The possible dimensions of controllability subspaces are shown to be completely determined by a set of invariants of the pencil of matrices. The minimum dimension of controllability subspaces which contain arbitrary subspaces of the image of $B$ is ascertained, and a construction for such subspaces is given.

## 1. Introduction

The theory of the decoupling of constant linear systems by state feedback received a considerable boost with the advent of the geometric theory of Wonham and Morse [10]. Their formulation relied heavily on the concept of a **controllability subspace (c.s.)**, that is, a vector subspace satisfying certain restrictive conditions. Solvability of decoupling problems then became equivalent to finding suitable sets of c.s.

At approximately the same time, the results of Wolovich and Falb [9], Brunovsky [1], Popov [7], Kalman [6] and Rosenbrock [8] led to a definitive canonical form for the input-state dynamics of time invariant linear systems. Kalman [6] and Rosenbrock [8] sensed the relationship between this canonical decomposition and Kronecker's classical theory of pencils of matrices, while Wonham and Morse [11] recognized that the decomposition was in terms of controllability subspaces.

The purpose of this paper is two-fold. First we show there is a strong and natural connection between controllability subspaces and elements in the kernel of a singular pencil of matrices. Furthermore, the pencil of matrices leads easily to the canonical form of Brunovsky. Then exploiting certain invariants of the pencil of matrices, we are able to make definitive statements about the dimensions of possible c.s., including the existence and uniqueness of c.s. of a given dimension.

In what follows, we shall be concerned with linear time invariant systems whose input-state dynamics are described by either the difference equation

$$
x_{k+1} = Ax_k + Bu_k,
$$

or the differential equation

$$
\dot{x}(t) = Ax(t) + Bu(t),
$$

where $x \in R^n$, a real $n$-dimensional vector space, and $u \in R^m$, with $A$ and $B$ real matrices of appropriate dimensions. The algebraic structure of $A$ and $B$ which we will develop is independent of the specific dynamics, and thus will apply equally well to systems governed by either differential or difference equations. Furthermore, although we choose real vector spaces for concreteness, everything that follows will hold for vector spaces over an arbitrary field.

Except where otherwise specified, we shall use upper case italic letters to refer to linear transformations between vector spaces or their associated matrices. Script letters will denote vector spaces or subspaces. Lower case italic letters will indicate vectors while reals (field elements) will be represented by lower case Greek letters. When appropriate, we shall also indicate the image of a map $B$ by $\mathscr{B}$; and if $b \in \mathscr{B}$, $\ell$ stands for the subspace spanned by $b$. Further, if $A:R^n \to R^n$ is a linear map, and $\mathscr{R}$ is $A$-invariant, we write $A|\mathscr{R}$ to indicate the restriction of $A$ to the subdomain $\mathscr{R}$. The dimension of a subspace $\mathscr{R}$ is given by $\dim \mathscr{R}$.

The space of polynomials with coefficients in $R$ is denoted by $R[\lambda]$; note that this is an $R[\lambda]$-module. The degree of a polynomial $u(\lambda)$ is indicated by $\deg u(\lambda)$. We let $\underline{m}$ denote the set of integers $\{1,2,\cdots,m\}$, and for an ordered set of scalars $\{v_1,\cdots,v_k\}$ we let

$$
v_j^* = \sum_{i \le j} v_i, \qquad j \le k.
$$

If $\{\cdot\}$ is a set of vectors, we refer to the subspace spanned by the elements as $\operatorname{span}\{\cdot\}$, and we indicate the $j$th standard unit vector ($1$ in the $j$th position, zeros elsewhere) by $e_j$. Finally the transpose of $A$ is given by $A^T$.

If $A:\mathscr{X} \to \mathscr{X}$, $\mathscr{B} \subset \mathscr{X}$, and $\dim \mathscr{X}=n$, then $\{A|\mathscr{B}\} = \mathscr{B} + A\mathscr{B} + \cdots + A^{n-1}\mathscr{B}$, i.e., the space reachable under the action of $A$ from inputs to $\mathscr{B}$. We say that $(A,B)$ is a controllable pair if $\{A|\mathscr{B}\} = \mathscr{X}$. Following [10], a subspace $\mathscr{V} \subset \mathscr{X}$ is $(A,B)$-invariant if there exists a map $F:R^n \to R^m$ such that $(A+BF)\mathscr{V} \subset \mathscr{V}$. A subspace $\mathscr{R}$ is a c.s. of $(A,B)$ if $\mathscr{R}$ is $(A,B)$-invariant and $\mathscr{R} = \{A+BF|\mathscr{B}\cap\mathscr{R}\}$ for some $F$; that is, every element in $\mathscr{R}$ is reachable under the action of $A+BF$ from inputs to $\mathscr{B}\cap\mathscr{R}$.

## 2. Some preliminary results

In this section we show that the concept of a controllability subspace for a pair $(A,B)$ has an analog in terms of the kernel of a particular polynomial matrix. Furthermore, certain invariants of this polynomial matrix are shown to lead quite naturally to the canonical form for controllable pairs developed in [1], [6], [7], [8] and [9].

**Lemma 1.** If $\mathscr{R}$ is a c.s., then for every nonzero $b \in \mathscr{B}\cap\mathscr{R}$, there exists a matrix $F$ such that

$$
\tag{1}
\{A+BF|\ell\} = \mathscr{R}.
$$

Moreover, $F$ can be chosen to satisfy both (1) and

$$
\tag{2}
(A+BF)^r b = 0,
$$

where $r = \dim \mathscr{R}$.

*Proof.* This is a special case of Theorem 4.2 in [10]. We are choosing $F$ so that $\mathscr{R}$ is cyclic with respect to $A+BF$, with generator $b$, and so that $(A+BF)|\mathscr{R}$ is nilpotent.

This last result leads to an interesting characterization of controllability subspaces.

**Lemma 2.** A subspace $\mathscr{R} \subset R^n$ of dimension $r$ is a c.s. if and only if there exist $x(\lambda)\in R^n[\lambda]$ and $u(\lambda)\in R^m[\lambda]$ such that

- (i) $\deg u(\lambda)=k$ and $\deg x(\lambda)=k-1$, for some $k \ge r$;
- (ii) $(\lambda I - A)x(\lambda) = Bu(\lambda)$;
- (iii) If $x(\lambda) = \sum_{i\in k} \lambda^{i-1}x_{i-1}$, then $\mathscr{R} = \operatorname{span}\{x_{i-1},\, i\in \underline{k}\}$.

*Proof. Necessity.* Suppose $\mathscr{R}$ is a c.s. of dimension $r$. Let $b \in \mathscr{B}\cap\mathscr{R}$ and $F$ be chosen to satisfy (1) and (2). Define

$$
u(\lambda) = \sum_{i=0}^{r} \lambda^i u_i \in R^m[\lambda]
\qquad\text{and}\qquad
x(\lambda) = \sum_{i=0}^{r-1} \lambda^i x_i
$$

so that

$$
Bu_r = b,
$$

$$
u_i = F(A+BF)^{r-i-1}b, \qquad 0 \le i \le r-1,
$$

$$
x_i = (A+BF)^{r-i-1}b, \qquad 0 \le i \le r-1.
$$

Then (i) is trivially satisfied; (ii) follows by comparing coefficients of powers of $\lambda$, and by using (2); (iii) follows from (1).

*Sufficiency.* Let $u(\lambda)\in R^m[\lambda]$ and $x(\lambda)\in R^n[\lambda]$ satisfy (i)–(iii). We shall demonstrate that

$$
\tag{3}
A\mathscr{R} \subset \mathscr{R} + \mathscr{B}
$$

and that

$$
\tag{4}
\mathscr{R} = \mathscr{W}_k,
$$

where $\mathscr{W}_0 = 0$, and $\mathscr{W}_i = (A\mathscr{W}_{i-1} + \mathscr{B})\cap\mathscr{R}$ for $i \le k$.

The result will then follow from Theorem 4.1 in [10].

From (ii) it is easily seen that $Ax_i = x_{i-1} - Bu_i$ for $1 \le i \le k-1$, and that $Ax_0 = -Bu_0$; thus (3) follows from (iii).

To demonstrate (4), define subspaces $\mathscr{S}_i$ as

$$
\mathscr{S}_i = \operatorname{span}\{x_{k-1}, x_{k-2}, \cdots, x_{k-i}\} \quad \text{for } i \in \underline{k}.
$$

Clearly, $\mathscr{S}_1 \subset \mathscr{W}_1$; moreover, from (iii) it is easily seen that $\mathscr{S}_i \subset (A\mathscr{S}_{i-1} + \mathscr{B})\cap\mathscr{R}$ for $2 \le i \le k$, whence it follows inductively that $\mathscr{S}_i \subset \mathscr{W}_i$ for all $i \in \underline{k}$. But clearly, $\mathscr{S}_k = \mathscr{R}$, and (4) follows.

**Remark 1.** If a pair $(x(\lambda), u(\lambda))$ can be found which satisfies conditions (i)–(iii) of Lemma 2, and satisfies the additional condition that the coefficients in $x(\lambda)$ are independent, then one can find a matrix $F$ such that $Fx_{i-1}=u_{i-1}$ for all $i \in \underline{k}$. It then follows that $x_{k-1} \in \mathscr{B}\cap\mathscr{R}$ is a cyclic generator for $\mathscr{R}$ with respect to the matrix $A+BF$.

We have thus established a characterization of controllability subspaces in terms of elements of $\ker(\lambda I - A; -B)$, where the matrix $(\lambda I - A; -B)$ is to be interpreted as representing an $R[\lambda]$-module morphism: $R^{m+n}[\lambda] \to R^n[\lambda]$. Elements in $\ker(\lambda I - A; -B)$ may in turn be characterized by the minimal column indices $\{v_i,\, i\in\underline{m}\}$ and a fundamental series $\{z_i(\lambda),\, i\in\underline{m}\}$ associated with the singular pencil of matrices $(\lambda I - A; -B)$. These two sets are determined as follows (see [5, Chap. 12]):

- (i) Let $v_1$ be the least degree of all nonzero elements of $\ker(\lambda I - A; -B)$, and choose $z_1(\lambda)\in\ker(\lambda I - A; -B)$ so that $\deg z_1(\lambda)=v_1$;
- (ii) For each $i$, $1 \le i \le m-1$, after having chosen $\{z_j(\lambda),\, j\le i\}$, we define $v_{i+1}$ to be the least degree of all elements $z(\lambda)\in\ker(\lambda I - A; -B)$ such that $z(\lambda)$ is not an element of the submodule generated by $\{z_j(\lambda),\, j\le i\}$. Then choose $z_{i+1}(\lambda)\in\ker(\lambda I - A; -B)$ so that $\deg z_{i+1}(\lambda)=v_{i+1}$ and so that $z_{i+1}(\lambda)$ is not an element of the submodule generated by $\{z_j(\lambda),\, j\le i\}$.

We shall call the set $\{v_i,\, i\in\underline{m}\}$, so obtained, the set of **Kronecker invariants** of the pair $(A,B)$. Note that by the construction of this set, the $v_i$'s are ordered as $0 \le v_1 \le v_2 \le \cdots \le v_m$. The sets $\{v_i,\,i\in\underline{m}\}$ and $\{z_i(\lambda),\,i\in\underline{m}\}$ enjoy other properties, which we now state.

**Proposition 1.** Let $(A,B)\in R^{n\times n}\times R^{n\times m}$ be a controllable pair such that $\operatorname{rank} B = m$. Then the Kronecker invariants and the fundamental series, as determined above, satisfy:

- (i) *The set $\{v_i,\,i\in\underline{m}\}$ is well-defined and unique;*
- (ii) *$v_i > 0$, all $i\in\underline{m}$;*
- (iii) *$\sum_{i\in\underline{m}} v_i = n$;*
- (iv) *$\{z_i(\lambda),\,i\in\underline{m}\}$ is a set of free generators for $\ker(\lambda I - A; -B)$, and any $z(\lambda)\in\ker(\lambda I - A; -B)$ can be uniquely written as*

$$
z(\lambda) = \sum_{i:\,v_i \le \deg z(\lambda)} z_i(\lambda)\alpha_i(\lambda)
$$

for appropriate $\alpha_i(\lambda)\in R[\lambda]$ such that $\deg \alpha_i(\lambda) \le \deg z(\lambda)-v_i$;

- (v) *The fundamental series $\{z_i(\lambda),\,i\in\underline{m}\}$ is not uniquely determined; however, for each $i$ such that $v_i < v_{i+1}$, the submodule $\mathscr{M}_i \triangleq$ (submodule generated by $\{z_j(\lambda),\, j\le i\}$) is invariant with respect to the choice of fundamental series;*
- (vi) *If each $z_i(\lambda)$ is partitioned as $z_i(\lambda) = (s_i^T(\lambda); t_i^T(\lambda))^T$, where $t_i(\lambda)\in R^m[\lambda]$ and $s_i(\lambda)\in R^n[\lambda]$, then $\deg s_i(\lambda)=v_i-1$ and the collections of coefficients $\{t_{i,j},\,i\in\underline{m}\}$ and $\{s_{i,j};\, 0\le j\le v_i-1,\, i\in\underline{m}\}$ are bases for $R^m$ and $R^n$.*

*Proof.* See references [1], [6], or [7] for (i)–(iii); [2] and [4] for (iv); [5] for (v); and [2, Thm. (4.5–22)] or [9] for (vi).

Now consider the pair $(s_i(\lambda), t_i(\lambda))$, as determined by $z_i(\lambda)$. This pair of polynomial vectors satisfies

$$
(\lambda I - A)s_i(\lambda) = Bt_i(\lambda).
$$

Thus, from statement (vi) of Proposition 1 and from Remark 1, it follows that $\operatorname{span}\{s_{i,j},\,0\le j\le v_i-1\}$ is a c.s. generated by $s_{i,v_i-1}$. We call this c.s. $\mathscr{R}_i$:

$$
\tag{5}
\mathscr{R}_i \triangleq \operatorname{span}\{s_{i,j},\,0\le j\le v_i-1\} \quad \text{for } i\in\underline{m}.
$$

Since $\{s_{i,j};\, 0\le j\le v_i-1,\, i\in\underline{m}\}$ is a basis for $R^n$, it is clear that

$$
\tag{6}
R^n = \mathscr{R}_1 \oplus \cdots \oplus \mathscr{R}_m.
$$

However, because the fundamental series $\{z_i(\lambda),\,i\in\underline{m}\}$ is not unique, the decomposition of $R^n$ via (6) is not unique. In spite of this fact, there are certain properties of the decomposition (6) which are invariant with respect to the choice of fundamental series $\{z_i(\lambda),\,i\in\underline{m}\}$.

**Proposition 2.** The subspaces $\mathscr{V}_i = \mathscr{R}_1 \oplus \cdots \oplus \mathscr{R}_i$ for which $v_i < v_{i+1}$ are invariant with respect to the choice of fundamental series $\{z_i(\lambda),\,i\in\underline{m}\}$.

*Proof.* From Proposition 1, (iv)–(v), it is easily seen that when $v_i < v_{i+1}$, $\operatorname{span}\{s_{k,j};\,0\le j\le v_k-1,\, k\le i\}$ is invariant with respect to the choice of fundamental series $\{z_i(\lambda),\,i\in\underline{m}\}$. This proves the proposition.

**Proposition 3.** The subspace $\mathscr{V}_i = \mathscr{R}_1 \oplus \cdots \oplus \mathscr{R}_i$ for which $v_i < v_{i+1}$ is the maximal c.s. contained in the subspace $A^{-v_i}(\mathscr{B} + \cdots + A^{v_i-1}\mathscr{B})$.

*Proof.* $\mathscr{V}_i$ is obviously a c.s. and is contained in

$$
\mathscr{S}_{v_i} = A^{-v_i}(\mathscr{B} + \cdots + A^{v_i-1}\mathscr{B}).
$$

Let $\mathscr{V}$ be a c.s. larger than $\mathscr{V}_i$. Let $P_i$ denote the projection on $\mathscr{R}_i$ and along $\bigoplus_{j\ne i}\mathscr{R}_j$. Then clearly $P_j\mathscr{V}\ne 0$ for some $j>i$, and since $\mathscr{V}$ is a c.s. we must have $P_j\mathscr{V} = \mathscr{R}_j$. Hence there exists an $x\in\mathscr{V}$ such that $x = \sum_{k,r}\alpha_{k,r}s_{k,r}$ with $\alpha_{j,v_j-1}\ne 0$. But $s_{j,v_j-1}\notin\mathscr{V}_i$ for $j>i$, and as the $s_{i,j}$ are a basis, clearly $x\notin\mathscr{V}_i$, proving the assertion.

Finally, from the fundamental series $\{z_i(\lambda)=(s_i^T(\lambda);t_i^T(\lambda))^T,\,i\in\underline{m}\}$ we can determine a feedback matrix $F$ such that the fundamental series associated with the controllable pair $(A+BF,B)$ is of a particularly simple form; this will then lead to a "canonical" form for $(A,B)$. We define $F$ as follows. Since $\{s_{i,j}\}$ is a basis for $R^n$, there exists a matrix $F$ such that

$$
Fs_{i,j} = t_{i,j}, \qquad 0\le j\le v_i-1,\quad i\in\underline{m}.
$$

It now follows easily that

$$
(\lambda I - A - BF)s_i(\lambda) = B\lambda^{v_i}t_{i,v_i} \qquad \text{for each } i\in\underline{m}.
$$

This last relation completely specifies the maps $A+BF:R^n\to R^n$ and $B:R^m\to R^n$ with respect to the bases $\{s_{i,j}\}$ (in $R^n$) and $\{t_{i,v_i}\}$ (in $R^m$). That is,

$$
Bt_{i,v_i} = s_{i,v_i-1}, \qquad i\in\underline{m},
$$

while

$$
(A+BF)s_{i,j} =
\begin{cases}
s_{i,j-1}, & \text{if } 1\le j\le v_i-1,\quad i\in\underline{m},\\
0, & \text{if } j=0,\quad i\in\underline{m}.
\end{cases}
$$

Thus, with nonsingular matrices $S$ and $G$ defined as

$$
S = (s_{1,0}; s_{1,1}; \cdots; s_{1,v_1-1}; s_{2,0}; \cdots; s_{m,v_m-1})
$$

and

$$
G = (t_{1,v_1}; \cdots; t_{m,v_m}),
$$

it follows that

$$
S^{-1}BG = (e_{v_1^*}; e_{v_2^*}; \cdots; e_{v_m^*}),
$$

$$
S^{-1}(A+BF)S = \text{block diagonal }(H_{v_1}; \cdots; H_{v_m}),
$$

where $H_k$ is $k\times k$ with ones on the superdiagonal and zeros elsewhere.

We shall refer to the pair $(S^{-1}(A+BF)S,\, S^{-1}BG)$ as the **Brunovsky canonical form** for the pair $(A,B)$. In the sequel it will be convenient to work with this canonical form. We note that the fundamental series associated with $(S^{-1}(A+BF)S, S^{-1}BG)$ is

$$
\{z_i(\lambda) = (s_i^T(\lambda); t_i^T(\lambda))^T,\, i\in\underline{m}\}
$$

with

$$
t_i(\lambda) = \lambda^{v_i}\hat{e}_i, \qquad i\in\underline{m},
$$

$$
s_i(\lambda) = \lambda^{v_i-1}e_{v_i^*} + \cdots + e_{v_i^* - v_i + 1}, \qquad i\in\underline{m},
$$

where $\hat{e}_i$ is the $i$th standard unit vector in $R^m$. For this choice of fundamental series the subspaces $\mathscr{R}_i \subset R^n$ are given as

$$
\mathscr{R}_i = \operatorname{span}\{e_{v_i^*}, \cdots, e_{v_i^*-v_i+1}\}, \qquad i\in\underline{m}.
$$

## 3. Dimensions of controllability subspaces

We consider a controllable pair $(A,B)$ in the Brunovsky canonical form. As indicated in the previous section, this form is compatible with a natural direct sum decomposition of the state space into controllability subspaces $\mathscr{R}_i$, $i\in\underline{m}$, with

$$
\mathscr{R}_j = \operatorname{span}\{e_{v_j^*-v_j+1}, \cdots, e_{v_j^*}\},
$$

where $e_j$ is the $j$th unit vector in the canonical basis for $R^n$. Denote the projection on $\mathscr{R}_i$ and along $\bigoplus_{j\ne i}\mathscr{R}_j$ by $P_i$, $i\in\underline{m}$, and the set $\{j\in\underline{m}\mid P_j\mathscr{R}\ne 0\}$ by $M(\mathscr{R})$ for any subspace $\mathscr{R}$. Then we have the following bound on the dimension of a c.s.

**Lemma 3.** Let $\mathscr{R}$ be a c.s. of the pair $(A,B)$. Then $\dim \mathscr{R} \ge \max\{v_j\mid j\in M(\mathscr{R})\}$.

*Proof.* Since $\mathscr{R}$ is a c.s., $\mathscr{R} = \{A+BF|\mathscr{B}\cap\mathscr{R}\}$ for some appropriate $F$. Further, we know that $\mathscr{R}$ may be singly generated by a $b\in\mathscr{B}\cap\mathscr{R}$. Pick such a $b = \sum_{i\in\underline{m}}\alpha_i e_{v_i^*}$, since the $e_{v_i^*}$ are a basis for $\mathscr{B}$. By the particular form of $(A,B)$ it is obvious that the c.s. $\mathscr{R}$ is spanned by the columns of the matrix

$$
W =
\begin{pmatrix}
\cdot & \cdot & \alpha_1 & \cdot & \cdot \\
\cdot & \alpha_1 & \beta_1 & \cdot & \cdot \\
\cdot & \alpha_1 & \beta_1 & \gamma_1 & \cdot & \cdot \\
\alpha_1 & \beta_1 & \gamma_1 & \delta_1 & \cdot & \cdot \\
\cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\
\cdot & \cdot & \cdot & \alpha_m & \cdot & \cdot \\
\cdot & \cdot & \alpha_m & \beta_m & \cdot & \cdot \\
\cdot & \alpha_m & \beta_m & \gamma_m & \cdot & \cdot \\
\alpha_m & \beta_m & \gamma_m & \delta_m & \cdot & \cdot
\end{pmatrix},
$$

where only possibly nonzero elements have been shown. It is obvious that $P_i\mathscr{R}=0$ iff the $v_i^* - v_i + 1$ through $v_i^*$ rows of $W$ are identically zero. Thus if $P_i\mathscr{R}\ne 0$, $W$ must contain a nonsingular lower triangular submatrix of dimension $v_i\times v_i$, hence must have column rank $\ge v_i$, which proves the lemma.

**Remark 2.** This lemma is the state space analog of Proposition 1 (iv). The dimension of a c.s. may be similarly bounded from above.

**Lemma 4.** Let $\mathscr{R}$ be a c.s. of the pair $(A,B)$. Then

$$
\dim \mathscr{R} \le \sum_{j\in M(\mathscr{R})} v_j.
$$

*Proof.* Clearly $P_i\mathscr{R}=0$ for $i\notin M(\mathscr{R})$. Then $\big(\sum_{i\notin M(\mathscr{R})}P_i\big)\mathscr{R}=0$ or equivalently $\mathscr{R}\subset\ker\big(\sum_{i\in M(\mathscr{R})}P_i\big)=\sum_{j\in M(\mathscr{R})}\mathscr{R}_j$. Since the $\mathscr{R}_j$'s are independent, this latter subspace has dimension $\sum_{j\in M(\mathscr{R})}v_j$ and contains $\mathscr{R}$, proving the lemma.

**Theorem 1.** Let $V = \{v_1,\cdots,v_m\}$ be the set of Kronecker invariants of $(A,B)$. Then there exists a c.s. $\mathscr{R}$ of dimension $p$ iff

$$
\tag{7}
\max\{v_i\mid v_i\in U\} \le p \le \sum_{v_i\in U} v_i
$$

for some subset $U$ of $V$.

*Proof. Necessity.* Let $U = \{v_i\mid i\in M(\mathscr{R})\}$. Then the result is immediate from the preceding two lemmas.

*Sufficiency.* Given a subset $U\subset V$ and a $p$ satisfying (7) we shall construct a c.s. $\mathscr{R}$ of dimension $p$ by summing the c.s. $\mathscr{R}_i$ possibly with some "overlap". First order the elements of $U$ in decreasing size $(v_{i_1},\cdots,v_{i_s})$ and define $s$ as the smallest integer such that $\eta_s = \sum_{j\le s}v_{i_j}$ is greater than or equal to $p$. If $p=\eta_s$ then we may construct a c.s. of dimension $p$ by forming the direct sum of c.s. $\mathscr{R}_{i_1}\oplus\cdots\oplus\mathscr{R}_{i_s}$. If $\eta_s$ exceeds $p$, then for $s>2$, we shall construct a c.s. of the form $\mathscr{R}_{i_1}\oplus\cdots\oplus\mathscr{R}_{i_{s-2}}\oplus\mathscr{Q}$, where $\mathscr{Q}$ is a c.s. of dimension $p-\eta_{s-2}$ obtained by "overlapping" the c.s. $\mathscr{R}_{i_{s-1}}$ and $\mathscr{R}_{i_s}$. Finally if $\eta_s>p$ and $s=2$, then we shall construct a c.s. of the form $\mathscr{Q}$ above. Hence it suffices to consider only the cases $p=\eta_s$ for some $s$, or $\eta_1<p<\eta_2$.

To prove the first case we need only show how to form the direct sum of two c.s., say $\mathscr{R}_i\oplus\mathscr{R}_j$. Consider the feedback which changes the $(v_j^*, v_i^*-v_i+1)$-element of $A$ from zero to one. With this feedback, $(A+BF)^{v_i}e_{v_i^*}=e_{v_j^*}$; that is, the c.s. $\mathscr{R}_i\oplus\mathscr{R}_j$ is generated by the generator of $\mathscr{R}_i$.

To prove the second case let $p<v_i+v_j$. By choosing feedback such that the $(v_j^*, v_i^*-(p-v_j-1))$-element of $A$ is changed from zero to one, it is easily seen that the resulting c.s. generated by $e_{v_i^*}$ is spanned by the set of $p$ independent vectors

$$
\left\{e_{v_i^*}, e_{v_i^*-1}, \cdots, e_{v_i^*-p+v_j}+e_{v_j^*}, \cdots, e_{v_i^*-v_i+1}+e_{v_j^*-v_i+v_j+p+1},\ e_{v_j^*-v_i+v_j+p}, \cdots, e_{v_j^*-v_j+1}\right\}
$$

and hence is of dimension $p$.

**Remark 3.** The constructions used to prove sufficiency have an analog in the context of Lemma 2. Let $[s_i^T(\lambda); t_i^T(\lambda)]^T$ be the $i$th free generator of $\ker[\lambda I-A;-B]$, that is, $\mathscr{R}_i$ is the span of the coefficients of $s_i(\lambda)$. Then for any $k\ge 0$ it is easily seen that

$$
(\lambda I - A)(\lambda^k s_i(\lambda)+s_j(\lambda)) = B(\lambda^k t_i(\lambda)+t_j(\lambda)).
$$

When $k=v_j$, the spans of the coefficients of $\lambda^{v_j}s_i(\lambda)+s_j(\lambda)$ yield the c.s. $\mathscr{R}_i\oplus\mathscr{R}_j$. For $0<k\le v_j\le v_i$ the span of the coefficients of $\lambda^k s_i(\lambda)+s_j(\lambda)$ is a c.s. of dimension $v_i+k$ of the form $\mathscr{Q}$ in the proof of Theorem 1. It should be clear that these constructions are not unique. We may replace $\lambda^k$ by $\alpha(\lambda)$, any polynomial of degree $k$, and achieve controllability subspaces, albeit possibly different ones, of the appropriate dimensions.

Theorem 1 indicates that the possible dimensions of controllability subspaces of a pair $(A,B)$ are directly determined by the Kronecker invariants of $(A,B)$. If one considers the Kronecker invariants to be represented by line segments of length $v_i$,

```
├── v₁ ──┤
├──── v₂ ────┤
       ⋮
├──────────── v_m ────────────┤
```

then the theorem states that the corresponding dimensions of possible c.s. are given by the lengths of line segments obtained by joining together some of the above line segments, with the possibility of integral overlap, for example,

```
├── v₁ ──┤├── v₂ ──┤   or   ├── v₁ ──┤├──── v₃ ────┤
```

etc.

Furthermore we have the following corollary.

**Corollary 1.** If for some $j\in\underline{m-1}$, $v_{j+1}>v_j^*+1$, then there exists no c.s. of dimension $p$, where $p$ is any integer satisfying $v_j^*<p<v_{j+1}$.

*Proof.* This follows directly from Theorem 1, as any subset of the set $U=\{v_l\mid l\le j\}$ clearly fails the upper bound in (7), while if $U$ includes any elements $v_k$ for $k>j$, it likewise fails the lower bound in (7).

For example, if the Kronecker invariants of $(A,B)$ are $(1,2,5)$, then c.s. of dimensions $1,2,3,5,6,7,8$ exist, whereas no c.s. of dimension $4$ exists.

The constructions of Theorem 1 and Remark 3 are suggestive of the uniqueness of c.s. of certain dimensions. Indeed, we have the following.

**Corollary 2.** Let $\mathscr{R}$ be a c.s. of dimension $p$. Then $\mathscr{R}$ is the unique c.s. of dimension $p$ iff $p=v_j^*<v_{j+1}$ for some $j\in\underline{m-1}$. In particular, if $v_2\ne v_1$, then $\mathscr{R}_1$ is the unique c.s. of dimension $v_1$.

*Proof. Sufficiency.* Assume $\dim\mathscr{R}=p=v_j^*<v_{j+1}$. By Lemma 3, $P_i\mathscr{R}=0$ for $i>j$, so $\mathscr{R}\subset\bigcap_{i>j}\ker P_i=\bigoplus_{k\le j}\mathscr{R}_k$. Since $\dim\bigoplus_{k\le j}\mathscr{R}_k=v_j^*$ we must have $\mathscr{R}=\bigoplus_{k\le j}\mathscr{R}_k$. However, regardless of the nonuniqueness of the set of c.s. $\mathscr{R}_k$, the subspace $\bigoplus_{k\le j}\mathscr{R}_k$ is unique by Proposition 2, since $v_{j+1}>v_j$.

*Necessity.* We will show that if there exists any c.s. of dimension $p$ such that either $p\ne v_j^*$ or $p=v_j^*<v_{j+1}$ for any $j\in\underline{m}$, then there are, in general, many different c.s. of identical dimension.

Consider first the case $p\ne v_j^*$ for any $j\in\underline{m}$. Assume there exists a c.s. of dimension $p$. Define $s$ to be the largest integer such that $v_s^*<p$, and let $q=p-v_s^*$. Then by Remark 3 following Theorem 1 it is clear that given the polynomial vector

$$
u_\alpha(\lambda) = \lambda^{v_s^*-1+q}t_s(\lambda) + \lambda^{v_s^*-2+q}t_{s-1}(\lambda) + \cdots + \lambda^q t_1(\lambda) + \alpha t_{s+1}(\lambda)
$$

for any nonzero $\alpha\in R$, the span of the coefficients of the corresponding $x_\alpha(\lambda)$ is a c.s. of dimension $p$. Further, since $q<v_{s+1}$, it is clear that for $\alpha\ne\beta$, both non-zero, the spans of the coefficients of $x_\alpha(\lambda)$ and $x_\beta(\lambda)$ differ.

Now assume $p=v_j^*$ for some $j\in\underline{m}$, but $v_j^*\ge v_{j+1}$. Clearly the polynomial vector

$$
u_0(\lambda) = \lambda^{v_j^*-1}t_j(\lambda) + \lambda^{v_j^*-2}t_{j-1}(\lambda) + \cdots + t_1(\lambda)
$$

has an associated $x_0(\lambda)$, the span of whose coefficients is given by $\mathscr{R}_1\oplus\cdots\oplus\mathscr{R}_j$, a c.s. of dimension $p$. However, the polynomial vector

$$
u_\alpha(\lambda) = \lambda^{v_j^*-1}t_j(\lambda) + \lambda^{v_j^*-2}t_{j-1}(\lambda) + \cdots + t_1(\lambda) + \alpha t_{j+1}(\lambda),
$$

where $\alpha\in R$, has an associated $x_\alpha(\lambda)$ whose coefficients span a different c.s. of dimension $p$. Further, if $\alpha\ne\beta$, then the c.s. associated with $u_\alpha(\lambda)$ differs from that associated with $u_\beta(\lambda)$.

Note that we have shown that for systems defined over the reals (or any other uncountably infinite field), if there exists more than one c.s. of a given dimension, then there exists an uncountable number. In the example with Kronecker invariants $1,2,5$, the c.s. of dimensions $1,3$ and $8$ are unique, while there are nondenumerably many c.s. of dimensions $2,5,6$ and $7$.

## 4. Minimal dimension controllability subspaces

In §2 a characterization of controllability subspaces in terms of the free generators of the kernel of the singular pencil of matrices $[\lambda I-A;-B]$ was developed. Using this representation, requirements on the possible dimensions of c.s. were derived in §3. In this section we wish to explore c.s. constrained to contain, or cover, a given subspace; in particular we will construct minimal dimension c.s. covering subspaces of $\mathscr{B}$.

Consider an element $b\in\mathscr{B}$. If $\mathscr{R}$ is a c.s. containing $b$, then by Lemma 1, there exists a feedback map $F$ such that

$$
\mathscr{R} = \operatorname{span}\{b,(A+BF)b,\cdots,(A+BF)^{n-1}b\},
$$

and $(A+BF)^n b = 0$. Combining this fact with the characterization of c.s. in terms of the pencil of matrices, we may view any c.s. $\mathscr{R}$ containing $b$ as the span of a trajectory generated by driving $b$ to zero. Clearly then, the minimal dimension c.s. containing $b$ are in $1$–$1$ correspondence with the spans of the trajectories arising from driving $b$ to zero in a minimal number of steps, i.e., the spans of trajectories $\{b,(A+BF)b,\cdots\}$ that contain a minimal number of nonzero vectors.

It should be noted that driving a vector $x$ to zero in $r$ steps implies the construction of an input string $\{u_{r-1},\cdots,u_0\}$ such that if

$$
x_{r-1}=x \quad\text{and}\quad x_{r-i-1}=Ax_{r-1}+Bu_{r-i}, \qquad 1\le i\le r,
$$

then $x_{-1}=0$. If $x\in\mathscr{B}$, this is of course equivalent to finding $u(\lambda)=\sum_{i=0}^r\lambda^i u_i$ and $x(\lambda)=\sum_{i=0}^{r-1}\lambda^i x_i$ such that $Bu_r=x$ and $(\lambda I-A)x(\lambda)=Bu(\lambda)$. It surely suffices to find a feedback map $F$ such that

$$
x_{r-1}=x \quad\text{and}\quad x_{r-i-1}=(A+BF)x_{r-i}, \qquad 1\le i\le r,
$$

then $x_{-1}=0$.

If we wish to drive an element $b\in\mathscr{B}$ to zero in a minimal number of steps, it seems natural that the span of the trajectory excluding $b$ should be independent of $\mathscr{B}$. This is indeed the case.

**Lemma 5.** Let $b\in\mathscr{B}$. If there exists a feedback map $F$ and a trajectory $\{b,(A+BF)b,\cdots,(A+BF)^{n-1}b\}$ such that $\sum_{i=1}^r\alpha_i(A+BF)^i b$, $\alpha_r\ne 0$, is an element of $\mathscr{B}$ for $1\le r\le n-1$, then $b$ may be driven to zero in $r$ or fewer steps.

*Proof.* We write $\hat b = \sum_{i=1}^r\alpha_i(A+BF)^i b$ and assume without loss of generality that $\alpha_r=1$. Since $B$ has full rank there exist unique elements $\hat u$ and $u$ such that $\hat u=B^{-1}\hat b$, $u=B^{-1}b$. Consider the input string $u_i$, $r-1\ge i\ge 0$, defined by

$$
u_{r-1}=Fb+\alpha_{r-1}u,
$$

$$
u_{r-2}=F(A+BF)b+\alpha_{r-1}Fb+\alpha_{r-2}u,
$$

$$
\vdots
$$

$$
u_0 = F(A+BF)^{r-1}b + \alpha_{r-1}F(A+BF)^{r-2}b + \cdots + \alpha_1 Fb - \hat u.
$$

Now let $x_{r-1}=b$, and consider the sequence generated by the recursion

$$
x_{r-i-1}=Ax_{r-i}+Bu_{r-i}, \qquad 1\le i\le r.
$$

Then it follows that

$$
x_{-1}=(A+BF)^r b + \alpha_{r-1}(A+BF)^{r-1}b + \cdots + \alpha_1(A+BF)b - \hat b = 0,
$$

and hence $b$ may be driven to zero in $r$ steps.

Note that Lemma 5 implies that for $b\in\mathscr{B}$, if $\mathscr{R}$ is a c.s. of minimum dimension containing $b$, then $\mathscr{R}\cap\mathscr{B}=\ell$. It is now natural to ask: What is the minimum dimension of a c.s. covering an element $x\in\mathscr{X}$? For $x\in\mathscr{B}$, we can easily answer this query.

Recall that $M(\mathscr{R})$ was defined as the set $\{j\in\underline{m}\mid P_j\mathscr{R}\ne 0\}$ for any subspace $\mathscr{R}$.

**Lemma 6.** Let $b\in\mathscr{B}$. Then the minimum dimension of a c.s. containing $b$ is given by $\mu=\max\{v_j\mid j\in M(\ell)\}$.

*Proof.* If $\mathscr{R}$ is a c.s. containing $b$, then by Lemma 3, $\dim\mathscr{R}\ge\mu$. Now consider the trajectory $(b,Ab,\cdots,A^{n-1}b)$, where $A,B$ are assumed in the Brunovsky canonical form. Since $b=\sum_{j\in M(\ell)}\gamma_j e_{v_j^*}$ and $A^{v_j}e_{v_j^*}=0$, it follows that $A^n b=0$, yielding a covering c.s. of dimension $\mu$.

We now can turn our attention to the case where we desire to cover an arbitrary subspace of $\mathscr{B}$. As we shall need a minor construction, we first prove a lemma to motivate that construction.

**Lemma 7.** Let $b_1$ and $b_2$ be elements of $\mathscr{B}$ such that $M(\ell_1)\cap M(\ell_2)=\varnothing$, and denote $\max\{v_j\mid j\in M(\ell_i)\}$ by $\mu_i$, $i\in\underline{2}$. Then if $\mathscr{R}$ is a c.s. covering $b_1$ and $b_2$, $\dim\mathscr{R}\ge\mu_1+\mu_2$.

*Proof.* If $\mathscr{R}$ contains $b_1$ and $b_2$, then $\mathscr{R}$ contains c.s. which may be generated by $b_1$ and $b_2$ respectively (by Lemma 1). Then it follows that for some $F_1,F_2$,

$$
\operatorname{span}\{b_1,(A+BF_1)b_1,\cdots,(A+BF_1)^{n-1}b_1, b_2,\cdots,(A+BF_2)^{n-1}b_2\}\subset\mathscr{R}.
$$

Recalling that $\{s_{i,v_i-1},\,i\in\underline{m}\}$ is a basis for $\mathscr{B}$, we may write

$$
b_1 = \sum_{j\in M(\ell_1)} \gamma_{1j}s_{j,v_j-1}
\qquad\text{and}\qquad
b_2 = \sum_{j\in M(\ell_2)} \gamma_{2j}s_{j,v_j-1}.
$$

Since the lemma obviously follows for $\mu_1=\mu_2=1$, we may assume that for some $i$, $\mu_i>1$. Now for $\mu_i>1$ we have

$$
\tag{8}
(A+BF_i)b_i = \sum_{j\in M(\ell_i)} \gamma_{ij}s_{j,v_j-2} + \sum_{k\in\underline{m}}\alpha_{ik}s_{k,v_k-1} \ne 0
$$

for some $\alpha_{ik1}$, $k\in\underline{m}$. Note that the second term on the right is an element of $\mathscr{B}$ and represents the arbitrary nature of the feedback map $F_i$. Continuing, we have for $\mu_i>r$,

$$
\tag{9}
(A+BF_i)^r b_i = \sum_{j\in M(\ell_i)} \gamma_{ij}s_{j,v_j-r-1} + \sum_{p\in\underline{r}}\sum_{k\in\underline{m}}\alpha_{ikp}s_{k,v_k-(r+1-p)} \ne 0
$$

for some $\alpha_{ikp}$, $k\in\underline{m}$, $p\in\underline{r}$, where $s_{i,j}\triangleq 0$ for $j<0$. Comparing the forms of elements from (8) and (9), it follows from the hypothesis $M(\ell_1)\cap M(\ell_2)=\varnothing$ and the fact that $\{s_{i,j};\,0\le j\le v_i-1,\,i\in\underline{m}\}$ is a basis for $R^n$, that the vectors

$$
\{b_1,(A+BF_1)b_1,\cdots,(A+BF_1)^{\mu_1-1}b_1,\, b_2,\cdots,(A+BF_2)^{\mu_2-1}b_2\}
$$

are independent, and hence $\mathscr{R}$ is of dimension $\ge\mu_1+\mu_2$.

**Corollary 3.** Let $b_1$ and $b_2$ be elements of $\mathscr{B}$ such that $M(\ell_1)\cap M(\ell_2)=\varnothing$. If $\mathscr{V}_1$ and $\mathscr{V}_2$ are minimal dimension covering c.s. for $b_1$ and $b_2$ respectively, then $\mathscr{V}_1\cap\mathscr{V}_2=0$ and $\mathscr{V}_1\oplus\mathscr{V}_2$ is a minimal dimension c.s. covering $\operatorname{span}\{b_1,b_2\}$.

*Proof.* The proof follows immediately from Lemmas 6 and 7.

**Theorem 2.** Let $\mathscr{D}\subset\mathscr{B}$ and $\{b_1,\cdots,b_k\}$ be a basis for $\mathscr{D}$ such that $M(\ell_i)\cap M(\ell_j)=\varnothing$ for $i\ne j$, $i,j\in\underline{k}$. Then if $\mathscr{R}$ is a c.s. covering $\mathscr{D}$, then $\dim\mathscr{R}\ge\sum_{i\in\underline{k}}\mu_i$. Furthermore, if $\mathscr{V}_i$ is a minimal dimension c.s. covering $b_i$, $i\in\underline{k}$, then $\{\mathscr{V}_i,\,i\in\underline{k}\}$ is an independent set of subspaces, and $\mathscr{V}_1\oplus\cdots\oplus\mathscr{V}_k$ is a minimal dimension c.s. containing $\mathscr{D}$.

*Proof.* First we note that any $\mathscr{D}\subset\mathscr{B}$ has such a basis. Let $\{d_1,\cdots,d_k\}$ be any basis for $\mathscr{D}$ and let $D$ be a matrix whose columns are given by the $\{s_{i,v_i-1};\,i\in\underline{m}\}$ with respect to the basis for $\mathscr{B}$. Then by applying elementary column operations, it is possible to transform $D$ to a matrix $D_0$ whose columns are a basis for $D$ and have the desired property (only one nonzero entry per row).

By expanding the argument of Lemma 7 to the case where for appropriate $F_1,\cdots,F_k$,

$$
\operatorname{span}\{b_1,\cdots,(A+BF_1)^{n-1}b_1,\cdots,b_k,\cdots,(A+BF_k)^{n-1}b_k\}\subset\mathscr{R},
$$

it is straightforward to show that $\mathscr{R}$ contains a subspace of dimension $\sum_{i\in\underline{k}}\mu_i$. Furthermore, it is clear that $\sum_{i\in\underline{k}}\mathscr{V}_i$ is a c.s. covering $\mathscr{D}$, hence

$$
\dim\left(\sum_{i\in\underline{k}}\mathscr{V}_i\right)\ge\sum_{i\in\underline{k}}\mu_i=\sum_{i\in\underline{k}}\dim\mathscr{V}_i,
$$

which implies that the $\mathscr{V}_i$, $i\in\underline{k}$, are independent subspaces.

**Remark 4.** It has been noted by one of the reviewers that the results of Theorem 2 are encompassed by Theorem 2.1 of [11]. That is, finding an $(A,B)$-invariant subspace $\mathscr{W}$ of least dimension such that $\mathscr{W}$ contains $\mathscr{D}$ is equivalent to finding a c.s. of minimal dimension containing $\mathscr{D}$ when $\mathscr{D}\subset\mathscr{B}$.

## 5. Conclusions

The description of controllability subspaces in terms of the kernel of the singular pencil of matrices $(\lambda I-A;-B)$ extends the notion of a c.s. presented in [10], and provides a basic link between c.s. and structural properties of linear systems. In addition, the pencil of matrices presents an alternative, and algebraically appealing determination of the canonical form of Brunovsky.

In §3 we showed how the Kronecker invariants completely specify the dimensions of possible c.s. It is to be noted that, generically, all the Kronecker invariants will be either $[n/m]$ or $[n/m]+1$, where $[a]$ is the largest integer not greater than $a$, in which case there should be considerable freedom in the construction of c.s. (see [3] and/or [7]). However, the results of that section allow one to ascertain that particular systems are structurally not decoupleable by state feedback, which strengthens the results of [10].

The ideas on minimal dimension c.s. developed in §4 are interesting in terms of limiting the effect of a system input, and in the dual sense of observability subspaces, for the determination of limited order observers. The general problem suggested in that section, finding minimal dimension c.s. containing arbitrary subspaces of $\mathscr{X}$, remains an open issue subject to further investigation.

## Acknowledgment

The authors wish to thank Dr. Sanjoy K. Mitter for his helpful comments during the course of this research.

## REFERENCES

[1] P. BRUNOVSKY, *A classification of linear controllable systems*, Kybernetika, 3 (1970), pp. 173–187.

[2] A. E. ECKBERG, *Algebraic system theory with application to decentralized control*, Ph.D. thesis, Mass. Inst. of Tech., Cambridge, Mass., 1973.

[3] E. FABIAN AND W. M. WONHAM, *Generic solvability of the decoupling problem*, Control System Rep. 7301, Univ. of Toronto, 1973.

[4] G. D. FORNEY, *Minimal bases of rational vector spaces with applications to multivariable linear system*, this Journal, 13 (1795), pp. 493–520.

[5] F. R. GANTMACHER, *The Theory of Matrices*, vol. II, Chelsea, New York, 1960.

[6] R. E. KALMAN, *Kronecker invariants and feedback*, Proc. of Conf. on Ordinary Diff. Eq., NRL Math. Res. Cent., 1971.

[7] V. M. POPOV, *Invariant description of linear, time-invariant controllable system*, this Journal, 10 (1972), pp. 252–264.

[8] H. H. ROSENBROCK, *State Space and Multivariable Theory*, Nelson–Wiley, London, 1970.

[9] W. A. WOLOVICH AND P. L. FALB, *On the structure of multivariable systems*, this Journal, 7 (1969), pp. 437–451.

[10] W. M. WONHAM AND A. S. MORSE, *Decoupling and pole assignment in linear multivariable systems: A geometric approach*, this Journal, 8 (1970), pp. 93–100.

[11] ——, *Feedback invariants of linear multivariable systems*, Automatica, 8 (1972), pp. 1–18.
