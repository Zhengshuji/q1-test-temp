# 不变性定理：$A(K_0)\subseteq K_0$ 时，可行 $V$ 必为 $A$-不变

> 2026-11-09。Task C 的结构基础：若 $A(K_0)\subseteq K_0$，则任何可行解的 $V=\ker H$ 都满足 $A(V)\subseteq V$。
> 这意味着乘法 gadget 的不变性方程是**被强制的**，硬度只剩谱条件。状态：**M2（纸面）**。

## 目标

证明：$A(K_0)\subseteq K_0$ 时，$(5a)(5b)$ 的任一可行 $V$ 都是 $A$-不变的。

## 设想与理由

对每行 $l\in L$，$h=lN$；$(5a)$ 给 $h|_V=0$，可容许性给 $(lAN)|_V=0$。
对 $v\in V$：$Av\in K_0$（因 $A(K_0)\subseteq K_0$），且
$$h(Av)=l(Av)=0$$
（$h=lN$ 在 $K_0$ 上与 $l$ 一致；$Av\in K_0$；第二式由 $lAN|_V=0$）。
所以每行 $h$ 都零化 $AV$，即 $h\in\operatorname{Ann}(V+AV)$。

## 做法

$$\operatorname{row}H\subseteq\operatorname{Ann}(V+AV)
\Longrightarrow\ \omega\le\dim\operatorname{Ann}(V+AV)=k-\dim(V+AV).$$
但 $\omega=k-c=k-\dim V$，故 $\dim(V+AV)\le\dim V$，即 $AV\subseteq V$。$\square$

### 专家 64 号的强化（2026-11-09）

局部版本：只需 $A(V)\subseteq K_0$（不需要 $A(K_0)\subseteq K_0$）且 $\omega>0$，就有 $A(V)\subseteq V$。
**但“进而铅笔秩降”不成立**（需要全局 $A(K_0)\subseteq K_0$）；seed 10 是反例（$A(V)\subseteq K_0$ 且可行）。详见 [210](210_local_leakage_correction.md)。

## 推论

- 对 $A(K_0)\subseteq K_0$ 的实例（包括 202 的 gadget 实例），**所有可行 $V$ 都是不变的**；
- 于是 chart 方程 $A_{21}+A_{22}X-XA_{11}-XA_{12}X=0$ 是**被强制的**，乘法 gadget 的几何部分不需要额外 gadget；
- 剩下的只有谱条件（$B_*$ 在特征空间单射）与提升完成。

### 对 202 的解释

202 中求解器对所有 $V$ 返回 none：非不变 $V$ 被本定理排除；不变 $V$ 则被谱条件（$\lambda=0$ 处秩降）排除。
所以 202 的失败是**谱**的，不是几何的。

### 边界

- 若 $A(K_0)\not\subseteq K_0$（如 seeds 16/21），本定理不适用；182 的超平面机制是另一条路；
- 定理只给“不变”，不给“好铅笔”。

## 进展

* 不变性定理证明；
* 202 的失败被解释为纯谱问题；
* Task C 的目标缩小为：在 $A(K_0)\subseteq K_0$ 的 gadget 实例中设计 $L_0$/提升使铅笔好。

## 最终结论

* $A(K_0)\subseteq K_0$ ⇒ 可行 $V$ 必不变；
* 乘法 gadget 的几何部分“免费”；
* 谱 gadget 是唯一剩余障碍。

## 放弃原因

* 未构造出谱好的 gadget 实例；
* 未处理 $A(K_0)\not\subseteq K_0$ 的对应结构；
* 未 Lean 化。

## 残留价值

* 一个干净的结构定理；
* 把 Task C 化归为谱设计；
* 解释了 202 的全部 none。

## 相关文件

* [attempts/202](202_gadget_naive_embedding.md)（谱障碍）
* [attempts/201](201_pair_lift_theorem.md)（pair-lift）
* [attempts/200](200_multiplication_gadget.md)（gadget）

## 状态

* 定理：**[已证-纸面，M2]**。
* 谱 gadget：**[未做]**。
