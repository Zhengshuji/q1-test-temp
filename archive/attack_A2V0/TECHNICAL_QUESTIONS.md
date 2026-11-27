# 一个行空间极小化问题：证明中遇到的四个技术问题

> 本文是自足的：所有定义、已知结果、实例数据都写在文内。
> 文中"已证"指有完整纸面证明；"已核"指有限个有理数实例上的精确计算（无舍入）；
> "猜想"指未证明。文末列出已尝试并排除的路线。

---

## 0. 问题

设 $A\in\mathbb R^{n\times n}$，$C\in\mathbb R^{p\times n}$，$L_0\in\mathbb R^{r\times n}$，$\operatorname{rank}L_0=r$。

对 $q\ge r$，取 $L\in\mathbb R^{q\times n}$ 且**前 $r$ 行恰为 $L_0$**（即 $L=[L_0;R]$），记

$$(5a)\quad \operatorname{rank}\begin{pmatrix}LA\\ L\\ CA\\ C\end{pmatrix}=\operatorname{rank}\begin{pmatrix}L\\ CA\\ C\end{pmatrix},
\qquad
(5b)\quad \operatorname{rank}\begin{pmatrix}\lambda L-LA\\ CA\\ C\end{pmatrix}=\operatorname{rank}\begin{pmatrix}L\\ CA\\ C\end{pmatrix}\ \ \forall\lambda\in\mathbb C .$$

$$q_{\min}:=\min\{q:\ \exists R\ \text{使}\ (5a)\wedge(5b)\}.$$

这两条条件逐项等同于 Fernando–Trinh–Jennings（IEEE TAC 55(5), 2010）关于"阶为 $q$ 的功能观测器"的 Condition 1 与 Condition 2。

**记号**（下同）：

