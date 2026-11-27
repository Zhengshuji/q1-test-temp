# 一般 $c$ 的型控制定理（归纳的精确陈述）

> **55 号裁决（专家）：本文件降级为猜想，见 [attempts/134](134_55_corrections_exact_fibre.md)**。
> 三处修正：(i) 精确纤维条件是 $\operatorname{rank}(V\to K/V)=c-t$，**不是** $A(V)\cap V=B$；
> (ii) $A|_W$ 不是自同态，Jordan 型无定义，应改用 Kronecker 型 of $(\iota|_W,A|_W)$；
> (iii) $N(c)\le\sum_\tau N(t(\tau))$ 不成立；$X_\tau$ 不自动是低层同一问题。
>
> 2026-11-08。把 130 的“线性映射型控制”写成精确的归纳命题：
> 固定 $c$，$\mathcal D_s$ 的每个分量都是“$t\le c$ 的 $W$-型层”上的 Grassmannian 丛；
> $W$-型层本身是同一问题在 $t$ 层的实例，故对 $c$ 归纳。状态：**M2（纸面草稿）**。

## 目标

证明（或精确陈述）：

> **型控制定理（草稿）**：固定 $c$。设 $V\in\operatorname{Gr}(c,K_0)$，$W=V\cap A^{-1}V$，$t=\dim W$。
> 则 $\mathcal D_s=\{V:\rho(V)\le s\}$ 的每个不可约分量都是
> “某个 $t\le c$ 的 $W$-型层 $X_\tau$ 上的 Grassmannian 丛”的像；
> 分量数由 $c$ 与 $A$ 在 $K_0$ 上的 Jordan 型控制，**与 $k$ 无关**。

## 设想与理由

* $\rho(V)=2c-t$；$\mathcal D_s=\{t\ge2c-s\}$。
* $W=V\cap A^{-1}V$，$B=A(W)\subseteq V$；$A(V)\cap V=B$。
* 给定 $W$，$B$ 固定；$V$ 必须包含 $W+B$，且 $V/(W+B)$ 是 $K/(W+B)$ 中的子空间，
  并满足“$A(V)\cap V=B$”这个开条件。
* 所以层 $=$（$W$ 的型层）上的 Grassmannian 丛；$W$ 的型层是同一问题在 $t$ 层的实例。
* 对 $c$ 归纳：$t<c$ 时归到 $t$ 层；$t=c$（不变）时 $V=W$，是“不变 $c$-子空间”的 Jordan 型分类。

## 做法

### 1. 型 $\tau$

对 $V$ 定义
$$\tau(V)=\big(t,\ r=\operatorname{rank}(A|_W),\ s_0=\dim(W\cap A(W)),\ 
\text{Jordan 型 of }A|_W\big).$$
前三个是整数；最后一个是 $A|_W:W\to K$ 的线性映射型（在 $W$ 的基下，$r\times t$ 的秩型；
当 $B\subseteq W$ 时就是 $A|_W$ 作为 $W$ 上自同态的 Jordan 型）。

**$W$-型层**：
$$X_\tau=\{W\in\operatorname{Gr}(t,K_0):\ A(W)\subseteq K_0,\ \operatorname{rank}(A|_W)=r,\ 
\dim(W\cap A(W))=s_0,\ \text{Jordan 型}=\tau\}.$$
这是 $W$ 上的局部闭层（秩/维数条件）。

### 2. 丛结构

固定 $W\in X_\tau$，$B=A(W)$（秩 $r$）。$V$ 的条件：
* $W\subseteq V$，$B\subseteq V$，故 $W+B\subseteq V$；
* $V/(W+B)$ 是 $K/(W+B)$ 中的 $(c-t-(r-s_0))$ 维子空间；
* 开条件：$A(V)\cap V=B$（等价于 $V\cap A^{-1}V=W$）。

$K/(W+B)$ 的维数是 $n-(t+r-s_0)$；纤维是
$$\operatorname{Gr}\big(c-t-(r-s_0),\ K/(W+B)\big)$$
的开子集（去掉 $A(V)\cap V\supsetneq B$ 的闭集）。它是不可约的（Grassmannian 不可约，开子集不可约）。

**丛**：$X_\tau$ 上的 Grassmannian 丛；若 $X_\tau$ 不可约，则总空间不可约；分量对应 $X_\tau$ 的分量。

