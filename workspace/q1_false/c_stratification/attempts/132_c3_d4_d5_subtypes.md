# $c=3$ 修正：$\mathcal D_4/\mathcal D_5$ 的“不变 / 非不变”两子型

> **55 号更正见 [attempts/134](134_55_corrections_exact_fibre.md)**（专家裁决）：
> 不变的含义是 $A(W)\subseteq W$（含奇异），不是 $A(W)=W$；
> $t=2$ 的 $V=U=W+A(W)$ 还需 $\operatorname{rank}\overline A_V=1$（例如 $Ab\notin V$），本文件漏了；
> $t=1$ 子型 A 需 $U\cap\bar A^{-1}U=0$（本文件的“不含 $\bar A$-不变线”太弱）；
> 子型 B 需 $A^2v+V$ 与 $Aw+V$ 在 $K_0/V$ 中独立（本文件的 $A^2v\notin V$ 只是必要）。
>
> 2026-11-08。128/129 把 $\mathcal D_4$ 说成“含不变 2-子空间”、$\mathcal D_5$ 说成“含不变线”，
> 这和 125 的 $\mathcal D_3$ 是同一个过度简化。按 131 的模板，$c=3$ 也要分
> $AW=W$（不变）与 $AW\ne W$（非不变）两子型。状态：**M2（纸面草稿）**。

## 目标

设 $c=3$、$V\in\operatorname{Gr}(3,K_0)$、$W=V\cap A^{-1}V$、$t=\dim W$。
对 $t=2$（$\mathcal D_4$）与 $t=1$（$\mathcal D_5$），补上“非不变”子型。

## 设想与理由

* $W=V\cap A^{-1}V$ 满足 $A(W)\subseteq V$，但**不必不变**（131 的反例）。
* 若 $AW=W$：128 的“不变子空间 + 线”结构成立。
* 若 $AW\ne W$：$A(W)$ 是 $V$ 中的另一个子空间，$V$ 由 $W$ 与 $A(W)$ 共同张成（或再加一条线）；
  这是**幂零型**，参数是 $W$（或 $L$），不是“$W$ 上的纤维”。

## 做法

### 1. $\mathcal D_4$：$t=2$

$W$ 是 2 维，$A(W)\subseteq V$，$V$ 是 3 维。

**(a) $A(W)=W$（不变 2-子空间）**：$W$ 是 $c=2$ 的 $\mathcal D_2$ 部件（点 / $\operatorname{Gr}(2,E_\lambda)$ / $J_\lambda$）；
$V=W\oplus\langle w\rangle$，$V/W$ 是 $K/W$ 中的线，且 $AV/W\ne V/W$。
非空 = $W$ 非空（126）+ 线条件（$K/W$ 维数 $\ge2$，即 $m_0\ge4$）。

**(b) $A(W)\ne W$（非不变）**：分两种：
* **$A|_W$ 可逆**：$A(W)$ 也是 2 维，$A(W)\ne W$；$V=W+A(W)$ 是 3 维 $\iff\dim(W\cap A(W))=1$。
  此时 $V$ **由 $W$ 唯一决定**。$W$ 的条件：$W\subseteq K_0\cap A^{-1}K_0$、$A(W)\subseteq K_0$、
  $A(W)\ne W$、$\dim(W\cap A(W))=1$。$W$ 跑一个开/构造集，像是不可约的（纤维有限）。
* **$A|_W$ 奇异**：$A(W)$ 是一条线。若 $A(W)\subseteq W$，则 $V=W\oplus\langle w\rangle$ 且 $Aw\notin V$
  （否则 $W$ 变成不变，$t=3$）；若 $A(W)\not\subseteq W$，则 $V=W+\langle A(W)\rangle$（3 维），
  同样由 $W$ 决定。
非空：$W$ 满足上述线性条件；具体哪一型由 $\operatorname{rank}(A|_W)$ 与 $A(W)\cap W$ 决定。

### 2. $\mathcal D_5$：$t=1$

$W=L$ 是一条线，$A(L)\subseteq V$。

**(a) $A(L)=L$（不变线）**：$L$ 是特征线；$V/L$ 是 $K/L$ 中的 2-平面，且不含 $\bar A$-不变线
（即 $V/L\in\mathcal D_4^{(c=2)}(\bar A)$）。非空：$e_\lambda\ge1$ + $c=2$ 的 $\mathcal D_4$ 条件。