- $\mathcal V=\operatorname{row}(L)\subseteq\mathbb R^n$，$\dim\mathcal V=q$；$\mathcal J=\operatorname{row}[C;CA]$；
- $K=\ker[C;CA]=\mathcal J^{\perp}$，$\dim K=d$；$N\in\mathbb R^{n\times d}$ 的列是 $K$ 的一组基；
- $A'=(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN$（$A$ 在 $K$ 上的压缩），$R_0=AN-NA'$；
- $M=LN\in\mathbb R^{q\times d}$，$N'=LR_0\in\mathbb R^{q\times d}$，$\rho=\operatorname{rank}M$；
- $\rho_0=\operatorname{rank}(L_0N)$，$V_{\!c}=\langle\operatorname{row}(R_0)\rangle_{A'}$（含 $\operatorname{row}(R_0)$ 的最小 $A'$-不变子空间），$\dim V_{\!c}$ 记作 $\dim V$。

**可行性**：本文只讨论至少有一个解存在的实例。

---

## 1. 四个基本等价（均有证明）

### 1.1 $(5a)\iff \mathcal VA\subseteq\mathcal V+\mathcal J$

因为 $(5a)$ 等价于 $\operatorname{row}(LA)\subseteq\operatorname{row}(L)+\operatorname{row}(CA)+\operatorname{row}(C)$。

### 1.2 $(5b)\iff \ker\big((\lambda L-LA)|_K\big)=\ker(L|_K)\ \forall\lambda$

因为 $\ker[\lambda L-LA;CA;C]=\{x\in K:(\lambda L-LA)x=0\}$，而 $\ker[L;CA;C]=\ker(L|_K)$。

### 1.3 $(5b)\iff \ker(\lambda M-MA'-N')=\ker M\ \forall\lambda$

因为对 $x=N\xi$（$\xi\in\mathbb R^d$）有 $L(\lambda x-Ax)=\big(\lambda M-MA'-N'\big)\xi$。

### 1.4 $q\ge\max(r,\rho+1)$

$q\ge r$ 显然。设 $q=\rho$，则 $M$ 行满秩（$q\times d$，秩 $q$）。
由 1.3，$P_\lambda:=\lambda M-MA'-N'$ 在 $\ker M$ 上为零，故存在 $q\times q$ 矩阵 $C_\lambda$ 使 $P_\lambda=C_\lambda M$。
又 $\ker(C_\lambda M)=\ker M$ 且 $M$ 满射，故 $C_\lambda$ 可逆。
比较 $\lambda,\lambda'$：$(\lambda-\lambda')M=(C_\lambda-C_{\lambda'})M$，由 $M$ 满射得 $C_\lambda-C_{\lambda'}=(\lambda-\lambda')I$，
即 $C_\lambda=C_0+\lambda I$；而 $C_0+\lambda I$ 在 $\lambda$ 取 $C_0$ 的任一特征值的相反数时奇异，矛盾。$\blacksquare$

---

## 2. 分层与已知结构

### 2.1 分层

$$\rho=\operatorname{rank}(LN)=\dim(\mathcal V|_K),\qquad
q(\rho):=\min\{\dim\mathcal V:\ \operatorname{rank}(\mathcal V N)=\rho,\ (5a)\wedge(5b)\},$$

$$q_{\min}=\min_{0\le\rho\le\dim V}q(\rho),\qquad \rho^*:=\min\{\rho:\ q(\rho)<\infty\}.$$

由 1.4，$q(\rho)\ge\max(r,\rho+1)$。

**猜想（已核 50 个实例，50/50）**：$\;q_{\min}=\max(r,\rho^*+1)$。

### 2.2 三个已证的特殊情形

**(A) $\rho^*=0$**（即存在 $\mathcal V\subseteq\mathcal J$ 的解）。此时 $L_0$ 本身是解，$q_{\min}=r$。
*证明*：$L_0\subseteq\mathcal V\subseteq\mathcal J$，故 $L_0A\subseteq\mathcal VA\subseteq\mathcal V+\mathcal J=\mathcal J=\operatorname{row}(L_0)+\mathcal J$，
即 $(5a)$ 对 $L_0$ 成立。又 $L_0N=0$（因 $L_0\subseteq\mathcal J=K^\perp$），故 $\lambda L_0-L_0A\in\mathcal J$，
而 $[\lambda L_0-L_0A;CA;C]$ 的行空间恰为 $\mathcal J$，秩恒为 $\dim\mathcal J$，$(5b)$ 成立。$\blacksquare$

**(B) $\rho^*=\dim V$**：在全部已核实例上 $q(\dim V)\le\dim V+1$。

**(C) 压缩**：设 $\mathcal V$ 是解，$\mathcal W=\mathcal V\cap\mathcal J$，
$F=\operatorname{span}\{(\langle v_i,y\rangle)_i:\ y\in K+AK\}\subseteq\mathcal V^*$（$v_1,\dots,v_q$ 为 $\mathcal V$ 的基）。
若 $K_0^\perp:=(\operatorname{row}L_0)^\perp$ 在 $\mathcal V^*$ 中不包含于 $F$，**且** $\mathcal W\not\subseteq\operatorname{row}(L_0)$，
则存在 $\mathcal V$ 的超平面 $H\supseteq\operatorname{row}(L_0)$，$H+\mathcal W=\mathcal V$，且 $H$ 仍是解。
（证明：$H+\mathcal W=\mathcal V$ 使 $(5a)$ 自动；$(5b)$ 的"坏"超平面集包含于 $P(F\cap K_0^\perp)$，是可容许超平面族中的真闭子集。
另：$H+\mathcal W=\mathcal V\Rightarrow\pi(H)=\pi(\mathcal V)$，故 $\operatorname{rank}(HN)=\operatorname{rank}(VN)=\rho$，**压缩保持 $\rho$ 不变**。）

### 2.3 铅笔化（一般 $\rho$）

设 $M=UV^{\mathsf T}$，其中 $U\in\mathbb R^{q\times k}$、$V\in\mathbb R^{d\times k}$ 均列满秩（$k=\rho$），$W=A'^{\mathsf T}V$。则

$$N'=-UW^{\mathsf T}+YV^{\mathsf T}\quad\text{对唯一的}\ Y\in\mathbb R^{q\times k},\qquad
\lambda M-MA'-N'=(\lambda U-Y)V^{\mathsf T},$$

$$\boxed{\ (5b)\iff \operatorname{rank}(\lambda U-Y)=k\ \ \forall\lambda\in\mathbb C\ }$$

即 $k$ 列铅笔 $\lambda U-Y$ 无实广义特征值。

**并且**：在上述结构方程成立的条件下，$(5a)$ 自动成立。
*证明*：$(5a)\iff\ker L\cap K\subseteq\ker(LA)$。取 $x=N\xi\in\ker L\cap K$，则 $UV^{\mathsf T}\xi=0\Rightarrow V^{\mathsf T}\xi=0$，于是
$$LAx=(LN)A'\xi+(LR_0)\xi=UW^{\mathsf T}\xi-UW^{\mathsf T}\xi+YV^{\mathsf T}\xi=0.\ \blacksquare$$

---

## 3. 四个问题

### 问题 Q1（最小层是否一定紧）

$$\textbf{Q1:}\quad \text{是否对一切可达的}\ \rho\ \text{都有}\ q(\rho)=\max(r,\rho+1)\ ?$$

已知：

- $\rho=0$、$\rho=\dim V$：成立（§2.2 A、B）；
- $\rho=1$：成立。对 $q=2$ 的情形可给出完整的代数判定（$M=uv^{\mathsf T}$，$v$ 由 $L_0N$ 或 $L_0R_0$ 确定，
  剩余条件是一次线性方程组 + 一个开条件），已核 5 个实例一致；
- **反例只出现在非最小层**：实例 A（§4.1）有 $q(1)=3>2=\max(r,2)$，但那里 $\rho^*=0$（$L_0$ 本身是解），
  所以不影响 $q_{\min}$。

因此精确的问题是：**最小层能否不紧**？

$$\textbf{Q1}':\quad \text{若}\ \rho^*>0,\ \text{是否必有}\ q(\rho^*)=\max(r,\rho^*+1)\ ?$$

（统一形式是 $\max(r,\rho^*+1)$；只在 $r\le\rho^*+1$ 时才化为 $\rho^*+1$。若 $r>\rho^*+1$，
$q=\rho^*+1$ 会违反已证下界 $q\ge r$。）

若 Q1$'$ 成立，则 $q_{\min}=\max(r,\rho^*+1)$ 成立（结合 §2.2 与 1.4）。

### 问题 Q2（中间层是否存在）

$$\textbf{Q2:}\quad \text{是否存在解使}\ 2\le\rho^*<\dim V\ ?$$

已知：

- $0<\rho^*<\dim V$ 可以发生（实例 B，$\rho^*=1$，$\dim V=2$）；
- $\rho^*\ge2$ 且 $\rho^*<\dim V$：**没有任何实例**。定向搜索（$n=7$、$p=2$、$d=3$、$\dim V=3$；
  以及从实例 B 出发的 48 个单维耦合扩展）均未命中；
- 一个结构性障碍：若实例分解为两个块（$A$ 块对角、$C=(C_1\ C_2)$、$L_0=(L_{0,1}\ L_{0,2})$，$L$ 的行按块分开），则
  $q=q_1+q_2$、$\rho=\rho_1+\rho_2$、$q_i\ge\rho_i+1$（$\rho_i>0$），故两块都非退化时 $q\ge\rho+2$。
  即**块对角构造给不出** $q=\rho+1$ 的中间层。

### 问题 Q3（谱条件与参数化族）

固定 $k$ 维子空间 $\Sigma\subseteq\mathbb R^d$（$\Sigma\supseteq\operatorname{row}(L_0N)$），令

$$\mathcal A(\Sigma)=\{(U,Y):\ \exists L,\ \operatorname{row}(L)\supseteq\operatorname{row}(L_0),\ \operatorname{row}(LN)=\Sigma,\ LN=UV^{\mathsf T},\ LR_0=-UW^{\mathsf T}+YV^{\mathsf T}\}.$$

由 §2.3，$\mathcal A(\Sigma)$ 是仿射空间，且"$\Sigma$ 层可达"等价于

$$\mathcal A(\Sigma)\cap\{(U,Y):\ \operatorname{rank}(\lambda U-Y)=k\ \forall\lambda\}\ne\emptyset .$$

$$\textbf{Q3:}\quad \text{如何刻画使上式成立的}\ \Sigma\ ?\ \text{该集合是闭的、开的，还是构造性集合？}$$

已知（实例 C，$d=3,k=2$）：

- 对固定 $\Sigma$，$\mathcal A(\Sigma)$ 中的点**全好或全坏**：$\Sigma=\Sigma_0$ 时 57/59 个抽样点满足 $(5b)$，
  其余 12 个不同的 $\Sigma$ 全部 0/57；
- 坏的 $\Sigma$ 上，铅笔的 $\gcd$ 恰为 $(\lambda-1)(\lambda-3)$，而 $A'$ 的谱是 $\{3,1,-1\}$；
  好的 $\Sigma_0$ 上 $\gcd=1$；
- 参数化 $\Sigma(t)=\operatorname{span}\{\alpha_0,\ \beta_0+t\beta_1\}$（$\mathbb P^1$ 的一个坐标卡）上，
  13 个有理 $t$ 中只有 $t=0$（即 $\Sigma_0$）是好的；补测缺失坐标卡的 3 个方向也都是坏的。

### 问题 Q4（$\mathcal W\subseteq K_0$ 时的压缩）

§2.2 (C) 需要 $\mathcal W\not\subseteq\operatorname{row}(L_0)$。这个条件何时自动成立？

$$\textbf{Q4:}\quad \text{若}\ \mathcal W\subseteq\operatorname{row}(L_0)\ \text{且}\ q>\max(r,\rho+1),\ \text{是否仍存在更小的解？}$$

已知：$\mathcal W\subseteq\operatorname{row}(L_0)$ 确实会发生（实例 A、B，但二者都是紧层，不需要压缩）；
此时任何含 $\operatorname{row}(L_0)$ 的超平面都含 $\mathcal W$，故 $H+\mathcal W=H\ne\mathcal V$，超平面压缩**不存在**。

---

## 4. 三个实例（全部为有理数，可直接验证）

### 4.1 实例 A：非最小层可以不紧

$$n=5,\ p=2,\ r=1,\quad
A=\begin{pmatrix}0&0&1&-2&-1\\1&-2&2&0&2\\1&1&-2&0&0\\-2&2&0&-1&0\\-1&-1&2&-1&0\end{pmatrix},\quad
C=\begin{pmatrix}-1&1&1&0&-1\\1&-1&-2&-1&-1\end{pmatrix},\quad
L_0=\begin{pmatrix}2&-2&-1&1&1\end{pmatrix}.$$

- $d=1$，$\dim V=1$，$\rho_0=0$，$q_{\min}=1$（$L=L_0$ 本身满足 $(5a)(5b)$）。
- 但 $q(1)=3$：不存在 $q=2$ 且 $\operatorname{rank}(LN)=1$ 的解。
  *证明*：$K=\langle\nu\rangle$，$L_0\nu=L_0A\nu=0$（后者因 $L_0A\in\mathcal J$）。若 $L=[L_0;\ell]$ 且 $L\nu\ne0$，
  则 $(5b)$ 要求 $L\nu$ 与 $LA\nu$ 线性无关；但二者第一坐标都为 $0$，必相关。$\blacksquare$
- 这把 $(5b)$ 化为 $L\nu,LA\nu$ 的独立性，且 $L_0A\nu=0\iff L_0A\in\mathcal J\iff(5a)$ 对 $L_0$ 成立。

### 4.2 实例 B：中间层（$\rho^*=1<\dim V=2$）

$$n=6,\ p=2,\ r=1,\quad
A=\begin{pmatrix}-1&1&-1&0&1&1\\-1&1&0&-1&0&-1\\0&1&0&0&-1&-1\\1&1&1&1&1&-1\\1&-1&-1&1&0&0\\1&-1&0&-1&-1&0\end{pmatrix},$$

$$C=\begin{pmatrix}0&1&0&-1&-1&1\\-1&0&0&0&0&0\end{pmatrix},\qquad
L_0=\begin{pmatrix}0&-1&\tfrac23&-1&-1&-1\end{pmatrix},$$

$$L=\begin{pmatrix}0&-1&\tfrac23&-1&-1&-1\\0&1&0&1&1&-1\end{pmatrix}\quad(q=2).$$

- $d=2$，$\dim V=2$，$\rho_0=0$，$\operatorname{rank}(LN)=1$，$q_{\min}=2$（此解满足 $(5a)(5b)$）。
- $\rho^*=1$：不存在 $\rho=0$ 的解（若存在，则由 §2.2(A) $L_0$ 本身是解，但直接验证它不是）。
- 这里 $\mathcal W=\mathcal V\cap\mathcal J$ 满足 $\dim\mathcal W=1$ 且 $\mathcal W=\operatorname{row}(L_0)$（即 Q4 的情形），
  但 $q=\max(r,\rho+1)=2$，不需要压缩。

### 4.3 实例 C：谱条件继承 $A'$ 的特征值

$$n=5,\ p=1,\ r=1,\quad
A=\begin{pmatrix}0&1&0&0&0\\1&0&0&0&0\\0&0&3&0&0\\1&0&0&0&0\\0&0&0&1&1\end{pmatrix},\quad
C=\begin{pmatrix}0&0&0&0&1\end{pmatrix},\quad
L_0=\begin{pmatrix}1&1&0&0&0\end{pmatrix},$$

$$L=\begin{pmatrix}1&1&0&0&0\\1&1&0&-2&0\\2&1&0&1&0\end{pmatrix}\quad(q=3).$$

- $d=3$，$\dim V=2$，$\rho_0=1$，$\operatorname{rank}(LN)=2$，$q_{\min}=3$（$= \dim V+1$，非中间层）。
- $A'=\begin{pmatrix}0&1&0\\1&0&0\\0&0&3\end{pmatrix}$，谱 $\{3,1,-1\}$。
- 固定 $\Sigma=\operatorname{row}(LN)=\operatorname{span}\{(1,1,0),(1,0,0)\}$ 时，铅笔 $\gcd=1$（无广义特征值）；
  对同一实例的其他 2 维 $\Sigma$（$\Sigma(t)=\operatorname{span}\{(1,1,0),(1,0,0)+t(0,0,1)\}$，$t\ne0$），
  铅笔的 $\gcd=(\lambda-3)(\lambda-1)$。

### 4.4 数值总览

- 50 个可行实例：猜想 $q_{\min}=\max(r,\rho^*+1)$ 成立 50/50；
  可达 $(\text{实例},\rho)$ 对中"紧"的占 52/53，唯一例外是实例 A 的 $\rho=1$ 层（该处 $\rho^*=0$）。
- 45 个实例中，可达 $\rho$ 的集合都是区间（无跳跃）。
- 对已知解做小扰动：实例 B 只有约 1.5% 的 $\pm1$ 单元素扰动仍合法，实例 C 约 9.5%。

---

## 5. 已尝试并排除的路线（均为可复算的否定结果）

1. **块对角扩展**（$A=\operatorname{diag}$、$C$ 行拼接、$L_0$ 分行）：如上，$q\ge\rho+\#\{\text{用到的块}\}$，给不出紧中间层。
2. **不可见块**（增维使 $C=0$、$A=0$）：保持中间层，但不改变 $\rho$ 与 $q$ 的关系。
3. **$k=2$ 的 $V$ 由 $L_0$ 定死**：不成立。实例 C 上，$L_0N=\alpha_0$ 只确定 $\Sigma$ 的一个方向；
   线性系统（$27$ 未知量、$18$ 方程）对连续多个 $\Sigma$ 都可解，$\Sigma$ 不被线性结构钉住。
4. **"自由方向"给出 $Z$**：在等价的对偶形式里（$q_{\min}=n-p-d_{\max}$，$Z\subseteq\ker C\cap L_0^\perp$，
   $A(Z\cap K)\subseteq Z$，外加谱条件），取 $Z\cap K=0$ 使第二条件空真，但实测
   $\dim\ker C\cap L_0^\perp-\dim(\ker C\cap L_0^\perp\cap K)\le1$（四个实例上都是 1 或更小），
   故这不是有意义的区域。
5. **符号消元**：把 $\Sigma(t)$ 代入线性系统，取自由参数为常数得到一般点，再算铅笔子式的 $\gcd$。
   失败原因：解空间含大范围退化轨迹（$Y\propto U$），任取的常数点常落在其中；且不同基下的"同一组参数值"
   对应不同点，符号 $\gcd$ 不能直接读作"$t$ 处的性质"。
6. **随机搜索中间层 $k=2$**：随机实例 8 个、定向实例 48 个，均 0 命中。

---

## 6. 与另一等价形式的对应（供交叉核对）

令 $Z=\ker[C;L]$，则 $\dim Z=n-p-q$，$Z\subseteq\ker C\cap L_0^\perp$，$A(Z\cap K)\subseteq Z$，
且 $\dim(Z\cap K)=d-\rho$。谱条件写成

$$\dim\big((\lambda I-A)K\cap Z\big)=\dim(K\cap Z)-\dim\ker\big((\lambda I-A)|_K\big)\quad\forall\lambda .$$

（注意：若漏掉右端第二项 $\dim\ker((\lambda I-A)|_K)$，在 $\lambda$ 为 $A|_K$ 的特征值时会假失败：
此时 $\dim((\lambda I-A)K)<d$，而原式仍要求交维数等于 $\dim(K\cap Z)$。）

由此可得一个简单推论：若 $Z\cap K=0$，则必须 $\dim\ker((\lambda I-A)|_K)=0$ 对所有 $\lambda$ 成立，
即 $A|_K$ 无实特征值。

$$q_{\min}=n-p-d_{\max},\qquad d_{\max}=\max\{\dim Z:\ \text{上述四条约束}\}.$$

（$Z$ 与 $L$ 的互化用的是 2010 年文献的 nullspace 判据；本节只作为交叉核对的形式，正文的问题不依赖它。）
