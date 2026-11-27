# Functional Observability and the Design of Minimum Order Linear Functional Observers
> IEEE TRANSACTIONS ON AUTOMATIC CONTROL, VOL. 55, NO. 5, MAY 2010

**Authors**: Tyrone Lucius Fernando, Hieu Minh Trinh, and Les Jennings

## Abstract
The design of a minimum‑order linear functional observer for linear time‑invariant systems has been an open problem for over four decades. This technical note provides a solution to this problem. The technical note also introduces the concept of **Functional Observability/Detectability** and shows that the well‑known concept of Observability/Detectability is a special case of Functional Observability/Detectability.

**Index Terms**: Functional detectability, functional observability, functional observers, minimum order observers.

## I. INTRODUCTION
Linear functional observers estimate linear functions of the state vector of a system without estimating all the individual states. Such functional estimates are useful in feedback control system design because the control signal is often a linear combination of the states, and it is possible to utilize a linear functional observer to directly estimate the feedback control signal. The concept of linear functional observers has been around for more than four decades [1]. Yet to date, a method for designing a minimum‑order linear functional observer has not been reported and this has remained an open problem [2]‑[12] until now.

For a long time, it was understood that an observer that estimates linear functions of the state vector can have a lower order than that would be required to estimate the entire state vector. The concept of estimating linear functions was first explored by Luenberger [1]. Following the pioneering work of Luenberger [1], several other methods for solving single‑functional and multi‑functional observers were presented [2]‑[16]. Darouach in [16] reported necessary and sufficient conditions for the existence and the design of an $r$-order linear functional observer where $r$ is the number of linear functions to be estimated. Conditions to assure minimality of observers are also reported in [17], however those minimality conditions cannot always be satisfied, and hence a minimum observer structure cannot always be designed using previously reported results.

Despite all the contributions related to linear functional observers made so far, the problem of designing a minimum‑order linear functional observer remained unsolved for over four decades. This technical note provides a solution to this problem. The proposed solution is based on recognizing:
1. Increasing the number of functions to be estimated increases the order of the observer by the same magnitude;
2. In order to estimate the desired linear functions, it is sometimes necessary to estimate extra linear functions as well as the desired linear functions.

Consequently, the problem of designing a minimum‑order linear functional observer is solved via finding the minimum number of extra linear functions that needs to be estimated. In solving the minimum‑order observer problem, the technical note also introduces the concept of Functional Observability/Detectability and shows that the well‑known concept of Observability/Detectability is a special case of Functional Observability/Detectability.

This technical note is organized as follows:
- Section II details the notations used in the technical note
- Section III provides a statement of the problem
- Section IV presents the methodology, here it is shown that in some instances it is necessary to estimate extra linear functions in order to estimate the desired linear functions
- Section V presents the main results
- Section VI gives two numerical examples
- Section VII is conclusion
- Proofs for all Lemmas and Theorems are given in Appendix

> Manuscript received July 29, 2008; revised August 06, 2008. First published February 08, 2010; current version published May 12, 2010. Recommended by Associate Editor A. Ferrara.
>
> T. L. Fernando is with the School of Electrical, Electronic and Computer Engineering, University of Western Australia, Crawley, WA 6009, Australia (e‑mail: tyrone@ee.uwa.edu.au).
>
> H. M. Trinh is with the School of Engineering, Deakin University, Geelong, VIC 3217, Australia (e‑mail: hieu.trinh@deakin.edu.au).
>
> L. Jennings is with the School of Mathematics and Statistics, University of Western Australia, Crawley, WA 6009, Australia (e‑mail: les@maths.uwa.edu.au).
>
> Digital Object Identifier 10.1109/TAC.2010.2042761
>
> $0018‑9286/\$26.00$ © 2010 IEEE

## II. NOTATION
A basis for a subspace of $\mathbb{R}^{n}$ is a set of row vectors $\{q_{1},\dots,q_{k}\}$. We use the notation $[[\cdot]]$ to mean a matrix of row basis vectors for the subspace.