### 3. 归纳

* $t<c$：$X_\tau$ 是“$t$ 维 $W$ 的型层”，正是同一问题在 $c'=t$ 的实例；对 $c$ 归纳。
* $t=c$：$W=V$，$V$ 是 $A$-不变 $c$-子空间；$\tau$ 是 $A|_V$ 的 Jordan 型（分拆 $c$ + 特征值）。
  这是“不变 $c$-子空间”的分类，有限、$k$-无关（$c=3$ 的表见 129）。
* 基例 $c=1$：$X_\tau$ 是 $\mathbb P(K_0)$ 上的特征线/点，分量有限（121）。

### 4. 分量界

设 $N(c)$ 是 $\mathcal D_s$（所有 $s$）的分量数上界。归纳给出
$$N(c)\le\sum_{\tau}N(t(\tau))\cdot 1,$$
其中 $\tau$ 跑 $t\le c$ 的型，$N(t)$ 是 $t$ 层的分量数。基例 $N(1)$ 有限；
型的个数对固定 $c$ 有限（整数元组 + Jordan 型）。故 $N(c)$ 有限，只依赖 $c$ 与 $A$ 的 Jordan 型，
**与 $k$ 无关**。

## 进展

* 型 $\tau$ 与 $W$-型层 $X_\tau$ 已定义；丛结构与开条件已写。
* 归纳框架已闭合：$t<c$ 归到 $t$ 层，$t=c$ 是 Jordan 型分类，基例 $c=1$ 是 121。
* 分量界是“$N(c)\le\sum_\tau N(t(\tau))$”，有限、$k$-无关。
* 与具体例子一致：$c=2$ 的 $\mathcal D_3$ 两子型（131）对应 $t=1$ 的 $X_\tau$（$AW=W$ vs $AW\ne W$）；
  $c=3$ 的 $\mathcal D_4/\mathcal D_5$ 两子型（132）对应 $t=2,1$ 的 $X_\tau$。

## 最终结论

* 固定 $c$ 时，$\mathcal D_s$ 的分量由 **$W$-型层 + Grassmannian 丛** 控制；$W$-型层递归到 $t<c$。
* 分量数有限，只依赖 $c$ 与 $A$ 的 Jordan 型，与 $k$ 无关。
* 这把 Q9 的“分量分解”归约成：
  $$\text{固定 }c\text{ 的型分类（有限）} + \text{每型的 Grassmannian 丛（不可约）}.$$
* 这是目前对“一般情形”最精确的陈述：不是“任意 determinantal variety”，也不是“不变子空间”，
  而是“$W=V\cap A^{-1}V$ 的型 + 丛”。

## 放弃原因

* 型分类（哪些 $\tau$ 非空、$X_\tau$ 的分量）没有对一般 $c$ 逐型列出；
* $X_\tau$ 的不可约性/分量数只做了框架论证，未逐型证明；
* $K_0$ 截断在一般 $c$ 的非空条件未写；
* 没有实例验证。

## 残留价值

* 一个精确、可归纳的型控制定理（草稿），把 $c=1,2,3$ 的具体分类统一起来。
* 分量界的递归式 $N(c)\le\sum_\tau N(t(\tau))$；基例 $c=1$ 已由 121 给出。
* 为论文的“一般 $c$”一节提供主陈述；为后续逐型证明提供清晰目标。

## 相关文件

* [attempts/130](../../decision_algorithms/attempts/130_general_induction_map_type.md)（型控制的起点 + 反例）
* [attempts/131](131_c2_d3_nilpotent_subtype.md)（$c=2$ 的两子型）
* [attempts/132](132_c3_d4_d5_subtypes.md)（$c=3$ 的两子型）
* [attempts/121](121_hyperplane_vector_bundle.md)（$c=1$ 基例）
* [docs/05 Q9](../../../../docs/05_open_questions.md)（$\mathcal D_s$ 的定位）

## 状态

* 型控制定理：**[草稿，M2]**（陈述 + 归纳框架 + 分量界递归）。
* 逐型证明：**[未做]**（$X_\tau$ 的分量、非空条件）。
* 未做：一般 $c$ 的型分类、$K_0$ 截断、实例验证。
