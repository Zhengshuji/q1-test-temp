# $c=2$ 的第一层：$\mathcal D_2/\mathcal D_3/\mathcal D_4$ 的结构

> 2026-11-08。按专家 54 号的 Priority 4，开始 $c=k-\omega=2$。底空间是
> $\operatorname{Gr}(2,K_0)$，$\rho(V)=\dim(V+AV)\in\{2,3,4\}$；
> 分量问题化成 $\mathcal D_s=\{V:\rho(V)\le s\}$。本文件给出三层的**结构分类**与分量界。
> 状态：**M2（纸面草稿）**；$A$-不变子空间的 Jordan 细节与具体实例验证未做完。
>
> **更正/补完见 [attempts/125](125_c2_structure_complete.md)**：$\mathcal D_2$ 的 Jordan 情形是丛
> $J_\lambda$（不是点）；$\mathcal D_3$ 每个特征值一个投影丛（不是“特征线 $\times$ 特征值”的散点）。
> 本文件保留作第一版结构图。

## 目标

设 $c=k-\omega=2$，$V\subseteq K_0$、$\dim V=2$。证明/描述：

1. $\mathcal D_2=\{V:AV\subseteq V\}$（$A$-不变 2-子空间）的分量；
2. $\mathcal D_3=\{V:\dim(V+AV)=3\}$（含一条不变线）的结构；
3. $\mathcal D_4$（开集）的不可约性；
4. 每层上 $R$ 的向量丛与 lifted incidence 的分量界。

## 设想与理由

* $\dim(V+AV)=2c-\dim(V\cap A^{-1}V)=4-\dim(V\cap A^{-1}V)$，故
  $$\rho=2\iff V\cap A^{-1}V=V\iff AV\subseteq V,$$
  $$\rho=3\iff\dim(V\cap A^{-1}V)=1,$$
  $$\rho=4\iff V\cap A^{-1}V=0.$$
* $\rho=2$ 是“$V$ 不变”，由 $A|_V$ 的谱型分类；
* $\rho=3$ 是“$V$ 含一条不变线”，由那条特征线与商上的 operator 分类；
* $\rho=4$ 是开条件，补集是闭的，故 $\mathcal D_4$ 是开集（若非空则不可约）。
* 每层上 $R$ 的约束是 $RV=0,RAV=0$，即每行落在 $(V+AV)^\perp$；$\rho$ 常值时是向量丛。

## 做法

### 1. $\mathcal D_2$：$A$-不变 2-子空间

设 $V$ 是 2 维 $A$-不变子空间，$B=A|_V$（2×2）。按 $B$ 的谱型：

* **两个不同特征值** $\lambda\ne\mu$：$V$ 由一条 $\lambda$-特征线和一条 $\mu$-特征线张成；
  对每对 $(\lambda,\mu)$ 至多一个这样的 $V$（若两条特征线都在 $K_0$ 里）。**点分量**。
* **重特征值 $\lambda$，$B=\lambda I$**：$V\subseteq\ker(A-\lambda I)=:E_\lambda$；
  所有这样的 $V$ 构成 $\operatorname{Gr}(2,E_\lambda\cap K_0)$。**Grassmannian 分量**（若 $\dim(E_\lambda\cap K_0)\ge2$）。
* **重特征值 $\lambda$，$B$ 是非平凡 Jordan 块**：$V$ 由一条广义特征向量链 $\{e_1,e_2\}$ 张成
  （$(A-\lambda I)e_1=0$、$(A-\lambda I)e_2=e_1$）；对每个 Jordan 块至多一个这样的 $V$（若在 $K_0$ 里）。
  **点分量**（多个块时需按块组合，见“未做”）。

所以 $\mathcal D_2$ 的分量数 $\le\binom{s}{2}+s_2$，其中 $s$ 是不同特征值个数、$s_2$ 是重特征值个数；
与 $k$ 无关。

### 2. $\mathcal D_3$：含一条不变线的 $V$

设 $L=\langle u\rangle$ 是特征线，$Au=\lambda u$。写 $V=L\oplus\langle w\rangle$，则
$$AV=L\oplus\langle Aw\rangle\subseteq V\iff Aw=\alpha u+\beta w\ \text{for some }\alpha,\beta.$$
* 若 $\beta\ne0$：$(A-\beta I)w=\alpha u$，即 $w$ 是 $A$ 关于 $\beta$ 的广义特征向量，
  且 $(A-\beta I)w\in L$。对固定的 $(L,\beta)$，满足此式的 $w$ 构成一个仿射空间
  （$ (A-\beta I)^{-1}L $ 模 $L$ 的原像）；$V$ 由 $w\bmod L$ 决定。
  所以分量是**以特征线 $L$ 为底、以该仿射空间为纤维的丛**。