The **row space** of a matrix $M$:
\[
\mathcal{R}(M)=\{v: v=\mu M,\ \forall \mu\}.
\]

The **row nullspace** of a matrix $M$:
\[
\mathcal{N}(M)=\{v: v M=0\}.
\]

Perpendicular subspace to subspace $S\subset\mathbb{R}^{n}$:
\[
S^{\perp}=\left\{v\in\mathbb{R}^{n}:\langle v,\mu\rangle=0,\ \forall \mu\in S\right\}
\]
where $\langle\cdot,\cdot\rangle$ denotes inner product.

Other symbols:
- $I$: identity matrix of appropriate dimension
- $(\cdot)'$: matrix transpose
- $\text{rank}(\cdot)$: matrix rank
- $\text{eig}(\cdot)$: set of eigenvalues
- $\text{rows}(\cdot),\ \text{cols}(\cdot)$: number of rows, columns
- $\text{bincoeff}(n,k)$: binomial coefficient, number of $k$‑element subsets of an $n$‑element set.

## III. PROBLEM STATEMENT
Consider a linear time‑invariant system:
\[
\(\begin{cases}
\dot{x}(t)=A x(t)+B u(t), \tag{1a}\\[4pt]
y(t)=C x(t), \tag{1b}\\[4pt]
z_{0}(t)=L_{0} x(t). \tag{1c}
\end{cases}\)
\]
Where:
- $x(t)\in\mathbb{R}^{n}$: state vector
- $u(t)\in\mathbb{R}^{m}$: input vector
- $y(t)\in\mathbb{R}^{p}$: output vector
- $z_{0}(t)\in\mathbb{R}^{r}$: vector of linear functions to be estimated
- Constant matrices: $A\in\mathbb{R}^{n\times n},\ B\in\mathbb{R}^{n\times m},\ C\in\mathbb{R}^{p\times n},\ L_{0}\in\mathbb{R}^{r\times n}$.

Assumptions (without loss of generality):
$\text{rank}(C)=p$, $\text{rank}(L_{0})=r$, $\text{rank}\begin{bmatrix}C\\L_{0}\end{bmatrix}=p+r$. Assume no stable uncontrollable states in the system.

Define extended function vector:
\[
\(z(t)\)=\begin{bmatrix}z_{0}(t)\\z_{1}(t)\end{bmatrix}=L x(t),\quad \(z(t)\)\in\mathbb{R}^{\bar{r}},\quad r\le \bar{r}\le n.
\]

Functional observer structure:
\[
\(\begin{cases}
\dot{w}(t)=N w(t)+J y(t)+H u(t), \tag{2a}\\[4pt]
\hat{z}(t)=w(t)+E y(t). \tag{2b}
\end{cases}\)
\]
with $w(t)\in\mathbb{R}^{\bar{r}}$.

**Problem**: Design minimum‑order linear functional observer of form (2a)‑(2b) with arbitrary poles. Find matrices $\(H,E,J,N\)$ with arbitrary eigenvalues and minimal $\bar{r}$, such that $\hat{z}(t)\to \(z(t)\)$ as $t\to\infty$ for any $\(x(0),w(0),u(t)\)$.

## IV. METHODOLOGY
Observer error: $\epsilon(t)=\(z(t)\)-\hat{z}(t)$. Error dynamics:
\[
\begin{aligned}
\dot{\epsilon}(t) &= N \epsilon(t)+\big(L A-E C A-N L+N E C-J C\big)x(t) \\
&\quad +\big(L B-E C B-H\big)u(t). \tag{3}
\end{aligned}
\]

**Theorem 1**: $\epsilon(t)\to 0$ as $t\to\infty$ for any $\(x(0),w(0),u(t)\)$ if and only if $N$ is Hurwitz and
\[
\begin{align}
L A-E C A-N L+N E C-J C &=0, \tag{4a}\\
L B-E C B-H &=0. \tag{4b}
\end{align}
\]

