# 乘法 gadget 的朴素嵌入：谱条件使其不可行

> 2026-11-09。Task B 的第一实验：把 200 的 $2\times2$ 乘法 gadget 直接作为 $A$ 的 $4\times4$ 块，
> 取 $K_0=\mathbb C^4$、$L_0=e_1$、$q=3,4,5$。求解器在 $\operatorname{Gr}(2,W_L)$ 上找不到可行见证；
> 本文件给出结构原因：顶部行在 $\lambda=0$ 处消失，底部值全平行。状态：**精确实验 + 纸面解释**。

## 目标

检验 gadget 能否直接嵌入观测器（$A(K_0)\subseteq K_0$ 的最简情形）。

## 设想与理由

200 的 gadget：$E=\langle e_1,e_2\rangle$、$F=\langle e_3,e_4\rangle$，
$$A_{11}=A_{22}=\begin{bmatrix}0&0\\0&1\end{bmatrix},\quad
A_{12}=-\begin{bmatrix}0&1\\0&0\end{bmatrix},\quad A_{21}=0.$$
在 $K_0=\mathbb C^4$ 上取此 $A$，$A e_1=0$、$A e_2=e_2$、$A e_3=0$、$A e_4=e_4-e_1$。

取 $n=6$、$C=[e_5;e_6]$（$K_0=\operatorname{span}\{e_1,\dots,e_4\}$）、$L_0=e_1$。

## 做法

用统一求解器 `solve_general` 试：
```
q=3, ω=2: none
q=4, ω=2: none
q=4, ω=3: none
q=5, ω=2: none
```
（`none` 是搜索失败；下面给出该 gadget 的结构性不可行原因。）

### 结构原因

$L_0=e_1$，故 $H_0=e_1^*$、$H_{A,0}=0$；在 $\lambda=0$ 处顶部行消失。

取候选 $V=\operatorname{span}(e_2,e_3)\subseteq W_L=\ker e_1^*$（不变：$A e_2=e_2$、$A e_3=0$）。
$\operatorname{Ann}(V)=\operatorname{span}(e_1^*,e_4^*)$。底部行 $h=a e_1^*+b e_4^*$，提升 $l=a e_1+b e_4$（$l\cdot Av=0$ 自动）。
则
$$h_A=lAN=(b)(e_4^*-e_1^*),$$
在 $\lambda=0$ 处 $P(0)$ 的行是
$$-H_{A,0}=0,\qquad -h_A=b(e_1^*-e_4^*).$$
所有底部行（不论 $a,b$）在 $\lambda=0$ 的值都是 $e_1^*-e_4^*$ 的倍数，**全平行**；
故 $\operatorname{rank}P(0)\le1<2$，**不可行**（对任意 $q$）。

这是 191 的 $B_*=0$ 机制：顶部 $e_1^*$ 在 $\lambda=0$ 消失，而所有可容许提升的 $h_A$ 都落在同一条线上。

## 进展

* 朴素嵌入的求解器实验：全部 `none`；
* 给出结构性原因（$\lambda=0$ 处秩 $\le1$），不是搜索不足；
* 确认 Task C（谱/提升 gadget）是必需的，几何 gadget 不能自动存活。

## 最终结论

* 200 的乘法 gadget 在**几何层**成立；
* 直接嵌入观测器时，顶部特征值与提升的耦合会让 $P(\lambda_0)$ 秩降；
* 需要一个“谱 gadget”：让顶部行的特征值与底部提升的像避开这种平行结构（例如 $B_*$ 在特征空间单射）。

## 放弃原因

* 未构造出可行的谱 gadget；
* 未扫描其他 $L_0$（如 $e_2$、$e_3+e_4$）；
* 未做符号判定。

## 残留价值

* 一个明确的失败机制与反例；
* 为 Task C 指明“避开顶部特征值”的设计原则。

## 相关文件

* [attempts/200](200_multiplication_gadget.md)（gadget）
* [attempts/191](../../../q1_false/c_stratification/attempts/191_c1_pencil_criterion.md)（$B_*=0$ 机制）
* [attempts/201](201_pair_lift_theorem.md)（pair-lift）

## 状态

* 实验/解释：**[精确实验 + 纸面]**。
* 可行谱 gadget：**[未做]**。
