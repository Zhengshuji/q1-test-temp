# $c=3$ 的结构：层与递归（“谱控制”的归纳）

> 2026-11-08。按专家 54 号的下一步，做 $c=3$。核心观察：
> $\mathcal D_s$ 可以**递归**到 $c=2$ 的分量——不变 3-子空间由不变 2-子空间 + 特征线（或 3-链）构成；
> 含不变线的层是“特征线上的 $c=2$ 纤维”。状态：**M2（纸面草稿）**。
>
> **更正见 [attempts/130](../../decision_algorithms/attempts/130_general_induction_map_type.md)**：$\mathcal D_4$ 的“含不变 2-子空间”只覆盖
> $AW=W$ 的子型；一般 $W=V\cap A^{-1}V$ 不必不变。正确的归纳用线性映射型。
>
> **$\mathcal D_4/\mathcal D_5$ 的两子型（不变 / 非不变）见 [attempts/132](132_c3_d4_d5_subtypes.md)**：
> 本文件只写了 (a) 不变子空间；非不变型 $AW\ne W$ 由 132 补上。

## 目标

设 $c=3$，$V\subseteq K_0$、$\dim V=3$。描述
$$\mathcal D_s=\{V:\dim(V+AV)\le s\},\qquad s=3,4,5,6,$$
并证明：分量由 $A$ 在 $K_0$ 上的**模结构**（≤3 维不变子空间）控制，与 $k$ 无关。

## 设想与理由

* $\rho(V)=\dim(V+AV)=6-\dim(V\cap A^{-1}V)$，故
  $$\rho=3\iff AV\subseteq V,\quad \rho=4\iff\dim(V\cap A^{-1}V)=2,\quad
  \rho=5\iff\dim=1,\quad \rho=6\iff\dim=0.$$
* $\rho=3$：$A|_V$ 是 3×3；按 Jordan 型（分拆 $3=1+1+1,\ 2+1,\ 3$）分类；
  其中 $2+1$ 型 = “不变 2-子空间（$c=2$ 的 $\mathcal D_2$）+ 特征线”。
* $\rho=4$：$V$ 含不变 2-子空间 $W$；$V/W$ 是 $K/W$ 中的线，且 $AV/W\ne V/W$；对每个 $W$（$c=2$ 分量），
  这是 $K/W$ 中“去掉一条线”的投影空间——不可约。
* $\rho=5$：$V$ 含特征线 $L$；$V/L$ 是 $K/L$ 中的 2-平面，且不含 $\bar A$ 的不变线——
  正是 $c=2$ 的 $\mathcal D_4$（对 $\bar A$）在 $K/L$ 上的纤维。
* $\rho=6$：开集。
* 所以 $c=3$ 的每一层都是“$c=2$ 的某个分量”上的丛；分量数由 $c=2$ 的分量数 + 谱决定。

## 做法

### 1. $\mathcal D_3$：不变 3-子空间

$B=A|_V$（3×3），按 Jordan 型：

* **$1+1+1$（三个特征线）**：$V$ 由三条特征线张成；对每个三重特征值（计重数）至多一个 $V$；
  若重特征值的特征空间 $\ge3$，则 $V\subseteq E_\lambda$，得到 $\operatorname{Gr}(3,E_\lambda\cap K_0)$。
* **$2+1$**：$V=W\oplus\langle u\rangle$，$W$ 是不变 2-子空间（$c=2$ 的 $\mathcal D_2$：点、$\operatorname{Gr}(2,E_\lambda)$、$J_\lambda$），
  $u$ 是另一条特征线（$\mu$ 特征值，可以与 $W$ 的 $\lambda$ 相同但来自不同的块）。
  这是**以 $c=2$ 的 $\mathcal D_2$ 分量为底、以特征线选择为纤维**的丛。
* **$3$（单个 3-链）**：$V=\langle e_1,e_2,e_3\rangle$，$(A-\lambda I)e_i=e_{i-1}$；
  固定特征线 $L=\langle e_1\rangle$，$e_2,e_3$ 的选取构成仿射空间（维数 $m_\lambda$ 量级）；
  这是以特征线为底的丛。

### 2. $\mathcal D_4$：含不变 2-子空间

设 $W\subset V$ 是不变 2-子空间（$c=2$ 的 $\mathcal D_2$ 点），$V/W$ 是 $K/W$ 中的线。
$AV/W$ 也是 $K/W$ 中的线（若 $A|_W$ 可逆）；$\dim(V+AV)=4\iff AV/W\ne V/W$。
所以对每个 $W$，纤维是 $\mathbb P(K/W)$ 去掉一条线——不可约。**以 $c=2$ 的 $\mathcal D_2$ 为底的丛**。