**Theorem 2 [16]**: There exists an $\bar{r}$‑order linear functional observer (2a)‑(2b) with arbitrary poles such that $\hat{z}(t)$ asymptotically estimates $\(z(t)\)$ for all $\(x(0),w(0),u(t)\)$ **iff** Condition 1 and Condition 2 hold:
\[
\textbf{Condition 1}:\quad
\operatorname{rank}\begin{bmatrix}L A\\C A\\C\\L\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}C A\\C\\L\end{bmatrix}. \tag{5a}
\]

\[
\textbf{Condition 2}:\quad
\operatorname{rank}\begin{bmatrix}s L-L A\\C A\\C\\C\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}C A\\C\\L\end{bmatrix},\quad \forall s\in\mathbb{C}. \tag{5b}
\]

> Remark: In reference [16], Condition 2 uses $s\in\mathbb{C},\Re(s)\ge 0$ giving only stable poles; using all $s\in\mathbb{C}$ allows arbitrary stable observer poles.

$\bar{r}$ equals the number of rows of matrix $L$ (which contains $L_0$ as subset). Minimum‑order observer problem reduces to finding the matrix $L$ with **minimum number of rows** satisfying Condition1 and Condition2.
- If $L=L_0$ satisfies both conditions: minimal observer order is $r$.
- If not: minimal order > $r$, equal to row count of smallest valid $L$.

## V. MAIN RESULTS
Define
\[
\tilde T_1=\begin{bmatrix}C\\C A\end{bmatrix},\quad
\tilde T_2=\begin{bmatrix}\tilde T_1\\L\end{bmatrix}.
\]
\[
T_1=\big[\big[\mathcal{R}(\tilde T_1)\big]\big],\quad
T_2=\big[\big[\mathcal{R}(\tilde T_2)\big]\big], \tag{7}
\]
\[
T_3=\begin{bmatrix}\bar L A\\T_2\end{bmatrix},
\]
where $\bar L$ consists of rows of $L$ such that $\bar L A$ does not belong to row space of $T_2$.

Let
\[
\(a=\operatorname{rank}(T_2),\tag{9}\qquad
b=\operatorname{rank}(T_3).\tag{10}\)
\]

Condition 1 is equivalent to:
\[
\mathcal{R}(T_3)=\mathcal{R}(T_2). \tag{11}
\]

When Condition1 fails, finite iteration on index $j$ augments $L$. Let $L_j$ denote augmented matrix containing original $L_0$. $a_j,b_j,T_2^j,T_3^j$ are corresponding quantities for $L=L_j$.

**Lemma 1**: Let $L=L_j$. Let matrices $\Phi_j,\Psi_j$ with $b_j$ columns satisfy
\[
\begin{bmatrix}\Phi_j & \Psi_j\end{bmatrix}
=\Big[\Big[\mathcal{N}\Big(\begin{bmatrix}T_3^j A\\T_3^j\end{bmatrix}\Big)\Big]\Big].
\]
Let $\Theta_j,\Xi_j$ satisfy
\[
\begin{bmatrix}\Theta_j & \Xi_j\end{bmatrix}
=\Big[\Big[\mathcal{N}\Big(\begin{bmatrix}\Phi_j T_3^j\\T_2^j\end{bmatrix}\Big)\Big]\Big]. \tag{13}
\]
Define
\[
\Gamma_j
=\Big[\Big[\mathcal{R}(\Phi_j T_3^j)\cap \mathcal{R}(\Theta_j \Phi_j T_3^j)^{\perp}\Big]\Big]
=\big[\big[\mathcal{R}(\Theta_j)^{\perp}\big]\big]\,\Phi_j T_3^j.
\]
If row vector $q\in\mathcal{R}(\Gamma_j)$, then $L=\begin{bmatrix}L_j\\q\end{bmatrix}$ increases $a_j$ by $1$ for each $q$ (up to $a_j+\operatorname{rank}(\Gamma_j)$), while keeping $b_j$ unchanged.

