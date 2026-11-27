# 算术侧：$(5a)$ 归约到 $P$，以及 $\rho_{ci}=P(T,B,U_0)$ 的证明

> 对应 [docs/02](../../../../../docs/02_theorems_proven.md) 的 E.1 / E.2，以及 [docs/04](../../../../../docs/04_structure.md) 的引理 4.2.1。本文是**展开版**。

## 1. 设定

$\mathcal J=\operatorname{row}[C;CA]$、$j=\dim\mathcal J$、$d=n-j$、$\pi:\mathbb C^n\twoheadrightarrow X:=\mathbb C^n/\mathcal J$。

记
$$B:=\pi(\mathcal J A)\subseteq X,\qquad U_0:=\pi(S)\subseteq X ,$$
并定义 $T:X\to X/B$ 为
$$T(\pi(x)):=\pi(Ax)\ \bmod B .$$

**引理 1.1** $T$ 良定义。

*证明*：若 $\pi(x)=\pi(x')$，则 $x-x'\in\mathcal J$，故 $A(x-x')\in\mathcal J A$，于是 $\pi(A(x-x'))\in\pi(\mathcal J A)=B$。故两个代表元给出同一个 $X/B$ 中的元素。$\square$

> **约定**：$T$ 是"到商空间 $X/B$ 的映射"。本项目的 $P$ 递归（[theorem.md](theorem.md)）正是对 $\Phi:Y\to Y/C$ 这种型定义的，故两者完全匹配。

## 2. 引理：$(5a)\iff T(U)\subseteq U+B$

**引理 2.1** 对任意子空间 $\mathcal V\subseteq\mathbb C^n$，令 $U=\pi(\mathcal V)$。则
$$(5a)\iff T(U)\subseteq U+B .$$

*证明*：
$(5a)$ $\iff$ $\operatorname{row}(\mathcal LA)\subseteq\operatorname{row}\mathcal L+\mathcal J=\mathcal V+\mathcal J$（[proof/lower_bound/theorem.md](../../../../../proof/lower_bound/theorem.md) 引理 1.1）
$\iff$ 对每个 $\ell\in\mathcal V$：$\pi(\ell A)\in\pi(\mathcal V)=U$
$\iff$ 对每个 $u=\pi(\ell)\in U$：$T(u)=\pi(\ell A)\bmod B\in(U+B)/B$
$\iff T(U)\subseteq U+B$。$\square$

（最后一行的等价：$\pi(\ell A)\in U$ $\iff$ $\pi(\ell A)$ 在 $(U+B)/B$ 里的类为零，而该结正是 $T(u)$。）

## 3. 主定理（E.1）

**定理 3.1**
$$\rho_{ci}:=\min_{\mathcal V\ \text{满足}\ (5a)}\dim\pi(\mathcal V)\;=\;P(T,B,U_0),$$
其中
$$P(T,B,U_0)=\min\{\dim U:\ U\supseteq U_0,\ T(U)\subseteq U+B\}\subseteq X .$$

*证明*：
**($\le$)** 取任一 $(5a)$-可行的 $\mathcal V$，令 $U=\pi(\mathcal V)$。由引理 2.1，$T(U)\subseteq U+B$；又 $S\subseteq\mathcal V$ 给出 $U_0=\pi(S)\subseteq\pi(\mathcal V)=U$。而 $\rho(\mathcal V)=\dim\pi(\mathcal V)=\dim U$。故 $\rho_{ci}\ge P$。

**($\ge$)** 取任一 $U\supseteq U_0$ 且 $T(U)\subseteq U+B$，令 $\mathcal V:=\pi^{-1}(U)\subseteq\mathbb C^n$。则
- $\pi(\mathcal V)=U$（$\pi$ 满射），故 $\dim\pi(\mathcal V)=\dim U$；
- $S\subseteq\mathcal V$（因 $U_0=\pi(S)\subseteq U$ 且 $S\subseteq\pi^{-1}(\pi(S))$）；
- 由引理 2.1，$(5a)$ 成立。
故 $\rho_{ci}\le\dim U$，对 $U$ 取下确界得 $\rho_{ci}\le P$。

两向合并即得。$\square$

**推论 3.2（E.2）** $\rho_{ci}$ 可在 $O(n^4)$ 内算出：由 [theorem.md](theorem.md) 的递归定理 + $O(n^4)$ 算法（[algorithm.md](algorithm.md)）。

## 4. 与 $q_{\min}$ 的关系

$$\rho_{ci}\ \text{只是}\ (5a)\ \text{一侧的最小}\ \rho;\qquad\text{真实}\ \rho^*\ge\rho_{ci},$$

且 $q_{\min}=\min\{(\rho,c):(\rho,c)\ \text{可达}\}$（[docs/04](../../../../../docs/04_structure.md)）。所以

$$\boxed{\ \text{算术侧已闭合：}\rho\ \text{这一侧的困难被完全消除；剩下的只有}\ (5b)\ \text{决定的}\ c\ \text{与可达性。}}$$

实测的 gap $\rho^*-\rho_{ci}$ 分布见 [archive/attempts_2026-10/q1_false/08_floor_gap.md](../../../../../archive/attempts_2026-10/q1_false/08_floor_gap.md)（**地板通常不紧**，故不能只用 $\rho_{ci}$）。

## 5. 复核

| 项 | 脚本 | 结果 |
|---|---|---|
| $P$ 的值 vs 穷举 | `python tools/p_algorithm/c195_P_q.py` | 29/29 |
| 值 + 见证 | `python tools/p_algorithm/c197_P_witness.py --n 5` | 12/12 |
| $\rho^*$ vs $\rho_{ci}$ | `python tools/layer_search/c199_floor_gap.py` | gap 分布 $\{0{:}7,1{:}8,2{:}1\}$ |
