# Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger

**Tyrone Fernando**

*arXiv:2609.37992v1 [eess.SY], 29 Sep 2026*

> T. Fernando is with the Department of Electrical, Electronic and Computer Engineering, University of Western Australia (UWA), 35 Stirling Highway, Crawley, WA 6009, Australia. (email: tyrone.fernando@uwa.edu.au)

---

## Abstract

This paper gives an order-by-order characterization of linear functional observers between the minimum dimension permitted by the algebraic observer condition and the upper endpoint determined by functional observability. Functional observability indices determine the minimum algebraically admissible order

$$
q_0=\sum_{j=1}^{r}\eta_j,
$$

where $r$ is the number of independent functionals to be estimated and $\eta_j$ is the functional observability index associated with the $j$th functional. For an $n$-dimensional system with $p$ independent measured outputs, let $n_0$ denote the rank of the observability matrix. Under functional observability, the upper endpoint of the functional-observer order range is $n_0-p$. The algebraic and spectral observer conditions are characterized at each prescribed order between these two endpoints. A nullspace representation in the original state space yields rank and matrix-pencil characterizations of the algebraic and spectral conditions, respectively. The minimum observer order is obtained as the smallest spectrally feasible order in the resulting order spectrum. The two endpoints include the classical Darouach and Luenberger orders as special cases: the lower endpoint reduces to the Darouach order when $q_0=r$, while, under complete observability, the upper endpoint reduces to the Luenberger order $n-p$.

**Index Terms**— Functional observers, functional observability indices, minimum-order observer, functional observability, Luenberger observer, Darouach observer.

---

## I. Introduction

Functional observers estimate prescribed linear functions of the state without necessarily reconstructing the complete state. Their dimension may therefore be substantially smaller than that required for state observation [1]. The determination of the smallest possible observer dimension has consequently received sustained attention; see, among others, [2]–[13]. More recently, functional-observer theory has been extended to large-scale and interconnected systems [14]–[16], networked systems [17]–[20], sampled-data systems [21] and nonlinear systems [22]–[24].

Consider the linear system

$$
\dot{x}(t)=Ax(t)+Bu(t),\qquad y(t)=Cx(t),
$$

and the prescribed functional

$$
z(t)=Lx(t).
$$

Let $n$ denote the state dimension, $p=\operatorname{rank}C$, and let $r$ denote the number of independent functional rows modulo the measured output. The dimension $r$ is the natural lower bound on the observer order and is the order of the classical Darouach observer [8].

In our previous work [25], the functional observability indices were used to determine the minimum dimension permitted by the algebraic observer condition. If $\eta_1,\ldots,\eta_r$ are the functional observability indices associated with the $r$ functional rows, this dimension is

$$
q_0=\sum_{j=1}^{r}\eta_j\ge r.
$$

The same construction gives the complete family of order-$q_0$ augmented functional matrices satisfying the algebraic condition, with observer existence at this order determined by a spectral rank condition.

At the opposite end, let

$$
n_0:=\operatorname{rank}\mathcal{O}_C,
$$

where $\mathcal{O}_C$ is the observability matrix of $(A,C)$. Under functional observability, we show that the lower and upper endpoints of the admissible functional-observer order range are $q_0$ and $n_0-p$, respectively. Hence

$$
r\le q_0\le \nu_{\min}\le n_0-p\le n-p.
$$

The classical Darouach and reduced-order Luenberger observer orders arise as the limiting cases of these endpoints: $q_0=r$ gives the Darouach order, whereas, when $(A,C)$ is observable, $n_0=n$ and the upper endpoint becomes $n-p$, the order of the classical reduced-order Luenberger observer.

The question addressed in this paper is what lies between the algebraic lower endpoint $q_0$ and the functional-observability upper endpoint $n_0-p$. In particular, if every algebraically admissible realization at order $q_0$ fails the spectral condition, at which subsequent orders can a functional observer exist, and can existence at each such order be characterized without prescribing a particular augmentation mechanism?

The first main result concerns the algebraically admissible orders between these two endpoints. Starting from the minimum algebraic order $q_0$, the admissible orders are characterized up to the functional-observability endpoint $n_0-p$. The second main result gives an exact matrix characterization of the algebraic and spectral observer conditions at an arbitrary prescribed order $q$. For each order $q$, a full-column-rank matrix $Z$ is used to represent the nullspace associated with a reduced order-$q$ realization. The analysis is carried out entirely in the original $n$-dimensional state space. The algebraic condition becomes a rank test involving $Z$ and a basis of $\ker(CAZ)$, while the spectral condition becomes an equivalent rank condition on a matrix pencil.

The principal contributions are therefore as follows. First, the complete algebraically admissible family is characterized at every prescribed admissible order, not only at the minimum algebraic order $q_0$. Second, the algebraic and spectral observer conditions are converted into dual nullspace tests expressed entirely in the original state coordinates. Third, a finite matrix-chart parameterization covers all admissible nullspaces at a prescribed order, so failure of the tests over all charts proves nonexistence at that order. Fourth, these fixed-order results are assembled into a complete characterization of the feasible-order spectrum $\Sigma_{FO}(L)$ and hence of the minimum functional-observer order. Finally, the minimum-order characterization of our previous work [25] is recovered explicitly as the specialization $q=q_0$.

The resulting theory characterizes the functional-observer order spectrum between $q_0$ and $n_0-p$, recovering the classical Darouach and Luenberger orders as its two limiting cases. The minimum observer order $\nu_{\min}$ is then obtained as the smallest order in this spectrum satisfying both the algebraic and spectral observer conditions.

---

## II. Notation and Problem Formulation

### A. Notation

For a matrix $M$, $\operatorname{row}(M)$, $\operatorname{rank}(M)$, $\ker(M)$, $\operatorname{im}(M)$ and $\operatorname{eig}(M)$ denote its row space, rank, nullspace, column space, and spectrum (set of eigenvalues), respectively. The symbol $I$ denotes the identity matrix when its dimension is clear from context; otherwise, $I_k$ denotes the $k\times k$ identity matrix.

Let

$$
\mathcal{O}_C:=\begin{pmatrix}C\\ CA\\ \vdots\\ CA^{n-1}\end{pmatrix},
\qquad
\mathcal{O}_L:=\begin{pmatrix}L\\ LA\\ \vdots\\ LA^{n-1}\end{pmatrix},
$$

denote the observability matrices of $(A,C)$ and $(A,L)$, respectively. We also use a full-column-rank matrix $V$ satisfying

$$
\operatorname{im}V=\ker\begin{pmatrix}C\\ CA\end{pmatrix}. \tag{1}
$$

All nullspaces are taken over $\mathbb{R}$ unless complex values of $\lambda$ are involved, in which case the corresponding complexified spaces are understood.

### B. Problem Formulation

Consider the linear time-invariant system

$$
\dot{x}(t)=Ax(t)+Bu(t),\qquad y(t)=Cx(t),
$$

where

$$
A\in\mathbb{R}^{n\times n},\quad B\in\mathbb{R}^{n\times m},\quad C\in\mathbb{R}^{p\times n}.
$$

The functional to be estimated is

$$
z(t)=Lx(t),\qquad L\in\mathbb{R}^{r\times n}.
$$

Throughout, redundant measured outputs and redundant functional rows are removed so that

$$
\operatorname{rank}(C)=p,\qquad \operatorname{rank}\begin{pmatrix}C\\ L\end{pmatrix}=p+r.
$$

Thus, components of $L$ already contained in $\operatorname{row}(C)$ are excluded from the functional estimation problem.

Recall that

$$
n_0=\operatorname{rank}(\mathcal{O}_C)
$$

is the dimension of the observable part of $(A,C)$. Functional observability is characterized by [26]

$$
\operatorname{rank}\begin{pmatrix}\mathcal{O}_C\\ \mathcal{O}_L\end{pmatrix}=\operatorname{rank}(\mathcal{O}_C)=n_0.
$$

The original $n$-dimensional state-space representation is retained throughout; no separate $n_0$-dimensional state realization is introduced.

Let $\mathcal{L}\in\mathbb{R}^{q\times n}$ be an augmented functional matrix of order $q$. The prescribed functional $Lx(t)$ is required to be recoverable from $\mathcal{L}x(t)$ and the measured output $Cx(t)$. Equivalently,

$$
\operatorname{row}(L)\subseteq\operatorname{row}\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}.
$$

In rank form, this condition is

$$
\operatorname{rank}\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}=\operatorname{rank}\begin{pmatrix}C\\ L\end{pmatrix}.
$$

A reduced order-$q$ realization further satisfies

$$
\operatorname{rank}\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}=p+q.
$$

Thus, the observer order is determined directly by the rank increase produced by adjoining $\mathcal{L}$ to $C$. For estimating the augmented functional $\mathcal{L}x(t)$, the **algebraic observer condition** is

$$
\operatorname{rank}\begin{pmatrix}\mathcal{L}A\\ \mathcal{L}\\ CA\\ C\end{pmatrix}
=
\operatorname{rank}\begin{pmatrix}\mathcal{L}\\ CA\\ C\end{pmatrix}, \tag{A}
$$

and the **spectral observer condition** is

$$
\operatorname{rank}\begin{pmatrix}\lambda\mathcal{L}-\mathcal{L}A\\ CA\\ C\end{pmatrix}
=
\operatorname{rank}\begin{pmatrix}\mathcal{L}\\ CA\\ C\end{pmatrix},
\qquad \lambda\in\Omega_S, \tag{S}
$$

where $\Omega_S=\mathbb{C}$ for pole assignability. For the detectability formulation of Darouach [8],

$$
\Omega_S=\{\lambda\in\mathbb{C}:\Re(\lambda)\ge 0\}.
$$

All real subspaces are understood through their complexifications when complex values of $\lambda$ are considered.

The objective of this paper is to characterize the functional-observer order spectrum within

$$
q_0\le q\le n_0-p,
$$

and, in particular, to determine the smallest order for which there exists an augmented functional matrix $\mathcal{L}$ satisfying the recoverability and reducedness requirements together with conditions (A) and (S).

---

## III. Algebraically Admissible Observer Orders

### A. Order Endpoints

We recall only the part of the functional observability indices construction required for the subsequent development. Write

$$
C=(C_1^T,\ldots,C_p^T)^T,\qquad L=(L_1^T,\ldots,L_r^T)^T,
$$

where $C_1,\ldots,C_p$ and $L_1,\ldots,L_r$ denote the rows of $C$ and $L$, respectively. We refer to these rows as generators and order them as

$$
g_1,\ldots,g_{p+r}=C_1,\ldots,C_p,L_1,\ldots,L_r. \tag{2}
$$

The candidates

$$
g_iA^k,\qquad k=0,1,2,\ldots,
$$