When Condition1 fails for $L_0$, construct
\[
L_1=\begin{bmatrix}
L_0\\
\Gamma_0\\
\Big[\Big[\mathcal{R}(T_3^0)\cap \mathcal{R}\Big(\begin{bmatrix}T_2^0\\\Gamma_0\end{bmatrix}\Big)^{\perp}\Big]\Big]
\end{bmatrix}. \tag{15}
\]

General iterative update:
\[
L_{j}=\begin{bmatrix}
L_{j-1}\\
\Gamma_{j-1}\\
\Big[\Big[\mathcal{R}(T_3^{j-1})\cap \mathcal{R}\Big(\begin{bmatrix}T_2^{j-1}\\\Gamma_{j-1}\end{bmatrix}\Big)^{\perp}\Big]\Big]
\end{bmatrix}. \tag{16}
\]

Iterate until $\mathcal{R}(T_3^j)=\mathcal{R}(T_2^j)$. Define
\[
\beta=\min\left\{j\;\big|\; \mathcal{R}(T_3^j)=\mathcal{R}(T_2^j)\right\}. \tag{18}
\]
Then minimal matrix satisfying Condition1:
\[
L_{\beta}=
\begin{cases}
L_0 & \beta=0,\\[4pt]
\begin{bmatrix}L_{\beta-1}\\\Gamma_{\beta-1}\end{bmatrix} & \beta>0.
\end{cases} \tag{19}
\]

Iteration steps for each $j$:
1. Append vectors to $L$ to increase $a$ without increasing $b$ (by Lemma 1).
2. Compute updated $T_2,T_3$. If $\mathcal{R}(T_3)=\mathcal{R}(T_2)$, stop; otherwise append rows of $LA$ outside $\mathcal{R}(T_2)$ and continue iteration.

**Lemma 2**: Let $X_2=\big[\big[\mathcal{R}(T_2^{\beta})^{\perp}\big]\big]$. Take $j$ left eigenvectors of matrix $X_2 A X_2'$ to form matrix $\Upsilon_j^i$, post‑multiply by $X_2$. There are $\text{bincoeff}(n-a_{\beta},j)$ such matrices indexed by $i$. Then Condition1 holds for $a=b=a_{\beta}+j$ with $L=\Sigma\begin{bmatrix}L_{\beta}\\\Upsilon_j^i\end{bmatrix}$ where $\Sigma$ is any compatible non‑singular matrix.

**Lemma 3**: If Condition1 holds but Condition2 fails, adding any row from $\mathcal{R}(C)$ to $L$ cannot make Condition2 hold.

**Lemma 4**: If Condition1 holds but Condition2 fails, adding row linearly independent of $\mathcal{R}(T_2)=\mathcal{R}(T_3)$ (increasing both $\(a,b\)$ by one) cannot satisfy Condition2.

From Lemma3‑4: To satisfy Condition2 (given Condition1 satisfied), new rows must come from $\mathcal{R}(CA)$.

**Lemma 5**: Let $\Omega_1,\Delta_1$ satisfy
\[
\begin{bmatrix}\Omega_1 & \Delta_1\end{bmatrix}
=\Big[\Big[\mathcal{N}\Big(\begin{bmatrix}C A^2\\T_2^{\beta}\end{bmatrix}\Big)\Big]\Big]. \tag{20}
\]
Define
\[
U_{\beta}=\Omega_1 C A. \tag{21}
\]
Then $L=\begin{bmatrix}L_{\beta}\\q\end{bmatrix}$ satisfies Condition1 with $a=b=a_{\beta}=b_{\beta}$ iff $q\in\mathcal{R}(U_{\beta})$.

