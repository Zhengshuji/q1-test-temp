# $c=3$ 重写：用精确纤维定理（专家 55 §4.3–§4.4 / §9 Step 3）

> 2026-11-08。用 135 的精确纤维定理重写 $c=3$，落实专家 55 的更正：
> $t=2$ 的 $V=U$ 需 $\operatorname{rank}\overline A_V=1$；$t=1$ 子型 A 需 $U\cap\bar A^{-1}U=0$；
> 子型 B 需 $A^2v+V$ 与 $Aw+V$ 独立；$t=3$ 按初等因子分类。
> 状态：**M2（纸面；表已按精确条件重写）**。

## 更正（专家 56 号）

所有商空间用环境状态空间 $\mathcal X$ 的商（$\mathcal X/V$、$\mathcal X/L$、$\mathcal X/U$、$\mathcal X/W$），
不是 $K_0/\cdot$——除非 $A(K_0)\subseteq K_0$。集合条件（$V=U$、$Ab\notin V$、$Aw\notin V$ 等）不受影响；
$\operatorname{Gr}(c-\dim U,K_0/U)$ 中的 $K_0/U$ 保留（$V\subseteq K_0$ 是参数空间）。

## 目标

对 $c=3$、$V\in\operatorname{Gr}(3,K_0)$、$W=V\cap A^{-1}V$、$t=\dim W\in\{0,1,2,3\}$，
给出精确纤维、非空条件与分类。

## 设想与理由

* 135：纤维 $=\operatorname{Gr}(3-\dim U,K_0/U)$ 中满足 $\operatorname{rank}(V\to \mathcal X/V)=3-t$ 的开子集。
* $t=0$：秩 3；$t=3$：$V$ 不变（$A|_V$ 自同态，初等因子）。
* $t=1$：$U=L+AL$，分 $AL\subseteq L$ / $AL\not\subseteq L$。
* $t=2$：$U=W+A(W)$，$\dim U=2$ 或 $3$；分 $A(W)\subseteq W$ / 不。

## 做法

### $t=0$

$U=0$；条件是 $\operatorname{rank}\overline A_V=3$，即 $V\cap A^{-1}V=0$；开集于 $\operatorname{Gr}(3,K_0)$。

### $t=1$：$W=L=\mathbb Cv$，$L\subseteq D$

**子型 A：$AL\subseteq L$**。$U=L$；$V/L$ 是 $\mathcal X/L$ 中的 2-平面（$V\subseteq K_0\subseteq\mathcal X$），记 $U'=V/L$；精确条件是
$$\boxed{U'\cap\bar A^{-1}U'=0}$$
（等价于 $\bar A_{U'}:U'\to(\mathcal X/L)/U'$ 秩 2）。这是 $\operatorname{Gr}(2,\mathcal X/L)$ 中的开集（限制在 $K_0/L$ 上）。
注意“$U'$ 不含 $\bar A$-不变线”**太弱**：可以有 $u\in U'$、$\bar Au\in U'$ 但 $u$ 不在不变线上。

**子型 B：$AL\not\subseteq L$**。$U=L+AL$ 是 2 维；$V=U+\langle w\rangle$；精确条件是
$$\boxed{A^2v+V\ \text{与}\ Aw+V\ \text{在}\ \mathcal X/V\ \text{中线性独立}}$$
（等价于 $\overline A_V:V/L\to \mathcal X/V$ 秩 2）。这是 $\mathcal X/U$ 的线空间中的开集。
“$A^2v\notin V$”只是必要。

### $t=2$：$W$ 2 维，$U=W+A(W)$

**$\dim U=3$**：$V=U$ 被决定；精确条件是 $\operatorname{rank}\overline A_V=1$（$c-t=1$）。
等价地，若 $B=\langle b\rangle$ 是 $A(W)$ 中不在 $W$ 的线，则 $Ab\notin V$。**132 漏了这个条件。**

**$\dim U=2$**：$A(W)\subseteq W$（$B\subseteq W$）；$V=W+\langle w\rangle$；精确条件是
$$Aw\notin V$$
（$\operatorname{rank}\overline A_V=1$），是 $\mathcal X/W$ 的线空间中的开集。
分界是 $A(W)\subseteq W$ vs $A(W)\not\subseteq W$，**不是** $A(W)=W$。

### $t=3$：不变 3-子空间

$W=V$、$A(V)\subseteq V$；$A|_V$ 是 3×3 自同态。按**初等因子**分类（不只按分拆 $3$）：
$$1_\lambda+1_\mu+1_\nu,\quad 2_\lambda+1_\mu,\quad 3_\lambda,\quad 1_\lambda+2_\lambda,\quad\ldots$$
参数空间是 $\mathbb C[x]$-子模簇（不必是点或单一仿射丛）。

### 精确非空条件汇总

| $t$ | 子型 | 非空条件 |
|---|---|---|
| 3 | 不变 3-子空间 | 按初等因子；存在对应子模 |
| 2 | $\dim U=3$ | 存在 $W$ 使 $V=U$ 且 $\operatorname{rank}\overline A_V=1$ |
| 2 | $\dim U=2$ | 存在 $W$ 与线 $w$ 使 $Aw\notin V$ |
| 1 | A（$AL\subseteq L$）| 存在 2-平面 $U'$ 使 $U'\cap\bar A^{-1}U'=0$ |
| 1 | B（$AL\not\subseteq L$）| 存在 $v,w$ 使 $A^2v+V$、$Aw+V$ 独立 |
| 0 | 开 | 存在 $V$ 使 $\operatorname{rank}\overline A_V=3$ |

## 进展

* $c=3$ 的六个子型都用精确纤维条件重写；132 的三处弱条件已修正。
* $t=2$ 的 $\dim U=3$ 补上了 $\operatorname{rank}\overline A_V=1$；$t=1$ A/B 的秩条件已写。
* $t=3$ 改为初等因子（含不同特征值组合）。

## 最终结论

* $c=3$ 的精确分层：$t=3$（不变，初等因子）、$t=2$（$\dim U=2/3$，秩 1）、
  $t=1$（A：$U'\cap\bar A^{-1}U'=0$；B：秩 2）、$t=0$（秩 3）。
* 每个纤维都是开 Grassmannian；非空条件是线性代数/子模存在性。
* 这是专家 55 §9 Step 3 的落实。

## 放弃原因

* 子型内部的不可约分量、参数空间的连通性未逐项证。
* $t=3$ 的初等因子表未逐项列出（只给规则）。
* $m_0$ 边界、实点未做。

## 残留价值

* 一张可用的 $c=3$ 精确表，替代 132 的弱条件版本。
* 为 $c=3$ 算法与 Kronecker 表述（138）提供正确输入。

## 相关文件

* [attempts/135](135_exact_fibre_theorem.md)（精确纤维）
* [attempts/132](132_c3_d4_d5_subtypes.md)（旧版；本文件修正）
* [attempts/136](136_c2_rewrite.md)（$c=2$）
* [attempts/138](../../decision_algorithms/attempts/138_kronecker_representation.md)（Kronecker 表述）

## 状态

* 分类：**[已证-纸面，M2]**（子型穷尽 + 精确条件）。
* 不可约分量/初等因子表：**[未逐项证]**。