are processed by increasing powers of $A$ and, at each power, according to the fixed generator order (2). A candidate is appended if and only if its inclusion increases the rank of the matrix constructed up to that point. Since

$$
\operatorname{rank}\begin{pmatrix}C\\ L\end{pmatrix}=p+r,
$$

all candidates corresponding to $k=0$ are appended. Hence the first $p+r$ rows of the functional observability matrix are $\begin{pmatrix}C\\ L\end{pmatrix}$.

For $k\ge 1$, the candidates are therefore processed in the order

$$
C_1A^k,\ldots,C_pA^k,\ L_1A^k,\ldots,L_rA^k.
$$

If $k_i$ denotes the largest power for which $g_iA^{k_i}$ is appended, define

$$
\alpha_i=1+k_i.
$$

The functional observability indices associated with the prescribed functional are

$$
\eta_j=\alpha_{p+j},\qquad j=1,\ldots,r.
$$

The result of [25] gives the minimum order for which condition (A) can be satisfied:

$$
q_0:=\sum_{j=1}^{r}\eta_j.
$$

Moreover, the complete family of order-$q_0$ augmented functional matrices $\mathcal{L}$ satisfying condition (A) is parameterized in [25]. We denote this family by

$$
\mathfrak{L}_{q_0}^{A}(L):=
\left\{
\mathcal{L}\in\mathbb{R}^{q_0\times n}:
\begin{array}{l}
\operatorname{row}\begin{pmatrix}C\\ L\end{pmatrix}\subseteq\operatorname{row}\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix},\\[2pt]
\operatorname{rank}\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}=p+q_0,\\[2pt]
\mathcal{L}\text{ satisfies condition (A)}
\end{array}
\right\}.
$$

Thus $\mathfrak{L}_{q_0}^{A}(L)$ is the complete algebraically admissible family at the minimum algebraic order, and no order $q<q_0$ can satisfy condition (A).

The lower and upper endpoints established above therefore restrict the orders considered in the sequel to

$$
q_0\le q\le n_0-p.
$$

The purpose of this section is to characterize the algebraically admissible families throughout this entire interval.

### B. No-Gap Property

The rank formulation of condition (A) permits an order-$q$ realization to be extended by adjoining one independent row. The following result is the matrix counterpart of the one-dimensional extension property.

**Theorem 1 (One-row admissible extension):** Assume $(A,C,L)$ is functionally observable. Let $\mathcal{L}\in\mathbb{R}^{q\times n}$ satisfy

$$
\operatorname{rank}\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}
=
\operatorname{rank}\begin{pmatrix}C\\ L\end{pmatrix}=p+q,
$$

condition (A), and

$$
\operatorname{row}\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}\subseteq\operatorname{row}(\mathcal{O}_C).
$$

If $q<n_0-p$, then there exists a row vector $v\in\operatorname{row}(\mathcal{O}_C)$ such that

$$
\operatorname{rank}\begin{pmatrix}C\\ \mathcal{L}\\ v\end{pmatrix}=p+q+1,
$$

and the augmented matrix

$$
\mathcal{L}^+:=\begin{pmatrix}\mathcal{L}\\ v\end{pmatrix}
$$

satisfies condition (A) at order $q+1$.

*Proof:* Put

$$
X:=\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix},\qquad
H:=\begin{pmatrix}C\\ CA\end{pmatrix}.
$$

Then $\operatorname{rank}X=p+q<n_0$ and $\operatorname{row}(X)\subseteq\operatorname{row}(\mathcal{O}_C)$. Condition (A) is equivalent to

$$
\operatorname{row}(XA)\subseteq\operatorname{row}\begin{pmatrix}X\\ H\end{pmatrix}.
$$

If $\operatorname{row}(H)\subseteq\operatorname{row}(X)$, then $\operatorname{row}(XA)\subseteq\operatorname{row}(X)$, so $\operatorname{row}(X)$ is right $A$-invariant. Since $\operatorname{row}(C)\subseteq\operatorname{row}(X)$, it follows successively that

$$
\operatorname{row}(CA^k)\subseteq\operatorname{row}(X),\quad k=0,1,\ldots,n-1.
$$

Hence $\operatorname{row}(\mathcal{O}_C)\subseteq\operatorname{row}(X)$, and therefore

$$
n_0=\operatorname{rank}(\mathcal{O}_C)\le\operatorname{rank}X,
$$

contradicting $\operatorname{rank}X=p+q<n_0$. Therefore $\operatorname{row}(H)\nsubseteq\operatorname{row}(X)$, and hence

$$
\operatorname{rank}\begin{pmatrix}X\\ H\end{pmatrix}>\operatorname{rank}X.
$$

By the Cayley–Hamilton theorem, $\operatorname{row}(\mathcal{O}_C)A\subseteq\operatorname{row}(\mathcal{O}_C)$. Define

$$
\mathcal{V}:=\{v\in\operatorname{row}(\mathcal{O}_C):vA\in\operatorname{row}\begin{pmatrix}X\\ H\end{pmatrix}\}.
$$

This is a linear subspace of $\operatorname{row}(\mathcal{O}_C)$. To estimate its dimension, consider

$$
T:\operatorname{row}(\mathcal{O}_C)\to\operatorname{row}(\mathcal{O}_C),\quad T(v)=vA,
$$

and let

$$
\pi:\operatorname{row}(\mathcal{O}_C)\to \operatorname{row}(\mathcal{O}_C)/\operatorname{row}\begin{pmatrix}X\\ H\end{pmatrix}
$$

be the quotient map. By definition, $\ker(\pi\circ T)=\mathcal{V}$. Since $\dim\operatorname{row}(\mathcal{O}_C)=n_0$, rank–nullity gives

$$
\dim\mathcal{V}=n_0-\operatorname{rank}(\pi\circ T).
$$

Moreover,

$$
\operatorname{rank}(\pi\circ T)\le\dim\frac{\operatorname{row}(\mathcal{O}_C)}{\operatorname{row}\begin{pmatrix}X\\ H\end{pmatrix}}=n_0-\operatorname{rank}\begin{pmatrix}X\\ H\end{pmatrix}.
$$

Consequently,

$$
\dim\mathcal{V}\ge\operatorname{rank}\begin{pmatrix}X\\ H\end{pmatrix}>\operatorname{rank}X,
$$

where the strict inequality follows from $\operatorname{row}(H)\nsubseteq\operatorname{row}(X)$. Since $\operatorname{row}(X)\subseteq\operatorname{row}(\mathcal{O}_C)$ and $\operatorname{row}(XA)\subseteq\operatorname{row}\begin{pmatrix}X\\ H\end{pmatrix}$, the definition of $\mathcal{V}$ gives $\operatorname{row}(X)\subseteq\mathcal{V}$. Since $\dim\mathcal{V}>\operatorname{rank}X=\dim\operatorname{row}(X)$, there exists $v\in\mathcal{V}\setminus\operatorname{row}(X)$. Thus $v$ is independent of the rows of $X$, and hence

$$
\operatorname{rank}\begin{pmatrix}C\\ \mathcal{L}\\ v\end{pmatrix}=p+q+1.
$$

Moreover, by the definition of $V$,

$$
vA\in\operatorname{row}\begin{pmatrix}X\\ H\end{pmatrix}.
$$

Together with $\operatorname{row}(XA)\subseteq\operatorname{row}\begin{pmatrix}X\\ H\end{pmatrix}$, this yields

$$
\operatorname{row}\begin{pmatrix}XA\\ vA\end{pmatrix}\subseteq\operatorname{row}\begin{pmatrix}X\\ v\end{pmatrix}.
$$

Since $\begin{pmatrix}X\\ v\end{pmatrix}=\begin{pmatrix}C\\ \mathcal{L}^+\end{pmatrix}$, this is precisely condition (A) for $\mathcal{L}^+$. $\blacksquare$

Theorem 1 is an extension result: starting from an admissible order-$q$ matrix, it constructs at least one admissible order-$(q+1)$ matrix by adjoining one row, but it does not parameterize all admissible matrices at the higher order. Combining it with the minimum condition-(A) order from [25] gives the following no-gap result.

**Theorem 2 (No gaps in condition-(A) feasibility):** Assume that the triple $(A,C,L)$ is functional observable, and let $q_0:=\sum_{j=1}^{r}\eta_j$. Then condition (A) is feasible at every order

$$
q\in\{q_0,q_0+1,\ldots,n_0-p\},
$$

whereas no order $q<q_0$ satisfies condition (A).

*Proof:* By [25], $q_0$ is the minimum order for which condition (A) can be satisfied. Hence no order $q<q_0$ is algebraically admissible, while an order-$q_0$ realization exists. Under functional observability, the functional-observability-index construction uses rows of $C$, $L$, and their $A$-iterates. Since functional observability gives $\operatorname{row}(\mathcal{O}_L)\subseteq\operatorname{row}(\mathcal{O}_C)$, all rows used in this construction belong to $\operatorname{row}(\mathcal{O}_C)$. Consequently, the order-$q_0$ realization may be chosen so that $\operatorname{row}\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}\subseteq\operatorname{row}(\mathcal{O}_C)$.

Suppose now that a condition-(A) realization of order $q$ has been obtained with $q_0\le q<n_0-p$ and $\operatorname{row}\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}\subseteq\operatorname{row}(\mathcal{O}_C)$. By Theorem 1, there exists $v\in\operatorname{row}(\mathcal{O}_C)$ such that $\mathcal{L}^+=\begin{pmatrix}\mathcal{L}\\ v\end{pmatrix}$ is a condition-(A) realization of order $q+1$. Moreover, because both $\operatorname{row}(C,\mathcal{L})$ and $v$ belong to $\operatorname{row}(\mathcal{O}_C)$, $\operatorname{row}\begin{pmatrix}C\\ \mathcal{L}^+\end{pmatrix}\subseteq\operatorname{row}(\mathcal{O}_C)$. Thus the hypothesis required to apply Theorem 1 is preserved after each extension.

Starting from the order-$q_0$ realization and applying Theorem 1 successively therefore yields condition-(A) realizations at every order $q=q_0,q_0+1,\ldots,n_0-p$. Together with the nonexistence of condition-(A) realizations for $q<q_0$, this proves the result. $\blacksquare$

Accordingly, the set of orders at which condition (A) is feasible is

$$
\{q_0,q_0+1,\ldots,n_0-p\}. \tag{3}
$$

When $(A,C)$ is observable, $n_0=n$, and (3) becomes $\{q_0,q_0+1,\ldots,n-p\}$.

