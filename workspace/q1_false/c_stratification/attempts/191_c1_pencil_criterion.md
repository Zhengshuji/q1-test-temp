# O1：$c=1$ 铅笔恒坏的判据（块分解）

> 2026-11-08。190 的 O1 是“铅笔恒坏”的结构判据。本文件用 $Z$ 的块分解把它写成：
> 坏 $\iff$ $A_*$ 的每个特征向量都落在 $\ker B_*$ 里；特别地 $B_*=0$（即 $H_A\in\operatorname{row}H$）必然坏。
> 状态：**M2（纸面）**。

## 目标

给定 $V=L$ 与 $L_0$，判断是否存在可容许的 $(H,H_A)$ 使
$$\operatorname{rank}(\lambda H-H_A)=\omega\quad\forall\lambda.$$

## 设想与理由

取 $W=\operatorname{im}H$（$\omega$ 维），补空间 $\mathbb C^q=W\oplus W'$，则
$Z:W\to\mathbb C^q$（$H_A=ZH$）写成
$$Z=\begin{bmatrix}A_*\\B_*\end{bmatrix},\qquad A_*:W\to W,\ B_*:W\to W'.$$
于是
$$P(\lambda)=(\lambda I-Z)H=\begin{bmatrix}(\lambda I-A_*)H\\-B_*H\end{bmatrix},$$
$$\operatorname{rank}P(\lambda)<\omega\iff\exists\,0\ne y\in W:\ A_*y=\lambda y,\ B_*y=0.$$
（因为 $H:V\to W$ 满射。）

## 做法

### 判据

- **坏 $\lambda$**：$\ker(\lambda I-A_*)\cap\ker B_*\ne0$。
- **好** $\iff$ $A_*$ 的**每个**特征向量（含广义特征向量对应的特征向量）都不在 $\ker B_*$ 里。

### $B_*=0$ 的结构性坏

若 $B_*=0$（即 $H_A$ 的每一行都在 $\operatorname{row}H$ 中，$H_A=SH$），则
$$P(\lambda)=H(\lambda I-S),$$
$\det(\lambda I-S)$ 是 $\omega$ 次非零多项式，必有根 $\lambda_0$；在 $\lambda_0$ 处 $\operatorname{rank}P<\omega$。
所以
$$\boxed{B_*=0\ \Longrightarrow\ \text{恒坏（不可行）}.}$$

### $B_*\ne0$ 时

- $A_*$ 可对角化：特征向量张成 $W$；若全在 $\ker B_*$，则 $W=\ker B_*$，$B_*=0$，矛盾。故**存在**特征向量不在
  $\ker B_*$ ⇒ 好。
- $A_*$ 不可对角化：可能有唯一点特征线落在 $\ker B_*$，此时坏；需要检查。

**结论**：$B_*\ne0$ 时，坏是**特殊**的（非对角化 + 特征线被 $\ker B_*$ 吞掉）；
$B_*=0$ 时**恒坏**。这给出 O1 的判据：
$$\text{可行}\ \Longrightarrow\ B_*\ne0\ \text{且}\ A_*\ \text{的特征向量不全在}\ \ker B_*.$$

## 对 $c=1$、$W_L\not\subseteq D$ 的应用

可容许提升的 $H_A$ 自由度来自 $g\in\operatorname{row}[C;CA]$：$H_A\mapsto H_A+\Gamma(g)$，$\Gamma(g)=gAN$。
若 $\Gamma$ 的像在 $\operatorname{row}H$ 之外有分量，则 $B_*\ne0$ 可实现；否则 $B_*=0$，恒坏。
189 的两个合成反例正是 $B_*$ 被结构压成 0（顶部行全消失、可容许切掉独立方向）的表现。

## 进展

* O1 写成块分解判据：坏 $\iff$ $A_*$ 的特征向量全在 $\ker B_*$；
* $B_*=0$ 的恒坏性证明（$\det(\lambda I-S)$ 有根）；
* $B_*\ne0$ 时坏是特殊的（非对角化 + 特征线被吞）；
* 与 189 的合成反例对应。

## 最终结论

* O1 的判据：$B_*=0$ ⇒ 恒坏；$B_*\ne0$ ⇒ 一般好，特殊坏；
* 对 $c=1$ 的算法：先判 $B_*$ 是否可非零（$\Gamma$ 模 $\operatorname{row}H$），再查非对角化特例；
* 这把 $c=1$ 的铅笔部分化成了有限维线性代数。

## 放弃原因

* 未给出“$A_*$ 特征线被 $\ker B_*$ 吞”的完整算法（需要特征向量计算/结式）；
* 未处理 $\omega=0$/$k=0$ 边界；
* 未 Lean 化。

## 残留价值

* O1 的块判据；
* $B_*=0$ 的恒坏证明；
* 为 $c=1$ 的判定树补上铅笔分支。

## 相关文件

* [attempts/190](190_c1_decision_tree.md)（O1）
* [attempts/189](189_c1_outside_D_feasible.md)（合成反例）
* [attempts/152](152_lift_completion_fixed_l0.md)（$\Gamma$、$B_*$ 的来源）

## 状态

* 判据：**[已证-纸面，M2]**。
* 特征线吞并的算法/Lean：**[未做]**。
