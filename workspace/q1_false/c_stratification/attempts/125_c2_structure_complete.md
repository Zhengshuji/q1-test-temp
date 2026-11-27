# $c=2$ 的结构补完：$\mathcal D_2$ 的 Jordan 丛与 $\mathcal D_3$ 的投影丛

> 2026-11-08。补 124 的两个缺口，并**更正** 124 的两处过度简化：
> (i) $\mathcal D_2$ 的 Jordan 情形不是“点”，而是以特征线为底、仿射空间为纤维的丛；
> (ii) $\mathcal D_3$ 的结构是“每个特征值一个投影丛”，不是“特征线 × 特征值”的散点。
> 状态：**M2（纸面）**。
>
> **非空条件（$K_0$ 截断）见 [attempts/126](126_c2_k0_truncation.md)**：
> 由 $m_0=\dim K_0$、$e_\lambda=\dim(E_\lambda\cap K_0)$、$T_\lambda=(A-\lambda I)|_{K_0}$ 判定。
>
> **更正见 [attempts/130](../../decision_algorithms/attempts/130_general_induction_map_type.md)**：$\mathcal D_3$ 的“含不变线”只覆盖
> $AW=W$ 的子型；$AW\ne W$ 的幂零链型（反例 $J_4(0)$、$V=\langle e_2,e_3\rangle$）不在 125 里。
> 一般归纳应用 $W=V\cap A^{-1}V$ 的**线性映射型**。
>
> **$\mathcal D_3$ 的正确两子型见 [attempts/131](131_c2_d3_nilpotent_subtype.md)**：(a) $AW=W$（不变线丛）、
> (b) $AW\ne W$（$V=L+AL$，幂零 2-步）。125 只含 (a)。

## 目标

设 $c=k-\omega=2$，$V\subseteq K_0$、$\dim V=2$，$A:V\to K$。证明：

1. $\mathcal D_2=\{V:AV\subseteq V\}$ 的精确分类（含 Jordan 情形）；
2. $\mathcal D_3=\{V:\dim(V+AV)=3\}$ 的精确结构；
3. $\mathcal D_4$ 的不可约性；
4. 分量界只依赖 $A$ 在 $K_0$ 上的谱/Jordan 型，与 $k$ 无关。

## 设想与理由

* $\rho(V)=\dim(V+AV)=4-\dim(V\cap A^{-1}V)$。
* $\mathcal D_2$：$AV\subseteq V$，$B=A|_V$ 是 2×2；按 $B$ 的 Jordan 型分类。
* $\mathcal D_3$：$V$ 含**唯一**不变线 $L$；在商 $K/L$ 上，$V/L$ 不是 $\bar A$ 的特征线。
  这给出“以特征线为底、以投影空间为纤维”的丛，而不是散点。
* 每层上 $R$ 的约束是 $RV=0,RAV=0$，即每行落在 $(V+AV)^\perp$；$\rho$ 常值时是向量丛。

## 做法

### 1. $\mathcal D_2$：按 $B=A|_V$ 的 Jordan 型

**情形 (a)：$B$ 有两个不同特征值 $\lambda\ne\mu$。**
$V$ 由一条 $\lambda$-特征线与一条 $\mu$-特征线张成；对每对 $\{\lambda,\mu\}$ 至多一个 $V$（若两条特征线都在 $K_0$ 里）。
**点分量**，至多 $\binom{s}{2}$ 个（$s$=不同特征值个数）。

**情形 (b)：$B=\lambda I$。**
$V\subseteq E_\lambda=\ker(A-\lambda I)$；所有这样的 $V$ 构成 $\operatorname{Gr}(2,E_\lambda\cap K_0)$。
**Grassmannian 分量**，每个 $\lambda$ 至多一个（若 $\dim(E_\lambda\cap K_0)\ge2$）。

**情形 (c)：$B$ 是非平凡 Jordan 块。**
取 $L=\langle u\rangle$ 为 $V$ 的特征线（$Au=\lambda u$），$V=L\oplus\langle w\rangle$，且
$$(A-\lambda I)w=c\,u,\qquad c\ne0.$$
固定 $L$，所有这样的 $w$ 构成
$$J_\lambda(L)=\big((A-\lambda I)^{-1}L\setminus E_\lambda\big)/L.$$
因为 $\dim(A-\lambda I)^{-1}L=\dim E_\lambda+1=m_\lambda+1$，模 $L$ 后纤维是**仿射空间** $\mathbb A^{m_\lambda}$
（去掉 $E_\lambda$ 不影响维数）。$L$ 跑遍 $\mathbb P(E_\lambda\cap K_0)$，得到**丛**
$$J_\lambda\longrightarrow\mathbb P(E_\lambda\cap K_0),\qquad \text{fibre }\mathbb A^{m_\lambda}.$$
它是不可约的（$\mathbb P(E_\lambda\cap K_0)$ 不可约，纤维仿射空间不可约，且是代数的局部平凡丛）。
**注**：124 说“每个 Jordan 块至多一点”是**错的**——纤维是正维的；只有 $m_\lambda=1$ 时才退化成点。

**$\mathcal D_2$ 的分量**：
* 点：$\{\lambda,\mu\}$（$\lambda\ne\mu$，两条特征线在 $K_0$ 里）；
* $\operatorname{Gr}(2,E_\lambda\cap K_0)$（$m_\lambda\ge2$）；
* $J_\lambda$（$\lambda$ 有 Jordan 块且特征线在 $\operatorname{im}(A-\lambda I)$ 里）。