The preceding theorem establishes feasibility, not a complete parameterization. At $q=q_0$, the complete condition-(A) family $\mathfrak{L}_{q_0}^{A}(L)$ is available from [25]. Hence an order-$q_0$ functional observer exists if and only if at least one member of $\mathfrak{L}_{q_0}^{A}(L)$ satisfies condition (S), in which case $\nu_{\min}=q_0$. Otherwise, the observer order must be increased. For $q>q_0$, Theorem 2 guarantees condition-(A) feasibility but does not characterize all admissible matrices at a prescribed order. The next sections give the complete fixed-order characterization using nullspace basis matrices.

> **Remark 1:** The functional observability indices determine the lower endpoint $q_0$. Once $q_0$ is reached, condition (A) is feasible at every successive order through $n_0-p$. The result does not imply corresponding monotonicity for the joint conditions (A) and (S).

---

## IV. Nullspace Matrix Characterization of Condition (A)

We now seek a matrix characterization of all condition-(A) realizations at a prescribed order. Rather than parameterizing the rows of $\mathcal{L}$ directly, it is convenient to represent $\operatorname{row}\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}$ through its nullspace. This leads to a column-space representation in which both the realization requirement and condition (A) admit simple matrix forms.

**Theorem 3 (Matrix characterization of condition (A)):** Let $\mathcal{L}\in\mathbb{R}^{q\times n}$ be a reduced order-$q$ realization satisfying

$$
\operatorname{rank}\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}=p+q,\qquad
\operatorname{row}\begin{pmatrix}C\\ L\end{pmatrix}\subseteq\operatorname{row}\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix},
$$

and let $d=n-p-q$. Let $Z\in\mathbb{R}^{n\times d}$ have full column rank and satisfy

$$
\operatorname{im}Z=\ker\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}.
$$

Let $R_Z$ be any full-column-rank matrix satisfying

$$
\operatorname{im}R_Z=\ker(CAZ).
$$

Then condition (A) is equivalent to

$$
\operatorname{im}(AZR_Z)\subseteq\operatorname{im}Z.
$$

Equivalently,

$$
\operatorname{rank}\begin{pmatrix}Z & AZR_Z\end{pmatrix}=d.
$$

*Proof:* Condition (A) is equivalent to

$$
\operatorname{row}\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}A
\subseteq\operatorname{row}\begin{pmatrix}\mathcal{L}\\ CA\end{pmatrix}.
$$

Taking nullspaces gives the equivalent implication

$$
\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}z=0
\;\Longrightarrow\;
\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}Az=0.
$$

Since $\operatorname{im}Z=\ker\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}$ and $Z$ has full column rank, every vector satisfying $Cz=\mathcal{L}z=0$ can be written uniquely as $z=Z\xi$. The additional condition $CAz=0$ is therefore equivalent to $CAZ\xi=0$, that is,

$$
\xi\in\ker(CAZ)=\operatorname{im}R_Z.
$$

Hence $\xi=R_Z\eta$ for some $\eta$, and consequently every vector satisfying the premise of the above implication has the form $z=ZR_Z\eta$. Substituting this expression into the conclusion gives

$$
\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}AZR_Z\eta=0\qquad\text{for every }\eta.
$$

Using again $\ker\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}=\operatorname{im}Z$, this is equivalent to $AZR_Z\eta\in\operatorname{im}Z$ for every $\eta$, or equivalently,

$$
\operatorname{im}(AZR_Z)\subseteq\operatorname{im}Z.
$$

Finally, since $Z\in\mathbb{R}^{n\times d}$ has full column rank, $\operatorname{rank}Z=d$. Therefore,

$$
\operatorname{im}(AZR_Z)\subseteq\operatorname{im}Z
\iff
\operatorname{rank}\begin{pmatrix}Z & AZR_Z\end{pmatrix}=d,
$$

which proves the rank condition. $\blacksquare$

**Corollary 1 (Fixed-order condition-(A) parameterization):** For a prescribed $q\in\{q_0,\ldots,n_0-p\}$, put $d=n-p-q$. The complete family of reduced matrices $\mathcal{L}\in\mathbb{R}^{q\times n}$ satisfying the realization requirement and condition (A) is parameterized by all full-column-rank matrices $Z\in\mathbb{R}^{n\times d}$ satisfying

$$
CZ=0,\quad LZ=0,
$$

and

$$
\operatorname{rank}\begin{pmatrix}Z & AZR_Z\end{pmatrix}=d,\qquad
\operatorname{im}R_Z=\ker(CAZ). \tag{4}
$$

For each such $Z$, the corresponding matrices $\mathcal{L}$ are exactly those satisfying

$$
\ker\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}=\operatorname{im}Z.
$$

> **Remark 2:** For a prescribed order $q$, Theorem 3 gives an equivalent nullspace condition for a given realization $\mathcal{L}$, whereas Corollary 1 parameterizes all realizations $\mathcal{L}$ satisfying condition (A) at that order.

Thus Corollary 1 parameterizes the complete condition-(A) family through nullspace basis matrices. The representation is not unique: $Z$ and $ZQ$, with $Q$ nonsingular, define the same nullspace. Likewise, two reduced matrices $\mathcal{L}$ and $\widehat{\mathcal{L}}$ represent the same nullspace if and only if

$$
\widehat{\mathcal{L}}=Q\mathcal{L}+EC,\qquad Q\text{ nonsingular}. \tag{5}
$$

The matrix $R_Z$ is not an independent design variable; once $Z$ is fixed, it is simply a basis matrix for $\ker(CAZ)$. The rank test (4) states that multiplication by $A$ of the columns of $ZR_Z$ produces no column direction outside $\operatorname{im}Z$.

---

## V. Nullspace Matrix Characterization of Condition (S)

The spectral condition can be expressed using the same nullspace basis matrix $Z$. Let $V$ be any full-column-rank matrix satisfying (1).

**Theorem 4 (Matrix-pencil form of condition (S)):** Assume condition (A) holds, and let $Z$ be a full-column-rank matrix satisfying

$$
\operatorname{im}Z=\ker\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}.
$$

Then condition (S) is equivalent to

$$
\operatorname{rank}\begin{pmatrix}(\lambda I-A)V & Z\end{pmatrix}
=
\operatorname{rank}\begin{pmatrix}V & Z\end{pmatrix},
\qquad \lambda\in\Omega_S. \tag{6}
$$

*Proof:* Let $v\in\operatorname{im}V$. Then $v=V\xi$ for some $\xi$. By (1), $Cv=CAv=0$. Since $\operatorname{im}Z=\ker\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}$, we have

$$
w\in\operatorname{im}Z\iff Cw=0,\ \mathcal{L}w=0,\qquad w\in\mathbb{C}^n. \tag{7}
$$

Taking $w=v$ and using $Cv=0$ gives $v\in\operatorname{im}Z\iff\mathcal{L}v=0$. Taking $w=(\lambda I-A)v$ in (7) gives

$$
(\lambda I-A)v\in\operatorname{im}Z
$$

if and only if

$$
C(\lambda I-A)v=0,\qquad \mathcal{L}(\lambda I-A)v=0.
$$

Since $C(\lambda I-A)v=\lambda Cv-CAv=0$, we obtain

$$
(\lambda I-A)v\in\operatorname{im}Z\iff(\lambda\mathcal{L}-\mathcal{L}A)v=0.
$$

Under condition (A), $\operatorname{row}(\mathcal{L}A)\subseteq\operatorname{row}\begin{pmatrix}\mathcal{L}\\ CA\\ C\end{pmatrix}$. Since $\operatorname{row}(\mathcal{L})$ is contained in the latter row space, it follows that

$$
\operatorname{row}\begin{pmatrix}\lambda\mathcal{L}-\mathcal{L}A\\ CA\\ C\end{pmatrix}
\subseteq
\operatorname{row}\begin{pmatrix}\mathcal{L}\\ CA\\ C\end{pmatrix}.
$$

Hence condition (S) is equivalent to equality of these row spaces, and therefore to equality of their nullspaces. Thus

$$
\begin{pmatrix}\lambda\mathcal{L}-\mathcal{L}A\\ CA\\ C\end{pmatrix}v=0
\iff
\begin{pmatrix}\mathcal{L}\\ CA\\ C\end{pmatrix}v=0.
$$

Both nullspaces are contained in $\ker\begin{pmatrix}C\\ CA\end{pmatrix}=\operatorname{im}V$. Hence it is sufficient to compare them on $\operatorname{im}V$.

For $v\in\operatorname{im}V$, we have $Cv=CAv=0$. Hence the right-hand nullspace condition reduces to $\mathcal{L}v=0$, which is equivalent to $v\in\operatorname{im}Z$, while the left-hand nullspace condition reduces to $(\lambda\mathcal{L}-\mathcal{L}A)v=0$, equivalent to $(\lambda I-A)v\in\operatorname{im}Z$. Therefore condition (S) is equivalent to

$$
(\lambda I-A)v\in\operatorname{im}Z\iff v\in\operatorname{im}Z,\qquad v\in\operatorname{im}V.
$$

Writing $v=V\xi$, this becomes

$$
(\lambda I-A)V\xi\in\operatorname{im}Z\iff V\xi\in\operatorname{im}Z.
$$

Define

$$
\mathscr{X}_\lambda=\{\xi:(\lambda I-A)V\xi\in\operatorname{im}Z\},\qquad
\mathscr{X}_0=\{\xi:V\xi\in\operatorname{im}Z\}.
$$

We first show that condition (A) implies $\mathscr{X}_0\subseteq\mathscr{X}_\lambda$. Let $\xi\in\mathscr{X}_0$ and put $v=V\xi$. Then $v\in\operatorname{im}Z$, and hence $\mathcal{L}v=0$. Since $v\in\operatorname{im}V$, $Cv=CAv=0$. Condition (A) gives $\operatorname{row}(\mathcal{L}A)\subseteq\operatorname{row}\begin{pmatrix}\mathcal{L}\\ CA\\ C\end{pmatrix}$, and therefore $\mathcal{L}Av=0$. Consequently,

$$
\mathcal{L}(\lambda I-A)v=\lambda\mathcal{L}v-\mathcal{L}Av=0,
$$

and $C(\lambda I-A)v=\lambda Cv-CAv=0$. Hence $(\lambda I-A)v\in\ker\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}=\operatorname{im}Z$, so $\xi\in\mathscr{X}_\lambda$. Therefore $\mathscr{X}_0\subseteq\mathscr{X}_\lambda$.

Now $(\lambda I-A)V\xi\in\operatorname{im}Z\iff V\xi\in\operatorname{im}Z$ for every $\xi$ if and only if $\mathscr{X}_\lambda=\mathscr{X}_0$. Since $\mathscr{X}_0\subseteq\mathscr{X}_\lambda$, this equality holds if and only if $\dim\mathscr{X}_0=\dim\mathscr{X}_\lambda$. By the rank–nullity theorem, this is equivalent to

