# $c=2$ 的 $K_0$ 截断：各分量的非空条件

> 2026-11-08。125 给了 $c=2$ 的分量分类；本文件补上“哪些分量真的存在”的**精确非空条件**。
> 设 $m_0=\dim K_0$、$e_\lambda=\dim(E_\lambda\cap K_0)$、$T_\lambda=(A-\lambda I)|_{K_0}:K_0\to K$。
> 状态：**M2（纸面）**。
>
> **$\mathcal D_3$ 的非空条件要按 [attempts/131](131_c2_d3_nilpotent_subtype.md) 的两子型分开**：
> 本文件只覆盖 (a) 不变线；子型 (b) 需要 $D=K_0\cap A^{-1}K_0\ne0$ 且 $A|_D$ 非标量。

## 目标

对 125 的每个分量，给出 $\operatorname{Gr}(2,K_0)$ 中的非空充要条件：

1. $\mathcal D_2$ 的点（$\lambda\ne\mu$）；
2. $\operatorname{Gr}(2,E_\lambda)$；
3. $J_\lambda$（Jordan 丛）；
4. $\mathcal D_3$（投影丛）；
5. $\mathcal D_4$（开集）。

## 设想与理由

* 分量必须落在 $K_0$ 里，故每个条件都是“$K_0$ 内是否存在这种 2-子空间”。
* $\mathcal D_2$ 的点与 $\operatorname{Gr}(2,E_\lambda)$ 只看 $E_\lambda\cap K_0$ 的维数。
* $J_\lambda$ 需要 $w\in K_0$ 且 $(A-\lambda I)w\in E_\lambda\cap K_0$，即
  $\operatorname{im}T_\lambda\cap\ker T_\lambda\ne0$。
* $\mathcal D_3$ 需要一条 $L\subset E_\lambda\cap K_0$ 与 $w\in K_0\setminus L$ 使 $V/L$ 不是 $\bar A$ 的特征线；
  当 $m_0\ge3$ 时，$\mathbb P(K_0/L)$ 的维数 $\ge1$，去掉有限条特征线仍非空。
* $\mathcal D_4$ 是开集；用维数比较给充分条件。

## 做法

**预备**：$\operatorname{Gr}(2,K_0)\ne\varnothing\iff m_0\ge2$。

**1. $\mathcal D_2$ 的点（$\lambda\ne\mu$）**：$V=\langle u_\lambda,u_\mu\rangle$，两条特征线都要在 $K_0$ 里：
$$\boxed{e_\lambda\ge1\ \text{且}\ e_\mu\ge1.}$$
（两条特征线不同，故张成 2 维；都在 $K_0$ 里故 $V\subset K_0$。）

**2. $\operatorname{Gr}(2,E_\lambda)$**：$V\subseteq E_\lambda\cap K_0$：
$$\boxed{e_\lambda\ge2.}$$

**3. $J_\lambda$**：$V=\langle u,w\rangle$，$u\in E_\lambda\cap K_0$、$w\in K_0$、
$(A-\lambda I)w=cu$（$c\ne0$）。即 $u\in\operatorname{im}T_\lambda\cap\ker T_\lambda$。故
$$\boxed{e_\lambda\ge1\ \text{且}\ \operatorname{im}T_\lambda\cap\ker T_\lambda\ne0.}$$
（等价说法：$T_\lambda$ 在 $K_0$ 上的像与核有非零交；若 $K_0\subseteq E_\lambda$ 则像为 0，无 Jordan 平面。）

**4. $\mathcal D_3$**：需要 $L\subset E_\lambda\cap K_0$（$e_\lambda\ge1$）与 $w\in K_0\setminus L$ 使
$V/L$ 不是 $\bar A$ 在 $K/L$ 上的特征线。
* 若 $m_0\ge3$：$\mathbb P(K_0/L)$ 的维数 $m_0-2\ge1$；$\bar A$ 的特征线在 $\mathbb P(K/L)$ 中只有有限条，
  故非特征线存在。**非空**（只要 $e_\lambda\ge1$）。
* 若 $m_0=2$：$K_0=L$ 是唯一的 2-子空间（$V=K_0$）；$\mathcal D_3$ 非空 $\iff$ $K_0$ 含特征线但
  $K_0/L$ 不是 $\bar A$ 的特征线，即 $K_0$ 不是 $A$-不变但含一条特征线。
故
$$\boxed{\mathcal D_3\ \text{非空}\iff e_\lambda\ge1\ \text{且}\ (m_0\ge3\ \text{或}\ m_0=2\ \text{时 }K_0\ \text{含特征线但不不变}).}$$

