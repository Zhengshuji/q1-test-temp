# 专家 74 号裁决落实：$q=2$ 门关闭、特征向量判据、$\\kappa_{\\rm obs}$ 与下一路线

> 2026-11-09。74 号答复接受 $q=2$ no-go，并给出三个新方向：
> （1）谱条件的特征向量判据 $\\operatorname{im}H\\cap E_\\lambda(F)=\\{0\\}$，必要 $\\omega\\le q-1$；
> （2）有效观测器维数 $\\kappa_{\\rm obs}=r\\operatorname{rank}[N,AN]$，固定时 XP；
> （3）耦合二平面（Plücker）与 Liu 式系数编码。状态：**M3（专家裁决）**。

## 目标

把 74 号答复转成可执行结论与下一步。

## 设想与理由

专家明确：
- $q=2$ 单行门路线关闭，但**不要**推广到所有行列式构造；
- 最有价值的新方向是“有效观测器维数”（Experiment A）；
- 硬度侧优先 Liu 系数编码 + ARM gauge；
- 结构论文现在开始。

## 做法：逐条落实

### 1. $q=2$ 结论的定位

专家认可：
> 在所述观测器表述下，没有 $q=2$ 实例能实现非平凡单行乘法门并同时满足 $(5a)(5b)$。

但**不能**说“所有行列式构造都不可能”；$q\\ge3$ 的耦合二平面仍开放。

### 2. 特征向量判据（新引理）

$(5a)$ ⇒ 存在 $F$ 使 $H_A=FH$（行包含）。于是
$$P(\\lambda)=\\lambda H-H_A=(\\lambda I-F)H.$$
因此
$$\\operatorname{rank}P(\\lambda)=\\operatorname{rank}H
\\iff \\operatorname{im}H\\cap\\ker(\\lambda I-F)=\\{0\\}.$$
$(5b)$ 等价于
$$\\boxed{\\operatorname{im}H\\cap E_\\lambda(F)=\\{0\\}\\quad\\text{对所有特征值 }\\lambda\\text{ 成立}.}$$
必要性：
$$\\boxed{\\omega=\\operatorname{rank}H\\le q-1.}$$
证明：$F$ 在 $\\mathbb C$ 上有特征值 $\\lambda_0$，$\\dim E_{\\lambda_0}\\ge1$；
若 $\\operatorname{im}H\\cap E_{\\lambda_0}=0$，则 $\\omega\\le q-1$。

这给出 $q=2,\\omega=2$ 不可能的**一行证明**：$\\operatorname{im}H=\\mathbb C^2$ 必与每个非零特征空间相交。

### 3. 有效观测器维数

专家定义：
$$\\mathcal T(\\Delta R)=(\\Delta RN,\\Delta RAN),\\qquad
\\mathcal N_{\\rm obs}=\\{\\Delta R:\\Delta RN=0,\\Delta RAN=0\\},$$
$$\\boxed{\\kappa_{\\rm obs}=\\operatorname{codim}\\mathcal N_{\\rm obs}
=r\\operatorname{rank}[N,AN].}$$
两个 $R$ 若 $RN$、$RAN$ 相同，则对 $(5a)(5b)$ 不可区分。
固定 $\\kappa_{\\rm obs}$ 时，可行域是**固定维数**的实代数问题；按 Liu 的模板可期望
$\\mathcal L^{O(1)}n^{O(\\kappa_{\\rm obs}+1)}$ 的 XP 算法（不是自动 FPT）。

**关键未决**：固定 $c$ 是否推出固定 $\\kappa_{\\rm obs}$？三种可能：
(a) $c$ 控制 $\\kappa_{\\rm obs}$（强算法推论）；
(b) 需要额外的 $\\operatorname{rank}[N,AN]$ 参数；
(c) 两者独立（两个可解性 regime）。

### 3.1 Experiment A 的初步数值

用 `c246_kappa_obs.py` 计算三个实例（$r=q-\operatorname{rank}L_0$）：