$$
\operatorname{rank}\begin{pmatrix}(\lambda I-A)V & Z\end{pmatrix}
=
\operatorname{rank}\begin{pmatrix}V & Z\end{pmatrix},
\qquad \lambda\in\Omega_S,
$$

which proves (6). $\blacksquare$

> **Remark 3 (Basis invariance):** Replacing $Z$ by $ZQ$, where $Q$ is nonsingular, leaves (4) and (6) unchanged. Thus the tests depend only on the column space of $Z$, although the formulation itself uses matrices throughout.

---

## VI. Complete Fixed- and All-Order Characterization

### A. Fixed-Order Characterization

At $q=q_0$, the complete condition-(A) family $\mathfrak{L}_{q_0}^{A}(L)$ is available from [25]. For every prescribed order in the admissible range, Corollary 1 parameterizes the complete condition-(A) family through $Z$. Applying the spectral condition of Theorem 4 to this family yields the following necessary and sufficient fixed-order existence test.

**Theorem 5 (Fixed-order functional-observer existence):** Assume $(A,C,L)$ is functionally observable and

$$
q_0\le q\le n_0-p.
$$

Put

$$
d=n-p-q,\qquad r_1=\operatorname{rank}\begin{pmatrix}C\\ CA\end{pmatrix},
$$

and let $V\in\mathbb{R}^{n\times(n-r_1)}$ have full column rank and satisfy

$$
\operatorname{im}V=\ker\begin{pmatrix}C\\ CA\end{pmatrix}.
$$

Then an order-$q$ functional observer exists if and only if there is a full-column-rank matrix $Z\in\mathbb{R}^{n\times d}$ such that

$$
CZ=0,\quad LZ=0, \tag{8a}
$$

$$
\operatorname{rank}\begin{pmatrix}Z & AZR_Z\end{pmatrix}=d,\quad
\operatorname{im}R_Z=\ker(CAZ), \tag{8b}
$$

$$
\operatorname{rank}\begin{pmatrix}(\lambda I-A)V & Z\end{pmatrix}
=
\operatorname{rank}\begin{pmatrix}V & Z\end{pmatrix},
\quad \lambda\in\Omega_S. \tag{8c}
$$

*Proof:* If an order-$q$ functional observer exists, choose a reduced augmented functional matrix $\mathcal{L}\in\mathbb{R}^{q\times n}$ and a full-column-rank matrix $Z\in\mathbb{R}^{n\times d}$ whose columns form a basis of $\ker\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}$. Since the prescribed functional $Lx$ is recoverable from $\mathcal{L}x$ and the measured output, $\operatorname{row}(L)\subseteq\operatorname{row}\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}$. Hence $CZ=0,\ LZ=0$, which gives (8a). Theorem 3 gives (8b), and Theorem 4 gives (8c).

Conversely, suppose that a full-column-rank matrix $Z$ satisfies (8). Since $\operatorname{rank}Z=d=n-p-q$ and $CZ=0$, we have $\operatorname{im}Z\subseteq\ker C$, $\dim(\operatorname{im}Z)=n-p-q$. Therefore, there exists a matrix $\mathcal{L}\in\mathbb{R}^{q\times n}$ such that $\ker\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}=\operatorname{im}Z$ and $\operatorname{rank}\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}=p+q$. Thus $\mathcal{L}$ is a reduced order-$q$ augmented functional matrix. Moreover, $LZ=0$ implies $\operatorname{im}Z\subseteq\ker L$. Since $\operatorname{im}Z=\ker\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}$, it follows that $\ker\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}\subseteq\ker L$, or equivalently, $\operatorname{row}(L)\subseteq\operatorname{row}\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}$. Hence the prescribed functional $Lx$ is recoverable from $\mathcal{L}x$ and the measured output. Finally, (8b), together with Theorem 3, gives condition (A), while (8c), together with Theorem 4, gives condition (S). Hence an order-$q$ functional observer exists. $\blacksquare$

**Corollary 2 (Recovery of the minimum-order family):** At $q=q_0$, the nullspace characterization of Theorem 5 is equivalent to the complete minimum-order characterization of [25]. In particular, if the complete condition-(A) family in [25] is written as

$$
\mathcal{L}_J(\Theta,K)=\begin{pmatrix}L\\ X_J(\Theta)M_C+KC\end{pmatrix}, \tag{9}
$$

then, with $d_0=n-p-q_0$, its corresponding nullspace is represented by any full-column-rank matrix $Z_J(\Theta)\in\mathbb{R}^{n\times d_0}$ satisfying

$$
\operatorname{im}Z_J(\Theta)=\ker\begin{pmatrix}C\\ L\\ X_J(\Theta)M_C\end{pmatrix}. \tag{10}
$$

The parameter $K$ does not affect this nullspace. Conversely, every order-$q_0$ matrix $Z$ satisfying (8a)–(8b) corresponds, up to a change of nullspace basis and the row equivalence (5), to a member of (9). Moreover, (8c) is equivalent to condition (S) of [25] for the corresponding $\mathcal{L}_J(\Theta,K)$.

*Proof:* A vector $\xi\in\mathbb{R}^n$ belongs to $\ker\begin{pmatrix}C\\ \mathcal{L}_J(\Theta,K)\end{pmatrix}$ if and only if $C\xi=0,\ L\xi=0,\ (X_J(\Theta)M_C+KC)\xi=0$. Since $C\xi=0$, the last equality is equivalent to $X_J(\Theta)M_C\xi=0$. Hence

$$
\ker\begin{pmatrix}C\\ \mathcal{L}_J(\Theta,K)\end{pmatrix}
=
\ker\begin{pmatrix}C\\ L\\ X_J(\Theta)M_C\end{pmatrix},
$$

which proves (10) and shows explicitly why $K$ disappears from the nullspace representation. Since $\mathcal{L}_J(\Theta,K)$ is reduced of order $q_0$, this nullspace has dimension $d_0$. Because every member of (9) satisfies condition (A), Theorem 3 gives $\operatorname{rank}\begin{pmatrix}Z_J(\Theta) & AZ_J(\Theta)R_{Z_J(\Theta)}\end{pmatrix}=d_0$, $\operatorname{im}R_{Z_J(\Theta)}=\ker(CAZ_J(\Theta))$. Thus every member of the complete family of [25] generates a member of the present order-$q_0$ nullspace family.

Conversely, let $Z\in\mathbb{R}^{n\times d_0}$ satisfy (8a)–(8b). By Corollary 1, the reduced matrices $\mathcal{L}$ satisfying $\ker\begin{pmatrix}C\\ \mathcal{L}\end{pmatrix}=\operatorname{im}Z$ are exactly the order-$q_0$ realizations satisfying condition (A). Since the parameterization (9) is complete, such an $\mathcal{L}$ is represented, up to (5), by $\mathcal{L}_J(\Theta,K)$ for an admissible $(J,\Theta,K)$. Therefore $\operatorname{im}Z=\operatorname{im}Z_J(\Theta)$, or equivalently $Z=Z_J(\Theta)Q$ for some nonsingular $Q$. Finally, Theorem 4 shows that (8c) is equivalent to the spectral condition (S) for the corresponding $\mathcal{L}$. Hence the present characterization recovers both the complete condition-(A) family and the minimum-order existence test of [25]. $\blacksquare$

> **Remark 4:** Corollary 2 also exhibits a useful feature of the nullspace formulation: the freedom $KC$ in the direct $\mathcal{L}$ parameterization is automatically quotiented out. The matrix $Z$ represents the underlying subspace rather than a particular row realization of it.

### B. Matrix Parameterization at a Prescribed Order

Theorem 5 characterizes fixed-order observer existence in terms of a nullspace matrix $Z$. We now parameterize all candidate matrices $Z$ at a prescribed order and then apply this parameterization over the entire admissible order range.

Let $K_L\in\mathbb{R}^{n\times m_L}$ have full column rank and satisfy

$$
\operatorname{im}K_L=\ker\begin{pmatrix}C\\ L\end{pmatrix}. \tag{11}
$$

For a prescribed $q\in\{q_0,\ldots,n_0-p\}$, put $d=n-p-q$. Since every candidate $Z\in\mathbb{R}^{n\times d}$ must satisfy $CZ=0,\ LZ=0$, its columns belong to $\operatorname{im}K_L$. Hence every full-column-rank candidate $Z$ can be written as

$$
Z=K_LW,\qquad W\in\mathbb{R}^{m_L\times d},\qquad \operatorname{rank}W=d.
$$

The matrices $W$ and $WQ$, where $Q\in\mathbb{R}^{d\times d}$ is nonsingular, have the same column space and therefore generate the same candidate subspace through $Z=K_LW$. Thus only the column space of $W$ is relevant.

Since $\operatorname{rank}W=d$, there exist $d$ rows of $W$ that form a nonsingular $d\times d$ submatrix. Let

$$
\mathcal{I}=\{i_1,\ldots,i_d\}\subseteq\{1,\ldots,m_L\}
$$

denote the indices of these $d$ rows. Let $P_{\mathcal{I}}$ be a permutation matrix that reorders the rows of $W$ so that the $d$ rows indexed by $\mathcal{I}$ occupy the first $d$ positions. Then write

$$
P_{\mathcal{I}}W=\begin{pmatrix}W_{\mathcal{I}}^{(1)}\\ W_{\mathcal{I}}^{(2)}\end{pmatrix},
$$

where $W_{\mathcal{I}}^{(1)}\in\mathbb{R}^{d\times d}$ is nonsingular. Right multiplication by $(W_{\mathcal{I}}^{(1)})^{-1}$ gives

$$
P_{\mathcal{I}}W\bigl(W_{\mathcal{I}}^{(1)}\bigr)^{-1}
=
\begin{pmatrix}I_d\\ \Theta\end{pmatrix},
\qquad
\Theta=W_{\mathcal{I}}^{(2)}\bigl(W_{\mathcal{I}}^{(1)}\bigr)^{-1}.
$$

Hence

$$
W_{\mathcal{I}}(\Theta):=P_{\mathcal{I}}^T\begin{pmatrix}I_d\\ \Theta\end{pmatrix}
=W\bigl(W_{\mathcal{I}}^{(1)}\bigr)^{-1},
\qquad \Theta\in\mathbb{R}^{(m_L-d)\times d}. \tag{12}
$$

Since $(W_{\mathcal{I}}^{(1)})^{-1}$ is nonsingular, $\operatorname{im}W_{\mathcal{I}}(\Theta)=\operatorname{im}W$. The corresponding nullspace matrix is

$$
Z_{\mathcal{I}}(\Theta)=K_LW_{\mathcal{I}}(\Theta). \tag{13}
$$

By (12), $Z_{\mathcal{I}}(\Theta)=Z(W_{\mathcal{I}}^{(1)})^{-1}$. Since $W_{\mathcal{I}}^{(1)}$ is nonsingular, $\operatorname{im}Z_{\mathcal{I}}(\Theta)=\operatorname{im}Z$.