**Lemma 6**: For $j\in\{1,\dots,n-a_{\beta}\}$ and index $i$, define
\[
\begin{bmatrix}\Omega_2^i & \Delta_2^i\end{bmatrix}
=\Big[\Big[\mathcal{N}\Big(\begin{bmatrix}C A^2\\T_2^{\beta+j}\end{bmatrix}\Big)\Big]\Big],
\]
\[
U_{\beta+j}^i=\Omega_2^i C A. \tag{23}
\]
Then $L=\begin{bmatrix}L_{\beta}\\\Upsilon_j^i\\q\end{bmatrix}$ satisfies Condition1 with $a=b=a_{\beta}+j=b_{\beta}+j$ iff $q\in\mathcal{R}(U_{\beta+j}^i)$.

> **Remark 1**:
> - $L=\begin{bmatrix}L_{\beta}\\U_{\beta}\end{bmatrix}$ satisfies Condition1 for $a=b=a_{\beta}=b_{\beta}$.
> - $L=\begin{bmatrix}L_{\beta}\\\Upsilon_j^i\\U_{\beta+j}^i\end{bmatrix}$ satisfies Condition1 for $a=b=a_{\beta}+j=b_{\beta}+j$.

### Definition 1 (Functional Observability)
Triple $(A,C,L_0)$ is **Functional Observable** if there exists matrix $L\in\mathbb{R}^{\bar{r}\times n}$ ($r\le\bar{r}\le n$) such that $\mathcal{R}(L)\supseteq\mathcal{R}(L_0)$ and $L$ satisfies Condition1 and Condition2.

**Theorem 3**: Triple $(A,C,L_0)$ is Functional Observable iff Condition2 holds for at least one matrix among
\[
L=\begin{bmatrix}L_{\beta}\\U_{\beta}\end{bmatrix},\quad
L=\begin{bmatrix}L_{\beta}\\\Upsilon_j^i\\U_{\beta+j}^i\end{bmatrix},\quad
j\in\{1,\dots,n-a_{\beta}\},\ i=1,\dots,\text{bincoeff}(n-a_{\beta},j).
\]

Define non‑negative deficiency quantities:
\[
\chi_1 = b_{\beta}-\min_{s\in\mathbb{C}}
\operatorname{rank}\begin{bmatrix}s L_{\beta}-L_{\beta}A\\T_1\end{bmatrix}, \tag{24}
\]
\[
\chi_2 = b_{\beta}-\min_{s\in\mathbb{C}}
\operatorname{rank}\begin{bmatrix}s L_{\beta}-L_{\beta}A\\s U_{\beta}-U_{\beta}A\\T_1\end{bmatrix}, \tag{25}
\]
\[
\chi_3(i,j) = b_{\beta}+j-\min_{s\in\mathbb{C}}
\operatorname{rank}\begin{bmatrix}s L_{\beta}-L_{\beta}A\\s \Upsilon_j^i-\Upsilon_j^i A\\T_1\end{bmatrix}, \tag{26}
\]
\[
\chi_4(i,j) = b_{\beta}+j-\min_{s\in\mathbb{C}}
\operatorname{rank}\begin{bmatrix}s L_{\beta}-L_{\beta}A\\s \Upsilon_j^i-\Upsilon_j^i A\\s U_{\beta+j}^i-U_{\beta+j}^i A\\T_1\end{bmatrix}. \tag{27}
\]

> **Remark 2**: When Condition1 holds but Condition2 fails, rank deficit occurs at eigenvalues of matrix $D_2$ defined by $LA=D_1 T_1+D_2 L$.

**Lemma 7**: $(A,C,L_0)$ is Functional Observable iff either there exists sub‑matrix $U_{k_1}$ (take $\chi_1$ rows from $U_\beta$) such that $L=\begin{bmatrix}L_\beta\\U_{k_1}\end{bmatrix}$ satisfies Condition2; or there exists $\tilde U_{k_2}$ (take $\chi_3(i,j)$ rows from $U_{\beta+j}^i$) such that $L=\begin{bmatrix}L_\beta\\\Upsilon_j^i\\\tilde U_{k_2}\end{bmatrix}$ satisfies Condition2.