这些分量两两不交（$B$ 的 Jordan 型不同，或特征值不同）。

### 2. $\mathcal D_3$：含唯一不变线的 $V$

设 $V\in\mathcal D_3$，$L$ 是 $V$ 的唯一不变线。则 $L$ 是特征线，$Au=\lambda u$。写 $V=L\oplus\langle w\rangle$。
在商 $K/L$ 上，$A$ 诱导 $\bar A:K/L\to K/L$（因为 $AL\subseteq L$），且 $AV/L=\bar A(V/L)$。于是
$$AV\subseteq V\iff \bar A(V/L)\subseteq V/L\iff V/L\ \text{是}\ \bar A\ \text{的特征线}.$$
所以
$$\mathcal D_3=\{V=L\oplus\langle w\rangle:\ L\ \text{特征线},\ V/L\ \text{不是}\ \bar A\ \text{的特征线}\}.$$
固定特征值 $\lambda$，$L$ 跑遍 $\mathbb P(E_\lambda\cap K_0)$，$V/L$ 跑遍 $\mathbb P(K/L)$ 去掉有限个特征线；
这是**投影丛** $\mathbb P(K/L)\to\mathbb P(E_\lambda\cap K_0)$ 的开子集（去掉有限个闭集），故**不可约**。
不同 $\lambda$ 的特征线不同，故这些分量不交。

**结论**：$\mathcal D_3$ 每个**特征值**至多一个不可约分量（不是 124 说的“特征线 × 特征值”的多个散点）。

### 3. $\mathcal D_4$：开集

$\mathcal D_4=\operatorname{Gr}(2,K_0)\setminus(\mathcal D_2\cup\mathcal D_3)$ 是开集；
$\operatorname{Gr}(2,K_0)$ 不可约，非空开集不可约。**一个分量**（若非空）。

### 4. $R$ 的向量丛与分量界

每层上 $\rho$ 常值（$\mathcal D_2$ 上 $\rho=2$，$\mathcal D_3$ 上 $\rho=3$，$\mathcal D_4$ 上 $\rho=4$）。
每行的约束是 $r\in(V+AV)^\perp$，维数 $n-\rho$；$m$ 行是向量丛。$\operatorname{rank}H=\omega$ 与
$\operatorname{rank}[L_0;R]=q$ 是开条件，故 lifted incidence 在该层上是不可约向量丛的开子集，非空即不可约。

**分量界**：
$$\boxed{\ \#\le\binom{s}{2}+3s+1\ }$$
（点 $\binom{s}{2}$ + $\operatorname{Gr}(2,E_\lambda)$ 至多 $s$ + $J_\lambda$ 至多 $s$ + $\mathcal D_3$ 至多 $s$ + $\mathcal D_4$ 一个），
只依赖不同特征值个数 $s$（以及 Jordan 块的存在性），**与 $k$ 无关**。

## 进展

* $\mathcal D_2$ 的 Jordan 丛、$\mathcal D_3$ 的投影丛已严格化；124 的两处过度简化已更正。
* 分量界 $\binom{s}{2}+3s+1$ 与 $k$ 无关。
* 未做：$K_0$ 截断后的非空性（例如 $E_\lambda\cap K_0$ 可能为 0，某些分量消失）；
  每层的 gcd；$c\ge3$。

## 最终结论

* $c=2$ 的底空间分层由**谱 + 特征线**控制：
  * $\mathcal D_2$：点（不同特征值）、$\operatorname{Gr}(2,E_\lambda)$（标量块）、$J_\lambda$（Jordan 丛）；
  * $\mathcal D_3$：每个特征值一个投影丛（去掉 $\bar A$ 的特征线）；
  * $\mathcal D_4$：开集。
* 每层上 $R$ 是向量丛；lifted incidence 的分量数 $\le\binom{s}{2}+3s+1$，只依赖谱。
* 这把 124 的“粗结构图”补成了可用的分类，并纠正了 Jordan 情形的维数错误。

## 放弃原因

* 没有逐项处理 $K_0$ 截断（哪些分量非空）；
* 没有具体 $c=2$ 实例的精确验证（工具未推广到 $k=4,\omega=2,q=3$）；
* 每层 gcd 未算；$c\ge3$ 未做。

## 残留价值

* $c=2$ 的严格分类与分量界，可支撑论文的“$c=2$”一节。
* 更正了 124 的两处错误（Jordan 丛、$\mathcal D_3$ 的投影丛）。
* 为 $c=2$ 的判定算法（同 123 模板）提供分量表。

## 相关文件

* [attempts/124](124_c2_degeneracy_loci.md)（第一版结构图；本文件补完并更正）
* [attempts/121](121_hyperplane_vector_bundle.md)（$c=1$ 的向量丛定理）
* [attempts/123](123_hyperplane_algorithm.md)（$c=1$ 的判定算法）
* [docs/05 Q9](../../../../docs/05_open_questions.md)（$\mathcal D_s$ 的定位）

## 状态

* 分类：**[已证-纸面，M2]**（$\mathcal D_2/\mathcal D_3/\mathcal D_4$）。
* 分量界：**[已证-纸面，M2]**（$\binom{s}{2}+3s+1$）。
* 未做：$K_0$ 截断、实例验证、每层 gcd、$c\ge3$。