Each chart contains $d(m_L-d)$ free scalar parameters. The finitely many choices of $\mathcal{I}$ cover all full-column-rank matrices $W$ up to right multiplication by a nonsingular matrix. Equivalently, these are the standard coordinate charts of the Grassmannian $\operatorname{Gr}(d,m_L)$, the set of all $d$-dimensional subspaces of $\mathbb{R}^{m_L}$.

Geometrically, the fixed-order problem selects a $d$-dimensional subspace $\mathcal{Z}\subseteq\ker\begin{pmatrix}C\\ L\end{pmatrix}$ that satisfies the $A$-compatibility and spectral requirements. The matrices $W_{\mathcal{I}}(\Theta)$ provide finite coordinates for all such subspaces; no geometric machinery is needed in the subsequent computations.

**Theorem 6 (Matrix parameterization at a prescribed order):** For a prescribed $q\in\{q_0,\ldots,n_0-p\}$, put $d=n-p-q$. Let $K_L$ satisfy (11), and let $Z_{\mathcal{I}}(\Theta)$ be defined by (12)–(13). Then an order-$q$ functional observer exists if and only if, for at least one matrix chart, there exists $\Theta\in\mathbb{R}^{(m_L-d)\times d}$ such that

$$
\operatorname{rank}\begin{pmatrix}Z_{\mathcal{I}}(\Theta) & AZ_{\mathcal{I}}(\Theta)R_{Z_{\mathcal{I}}(\Theta)}\end{pmatrix}=d, \tag{14a}
$$

$$
\operatorname{rank}\begin{pmatrix}(\lambda I-A)V & Z_{\mathcal{I}}(\Theta)\end{pmatrix}
=
\operatorname{rank}\begin{pmatrix}V & Z_{\mathcal{I}}(\Theta)\end{pmatrix},
\quad \lambda\in\Omega_S, \tag{14b}
$$

where $\operatorname{im}R_{Z_{\mathcal{I}}(\Theta)}=\ker(CAZ_{\mathcal{I}}(\Theta))$.

For a prescribed chart and parameter value $\Theta$, put

$$
h_{\mathcal{I},\Theta}=\operatorname{rank}\begin{pmatrix}V & Z_{\mathcal{I}}(\Theta)\end{pmatrix},
$$

and let $\Delta_j(\lambda)$ denote the nonzero $h_{\mathcal{I},\Theta}\times h_{\mathcal{I},\Theta}$ minors of

$$
P_{\mathcal{I},\Theta}(\lambda)=\begin{pmatrix}(\lambda I-A)V & Z_{\mathcal{I}}(\Theta)\end{pmatrix}.
$$

Under (14a), $\operatorname{rank}P_{\mathcal{I},\Theta}(\lambda)\le h_{\mathcal{I},\Theta},\ \lambda\in\mathbb{C}$. Hence, with

$$
g_{\mathcal{I},\Theta}(\lambda)=\gcd_{\lambda}\{\Delta_j(\lambda)\},
$$

condition (14b) is equivalent to

$$
g_{\mathcal{I},\Theta}(\lambda)\neq 0,\qquad \lambda\in\Omega_S.
$$

In particular, for pole assignability, $g_{\mathcal{I},\Theta}$ is a nonzero constant and may be normalized to $g_{\mathcal{I},\Theta}=1$. For detectability, $g_{\mathcal{I},\Theta}$ has no zeros in the closed right half-plane.

*Proof:* Since $\operatorname{im}K_L=\ker\begin{pmatrix}C\\ L\end{pmatrix}$, every full-column-rank matrix $Z\in\mathbb{R}^{n\times d}$ satisfying $CZ=0,\ LZ=0$ can be written as $Z=K_LW$, where $W\in\mathbb{R}^{m_L\times d}$ has rank $d$. Conversely, every such $W$ produces a full-column-rank matrix $Z=K_LW$ satisfying $CZ=LZ=0$. Since $\operatorname{rank}W=d$, some $d\times d$ row submatrix of $W$ is nonsingular. Let $\mathcal{I}$ denote its row-index set and let $P_{\mathcal{I}}$ be a permutation matrix that moves the rows indexed by $\mathcal{I}$ to the first $d$ positions. Right multiplication by the inverse of the resulting leading $d\times d$ submatrix gives

$$
P_{\mathcal{I}}WQ=\begin{pmatrix}I_d\\ \Theta\end{pmatrix}
$$

for some nonsingular $Q$. Equivalently,

$$
WQ=P_{\mathcal{I}}^T\begin{pmatrix}I_d\\ \Theta\end{pmatrix}=W_{\mathcal{I}}(\Theta).
$$

Since $Q$ is nonsingular, $\operatorname{im}(K_LWQ)=\operatorname{im}(K_LW)$. Hence $Z_{\mathcal{I}}(\Theta)=K_LW_{\mathcal{I}}(\Theta)$ represents the same nullspace as $Z=K_LW$. Varying $\mathcal{I}$ over all $d$-element subsets of $\{1,\ldots,m_L\}$ therefore covers all candidate nullspaces appearing in Theorem 5.

The conditions $CZ=0$ and $LZ=0$ hold by construction. Substitution of $Z=Z_{\mathcal{I}}(\Theta)$ into the remaining conditions of Theorem 5 therefore gives (14a)–(14b).

It remains to establish the finite spectral test. For brevity, write $Z=Z_{\mathcal{I}}(\Theta)$, $P(\lambda)=\begin{pmatrix}(\lambda I-A)V & Z\end{pmatrix}$, $h=\operatorname{rank}\begin{pmatrix}V & Z\end{pmatrix}$. Define

$$
\mathscr{X}_\lambda=\{\xi:(\lambda I-A)V\xi\in\operatorname{im}Z\},\qquad
\mathscr{X}_0=\{\xi:V\xi\in\operatorname{im}Z\}.
$$

By (14a), condition (A) holds. Hence, as in the proof of Theorem 4, $\mathscr{X}_0\subseteq\mathscr{X}_\lambda,\ \lambda\in\mathbb{C}$. Let $r_V$ denote the number of columns of $V$. Since $Z$ has full column rank $d$, rank–nullity gives

$$
\dim\mathscr{X}_\lambda=r_V+d-\operatorname{rank}P(\lambda),\qquad
\dim\mathscr{X}_0=r_V+d-h.
$$

Therefore $\mathscr{X}_0\subseteq\mathscr{X}_\lambda$ implies $\operatorname{rank}P(\lambda)\le h,\ \lambda\in\mathbb{C}$. Consequently, $\operatorname{rank}P(\lambda)=h$ if and only if at least one $h\times h$ minor of $P(\lambda)$ is nonzero. Thus (14b) holds if and only if these minors have no common zero in $\Omega_S$. Their common zeros are precisely the zeros of $g_{\mathcal{I},\Theta}(\lambda)$. Hence (14b) is equivalent to $g_{\mathcal{I},\Theta}(\lambda)\neq 0,\ \lambda\in\Omega_S$.

For pole assignability, $\Omega_S=\mathbb{C}$, so the gcd is a nonzero constant and may be normalized to one. For detectability, $\Omega_S=\{\lambda\in\mathbb{C}:\Re(\lambda)\ge 0\}$, so the gcd must have no zeros in the closed right half-plane. $\blacksquare$

> **Remark 5 (Testing the fixed-order conditions):** For a prescribed chart and parameter value $\Theta$, (14a) is tested by computing a basis $R_{Z_{\mathcal{I}}(\Theta)}$ of $\ker(CAZ_{\mathcal{I}}(\Theta))$ and evaluating the indicated rank. For pole assignability, (14b) is tested by the maximal-minor gcd condition in Theorem 6, avoiding a pointwise search over $\lambda\in\mathbb{C}$.

> **Remark 6 (Observer construction):** In general, once a reduced matrix $\mathcal{L}$ satisfying condition (A) and condition (S) at a prescribed order $q$ has been found — whether via the chart parameterization above or by any other means — the observer parameters can be constructed directly using the procedure in [8], with the functional matrix $L$ therein replaced by this $\mathcal{L}$.

Thus the complete fixed-order search is reduced to finitely many matrix charts, each parameterized by $d(m_L-d)$ scalar variables and subject to the two rank tests (14a)–(14b). In particular, the realization conditions $CZ=0$ and $LZ=0$ are satisfied by construction.

### C. All-Order Characterization and Procedure

We now pass from the fixed-order characterization to the complete characterization of feasible observer orders.

**Definition 1 (Observer families and order spectra):** For each $q_0\le q\le n_0-p$, define

$$
\mathfrak{L}_q^A(L):=\{\mathcal{L}:\mathcal{L}\text{ is an order-}q\text{ realization satisfying (A)}\},
$$

$$
\mathfrak{L}_q^{FO}(L):=\{\mathcal{L}\in\mathfrak{L}_q^A(L):\mathcal{L}\text{ satisfies (S)}\}.
$$

The corresponding order spectra are

$$
\Sigma_A(L):=\{q:\mathfrak{L}_q^A(L)\neq\varnothing\},\qquad
\Sigma_{FO}(L):=\{q:\mathfrak{L}_q^{FO}(L)\neq\varnothing\}.
$$

By Theorem 2,

$$
\Sigma_A(L)=\{q_0,q_0+1,\ldots,n_0-p\}.
$$

Membership in $\Sigma_{FO}(L)$ is characterized at each prescribed order by Theorem 5, with the complete matrix parameterization and finite spectral test provided by Theorem 6. No interval property of $\Sigma_{FO}(L)$ is assumed.

Parameterize the admissible orders by

$$
k_{\max}=n_0-p-q_0,\qquad q_k=q_0+k,\qquad d_k=n-p-q_k,
$$

for $k=0,1,\ldots,k_{\max}$. At the terminal order $q_{k_{\max}}=n_0-p$,

$$
d_{k_{\max}}=n-n_0,
$$

which is zero only under full observability.

For each $k=0,1,\ldots,k_{\max}$, define the condition-(A) nullspace family

$$
\mathfrak{X}_{d_k}^A(L):=\{Z\in\mathbb{R}^{n\times d_k}:\operatorname{rank}Z=d_k,\ (8a)\text{–}(8b)\text{ hold}\},
$$

and the algebraic-spectral nullspace family

$$
\mathfrak{X}_{d_k}^{AS}(L):=\{Z\in\mathfrak{X}_{d_k}^A(L):(8c)\text{ holds}\}.
$$

Thus $\mathfrak{X}_{d_k}^{AS}(L)\subseteq\mathfrak{X}_{d_k}^A(L)$. Since these conditions depend only on $\operatorname{im}Z$, matrices related by