* 若 $\beta=0$：$Aw\in L$，即 $w\in A^{-1}L$；同样是以 $L$ 为底的丛。

分量按 $(\text{特征线 }L,\ \beta\in\operatorname{spec}(A))$ 索引；
特征线本身是 $\mathbb P(E_\lambda\cap K_0)$（射影线性子空间），故**至多**
$$\#\{\text{特征线}\}\times\#\{\text{特征值}\}$$
个分量，有限且与 $k$ 无关（$\le(\sum_\lambda\dim E_\lambda)\cdot s$）。

### 3. $\mathcal D_4$：开集

$\mathcal D_4=\operatorname{Gr}(2,K_0)\setminus(\mathcal D_2\cup\mathcal D_3)$ 是开集；
若 $\operatorname{Gr}(2,K_0)$ 不可约（它总是不可约），非空开集不可约。**一个分量**（若非空）。

### 4. $R$ 的向量丛与 lifted incidence

固定一层，$\rho=\rho(V)$ 常值。每行的约束是 $r\in(V+AV)^\perp$，维数 $n-\rho$；$m$ 行共
$m(n-\rho)$ 维，构成向量丛。$\operatorname{rank}H=\omega$ 与 $\operatorname{rank}[L_0;R]=q$ 是开条件。
故 lifted incidence 在该层上是不可约向量丛的开子集；非空即不可约。
总分量数 $\le\#\mathcal D_2+\#\mathcal D_3+1$，即
$$\boxed{\ \le\binom{s}{2}+s_2+\#\{\text{特征线}\}\cdot s+1\ }$$
（粗界；$s$=不同特征值个数），**与 $k$ 无关**。

## 进展

* $\mathcal D_2/\mathcal D_3/\mathcal D_4$ 的结构已写出；分量界是“谱的函数”，不是 $k$ 的函数。
* $R$ 的向量丛论证与 121 同型（把 $\operatorname{span}\{v,Av\}$ 换成 $V+AV$）。
* 未做：Jordan 多块的组合（$\mathcal D_2$ 的第三种情形）；$\mathcal D_3$ 的仿射纤维的精确维数；
  具体 $c=2$ 实例的枚举验证（工具要从 $k=3$ 推广到 $k=4$）；每层 gcd。

## 最终结论

* $c=2$ 的底空间分层由**谱**控制：不变 2-子空间（点或 $\operatorname{Gr}(2,E_\lambda)$）、
  含不变线的 2-子空间（特征线 $\times$ 特征值）、开集。
* 分量数有限，界只依赖 $A$ 在 $K_0$ 上的特征结构，与 $k$ 无关；每层上 $R$ 是向量丛。
* 这把 $c=2$ 的分量问题从“任意 determinantal variety”降到“谱 + 特征线”，与 $c=1$ 的
  特征向量分解同型。

## 放弃原因

* $\mathcal D_2$ 的 Jordan 多块情形只给了单块；多块组合未分类。
* $\mathcal D_3$ 的仿射纤维维数没有逐项写；$\beta$ 与 $\lambda$ 的关系（何时非空）未细究。
* 没有具体 $c=2$ 实例的数值/精确验证。

## 残留价值

* $c=2$ 的第一张结构图：$\mathcal D_2$（谱）/$\mathcal D_3$（特征线）/$\mathcal D_4$（开）。
* 分量界与 $k$ 无关，延续 121 的“谱控制分量”思想。
* 为 $c=2$ 的判定算法（同 123 的模板）提供分量表。

## 相关文件

* [attempts/121](121_hyperplane_vector_bundle.md)（$c=1$ 的向量丛定理）
* [attempts/123](123_hyperplane_algorithm.md)（$c=1$ 的判定算法）
* [attempts/113](../../decision_algorithms/attempts/113_projective_theorem_corrected.md)（一般定理）
* [attempts/115](115_k3_component_decomposition.md)（determinantal 框架）
* [docs/05 Q9](../../../../docs/05_open_questions.md)（$\mathcal D_s$ 的定位）

## 状态

* $\mathcal D_2/\mathcal D_3/\mathcal D_4$ 结构：**[草稿，M2]**。
* 分量界：**[草稿，M2]**（粗界，谱的函数）。
* 未做：Jordan 多块、仿射纤维维数、具体实例验证、每层 gcd。
