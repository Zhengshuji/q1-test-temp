# 表达力引理的第一个限制：$H$ 的约束是“行空间型”，不是任意仿射型

> 2026-11-09。196 的最小 gadget 实验：观测器对压缩矩阵 $H$ 的约束是什么形状？
> 结论：$(5a)$ 只给“行空间 $\subseteq\operatorname{Ann}(V)$”型的**子空间**约束，加上固定顶行与铅笔条件；
> 它**不**直接给出 ARM 所需的任意仿射方程 $\langle A_i,X\rangle=b_i$。状态：**M2（结构性观察）**。

## 目标

判断观测器数据能否把任意仿射约束编码到压缩矩阵 $H$ 上（196 的表达力引理第一步）。

## 设想与理由

$H=LN$，$L$ 的行任意；$N$ 列满秩，故 $lN$ 可取 $K_0^*$ 中任意向量。于是**底部行 $h_i$ 在 $\mathbb C^k$ 中自由**，
除非被 $(5a)/(5b)$ 约束。$(5a)$ 的压缩形式是
$$\ker H\subseteq\ker H_A\iff \operatorname{row}H\subseteq\operatorname{Ann}(V),\qquad V=\ker H.$$
所以 $H$ 的约束是“所有行落在一个由 $V$ 决定的子空间 $\operatorname{Ann}(V)$ 里”——**行空间型**，
不是对单个元素的仿射方程。

## 做法

### 1. 自由的部分（**已更正，见 200**）

> **更正（专家 63 号）**：$H$ 与 $H_A$ 由同一个提升 $l$ 耦合，所以“底部行在 $\operatorname{Ann}(V)$ 内自由”**过强**。
> 正确表述是 pair-space 约束：$(h_i,h_{A,i})=(l_iN,l_iAN)=\Theta(l_i)$ 属于固定子空间
> $\mathcal P_{A,C}=\operatorname{im}\Theta$，且 $l_i\in\mathcal L_V=\{l:lN|_V=0,lAN|_V=0\}$。
> 本节下面的“自由”只在忽略 $H_A$ 时成立。


固定 $V$（$\dim V=c$）后，$H$ 的行可在 $\operatorname{Ann}(V)$（$\omega$ 维）中**任意**选取，
只需 $\operatorname{rank}H=\omega$（开条件）与顶行固定。因此：
- 在 $\operatorname{Ann}(V)$ 的坐标里，$H$ 的底部行**没有任何线性等式约束**；
- 唯一的等式来自顶行 $L_0N$ 与 $V$ 的定义（$V=\ker H$）。

### 2. 约束的形状

- 若 $V$ 被 $A$ 强制（如 $\dim W_L=c$），则 $H$ 的全部行必须落在 $\operatorname{Ann}(V_0)$：这是一个**子空间包含**；
- 在 $\operatorname{Ann}(V_0)$ 内部，行坐标自由（只受秩开条件与铅笔约束）；
- 因此**不能**用观测器数据直接实现“某个矩阵元素等于 $b$”或“某一行的线性泛函等于 $b$”这类任意仿射约束；
  能实现的只是“行空间落在某个子空间”与“固定顶行”。

### 3. 与 ARM 的差距

ARM 的输入是任意仿射方程 $\langle A_i,X\rangle=b_i$（$i=1,\dots,m$）。若把 $X$ 等同于 $H$ 的底部行矩阵：
- 观测器**没有** $\langle A_i,H\rangle=b_i$ 这样的自由度；
- 它只给“行空间 $\subseteq\operatorname{Ann}(V)$”（同一条约束对所有行），以及顶行、秩、铅笔；
- 所以直接等同 $X=H$ 的归约**不成立**。

### 4. 可能的绕法（待研究）

1. **块对角 gadget**：让 $A$ 分解成多个块，每块强制一个 $V_j$，从而对不同行块给不同子空间；
   但仍是子空间型，不是逐条仿射方程。
2. **用 $V$ 的参数化**：$V$ 的 chart 坐标 $X$ 上，$F_A(X)$ 是二次的；ARM 的仿射约束也许能编码在 $V$ 的
   incidence 上，而不是 $H$ 上。
3. **用铅笔不等式**：$(5b)$ 给的是“所有 $\lambda$ 满秩”的开条件，不是等式；难以编码仿射方程。
4. **混合**：部分约束来自 $V$，部分来自顶行，部分来自提升层；需要显式构造。

## 进展

* 证明了观测器对 $H$ 的约束是行空间型（子空间包含 + 顶行 + 开条件），不是任意仿射型；
* 直接 $X=H$ 的 ARM 归约不成立；
* 列出四种可能的绕法，均待研究。

## 最终结论

* 196 的最小 gadget：**不能**用观测器数据直接实现任意仿射约束在 $H$ 上；
* 这是 $H=LN$ 结构的硬限制；
* 硬度归约需要把变量放到 $V$ 的 chart 或提升层，或使用块 gadget 并接受子空间型约束。

## 放弃原因

* 未构造任何具体 gadget；
* 未证明“子空间型约束不能编码 ARM”的不可行性（只是没有直接构造）；
* 未尝试 $V$-chart 的编码。

## 残留价值

* 明确了 ARM 归约的第一个结构性障碍；
* 为“硬度可能来自 $V$ 的 incidence 而非 $H$ 的仿射约束”提供依据。

## 相关文件

* [attempts/196](196_ARM3_reduction_plan.md)（归约计划）
* [attempts/171](../../../q1_false/c_stratification/attempts/171_Buv_rank_strata.md)（chart 的二次项）
* [attempts/152](../../../q1_false/c_stratification/attempts/152_lift_completion_fixed_l0.md)（提升）

## 状态

* 结构性观察：**[M2]**。
* 具体 gadget / 不可行性：**[未做]**。