$$
Z\sim ZQ,\qquad Q\in\mathbb{R}^{d_k\times d_k}\text{ nonsingular},
$$

represent the same candidate nullspace.

**1) Terminal Functional-Observability Endpoint:** The upper endpoint $n_0-p$ is spectrally feasible. In matrix terms, its nullspace basis is any full-column-rank matrix $Z_0$ satisfying

$$
\operatorname{im}Z_0=\ker(\mathcal{O}_C),\qquad \operatorname{rank}Z_0=n-n_0.
$$

**Theorem 7 (Functional-observability endpoint):** Assume $(A,C,L)$ is functionally observable. Then

$$
n_0-p\in\Sigma_{FO}(L).
$$

*Proof:* Functional observability gives $LZ_0=0$, while $CZ_0=0$ follows from $\operatorname{im}Z_0=\ker(\mathcal{O}_C)$. Since $\ker(\mathcal{O}_C)$ is $A$-invariant, there exists a matrix $F_0$ such that $AZ_0=Z_0F_0$. Hence (8b) holds automatically.

To verify (8c), let $v=V\xi$ and suppose $(\lambda I-A)v\in\operatorname{im}Z_0$. Since $\operatorname{im}Z_0=\ker(\mathcal{O}_C)$ and $\ker(\mathcal{O}_C)$ is $A$-invariant, we have $CA^k(\lambda I-A)v=0,\ k\ge 0$. Therefore $\lambda CA^kv-CA^{k+1}v=0,\ k\ge 0$. Moreover, since $v\in\operatorname{im}V$ and $\operatorname{im}V=\ker\begin{pmatrix}C\\ CA\end{pmatrix}$, we have $Cv=0,\ CAv=0$. The preceding recurrence then gives successively $CA^kv=0,\ k\ge 0$. Hence $v\in\ker(\mathcal{O}_C)=\operatorname{im}Z_0$.

Conversely, if $v\in\operatorname{im}Z_0$, then the $A$-invariance of $\operatorname{im}Z_0$ gives $(\lambda I-A)v\in\operatorname{im}Z_0$ for every $\lambda\in\mathbb{C}$. Therefore

$$
(\lambda I-A)v\in\operatorname{im}Z_0\iff v\in\operatorname{im}Z_0,\qquad v\in\operatorname{im}V.
$$

Thus the two solution sets underlying (6) coincide for every $\lambda\in\Omega_S$, and condition (S) holds. Therefore $n_0-p\in\Sigma_{FO}(L)$. $\blacksquare$

**Corollary 3 (Luenberger endpoint):** If $(A,C)$ is observable, then $n_0=n$, $Z_0$ has no columns, and

$$
n-p\in\Sigma_{FO}(L).
$$

Thus the functional-observability endpoint reduces to the classical reduced-order Luenberger order.

Then Theorem 5 gives

$$
q_k\in\Sigma_{FO}(L)\iff \mathfrak{X}_{d_k}^{AS}(L)\neq\varnothing.
$$

Moreover, Theorem 6 provides a complete matrix parameterization for testing the nonemptiness of $\mathfrak{X}_{d_k}^{AS}(L)$ at each prescribed order.

**Theorem 8 (Functional-observability characterization):** The triple $(A,C,L)$ is functionally observable if and only if

$$
\Sigma_{FO}(L)\neq\varnothing.
$$

Equivalently, there exist $q\in\{q_0,\ldots,n_0-p\}$ and a full-column-rank matrix $Z\in\mathbb{R}^{n\times(n-p-q)}$ satisfying (8a)–(8c).

*Proof:* If $(A,C,L)$ is functionally observable, then Theorem 7 guarantees a functional observer at $q=n_0-p$. Hence $\Sigma_{FO}(L)\neq\varnothing$. Conversely, if $\Sigma_{FO}(L)\neq\varnothing$, then a functional observer exists at some admissible order. Its augmented functional matrix satisfies conditions (A) and (S), and hence $(A,C,L)$ is functional observable by the augmentation characterization of functional observability [10]. The equivalent characterization in terms of $Z$ follows directly from Theorem 5. $\blacksquare$

**Theorem 9 (All-Order Observer Characterization):** Assume $(A,C,L)$ is functionally observable. Then the complete feasible-order spectrum is

$$
\Sigma_{FO}(L)=\{q_k:\mathfrak{X}_{d_k}^{AS}(L)\neq\varnothing,\ k=0,1,\ldots,k_{\max}\}. \tag{15}
$$

Equivalently, $q_k$ is a functional-observer order if and only if at least one chart $Z_{\mathcal{I}}(\Theta)$ at dimension $d_k$ satisfies (14a)–(14b). Moreover,

$$
\nu_{\min}=q_0+\min\{k:\mathfrak{X}_{d_k}^{AS}(L)\neq\varnothing\}. \tag{16}
$$

*Proof:* For each $k$, Theorem 5 gives $q_k\in\Sigma_{FO}(L)$ if and only if $\mathfrak{X}_{d_k}^{AS}(L)\neq\varnothing$. Theorem 6 covers every full-rank candidate $Z$ through finitely many matrix charts, so this test is complete at each order. Taking the union over $k=0,\ldots,k_{\max}$ proves (15). By Theorem 7, the terminal set is nonempty, so the minimum in (16) exists and gives the smallest feasible order. $\blacksquare$

Theorem 9 is a completeness statement: at a prescribed order, failure of (14a)–(14b) over every chart proves nonexistence of a functional observer at that order; it is not merely failure of a selected realization.

**Algorithm 1** Order-by-order functional-observer characterization

```text
1:  Compute the FO indices η_j and q_0 = Σ_j η_j.
2:  Compute n_0 = rank O_C and k_max = n_0 − p − q_0.
3:  Compute basis matrices V and K_L from (1) and (11) respectively.
4:  for k = 0,1,...,k_max do
5:      Set q_k = q_0 + k and d_k = n − p − q_k.
6:      if k = 0 then
7:          Use L^A_{q_0}(L) from [25] and test the spectral condition.
8:      else if k = k_max then
9:          Use a basis Z_0 of ker(O_C) and test the spectral condition.
10:     else
11:         Parameterize Z = K_L W_I(Θ) using (12)–(13).
12:         Test (14a)–(14b).
13:     end if
14:     Record whether q_k ∈ Σ_FO(L).
15: end for
16: Return Σ_FO(L) and ν_min = min Σ_FO(L).
```

---

## VII. Illustrative Example

We illustrate the all-order characterization with an example in which the algebraic lower bound $q_0$ is separated by two orders from the actual minimum functional-observer order. Condition (A) first becomes possible at $q=q_0$, but condition (S) excludes every admissible realization at both $q=q_0$ and $q=q_0+1$. A functional observer first exists at $q=q_0+2$, strictly below the functional-observability endpoint $n_0-p$.

Consider

$$
\dot{x}(t)=Ax(t)+Bu(t),\qquad y(t)=Cx(t),\qquad z(t)=Lx(t),
$$

where

$$
A=
\begin{pmatrix}
0 & 1 & 0 & 1 & 0 & 0 & 0 & 0\\
0 & -1 & 1 & 0 & 0 & 0 & 0 & -1\\
1 & 0 & -1 & 1 & 0 & 0 & 1 & -1\\
-1 & -1 & 0 & -2 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & -2 & 0 & 0 & 1\\
0 & 0 & 0 & 0 & 0 & -2 & 1 & 0\\
0 & 0 & 0 & 0 & 0 & -1 & -2 & 1\\
0 & 0 & 0 & 0 & 0 & 0 & 1 & -2
\end{pmatrix},
$$

$$
B=e_1+e_8,
$$

$$
C=
\begin{pmatrix}
-2 & -2 & 2 & -2 & -1 & 0 & 1 & -3\\
0 & 0 & 1 & 2 & 2 & 3 & -1 & -2
\end{pmatrix},
$$

$$
L=
\begin{pmatrix}
-2 & -1 & -2 & -3 & -1 & 3 & 2 & 0\\
1 & -1 & -2 & 1 & 0 & 2 & 0 & 1
\end{pmatrix},
$$

where $e_i$ is the $i$-th standard basis vector of $\mathbb{R}^8$. Thus

$$
n=8,\qquad p=\operatorname{rank}C=2,\qquad r=\operatorname{rank}L=2.
$$

The observability matrix satisfies

$$
n_0=\operatorname{rank}\mathcal{O}_C=8=n,
$$

so that $(A,C)$ is completely observable.

Applying the functional-observability-index construction gives

$$
\eta_1=2,\qquad \eta_2=1,
$$

and hence

$$
q_0=\eta_1+\eta_2=3.
$$

Therefore

$$
r=2<q_0=3.
$$

Since $(A,C)$ is observable, the functional-observability endpoint reduces to the classical reduced-order Luenberger order,

$$
n_0-p=6,
$$

and the complete order range that must be considered is

$$
q_0\le q\le n_0-p,\quad\text{that is,}\quad q\in\{3,4,5,6\}.
$$

For this example,

$$
\dim\ker\begin{pmatrix}C\\ L\end{pmatrix}=4,\qquad
\dim\ker\begin{pmatrix}C\\ CA\end{pmatrix}=4.
$$

Consequently, every candidate nullspace matrix $Z$ at orders $q_0$ and $q_0+1$ has its image in the four-dimensional subspace $\ker\begin{pmatrix}C\\ L\end{pmatrix}$. The fixed-order characterization of Theorem 5, together with the Grassmann-chart parameterization, can therefore be applied at each of the four admissible orders.

### A. Failure at the lower bound $q=q_0=3$

At the lower endpoint,

$$
q=q_0=3,\qquad d=n-p-q=3.
$$

Thus $\operatorname{im}Z$ must be a three-dimensional subspace of $\ker\begin{pmatrix}C\\ L\end{pmatrix}$, which has dimension four.

Let $K_L\in\mathbb{R}^{8\times 4}$, $\operatorname{im}K_L=\ker\begin{pmatrix}C\\ L\end{pmatrix}$, be any full-column-rank basis matrix. Every candidate can then be written as

$$
Z=K_LW,\qquad W\in\mathbb{R}^{4\times 3},\qquad \operatorname{rank}W=3.
$$

The complete family of such subspaces is covered by the four standard Grassmann charts of $\operatorname{Gr}(3,4)$.

For each chart, the chart matrix $W_{\mathcal{I}}(\Theta)$ is substituted into $Z_{\mathcal{I}}(\Theta)=K_LW_{\mathcal{I}}(\Theta)$, and condition (A) is imposed through

$$
\operatorname{rank}\begin{pmatrix}Z_{\mathcal{I}}(\Theta) & AZ_{\mathcal{I}}(\Theta)R_{Z_{\mathcal{I}}(\Theta)}\end{pmatrix}=3,
\qquad
\operatorname{im}R_{Z_{\mathcal{I}}(\Theta)}=\ker(CAZ_{\mathcal{I}}(\Theta)).
$$

