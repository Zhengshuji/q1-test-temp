# $c=3$ 的 Jordan 组合与 $K_0$ 截断：归纳的“更好结论”

> 2026-11-08。补 128 的两块：$\mathcal D_3$ 的 Jordan 组合、$c=3$ 的 $K_0$ 截断。
> 结论：$c=3$ 的每个分量都是“某个 $c=2$ 分量 + 特征线/3-链”的丛；分量数与非空条件只依赖
> $A$ 在 $K_0$ 上的**模型**（$\le3$ 维不变子空间的 Jordan 型），与 $k$ 无关。
> 这把 128 的“递归”提升为一个可陈述的**模型控制**命题。状态：**M2（纸面草稿）**。
>
> **$\mathcal D_4/\mathcal D_5$ 的两子型（不变/非不变）见 [attempts/132](132_c3_d4_d5_subtypes.md)**：
> 本文件的 $\mathcal D_4$ 只覆盖 $AW=W$ 的子型。

## 目标

1. 补全 $\mathcal D_3$（不变 3-子空间）的 Jordan 组合；
2. 补全 $c=3$ 各层的 $K_0$ 截断（非空条件）；
3. 提取归纳的“更好结论”：固定 $c$ 时分量由模型控制，而不是任意 determinantal variety。

## 设想与理由

* $B=A|_V$ 是 3×3，按 Jordan 型分拆 $3=1+1+1,\ 2+1,\ 3$。
* 每个型都是“一个 $c=2$ 的部件（不变 2-子空间或特征线）+ 一条特征线/一个链向量”；
  所以 $K_0$ 截断可以复用 126 的条件，再加新向量在 $K_0$ 里的条件。
* 所有条件都是 $e_\lambda=\dim(E_\lambda\cap K_0)$、$T_\lambda=(A-\lambda I)|_{K_0}$、
  以及迭代原像的线性代数条件；与 $k$ 无关。

## 做法

### 1. $\mathcal D_3$ 的 Jordan 组合

**$1+1+1$，三个不同特征值** $\lambda,\mu,\nu$：$V$ 由三条特征线张成；**点**。
非空：$e_\lambda,e_\mu,e_\nu\ge1$。

**$1+1+1$，同一特征值 $\lambda$**：$V\subseteq E_\lambda$；$\operatorname{Gr}(3,E_\lambda\cap K_0)$。
非空：$e_\lambda\ge3$。

**$2+1$**：$V=W\oplus\langle u\rangle$，$W$ 是 $c=2$ 的 $\mathcal D_2$ 部件，$u$ 是特征线：
* $W=\operatorname{Gr}(2,E_\lambda)$ 或 $W=J_\lambda$（$c=2$），$u\in E_\mu$，$\mu\ne\lambda$；
* 或 $\mu=\lambda$：则 $u$ 必须是 $W$ 之外的另一条 $\lambda$-特征线；只有 $W=J_\lambda$（含一条特征线）时才可能，
  需要 $e_\lambda\ge2$；若 $W=\operatorname{Gr}(2,E_\lambda)$ 则 $V\subseteq E_\lambda$，回到 $\operatorname{Gr}(3,E_\lambda)$。
非空条件 = $W$ 的非空条件（126）+ $e_\mu\ge1$，且 $u\notin W$（$\mu=\lambda$ 时 $e_\lambda\ge2$）。

**$3$（单个 3-链）**：$V=\langle e_1,e_2,e_3\rangle$，
$$T_\lambda e_1=0,\qquad T_\lambda e_2=e_1,\qquad T_\lambda e_3=e_2,\qquad e_1\ne0.$$
非空条件：存在这样的链且 $e_i\in K_0$。等价地，在 $K_0$ 上迭代：
$$K_0\cap T_\lambda^{-1}K_0\cap T_\lambda^{-2}\big(K_0\cap\ker T_\lambda\big)\ \text{含非零的 }e_1.$$
这是可判定的线性代数条件（迭代原像的维数）。

### 2. $c=3$ 的 $K_0$ 截断

**$\mathcal D_4$**：$V$ 含不变 2-子空间 $W$（$c=2$ 的 $\mathcal D_2$），$V/W$ 是 $K_0/W$ 中的线，
且 $AV/W\ne V/W$。
* $W$ 非空：126 的条件；
* $V/W$：$K_0/W$ 的维数 $m_0-2$；线空间 $\mathbb P(K_0/W)$ 的维数 $m_0-3$。
  若 $m_0\ge4$，去掉一条线（$AV/W$）后仍非空；$m_0=3$ 时 $K_0=W\oplus$ 一条线，需特例判定。