| 实例 | $n$ | $q$ | $r$ | $\operatorname{rank}[N,AN]$ | $\kappa_{\rm obs}$ | $k=\dim K_0$ | $c=k-\omega$ |
|---|---|---|---|---|---|---|---|
| 234 | 5 | 2 | 1 | 4 | 4 | 3 | —（不可行）|
| 244 | 7 | 3 | 2 | 5 | 10 | 3 | 1 |
| 228 | 10 | 3 | 2 | 7 | 14 | 4 | 2 |

**观察**：$c=1$ 时 $\kappa_{\rm obs}=10$，$c=2$ 时 $\kappa_{\rm obs}=14$；
固定 $c$ **不**自动固定 $\kappa_{\rm obs}$，后者随 $n$ 增长。
所以“固定 $c$ ⇒ 多项式”不能直接由 Liu 模板得到；需要把
$\operatorname{rank}[N,AN]$（或 $\kappa_{\rm obs}$ 本身）作为独立参数。
这正是专家列的三种可能中的 (b)/(c)。

### 4. 下一路线（专家排序）

| 路线 | 优先级 | 理由 |
|---|---|---|
| (d) 固定 $c$ + 结构论文 | 1 | 可立即产出独立结果 |
| (c) Liu 式系数编码 | 2 | 最好的新硬度路线 |
| (a) $q\\ge3$ 耦合门 | 3 | 新结构结果的延续 |
| (b) ARM gauge/rank-forcing | 4 | 强但需要非平凡嵌入 |

专家建议 **(c)+(b) 结合**：把算术残差编进铅笔极大子式，用观测器 gauge 防止 unwanted row-space。

### 5. 耦合二平面（Plücker）

$q=3$、$\\operatorname{rank}H=2$，变量二平面 $U=\\operatorname{span}\\{x_1,x_2\\}$；
目标：让 $x_2$ 被 $x_1$ 强制（不是自由吸收），并用 Plücker 关系
$$p_{12}p_{34}-p_{13}p_{24}+p_{14}p_{23}=0$$
作为候选二次约束；再要求 $\\operatorname{im}H\\cap E_\\lambda(F)=0$。

### 6. 论文

专家建议现在开始，主题改为“代数不变性与谱容许性的交互”，标题候选：
*Algebraic Structure and Complexity of Minimum-Order Functional Observer Synthesis*。

论文骨架（专家版）：
1 引言；2 代数预备；3 一般刻画 $(5a)(5b)$/gcd；4 低 $c$ 分类（含 $q=2$ 二分）；
5 谱障碍（$\\omega=2$ 障碍 + $q=2$ no-go）；6 多行现象（$q=3$ 实例 + 行吸收）；
7 刚性与不变子空间；8 代数复杂度（$\\exists\\mathbb R$ + $\\kappa_{\\rm obs}$）；
9 精确算法（gcd/Bezout/四层求解器）；10 开放问题。

$q=2$ no-go 的定位：**$(5a)$ 的代数表达力 $\\ne$ 完整观测器问题的表达力**。

## 进展

* $q=2$ 结论被专家接受并给定性；
* 特征向量判据与 $\\omega\\le q-1$ 写出；
* $\\kappa_{\\rm obs}$ 定义与 XP 预期；
* 路线排序、耦合二平面、论文骨架。

## 最终结论

* 停止单行门搜索；
* **Experiment A（$\\kappa_{\\rm obs}$）是下一个定理**；
* 硬度侧优先 Liu 系数编码 + ARM gauge；
* 结构论文立即开始。

## 放弃原因

* 未证 fixed $c$ ⇒ fixed $\\kappa_{\\rm obs}$；
* 未构造耦合二平面门；
* 未做系数编码。

## 残留价值

* 一条清晰的算法/论文主线；
* 特征向量判据（可复用）；
* $\\kappa_{\\rm obs}$ 的精确定义。

## 相关文件

* [74 答复](../../../for_expert/archive/74_gate_no_go_and_literature-answer.md)
* [attempts/245](245_q2_no_gate_theorem.md)
* [attempts/244](../../multiplication_gate/attempts/244_q3_feasible_absorbed.md)

## 状态

* 裁决落实：**[完成，M3]**。
* Experiment A：**[未做]**。
