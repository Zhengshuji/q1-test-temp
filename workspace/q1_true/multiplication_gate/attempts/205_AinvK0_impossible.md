> **更正（专家 64 号）**：本定理只对 $0<\omega<k$（即 $0<c<k$）成立；$c>0$ 还包含 $\omega=0$（$c=k$），
> 该边界**可行**（反例见 [207](207_64_verdict_implementation.md)）。正确表述：
> $A(K_0)\subseteq K_0$、$\omega>0$ ⇒ 不可行（专家 65 号进一步：$c=0$ 也可，唯一例外是 $\omega=0$）。
> 局部版本 $A(V)\subseteq K_0$ 的铅笔步骤**不成立**（见 210）。

# Task C 的否定结论：$A(K_0)\subseteq K_0$ 时 $c>0$ 恒不可行

> 2026-11-09。Task C 要找“谱好的 gadget”。本文件证明一个**决定性的否定结果**：
> 只要 $A(K_0)\subseteq K_0$ 且 $c>0$，$(5a)(5b)$ **恒不可行**——与 $L_0$、$q$、$\omega$、gadget 无关。
> 因此“不变子空间乘法 gadget”路线在此 regime 下被谱条件彻底堵死。状态：**M2（纸面，短证明）**。

## 目标

判定 $A(K_0)\subseteq K_0$ 时是否存在可行解（$c>0$）。

## 设想与理由

203 已证：$A(K_0)\subseteq K_0$ ⇒ 可行 $V$ 必 $A$-不变。
于是 $V^\perp\subseteq K_0^*$ 是 $A^{\mathsf T}$-不变的（$l\in V^\perp\Rightarrow lA\in V^\perp$）。
由 $(5a)$，$\operatorname{row}H\subseteq\operatorname{Ann}(V)=V^\perp$；又 $\operatorname{rank}H=\omega=\dim V^\perp$，故
$$\operatorname{row}H=V^\perp.$$
$V^\perp\ne0$（$c>0\Rightarrow\omega>0$）。任意非零不变子空间在 $\mathbb C$ 上必含特征向量：
$A^{\mathsf T}|_{V^\perp}$ 有特征值 $\lambda$，其特征向量 $l\in V^\perp$ 满足 $lA=\lambda l$。

## 做法

取 $y$ 使 $yH=l$（$l\in\operatorname{row}H$）。则
$$yP(\lambda)=yH(\lambda I-A)=l(\lambda I-A)=\lambda l-lA=0.$$
所以 $P(\lambda)$ 的行线性相关，$\operatorname{rank}P(\lambda)<\omega$，与 $(5b)$ 矛盾。$\square$

## 推论

1. **202 的 gadget 不可行**：$A(K_0)\subseteq K_0$、$c>0$，故对任意 $L_0,q,\omega$ 都不可行——解释了 202/204 的全部 `none`。
2. **不变子空间 gadget 路线被堵死**：乘法 gadget 依赖 $A(V)\subseteq V$；而此 regime 下任何可行 $V$ 都导致谱条件失败。
3. **可行实例必须 $A(K_0)\not\subseteq K_0$**：seeds 16/21 正是如此（$Av\notin K_0$），所以它们能避开这个障碍。
4. **Task C 的答案是否定的**：在 $A(K_0)\subseteq K_0$ 的 observer 数据中不存在“谱好的 gadget”；硬度构造必须用 $A(K_0)\not\subseteq K_0$。

## 进展

* 证明了 $A(K_0)\subseteq K_0\Rightarrow$ 不可行（$c>0$）；
* 解释了 202/204 的全部失败；
* 明确了 hardness 构造的必要条件：$A(K_0)\not\subseteq K_0$。

## 最终结论

* **Task C 在 $A(K_0)\subseteq K_0$ 的 regime 下以否定告终**：不存在谱好的 gadget；
* 这是 observer 问题的一个强结构性刚性；
* hardness 必须走 $A(K_0)\not\subseteq K_0$ 的路线（如 seeds 的超平面/非不变机制）。

## 放弃原因

* 未构造 $A(K_0)\not\subseteq K_0$ 的乘法 gadget；
* 未把该不可能性推广到 $A(K_0)\not\subseteq K_0$ 的部分不变量；
* 未 Lean 化。

## 残留价值

* 一个干净、强力的不可行定理；
* 为 hardness 路线排除了整条“不变子空间 gadget”分支；
* 解释了此前所有 gadget 实验的失败。

## 相关文件

* [attempts/202](202_gadget_naive_embedding.md)、[204](204_spectral_gadget_conditions.md)（被解释）
* [attempts/203](203_invariance_theorem.md)（不变性）
* [attempts/201](201_pair_lift_theorem.md)（$\mathcal L_V$）
* [attempts/200](200_multiplication_gadget.md)（gadget）

## 状态

* 否定定理：**[已证-纸面，M2]**。
* $A(K_0)\not\subseteq K_0$ 的 gadget：**[未做]**。