On each chart, imposing condition (A) reduces the complete candidate family to a one-parameter family $Z_{\mathcal{I}}(\Theta)$. Condition (S) is then tested along each of these families through

$$
\operatorname{rank}\begin{pmatrix}(\lambda I-A)V & Z_{\mathcal{I}}(\Theta)\end{pmatrix}
=
\operatorname{rank}\begin{pmatrix}V & Z_{\mathcal{I}}(\Theta)\end{pmatrix},
\quad \lambda\in\mathbb{C},
\qquad
\operatorname{im}V=\ker\begin{pmatrix}C\\ CA\end{pmatrix}.
$$

Exact evaluation of condition (S) over the condition-(A) families obtained from all four charts of $\operatorname{Gr}(3,4)$ shows that no member satisfies condition (S). Since these charts cover all three-dimensional subspaces of $\ker\begin{pmatrix}C\\ L\end{pmatrix}$, this proves that no order-3 functional observer exists. Hence

$$
3\notin\Sigma_{FO}(L).
$$

Thus $q_0=3$ is the algebraic lower bound predicted by the functional-observability indices, but it is not itself a functional-observer order.

### B. Failure at $q=q_0+1=4$

Consider next

$$
q=q_0+1=4,\qquad d=n-p-q=2.
$$

Now $\operatorname{im}Z$ must be a two-dimensional subspace of the same four-dimensional space $\ker\begin{pmatrix}C\\ L\end{pmatrix}$. Writing

$$
Z=K_LW,\qquad W\in\mathbb{R}^{4\times 2},\qquad \operatorname{rank}W=2,
$$

the complete candidate family is covered by the six standard Grassmann charts of $\operatorname{Gr}(2,4)$.

For each chart, the complete condition-(A) family is obtained by substituting $Z_{\mathcal{I}}(\Theta)=K_LW_{\mathcal{I}}(\Theta)$ into

$$
\operatorname{rank}\begin{pmatrix}Z_{\mathcal{I}}(\Theta) & AZ_{\mathcal{I}}(\Theta)R_{Z_{\mathcal{I}}(\Theta)}\end{pmatrix}=2,
\qquad
\operatorname{im}R_{Z_{\mathcal{I}}(\Theta)}=\ker(CAZ_{\mathcal{I}}(\Theta)).
$$

Condition (S) is then tested on every retained condition-(A) branch through

$$
\operatorname{rank}\begin{pmatrix}(\lambda I-A)V & Z_{\mathcal{I}}(\Theta)\end{pmatrix}
=
\operatorname{rank}\begin{pmatrix}V & Z_{\mathcal{I}}(\Theta)\end{pmatrix},
\quad \lambda\in\mathbb{C}.
$$

Exact evaluation of condition (S) over all condition-(A) branches obtained from the six charts of $\operatorname{Gr}(2,4)$ shows that no branch satisfies condition (S). Since these six charts cover all two-dimensional subspaces of $\ker\begin{pmatrix}C\\ L\end{pmatrix}$, this proves that no order-4 functional observer exists. Consequently,

$$
4\notin\Sigma_{FO}(L).
$$

Hence feasibility need not occur even at the first order above the algebraic lower bound.

### C. Feasibility at $q=q_0+2=5$

Consider now

$$
q=q_0+2=5,\qquad d=n-p-q=1.
$$

A feasible one-dimensional subspace is generated by

$$
Z_5=\begin{pmatrix}1&1&1&0&-2&1&0&0\end{pmatrix}^T.
$$

Indeed,

$$
\operatorname{rank}Z_5=1,\qquad CZ_5=0,\qquad LZ_5=0.
$$

Moreover,

$$
CAZ_5=\begin{pmatrix}-3\\ -1\end{pmatrix},
$$

which has full column rank, so that $\ker(CAZ_5)=\{0\}$ and $R_{Z_5}$ has no columns. Condition (A) therefore reduces to $\operatorname{rank}(Z_5)=1$, which holds trivially.

For condition (S), choose any full-column-rank matrix $V$ satisfying $\operatorname{im}V=\ker\begin{pmatrix}C\\ CA\end{pmatrix}$, $\operatorname{rank}V=4$. For the present $Z_5$,

$$
h=\operatorname{rank}\begin{pmatrix}V & Z_5\end{pmatrix}=5.
$$

Consider

$$
P_5(\lambda)=\begin{pmatrix}(\lambda I-A)V & Z_5\end{pmatrix}.
$$

Let $\Delta_j(\lambda)$ denote its nonzero $5\times 5$ minors. Exact symbolic computation with rational coefficients gives

$$
\gcd_{\lambda}\{\Delta_j(\lambda)\}=1.
$$

Hence the maximal minors have no common zero in $\mathbb{C}$, and therefore

$$
\operatorname{rank}\begin{pmatrix}(\lambda I-A)V & Z_5\end{pmatrix}
=
\operatorname{rank}\begin{pmatrix}V & Z_5\end{pmatrix}=5,
\qquad \lambda\in\mathbb{C}.
$$

Condition (S) is therefore satisfied, and

$$
5\in\Sigma_{FO}(L).
$$

Since the only admissible orders below $q=5$ are $q=3$ and $q=4$, both of which have been proved infeasible, it follows that

$$
\nu_{\min}=5=q_0+2.
$$

### D. Existence at the functional-observability endpoint

It remains to consider

$$
q=n_0-p=6.
$$

At this order, $d=n-p-q=0$. Since $d=0$, the terminal nullspace is trivial. Hence Theorem 7 gives

$$
6\in\Sigma_{FO}(L).
$$

Combining the four admissible orders therefore gives

$$
\Sigma_{FO}(L)=\{5,6\}
$$

and

$$
\nu_{\min}=5=q_0+2<n_0-p=6.
$$

Equivalently,

$$
q=3:\text{ infeasible},\quad q=4:\text{ infeasible},\quad
q=5:\text{ feasible},\quad q=6:\text{ feasible}.
$$

### E. Explicit Observer Realization at $q=5$

We complete the example by exhibiting an explicit order-5 realization and the resulting observer parameters. An explicit $\mathcal{L}$ satisfying conditions (A) and (S) at $q=5$, obtained by augmenting $L$ with three additional rows spanning a complement of a one-dimensional admissible $\operatorname{im}Z$ within $\ker\begin{pmatrix}C\\ L\end{pmatrix}$, is

$$
\mathcal{L}=
\begin{pmatrix}
-2 & -1 & -2 & -3 & -1 & 3 & 2 & 0\\
1 & -1 & -2 & 1 & 0 & 2 & 0 & 1\\
-47/460 & 1 & 0 & 0 & 0 & 0 & 0 & 0\\
-137/230 & 0 & 1 & 0 & 0 & 0 & 0 & 0\\
313/460 & 0 & 0 & 1 & 0 & 0 & 0 & 0
\end{pmatrix}.
$$

The first two rows of $\mathcal{L}$ are exactly $L$, so that $\hat{z}(t)=\begin{pmatrix}\hat{z}_1(t)\\ \hat{z}_2(t)\end{pmatrix}$, the first two components of the observer's output estimate, recovers an estimate of the original functional $Lx(t)$; the remaining three rows complete $\mathcal{L}$ to order 5.

With $\mathcal{L}$ fixed, the classical construction of Darouach [8] applies directly to the augmented functional $z(t)=\mathcal{L}x(t)$: writing $\mathcal{L}^+$ for the Moore–Penrose pseudoinverse of $\mathcal{L}$ and $\bar A=A(I-\mathcal{L}^+\mathcal{L})$, $\bar C=C(I-\mathcal{L}^+\mathcal{L})$, the matrices $F$ and $G$ of [8] are computed from $\Sigma=(\bar C\bar A;\ \bar C)$ exactly as in [8, eq. (18)–(19)]. Choosing the pole-placement gain so that

$$
\operatorname{eig}(N)=\{-1,-2,-3,-4,-5\},
$$

the resulting observer

$$
\dot{w}(t)=Nw(t)+Jy(t)+Hu(t),\qquad \hat{z}(t)=w(t)+Ey(t)
$$

with $B=e_1+e_8$, has parameters (to four decimal places)

$$
N=
\begin{pmatrix}
-6.4875 & 5.9071 & 8.4553 & -4.8640 & -20.234\\
12.169 & -18.141 & -9.5627 & 5.1427 & 34.253\\
1.8872 & -2.7798 & -3.9721 & 1.3778 & 6.3501\\
-4.3193 & 5.4644 & 3.6803 & -4.9568 & -12.670\\
6.4681 & -8.7816 & -6.4945 & 3.6414 & 18.557
\end{pmatrix},
$$

$$
J=
\begin{pmatrix}
-3.7981 & -5.1655\\
-41.180 & 28.916\\
-6.3270 & 4.6726\\
13.788 & -10.727\\
-17.718 & 14.100
\end{pmatrix},
\qquad
H=
\begin{pmatrix}
-1.2552\\
37.467\\
1.9827\\
-11.249\\
16.003
\end{pmatrix},
$$

$$
E=
\begin{pmatrix}
-1.0312 & 2.9504\\
8.1345 & -2.6025\\
0.74289 & -0.81478\\
-2.7973 & 1.6668\\
3.8531 & -1.9714
\end{pmatrix}.
$$

Direct substitution confirms that these parameters satisfy the Sylvester equation $PA-NP-JC=0$ of [8, eq. (3)], where $P=\mathcal{L}-EC$, to within machine precision (residual norm $\approx 1.4\times 10^{-13}$), and $H=PB$ as required by [8, eq. (4)]. This exhibits, for the present example, a complete and numerically verified order-5 functional observer at the true minimum order $\nu_{\min}=5$, with eigenvalues placed at $-1,-2,-3,-4,-5$, realized via the classical Sylvester-equation construction applied to the augmented functional $\mathcal{L}$ rather than to $L$ itself.

### F. Interpretation

Combining the relevant dimensions gives

$$
r=2<q_0=3<\nu_{\min}=5<n_0-p=6.
$$

Unlike an example in which the minimum functional-observer order coincides with the functional-observability endpoint, here $\nu_{\min}$ is strictly interior to the admissible range: one order, $q=6$, remains feasible above the minimum. The example therefore separates all four quantities $r$, $q_0$, $\nu_{\min}$, and $n_0-p$ simultaneously.

The gap between the algebraic lower bound and the actual minimum is again greater than one:

$$
q_0=3,\qquad q_0+1=4,
$$

are both excluded by condition (S) — in both cases through the same underlying mechanism, in which condition (A)'s complete family is confined to a locus on which the pencil matrix $H$ is provably full-rank — whereas