非空：$m_0\ge4$（或 $m_0=3$ 特例）。

**$\mathcal D_5$**：$V$ 含特征线 $L$（$e_\lambda\ge1$），$V/L$ 是 $K_0/L$ 中不含 $\bar A$-不变线的 2-平面，
即 $V/L\in\mathcal D_4^{(c=2)}(\bar A)$。
非空：$e_\lambda\ge1$ 且 $c=2$ 的 $\mathcal D_4$ 条件对 $\bar A$ 在 $K_0/L$ 上成立；用 126 的
$m_0'=\dim(K_0/L)=m_0-1$、$e'_\mu=\dim(E_\mu(\bar A)\cap K_0/L)$ 判定。

**$\mathcal D_6$**：开集；维数充分条件同 126（用 $m_0$、$e_\lambda$ 的维数比较）。

### 3. 归纳的“更好结论”

把 $c=1,2,3$ 的结论并起来，得到一个**模型控制**命题（草稿）：

> **命题（固定 $c$）**：$\mathcal D_s$ 的每个分量都是“某个不变 $t$-子空间（$t<c$）的
> $c'=t$ 分量 + 一条线/一个链向量”的丛；分量数与非空条件只依赖 $A$ 在 $K_0$ 上的**模型**
> （不变 $t$-子空间的 Jordan 型，$t\le c$），与 $k$ 无关。

* $c=1$：$t=1$（特征线）；
* $c=2$：$t=1,2$（特征线、不变 2-子空间：点 / $\operatorname{Gr}(2,E_\lambda)$ / $J_\lambda$）；
* $c=3$：$t=1,2,3$（再加 3-链、$2+1$ 组合），每层递归到 $c=2$。

**为什么这是“更好结论”**：它把 $\mathcal D_s$ 从“任意 determinantal variety”降成
“$A$ 的有限维模型 + 线性代数非空条件”。若对一般 $c$ 成立，则：

* 分量数只依赖 $c$ 与 $A$ 的 Jordan 型（不依赖 $k$）；
* 判定算法只需枚举模型，而不是任意行列式簇；
* $q1$ 的几何部分被归约成“$A$ 的模分类”，这是有限、可计算的。

## 进展

* $\mathcal D_3$ 的 $1+1+1$ / $2+1$ / $3$ 已分类；$K_0$ 条件已写出（含 3-链的迭代原像条件）。
* $\mathcal D_4/\mathcal D_5/\mathcal D_6$ 的 $K_0$ 截断已写出（$m_0\ge4$、$\bar A$ 的 $c=2$ 条件、维数充分条件）。
* 模型控制命题已陈述（草稿）；$c=3$ 是它的第三个实例。

## 最终结论

* $c=3$ 的 Jordan 组合与 $K_0$ 截断补齐；所有条件都是 $e_\lambda$、$T_\lambda$、$m_0$ 的线性代数。
* 归纳给出一个更强的图景：**固定 $c$ 时分量由 $A$ 的模型控制**，与 $k$ 无关。
* 这把 Q9 的“分量分解”从代数几何问题转成“$A$ 的模分类 + 线性代数”，是目前最清晰的
  一般情形路线。

## 放弃原因

* $2+1$ 型中“同特征值、多块”的完整组合只给了规则，未逐项列全；
* 3-链的迭代原像条件只给了形式，未给显式维数公式；
* 模型控制命题只是草稿，未对一般 $c$ 证明；
* 没有实例验证。

## 残留价值

* $c=3$ 的可用的“Jordan 组合 + 非空条件”表。
* 模型控制命题：把分量问题归约成 $A$ 的模分类，是比“determinantal variety”更强的结构。
* 为一般 $c$ 的归纳（不变 $t$-子空间 + 链 + 线）提供模板。

## 相关文件

* [attempts/128](128_c3_structure.md)（$c=3$ 层结构）
* [attempts/126](126_c2_k0_truncation.md)（$c=2$ 非空条件）
* [attempts/125](125_c2_structure_complete.md)（$c=2$ 分类）
* [attempts/121](121_hyperplane_vector_bundle.md)（$c=1$ 定理）
* [docs/05 Q9](../../../../docs/05_open_questions.md)（$\mathcal D_s$ 的定位）

## 状态

* $\mathcal D_3$ Jordan 组合：**[草稿，M2]**。
* $K_0$ 截断：**[草稿，M2]**（$\mathcal D_4/\mathcal D_5/\mathcal D_6$）。
* 模型控制命题：**[草稿，M2]**（$c=1,2,3$ 的实例；一般 $c$ 未证）。
* 未做：多块组合的完整列举、迭代原像的显式维数、一般 $c$、实例验证。