**Theorem 4**: Assume $(A,C,L_0)$ is Functional Observable.
Let $U_1^*=U_{k_1}$ such that $L=\begin{bmatrix}L_\beta\\U_1^*\end{bmatrix}$ satisfies Condition2.
Let $j^*$ be minimal integer $j$ for which there exists $i^*$ and $\tilde U_{k_2}=U_2^*$ making $L=\begin{bmatrix}L_\beta\\\Upsilon_{j^*}^{i^*}\\U_2^*\end{bmatrix}$ satisfy Condition2.
Then minimal valid $L$ is:
\[
L_{\text{min}}=
\begin{cases}
L_{\beta} & \chi_1=0,\\[4pt]
\begin{bmatrix}L_{\beta}\\U_1^{*}\end{bmatrix} & \chi_1\neq0,\ \chi_2=0,\\[6pt]
\begin{bmatrix}L_{\beta}\\\Upsilon_{j^*}^{i^*}\\U_2^{*}\end{bmatrix} & \chi_1\neq0,\ \chi_2\neq0.
\end{cases}
\]

> **Remark3**: Restrict $s\in\mathbb{C},\Re(s)\ge0$ in Condition2 and formulas (24)‑(27): then we get **Functional Detectability**, guaranteeing only stable observer poles (not arbitrary assignment).
>
> **Remark4**: When $L_0=I$, Functional Observability/Detectability of triple $\((A,C,I)\)$ reduces exactly to standard Observability/Detectability of pair $\((A,C)\)$.

## VI. NUMERICAL EXAMPLES
### Example 1
\[
A=\begin{bmatrix}
1 & 0 & 0 & 0 & -6 & 0 & 1 & 0 & 2 & -2 \\
0 & -1 & 29 & 136 & -64 & -64 & -123 & -91 & 112 & * \\
1 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
2 & 1 & 0 & -2 & 3 & 2 & 0 & 1 & -2 & * \\
-3 & 1 & 0 & 1 & 0 & -1 & 0 & 0 & 0 & * \\
-1 & 0 & 1 & 3 & 0 & -1 & 1 & 1 & 0 & * \\
0 & 0 & 2 & 1 & 0 & 4 & -5 & 1 & -1 & * \\
1 & 1 & 1 & 0 & 1 & -2 & -3 & 0 & 0 & * \\
-1 & 1 & 1 & 0 & 0 & -1 & 2 & 4 & -3 & *
\end{bmatrix},
\]
$L_0=\begin{bmatrix}1 & 4 & 1 & 21 & 16 & 16 & 9 & 15 & 20 & *\end{bmatrix}$,
$C=\begin{bmatrix}I_{2\times 2} & 0_{2\times 8}\end{bmatrix}$.

System $(A,C,L_0)$ is Functional Observable.
$\beta=0 \Rightarrow L_{\beta}=L_0$, $\chi_1=1$, $\chi_2=0$.
\[
U_1^*=\begin{bmatrix}1 & 0 & 0 & -6 & 0 & 1 & 0 & 2 & -2 & *\end{bmatrix}.
\]
Minimal $L=\begin{bmatrix}L_\beta\\U_1^*\end{bmatrix}$, observer order = $2$.

### Example 2
\[
A=\begin{bmatrix}-1 & 0 & 0\\0 & -1 & 0\\0 & 0 & 2\end{bmatrix},\quad
C=\begin{bmatrix}1 & 1 & 0\end{bmatrix},\quad
L_0=\begin{bmatrix}1 & 2 & 0\end{bmatrix}.
\]
This system is not observable, not detectable, but **Functional Detectable**. $L=L_0$ satisfies Condition1 and Condition2 for $s\in\mathbb{C},\Re(s)\ge0$. A first‑order functional observer exists, but observer pole is fixed at $s=-1$, cannot be arbitrarily assigned.

