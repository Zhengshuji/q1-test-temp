> **更正（243/245）**：单行列式 rank-4 的最小是 **$n=7,p=2$**（不是 $n=6$）；
> $n=6,p=1$ 时 $Q$ 维 3，$(5a)$ 是 $2\times3$ 秩一（三方程）。$q=2$ 整体已被 [245](../../rank_gates/attempts/245_q2_no_gate_theorem.md) 封闭。

# $q=2$ 的 rank-4 门：$n=5$ 不可能，最小 $n=6$；但 $(5a)$ 变成 $2\times3$ 秩一

> 2026-11-09。按 73 号“刻画 $D(l)$ 的 rank/signature/边界”的单一实验：
> 证明 $n=5$、$q=2$、$u=0$ 时 $D(l)=\det[S;l;lA]$ 的秩 **≤3**，所以 $xy-zw$（rank 4）**不可能**；
> 最小 $n=6$ 时 $Q$ 维 3，$(5a)$ 变成 $2\times3$ 矩阵的**秩一**（三个二次方程），单一行列式不够。
> 状态：**M2（纸面）+ 结构分析**。

## 目标

回答 73 号的问题：$u=0$ 时 $D(l)$ 能实现的 rank/signature；$xy-zw$ 是否可实现；最小 $n$。

## 设想与理由

$S=\operatorname{row}[L_0;CA;C]$（秩 3），$Q=(\mathbb C^n)^*/S$，$u=[L_0A]$，$x=[l]$，$v=[lA]$。
$u=0$ 时 $(5a)\iff v\in\operatorname{span}\{x\}$。

## 做法

### 1. $n=5$：rank $D\le3$

设 $C,L_0$ 独立，$W=\ker C\cap\ker L_0$。由 $CA\in S$、$L_0A\in S$：
$$C\cdot\operatorname{col}_j=0,\qquad L_0\cdot\operatorname{col}_j=0\quad(j=1,2),$$
所以 $A$ 的前两列 $\operatorname{col}_1,\operatorname{col}_2\in W$。

$n=5$ 时 $\dim W=3$，且
$$W=S^\perp\oplus\langle w\rangle,\qquad S^\perp\ \text{是商坐标方向（2 维）},\ w\in S.$$
于是
$$\operatorname{col}_j\cdot l=p_j(l)+a_j\,l(w),\qquad p_j\ \text{只含 }l|_{S^\perp}\text{ 的两个坐标};$$
$$D(l)=l_1(\operatorname{col}_2\cdot l)-l_2(\operatorname{col}_1\cdot l)$$
只依赖 $l_1,l_2,l(w)$ 三个变量 ⇒
$$\boxed{\operatorname{rank}D\le3.}$$
所以 $xy-zw$（rank 4，signature $(2,2)$）在 $n=5$、$q=2$、$u=0$ 下**不可能**。

### 2. $n=6$：最小情形，但 $(5a)$ 是三个二次方程

$n=6$ 时 $S^\perp$ 维 3，$W=S^\perp\oplus\langle w\rangle$ 维 4；$D$ 可依赖 4 个变量，rank 4 **可能**。
但 $Q$ 维 3，$v\in\operatorname{span}\{x\}$ 是 $2\times3$ 矩阵的秩一条件，即**三个** $2\times2$ 子式为零：
$$x_1v_2-x_2v_1=0,\quad x_1v_3-x_3v_1=0,\quad x_2v_3-x_3v_2=0.$$
不再是单个行列式门。

### 3. 一个 $n=6$ 的候选

取 $S=\operatorname{span}\{e_4,e_5,e_6\}$、$C=e_4^*$、$L_0=e_5^*$、$CA=e_6^*$，
前两列 $\operatorname{col}_1=e_3$、$\operatorname{col}_2=e_6$，则
$$v_1=l_3,\quad v_2=l_6,\quad D_{12}=l_1l_6-l_2l_3=xy-zw$$
（rank 4、signature $(2,2)$，取 $x=l_1,y=l_6,z=l_2,w=l_3$）。
但第三个方向 $v_3$ 由 $\operatorname{col}_3$ 决定；若 $\operatorname{col}_3=0$，秩一条件会额外迫使
$l_3=0$ 或 $v=0$，门退化。需要选 $\operatorname{col}_3$ 使另外两个子式**自动满足**或与门一致；
这是下一步的构造问题。

## 进展

* 证明 $n=5$ 的 rank≤3 定理（$xy-zw$ 不可能）；
* 确定最小 $n=6$，并说明 $(5a)$ 变成 $2\times3$ 秩一（三方程）；
* 给出一个 $D_{12}=xy-zw$ 的候选，指出第三个方程的障碍。

## 最终结论

* 专家问的 rank-4/signature-(2,2) 门**不能**在 $n=5$、$q=2$ 的单行列式设定中实现；
* 最小 $n=6$，但目标应改为“$2\times3$ 秩一条件中的一个子式是门，另两个自动/一致”；
* 这不是单纯的 rank-4 二次型问题，而是**三方程联立**问题。

## 放弃原因

* 未构造 $n=6$ 的完整门（第三方程未处理）；
* 未证 signature/边界；
* 未接 $(5b)$。

## 残留价值

* 一个干净的不可能性（$n=5$ rank≤3）；
* 最小 $n=6$ 的结论；
* 明确的下一步：$2\times3$ 秩一的第三方程。

## 相关文件

* [attempts/240](../../rank_gates/attempts/240_full_5a_q2_structure.md)
* [73 答复](../../../for_expert/archive/73_inventory_and_route-answer.md)
* [241](241_73_verdict.md)

## 状态

* $n=5$ 不可能：**[M2 纸面]**。
* $n=6$ 门：**[未完成]**。