**5. $\mathcal D_4$**：$\mathcal D_4=\operatorname{Gr}(2,K_0)\setminus(\mathcal D_2\cup\mathcal D_3)$ 是开集；
非空 $\iff$ 闭集 $\mathcal D_2\cup\mathcal D_3$ 不覆盖 $\operatorname{Gr}(2,K_0)$。

**充分条件（维数）**：$\dim\operatorname{Gr}(2,K_0)=2m_0-4$。各闭片的维数：
* 点：$0$；
* $\operatorname{Gr}(2,E_\lambda)$：$2(e_\lambda-2)$；
* $J_\lambda$：底 $\mathbb P(E_\lambda\cap K_0)$ 维 $e_\lambda-1$，纤维 $\mathbb A^{e_\lambda}$ 维 $e_\lambda$，共 $2e_\lambda-1$；
* $\mathcal D_3$：底 $\mathbb P(E_\lambda\cap K_0)$ 维 $e_\lambda-1$，纤维 $\mathbb P(K/L)$ 维 $m_0-2$，共 $m_0+e_\lambda-3$。

若对所有 $\lambda$ 有 $e_\lambda\le m_0-2$，则
$$2e_\lambda-1\le2m_0-5<2m_0-4,\qquad m_0+e_\lambda-3\le2m_0-5<2m_0-4,$$
故 $\mathcal D_2\cup\mathcal D_3$ 的维数严格小于 $\operatorname{Gr}(2,K_0)$，**$\mathcal D_4$ 非空**。

**精确情形**（$m_0=2$）：$V=K_0$ 唯一；
* $\mathcal D_2$ 非空 $\iff AK_0\subseteq K_0$；
* $\mathcal D_3$ 非空 $\iff K_0$ 含特征线但 $AK_0\not\subseteq K_0$；
* $\mathcal D_4$ 非空 $\iff K_0\cap A^{-1}K_0=0$（即 $K_0$ 不含特征线）。
三者互斥且穷尽。

## 进展

* $\mathcal D_2$ 点、$\operatorname{Gr}(2,E_\lambda)$、$J_\lambda$、$\mathcal D_3$ 的非空条件已给出；
* $\mathcal D_4$ 有维数充分条件与 $m_0=2$ 的精确条件；
* 这些条件都是**线性代数**的（$e_\lambda$、$\operatorname{im}T_\lambda\cap\ker T_\lambda$、$m_0$），
  与 $k$ 无关，可直接判定。

## 最终结论

* $c=2$ 的分量是否非空，完全由 $K_0$ 与 $A$ 在 $K_0$ 上的线性结构决定：
  $e_\lambda=\dim(E_\lambda\cap K_0)$、$T_\lambda=(A-\lambda I)|_{K_0}$、$m_0=\dim K_0$。
* 这补上了 125 缺的“$K_0$ 截断”：分量分类 + 非空条件 = 真正可用的分量表。
* 每层上 $R$ 的向量丛与 gcd 仍按 123 的模板处理。

## 放弃原因

* $\mathcal D_4$ 的一般精确条件（非维数充分条件）未给；需要判定 $\mathcal D_2\cup\mathcal D_3$ 是否覆盖
  $\operatorname{Gr}(2,K_0)$，这是另一层 determinantal 问题。
* 没有具体实例的验证（实验只作辅助）。
* $c\ge3$ 未做。

## 残留价值

* 一张“分量 + 非空条件”的完整表，可直接用于 $c=2$ 的判定算法。
* 所有条件都是线性代数的，可精确计算。
* 为 $c\ge3$ 的“谱控制分量”猜想提供模板。

## 相关文件

* [attempts/125](125_c2_structure_complete.md)（$c=2$ 分类）
* [attempts/124](124_c2_degeneracy_loci.md)（第一版结构图）
* [attempts/123](123_hyperplane_algorithm.md)（$c=1$ 判定算法模板）
* [docs/05 Q9](../../../../docs/05_open_questions.md)（$\mathcal D_s$ 的定位）

## 状态

* 非空条件：**[已证-纸面，M2]**（$\mathcal D_2$ 点、$\operatorname{Gr}(2,E_\lambda)$、$J_\lambda$、$\mathcal D_3$，以及 $\mathcal D_4$ 的充分条件）。
* $\mathcal D_4$ 精确条件：**[开放]**（除 $m_0=2$）。
* 未做：实例验证、$c\ge3$。
