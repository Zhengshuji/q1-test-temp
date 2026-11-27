# 乘法 gadget 的验证与 pair-space 更正（专家 63 号）

> 2026-11-09。专家 63 号给出一个 $2\times2$ 乘法 gadget，并更正 197 的“$H$ 的行自由”：
> $H$ 与 $H_A$ 由同一个提升 $l$ 耦合，可行对空间是 $\mathcal P_{A,C}=\operatorname{im}\Theta$。
> 本文件验证 gadget 并记录更正。状态：**精确验证 1/1**。

## 目标

1. 验证专家给的 $2\times2$ gadget：不变性方程 $\iff z=xy$；
2. 记录 pair-space 更正。

## 设想与理由

专家取
$$A_{11}=A_{22}=\begin{bmatrix}0&0\\0&1\end{bmatrix},\quad
A_{12}=-\begin{bmatrix}0&1\\0&0\end{bmatrix},\quad A_{21}=0,\quad
X=\begin{bmatrix}x&z\\w&y\end{bmatrix}.$$
不变性方程
$$A_{21}+A_{22}X-XA_{11}-XA_{12}X=0.$$

## 做法：验证

sympy 展开：
$$A_{22}X-XA_{11}-XA_{12}X
=\begin{bmatrix}wx&xy-z\\w(w+1)&wy\end{bmatrix}.$$
（已用 `sympy.simplify` 验证。）

于是不变性等价于
$$wx=0,\qquad z=xy,\qquad w(w+1)=0,\qquad wy=0.$$
- **正向**：任何解都满足 $z=xy$（第二条）；
- **反向**：给定任意 $x,y$，取 $w=0$、$z=xy$，四条全满足。

所以
$$\boxed{\exists w:\ F_A(X)=0\iff z=xy.}$$

## pair-space 更正（197 的修正）

197 说“$H$ 的底部行在 $\operatorname{Ann}(V)$ 内自由”——**过强**。实际上每行是
$$(h_i,h_{A,i})=(l_iN,\ l_iAN)=\Theta(l_i),$$
两个分量由**同一个** $l_i$ 耦合。可行的对空间是固定线性子空间
$$\mathcal P_{A,C}=\operatorname{im}\Theta\subseteq K_0^*\oplus K_0^*.$$
对候选 $V$，可容许行对属于
$$\mathcal P_{A,C}\cap\bigl(\operatorname{Ann}(V)\oplus\operatorname{Ann}(V)\bigr).$$
等价地，行 $l$ 属于
$$\mathcal L_V=\{l:\ lN|_V=0,\ lAN|_V=0\}.$$
所以 197 的“自由”只在**忽略 $H_A$** 时成立；加上 $(5a)$ 后是 pair-space 约束。

## 对硬度路线的意义

- 乘法 gadget 在**不变子空间层**成立（$z=xy$），这是正向进展；
- 但要变成观测器归约，还需：
  1. 强制可行 $V$ 满足不变性方程（$H_A|_V=0$ 不要求 $A(V)\subseteq V$）；
  2. 实现行对（$\mathcal P_{A,C}$）与铅笔条件（$B_*$ 在特征空间单射）；
  3. 同时提升（$d'_C$）。
- 专家建议的顺序：Task A pair-lift 定理 → Task B gadget 实现 → Task C 谱/提升 → Task D 组合。

## 进展

* gadget 精确验证：$z=xy$；
* pair-space 更正写入；
* 硬度路线细化为四任务。

## 最终结论

* 乘法 gadget 是**几何层**的真结果；
* 197 的“行自由”已更正为 pair-space 约束；
* 下一步是 pair-lift 定理与 gadget 的观测器实现。

## 放弃原因

* 未把 gadget 嵌入完整观测器（$A,C,L_0$、提升、谱）；
* 未证明“可行 $V$ 必为不变”；
* 未 Lean 化。

## 残留价值

* 一个可复现的乘法 gadget；
* pair-space 的正确表述。

## 相关文件

* [attempts/197](../../arm_reduction/attempts/197_ARM3_expressiveness_limit.md)（被更正）
* [attempts/198](../../arm_reduction/attempts/198_V_chart_expressiveness.md)、[199](../../arm_reduction/attempts/199_incidence_linearization.md)
* [attempts/196](../../arm_reduction/attempts/196_ARM3_reduction_plan.md)（计划）

## 状态

* gadget 验证：**[精确验证 1/1]**。
* 观测器实现：**[未做]**。