**(b) $A(L)\ne L$（非不变）**：$A(L)$ 是 $V$ 中的另一条线；$V$ 含 2-维的 $L\oplus A(L)$，再取一条线 $w$：
$$V=L\oplus A(L)\oplus\langle w\rangle,$$
且 $A(A(L))\notin V$（否则 $A(L)\in V\cap A^{-1}V=L$）。$V/L$ 是 $K/L$ 中含 $A(L)/L$ 的 2-平面，
且不含 $\bar A$-不变线（除 $L$ 外）。$L$ 跑 $\mathbb P(D)\setminus$ 特征线（$D=K_0\cap A^{-1}K_0$），
纤维是 $K/(L+A(L))$ 中的线（避开不变线条件）——不可约丛。

### 3. $\mathcal D_6$：开集

补集闭；$\operatorname{Gr}(3,K_0)$ 不可约；非空开集不可约。一个分量。

### 4. 分量界（草稿）

| 层 | 分量 | 数量 |
|---|---|---|
| $\mathcal D_3$ | 不变 3-子空间（$1+1+1$/$2+1$/$3$）| 由 129 的表 |
| $\mathcal D_4$ (a) | $\mathcal D_2^{(c=2)}$ 上的丛 | $\le\binom{s}{2}+2s$ |
| $\mathcal D_4$ (b) | 非不变 $W$（按 $\operatorname{rank}(A|_W)$ 与 $A(W)\cap W$ 分型）| $\le$ 常数（型数）|
| $\mathcal D_5$ (a) | 特征线上的 $c=2$ $\mathcal D_4$ | $\le s$ |
| $\mathcal D_5$ (b) | 非不变 $L$ 上的丛 | $\le$ 常数（型数）|
| $\mathcal D_6$ | 开 | $1$ |

总界只依赖 $s$ 与 $A$ 在这些 $W/L$ 上的秩型，与 $k$ 无关（草稿；常数的显式值未算）。

## 进展

* $\mathcal D_4/\mathcal D_5$ 的“不变 / 非不变”两子型已分开；128/129 的“含不变子空间”只覆盖 (a)。
* 非不变型的参数是 $W$（或 $L$），$V$ 由 $W$ 与 $A(W)$（或 $L,A(L),w$）决定；这是 130 的型控制在 $c=3$ 的具体化。
* 分量界仍是“谱 + 秩型”的函数，与 $k$ 无关（草稿）。

## 最终结论

* $c=3$ 的 $\mathcal D_4$、$\mathcal D_5$ 都有 (a) 不变 / (b) 非不变两子型；128/129 只写了 (a)。
* 非不变型不是“$W$ 上的纤维”，而是“$W$ 的像”（$\mathcal D_4$）或“$L$ 与 $A(L)$ 上的丛”（$\mathcal D_5$）。
* 修正后，$c=3$ 的分量表与 130 的型控制一致：由 $W=V\cap A^{-1}V$、$A(W)$、秩型决定。

## 放弃原因

* 非不变型的**完整分型**（$A|_W$ 的秩、$A(W)\cap W$ 的维数、$A(A(W))$ 的位置）只给了框架，未逐型列全；
* 分量界的显式常数未算；
* $K_0$ 截断在非不变型的精确条件未逐项写；
* 没有实例验证。

## 残留价值

* $c=3$ 的**正确**两子型表，替换 128/129 的“含不变子空间”说法。
* 非不变型的“$W$ 决定 $V$”结构，是 130 型控制在 $c=3$ 的具体化。
* 为 $c=3$ 算法（127 的模板）提供正确的分量表。

## 相关文件

* [attempts/131](131_c2_d3_nilpotent_subtype.md)（$c=2$ 的两子型；本文件的模板）
* [attempts/130](../../decision_algorithms/attempts/130_general_induction_map_type.md)（型控制；反例）
* [attempts/128](128_c3_structure.md)（$c=3$ 层；本文件修正其 $\mathcal D_4/\mathcal D_5$）
* [attempts/129](129_c3_jordan_truncation.md)（$c=3$ Jordan/截断）

## 状态

* $\mathcal D_4/\mathcal D_5$ 两子型：**[草稿，M2]**。
* 分量界：**[草稿，M2]**（谱 + 秩型，常数未算）。
* 未做：完整分型、显式常数、$K_0$ 截断、实例验证。