$$
q_0+2=5
$$

is feasible. This confirms that $q_0$ is an algebraic lower bound, not a guarantee that a functional observer exists either at that order or at the immediately succeeding order, and that this two-order gap can occur independently of whether $\nu_{\min}$ coincides with the functional-observability endpoint.

For the present example, we also apply the functional-observer design algorithm of Darouach and Fernando [27], which is based on sufficient solvability conditions. The order-$r$ existence condition fails at $q=2$. At $q=3,4,5$, the corresponding solvability conditions impose nontrivial restrictions on the pole-placement matrix $N$ and hence fail for a generic choice of $N$. At $q=6=n-p$, by contrast, $\mathcal{O}(C,A,4)$ has full column rank, so the solvability condition is satisfied for arbitrary $N$. Thus the algorithm of [27] generically reaches the reduced-order Luenberger endpoint $q=6$, whereas the present order-by-order characterization establishes that the true minimum functional-observer order is $\nu_{\min}=5$.

---

## VIII. Discussion and Conclusion

### A. Discussion

The characterization separates three questions that are easily conflated in minimum-order observer design. First, the FO indices determine the smallest order at which the algebraic condition can hold. Second, functional observability implies that algebraic feasibility then persists at every higher order through $n_0-p$. Third, spectral feasibility is a separate fixed-order question. The nullspace pencil (6) provides the same spectral test at every one of these predetermined orders.

This distinction also avoids a replacement-versus-augmentation difficulty: a higher-order realization $\mathcal{L}$ may either *augment* a smaller one, in the sense of containing the rows of a particular minimum-order realization as a submatrix (modulo $C$), or it may be a *replacement* realization whose rows bear no such relationship to any specific smaller solution, yet still satisfy condition (A) at the higher order in their own right. Consequently, parameterizing only one-row extensions of the complete minimum-(A) family would not in general describe all higher-order realizations. The matrix representation $Z=K_LW$, together with the rank conditions (14a)–(14b), parameterizes the order-$q$ problem directly and therefore includes replacement realizations automatically.

An important consequence is that $\Sigma_{FO}(L)$ need not inherit the interval structure of the algebraic spectrum $\Sigma_A(L)$; functional-observer existence must therefore be determined independently at each admissible order.

For the all-$\lambda$ pole-assignability formulation, additional rank screening can be developed from the common columns represented by $Z$ and $V$. Such screening is useful computationally but is not required for the main equivalence. For the detectability formulation, care is required because rank loss at a strictly stable value of $\lambda$ is permitted.

### B. Conclusion

This paper has given an order-by-order characterization of functional observers between the algebraic lower endpoint and the endpoint determined by functional observability. The FO indices determine $q_0=\sum_{j=1}^{r}\eta_j$, the minimum order for which condition (A) is feasible, and the one-row extension theorem shows that condition (A) remains feasible at every order $q_0,q_0+1,\ldots,n_0-p$ under functional observability. At each such order, the fixed-order problem is expressed entirely through matrix ranks, nullspaces, and column spaces in the original state coordinates, yielding a complete matrix parameterization of the algebraic and spectral observer conditions.

Evaluating these conditions over $q\in\{q_0,\ldots,n_0-p\}$ yields the complete functional-observer order spectrum $\Sigma_{FO}(L)$ and hence the true minimum order

$$
\nu_{\min}=\min\Sigma_{FO}(L).
$$

As the example in Section VII demonstrates, the algebraic lower bound $q_0$ need not itself be feasible, nor need feasibility occur at the immediately succeeding order. Thus $q_0$ determines where the search begins, whereas $\nu_{\min}$ identifies the first order at which both the algebraic and spectral conditions are satisfied.

The upper endpoint $n_0-p$ is represented by a basis of $\ker(\mathcal{O}_C)$; when $n_0=n$, this basis has no columns and the endpoint reduces to the classical reduced-order Luenberger order $n-p$. When $q_0=r$, the lower endpoint reduces to Darouach's prescribed order. Thus the Darouach and Luenberger orders arise as specializations of the two endpoints of the same matrix-based functional-observer framework, with $\nu_{\min}$ characterized as the smallest order in this range at which the algebraic and spectral conditions hold jointly.

---

## References

[1] D. G. Luenberger, "Observers for multivariable systems," *IEEE Trans. Autom. Control*, vol. AC-11, no. 2, pp. 190–197, Apr. 1966.

[2] T. E. Fortmann and D. Williamson, "Design of a low order observer for linear feedback control laws," *IEEE Trans. Autom. Control*, vol. AC-17, no. 3, pp. 301–308, Jun. 1972.

[3] P. Murdoch, "Observer design of a linear functional of the state vector," *IEEE Trans. Autom. Control*, vol. AC-18, no. 3, pp. 308–310, Jun. 1973.

[4] J. R. Roman and T. E. Bullock, "Design of minimal-order stable observers for linear functions of the state via realization theory," *IEEE Trans. Autom. Control*, vol. AC-20, no. 5, pp. 613–622, Oct. 1975.

[5] J. B. Moore and G. F. Ledwich, "Minimal-order observers for estimating linear functionals of a state vector," *IEEE Trans. Autom. Control*, vol. AC-20, no. 5, pp. 623–632, Oct. 1975.

[6] K. Furuta and S. Kawaji, "Linear functional observer with possible minimal dimension," *IEEE Trans. Autom. Control*, vol. AC-22, no. 6, pp. 977–980, Dec. 1977.

[7] H. R. Sirisena, "Minimal-order observer for linear functions of the state vector," *Int. J. Control*, vol. 29, pp. 235–254, 1979.

[8] M. Darouach, "Existence and design of functional observers," *IEEE Trans. Autom. Control*, vol. 45, no. 5, pp. 940–943, 2000.

[9] H. Trinh, T. D. Tran, and S. Nahavandi, "Design of scalar functional observers of order less than $\nu-1$," *International Journal of Control*, vol. 79, no. 12, pp. 1654–1659, 2006.

[10] T. Fernando, H. Trinh, and L. Jennings, "Functional observability and the design of minimum order linear functional observers," *IEEE Trans. Autom. Control*, vol. 55, no. 5, pp. 1268–1273, 2010.

[11] L. Jennings, T. Fernando, and H. Trinh, "Existence conditions for functional observability from an eigenspace perspective," *IEEE Trans. Autom. Control*, vol. 56, no. 12, pp. 2957–2961, 2011.

[12] F. Rotella and I. Zambettakis, "Minimal single linear functional observers for linear systems," *Automatica*, vol. 47, no. 1, pp. 164–169, Jan. 2011.

[13] M. Hamdoun, M. Ayadi, F. Rotella, and I. Zambettakis, "Minimal single linear functional observers for discrete-time linear systems," in *Proc. 4th Int. Conf. Control, Decision and Inf. Technol. (CoDIT)*, Barcelona, Spain, pp. 772–777, 2017.

[14] K. Kumar, A. Prakash, S. K. Parida, S. Ghosh, and C. Kumar, "A novel multi-functional observer based distributed WADC for large power system using modified decoupled control approach," *IEEE Trans. Power Systems*, vol. 39, no. 5, pp. 6662–6674, 2024.

[15] H. H. Alhelou, M. E. H. Golshan, and N. D. Hatziargyriou, "A decentralized functional observer based optimal LFC considering unknown inputs, uncertainties, and cyber-attacks," *IEEE Trans. Power Systems*, vol. 34, no. 6, pp. 4408–4417, 2019.

[16] D. C. Huong and H. Trinh, "Dynamic event-triggered distributed interval functional observers for interconnected systems," *Asian Journal of Control*, vol. 25, pp. 2194–2203, 2023.

[17] Y. Zhang, R. Cheng, and Y. Xia, "On the structural output controllability and functional observability of undirected networks," *Automatica*, vol. 173, Art. no. 112063, 2025.

[18] Y. Zhang, R. Cheng, and Y. Xia, "Observability blocking for functional privacy of linear dynamic networks," in *Proc. 62nd IEEE Conf. Decision and Control*, 2023, pp. 7469–7474.

[19] A. N. Montanari, C. Duan, L. A. Aguirre, and A. E. Motter, "Functional observability and target state estimation in large-scale networks," *Proc. Natl. Acad. Sci. USA*, vol. 119, no. 1, e2113750119, 2022.

[20] A. N. Montanari, C. Duan, and A. E. Motter, "Duality between controllability and observability for target control and estimation in networks," *IEEE Trans. Autom. Control*, 2025, doi: 10.1109/TAC.2025.3552001.

[21] I. Krauss, V. G. Lopez, and M. A. Müller, "On sample-based functional observability of linear systems," *IEEE Control Systems Letters*, 2025, doi: 10.1109/LCSYS.2025.3582512.

[22] S. Muntwiler, J. Köhler, and M. N. Zeilinger, "Nonlinear functional estimation: Functional detectability and full information estimation," *Automatica*, vol. 171, Art. no. 111945, 2025.

[23] C. Kravaris, "Functional observers for nonlinear systems," *IFAC-PapersOnLine*, vol. 49, no. 18, pp. 505–510, 2016.

[24] C. Kravaris and S. Venkateswaran, "Functional observers with linear error dynamics for nonlinear systems," *Systems & Control Letters*, vol. 157, Art. no. 105021, 2021.

[25] T. Fernando, "A minimum-order functional observer beyond the Darouach and Luenberger constructions," arXiv preprint arXiv:2609.33615, 2026, doi: 10.48550/arXiv.2609.33615. [Online]. Available: https://arxiv.org/abs/2609.33615

[26] T. Fernando, H. Trinh, and L. Jennings, "Functional observability," in *Proc. 5th Int. Conf. Information and Automation for Sustainability*, Colombo, Sri Lanka, 2010, pp. 421–423.

[27] M. Darouach and T. Fernando, "On functional observability and functional observer design," *Automatica*, vol. 173, Art. no. 112115, 2025.

---

## Biography

**Tyrone Fernando** received his B.E. (Hons.) and Ph.D. degrees in Electrical Engineering from the University of Melbourne, Victoria, Australia, in 1990 and 1996, respectively. In 1996, he joined the Department of Electrical, Electronic and Computer Engineering, University of Western Australia (UWA), Crawley, WA, Australia, where he currently holds the position of Professor of Electrical Engineering. He previously served as Associate Head and Deputy Head of the department from 2008 to 2010.

Prof. Fernando is currently the Head of the Power and Clean Energy Research Group at UWA. He has provided professional consultancy to Western Power on the integration and management of distributed energy resources in the electric grid. In recognition of his professional contributions, he was named the Outstanding WA IEEE PES/PELS Engineer in 2018. His research interests include theoretical control, observer design, and power system stability and control. He has received multiple teaching awards from UWA in recognition of his contributions to control systems and power systems education.