### 3. $\mathcal D_5$：含不变线

设 $L=\langle u\rangle$ 是特征线。$V/L$ 是 $K/L$ 中的 2-平面；
$\dim(V\cap A^{-1}V)=1\iff V/L$ 在 $K/L$ 中不含 $\bar A$ 的不变线，即 $V/L\in\mathcal D_4^{(c=2)}(\bar A)$。
所以**以特征线为底、以 $c=2$ 的 $\mathcal D_4$ 为纤维的丛**。

### 4. $\mathcal D_6$：开集

补集闭，$\operatorname{Gr}(3,K_0)$ 不可约，非空开集不可约。**一个分量**。

### 5. 分量界与“谱控制”

* $\mathcal D_3$：由 $c=2$ 的 $\mathcal D_2$ 分量数（$\le\binom{s}{2}+2s$）加特征线选择（$\le s$）控制；
* $\mathcal D_4$：由 $c=2$ 的 $\mathcal D_2$ 分量数控制；
* $\mathcal D_5$：由特征线数（$\le s$）与 $c=2$ 的 $\mathcal D_4$ 分量数（$\le1$）控制；
* $\mathcal D_6$：$1$。

所以
$$\boxed{\#\{\text{components of }c=3\}\ \le\ \text{（谱的显式函数）},}$$
与 $k$ 无关。结构上，$c=3$ 的每一层都是 $c=2$ 的某个分量上的丛——**归纳成立**。

## 进展

* 四层的递归结构已写出：$\mathcal D_3$（$1+1+1$ / $2+1$ / $3$）、$\mathcal D_4$（$\mathcal D_2$ 上的丛）、
  $\mathcal D_5$（特征线上的 $\mathcal D_4^{(c=2)}$）、$\mathcal D_6$（开）。
* 核心结论：$c=3$ 的分量由 $c=2$ 的分量与谱决定，不是新的 determinantal 几何。
* 未做：$2+1$ 型中“同一特征值、不同块”的组合；$3$-链的仿射纤维维数；$K_0$ 截断的非空条件；
  分量界的显式常数；具体实例验证。

## 最终结论

* $c=3$ 的层结构是**递归**的：
  $$\mathcal D_3\ \text{（不变 3-子空间）},\quad
  \mathcal D_4\ \text{（}\mathcal D_2\text{ 上的丛）},\quad
  \mathcal D_5\ \text{（特征线上的 }\mathcal D_4^{(c=2)}\text{）},\quad
  \mathcal D_6\ \text{（开）}.$$
* 分量数只依赖 $A$ 在 $K_0$ 上的模结构（≤3 维不变子空间），与 $k$ 无关。
* 这支持“固定 $c$ 时谱控制分量”的普遍图景；$c=3$ 的完整分类只需把 $c=2$ 的部件组合起来。

## 放弃原因

* $2+1$ 型的 Jordan 组合（同特征值、多块）未逐项分类；
* $3$-链的仿射纤维维数与 $K_0$ 截断未写；
* 分量界只给了“谱的显式函数”的存在性，没有具体常数；
* 没有实例验证。

## 残留价值

* $c=3$ 的第一张结构图：四层 + 递归到 $c=2$。
* 把“$c$ 固定时分量由模结构控制”从 $c=1,2$ 推广到 $c=3$。
* 为一般 $c$ 的归纳（不变 $t$-子空间 + 链）提供模板。

## 相关文件

* [attempts/125](125_c2_structure_complete.md)（$c=2$ 分类）
* [attempts/126](126_c2_k0_truncation.md)（$c=2$ 非空）
* [attempts/127](../../decision_algorithms/attempts/127_c2_algorithm.md)（$c=2$ 算法）
* [attempts/121](121_hyperplane_vector_bundle.md)（$c=1$ 定理）
* [docs/05 Q9](../../../../docs/05_open_questions.md)（$\mathcal D_s$ 的定位）

## 状态

* 层结构：**[草稿，M2]**（$\mathcal D_3/\mathcal D_4/\mathcal D_5/\mathcal D_6$ 的递归）。
* 分量界：**[草稿，M2]**（谱的显式函数，常数未算）。
* 未做：Jordan 组合、$K_0$ 截断、具体常数、实例验证。
