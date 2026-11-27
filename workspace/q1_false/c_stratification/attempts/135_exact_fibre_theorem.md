# 精确 Grassmannian 纤维定理（专家 55 §1 / §9 Step 1）

> 2026-11-08。专家 55 号裁决的第一步：把 133 的错误纤维条件 $A(V)\cap V=B$ 换成
> $V\cap A^{-1}V=W$ 的**极大秩**形式。这是后续 $c=2/c=3$ 重写的基础。
> 状态：**M2（纸面证明；总层分量行为未证）**。

## 更正（专家 56 号）

商空间应为环境状态空间 $\mathcal X/V$（$A$ 在其上有定义），不是 $K_0/V$——除非 $A(K_0)\subseteq K_0$。
$\Phi_V:V\to\mathcal X/V$、$v\mapsto Av+V$ 恒有定义，$\ker\Phi_V=V\cap A^{-1}V$，故
$\operatorname{rank}\Phi_V=c-\dim W$；纤维的开性不变。下文已按 $\mathcal X/V$ 改写。

## 目标

设 $c\ge1$、$V\in\operatorname{Gr}(c,K_0)$、$W=V\cap A^{-1}V$、$t=\dim W$、
$B=A(W)$、$U=W+B$。证明：

> **精确纤维定理**：固定 $W$（$W\subseteq D=K_0\cap A^{-1}K_0$、$\dim W=t$、$U=W+A(W)\subseteq K_0$），
> 映射 $V\mapsto V\cap A^{-1}V$ 在 $W$ 上的纤维是
> $$\boxed{\mathcal F_W=\big\{V\in\operatorname{Gr}(c,K_0):\ U\subseteq V,\ 
> \operatorname{rank}(V\to \mathcal X/V)=c-t\big\},}$$
> 其中 $V\to \mathcal X/V$ 由 $A$ 诱导（$v\mapsto Av+V$）。它是
> $$\operatorname{Gr}\big(c-\dim U,\ K_0/U\big)$$
> 的**开子集**（极大秩条件）；非空即不可约。

## 设想与理由

* $W=V\cap A^{-1}V=\ker(\overline A_V)$，$\overline A_V:V\to \mathcal X/V$，$\overline A_V(v)=Av+V$。
* 故 $V\cap A^{-1}V=W\iff\ker\overline A_V=W\iff\operatorname{rank}\overline A_V=c-t$。
* $U=W+A(W)\subseteq V$ 是必要的：$W\subseteq V$、$A(W)\subseteq V$。
* 在 $\operatorname{Gr}(c-\dim U,K_0/U)$ 上，$\operatorname{rank}\overline A_V=c-t$ 是**极大秩开条件**。
* 开子集不可约（Grassmannian 不可约）。

## 做法

**引理 1（核 = 交）**：$\ker\overline A_V=V\cap A^{-1}V$。

*证明*：$\overline A_V(v)=0\iff Av\in V\iff v\in V\cap A^{-1}V$。$\square$

**引理 2（$U\subseteq V$ 必要）**：$W\subseteq V$ 且 $A(W)\subseteq V$，故 $U=W+A(W)\subseteq V$。

**定理证明**：设 $V$ 满足 $W=V\cap A^{-1}V$。由引理 1，$\ker\overline A_V=W$，故
$\operatorname{rank}\overline A_V=c-t$；由引理 2，$U\subseteq V$。反之，若 $U\subseteq V$ 且
$\operatorname{rank}\overline A_V=c-t$，则 $\ker\overline A_V$ 是 $V$ 的 $t$ 维子空间，含 $W$
（因为 $W\subseteq V$ 且 $A(W)\subseteq V$，即 $W\subseteq\ker\overline A_V$）；同维故
$\ker\overline A_V=W$，于是 $V\cap A^{-1}V=W$。$\square$

**开性/不可约性**：$V\supseteq U$ 的 $V$ 构成 $\operatorname{Gr}(c-\dim U,K_0/U)$；
$\operatorname{rank}\overline A_V=c-t$ 是“某个 $(c-t)$-子式非零”，是开条件；开子集不可约。$\square$

**重要限定（专家 55 §1.3）**：这不自动给出“总层每个底分量一个不可约分量”。还需：
底层的有限分层、纤维随 $W$ 的代数变化、总空间到基的投影的像/分量行为。后者是 139 的猜想内容。

## 进展

* 精确纤维定理已证（引理 1/2 + 定理）。
* 与 134 §1 一致；本文件给出独立、完整的证明。
* 它替代 133 的 $A(V)\cap V=B$：后者只保证 $\operatorname{im}(A|_V)\cap V=B$，不保证 $\ker\overline A_V=W$。

## 最终结论

* 纤维 = 开 Grassmannian；条件是 $\operatorname{rank}(V\to \mathcal X/V)=c-t$。
* 这是 $c=2/c=3$ 重写与 Kronecker 表述的基础。
* 总层的分量行为仍是开放问题（型控制猜想）。

## 放弃原因

* 未证总层分量的对应（投影像、底分层）。
* 未处理 $K_0$ 截断的非空条件（各 $W$ 是否在 $K_0$ 内）。

## 残留价值

* 一个可复用的精确纤维引理，替代错误条件。
* 为 $c=2$（136）、$c=3$（137）、Kronecker（138）提供统一入口。

## 相关文件

* [attempts/134](134_55_corrections_exact_fibre.md)（55 裁决总表）
* [attempts/133](133_type_control_theorem.md)（被本文件修正的旧纤维条件）
* [attempts/136](136_c2_rewrite.md)（$c=2$ 重写）
* [attempts/138](../../decision_algorithms/attempts/138_kronecker_representation.md)（Kronecker 表述）

## 状态

* 精确纤维定理：**[已证-纸面，M2]**。
* 总层分量：**[开放]**（139 猜想）。