## VII. CONCLUSION
This technical note introduced the concept of Functional Observability / Functional Detectability for triple $(A,C,L_0)$, which characterizes whether given linear functions of system state can be estimated via dynamical functional observer. Necessary‑and‑sufficient conditions are given. For Functional‑Observable/Detectable systems, constructive procedure for **minimum‑order linear functional observer** is developed. Standard Observability/Detectability for pair $\((A,C)\)$ is shown as special case when $L_0=I$.

## APPENDIX
> Contains proofs for Theorem1, Lemma1‑7, Theorem3‑4. (Mathematical derivations omitted for brevity in this markdown summary; see original paper for full algebraic proofs.)

## REFERENCES
[1] D. G. Luenberger, “Observers for multivariable systems,” *IEEE Trans. Autom. Control*, vol. AC‑11, no. 2, pp. 190‑197, Apr. 1966.

[2] T. E. Fortman and D. Williamson, “Design of a low order observer for linear feedback control laws,” *IEEE Trans. Autom. Control*, vol. AC‑17, no. 3, pp. 301‑308, Jun. 1972.

[3] P. Murdoch, “Observer design of a linear functional of the state vector,” *IEEE Trans. Autom. Control*, vol. AC‑18, no. 3, pp. 308‑310, Jun. 1973.

[4] P. Murdoch, “Design of degenerate observers,” *IEEE Trans. Autom. Control*, vol. AC‑19, no. 4, pp. 441‑442, Aug. 1974.

[5] J. R. Roman and T. E. Bullock, “Design of minimal‑order stable observers for linear functions of the state via realization theory,” *IEEE Trans. Autom. Control*, vol. AC‑20, no. 5, pp. 613‑622, Oct. 1975.

[6] J. B. Moore and G. F. Ledwich, “Minimal‑order observers for estimating linear functionals of a state vector,” *IEEE Trans. Autom. Control*, vol. AC‑20, no. 5, pp. 623‑632, Oct. 1975.

[7] K. Furuta and S. Kawaji, “Linear functional observer with possible minimal dimension,” *IEEE Trans. Autom. Control*, vol. AC‑22, no. 6, pp. 977‑980, Dec. 1977.

[8] H. R. Sirisena, “Minimal‑order observer for linear functions of the state vector,” *Int. J. Control*, vol. 29, pp. 235‑254, 1979.

[9] T. Kailath, *Linear Systems*. Englewood Cliffs, NJ: Prentice‑Hall, 1980.

[10] K. Furuta and T. Suzuki, “Design of functional observer in transfer function form,” in *Proc. Amer. Control Conf.*, 1999, pp. 4305‑4309.

[11] C.‑C. Tsui, “On the order reduction of linear functional observers,” *IEEE Trans. Autom. Control*, vol. AC‑31, no. 5, pp. 447‑449, May 1986.

[12] C.‑C. Tsui, “What is the minimum function observer order,” in *Proc. 3rd World Congress Intell. Control Autom.*, Hefei, China, 2000, pp. 2811‑2816.

[13] B. D. O. Anderson, N. K. Bose, and E. I. Jury, “Output feedback stabilization and related problems‑solution via decision methods,” *IEEE Trans. Autom. Control*, vol. AC‑20, no. 1, pp. 53‑65, Feb. 1975.

[14] R. D. Gupta, F. W. Fairman, and T. Hinamoto, “A direct procedure for the design of single functional observers,” *IEEE Trans. Circuits Syst.*, vol. CAS‑28, no. 4, pp. 294‑300, Apr. 1981.

[15] J. T. Watson and K. M. Grigoriadis, “Optimal unbiased filtering via linear matrix inequalities,” *Syst. Control Lett.*, vol. 35, pp. 111‑118, 1998.

[16] M. Darouach, “Existence and design of functional observers for linear systems,” *IEEE Trans. Autom. Control*, vol. 45, no. 5, pp. 940‑943, May 2000.

[17] J. O’Reilly, *Observers for Linear Systems*. New York: Academic, 1983.

> Note: Some matrix entries in Example1 original PDF are garbled / truncated; marked with $*$ in above markdown. All mathematical formulas are faithfully transcribed from source PDF.
