# $c=1$、$q=4$、$\omega=3$ 的结构性不可行引理（非特征线情形）

> 2026-11-08。把 seeds 16/21 在 $q=4,\omega=3$ 的 `none` 升级为**结构性引理**：
> 对 $V=L\subseteq W_L$，若 $A v\notin\operatorname{span}(v)$（非特征线），则 $\operatorname{rank}H\le2<3$，
> 不可行；特征线情形是**有限个** $L$，需单独检查（未完成）。状态：**M2（部分）**。

## 目标

证明：若 $W_L\subseteq D=K_0\cap A^{-1}K_0$，则对任意非特征线 $L=\mathbb Cv\subseteq W_L$，
$c=1$、$q=4$、$\omega=3$ 的层不可行。

## 设想与理由

关键观察：$v\in W_L$ 给
$$L_0Nv=0,\qquad L_0ANv=0,$$
而 $v\in D$ 给 $Av\in K_0$，写 $Av=Nw$（$w\in K_0$ 的坐标）。则
- 顶部 $A$-系数 $A_0\cdot v=L_0ANv=0$；
- 修正系数 $G_j\cdot v=RD_j\cdot(Av)=RD_j\cdot(Nw)=0$（$RD_j\in\operatorname{row}[C;CA]$ 零化 $K_0$）。

## 做法

固定 $L=\mathbb Cv$，$\operatorname{Ann}(L)=\{h:h\cdot v=0\}$（3 维），$h_0=L_0N\in\operatorname{Ann}(L)$。
底部行 $h_i=a_ih_0+\sum_{j=1}^2 b_{ij}u_j$；可容许 $H_{A,i}\cdot v=0$ 变成
$$(l_iAN)\cdot v=l_i\cdot(Av)=l_i\cdot(Nw)=(l_iN)\cdot w=h_i\cdot w=0$$
（$a_i$ 项乘 $A_0\cdot v=0$、$g_i$ 项乘 $G\cdot v=0$ 都消失）。所以每个底部行满足
$$h_i\cdot w=0.$$
若 $w\notin\operatorname{span}(v)$，则 $\{h\in\operatorname{Ann}(L):h\cdot w=0\}$ 是 $\operatorname{Ann}(L)$ 的**真超平面**，2 维。
$h_0$ 也在其中（$h_0\cdot w=L_0Nw=L_0ANv=0$），所以 $H$ 的全部 4 行都落在这个 2 维空间里：
$$\operatorname{rank}H\le2<3=\omega,$$
与 $\operatorname{rank}H=\omega$ 矛盾。$\square$

## 对 seeds 16/21 的验证

- $W_L\subseteq D$：对 $W_L$ 的基向量 $w_0,w_1$ 验证 $Aw_i\in K_0$（精确有理）——两者都成立；
- 特征线：在 $W_L$ 的 $(-3..3)^2$ 整数组合中，$\operatorname{rank}[v,Av]=1$ 的组合数为 **0**（两个 seed 都是）；
- 因此对**非特征线**的所有 $V$（在采样网格内）引理适用，$q=4,\omega=3$ 不可行。

## 残留：特征线

严格证明需要对**所有** $v\in W_L$（包括复特征线）验证。特征线由齐次二次方程
$$\det[v,Av]=0\quad(v=a w_0+b w_1)$$
给出，至多 2 条（复）特征线。它们需要单独检查：
- 在特征线上，超平面条件平凡，$\operatorname{rank}H=3$ 可能；
- 需检验铅笔好性（子式 gcd）。

**未完成**：特征线的显式计算见 [183](183_c1_eigenlines.md)（21 两条有理线、16 两条复共轭线）；逐线精确检验仍待做。

## 进展

* 非特征线情形的结构性不可行引理已证；
* $W_L\subseteq D$ 与“网格内无特征线”已精确验证；
* 特征线（≤2 条）待查。

## 最终结论

* 对 16/21，$q=4,\omega=3$ 的**非特征线** $V$ 都不可行（引理）；
* 特征线情形是有限（≤2）的剩余检查；
* 这是 `none` → 证明的一个实质性步骤，但**尚未完全闭合**。

## 放弃原因

* 复特征线的显式计算未做；
* 未把引理写成对所有 $W_L$（不必 $\subseteq D$）的一般形式；
* 未 Lean 化。

## 残留价值

* 一个清晰的“超平面维数”不可行机制，可复用到其他 $c=1$ 层；
* $W_L\subseteq D$ 的判定与特征线计数可算法化。

## 相关文件

* [attempts/179](../../decision_algorithms/attempts/179_c2_scope.md)（范围）
* [attempts/180](180_uniform_stratum_solver.md)（工具）
* [attempts/181](181_solver_complexity_status.md)（复杂性定位）

## 状态

* 非特征线引理：**[已证-纸面，M2]**。
* 特征线剩余检查：**[未做]**。
