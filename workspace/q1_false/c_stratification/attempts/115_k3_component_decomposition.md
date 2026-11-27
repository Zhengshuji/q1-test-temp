# $k=3$ 的秩层：一般线性性不成立（撤回）

> 2026-11-08。专家 53 号给出反例，**撤回**"$k=3,e=0$ 时秩层 = 不可约分量"的一般断言。
> 保留正确的 $\operatorname{rank}Q$ 公式与五个实例的逐实例表；把 stacked rank 改述为 **determinantal**。
> 状态：一般断言 **[撤回]**；实例表 **[精确验证]**。

## 目标

1. 记录撤回与反例；
2. 保留正确的部分（$\operatorname{rank}Q$ 的线性公式、112 的逐实例数据）；
3. 给出正确的替代陈述（代数性，不是不可约性）。

## 设想与理由

* 旧证明只用了
  $$\operatorname{rank}Q=\operatorname{rank}Z_2-\dim(\operatorname{im}Z_2\cap\operatorname{span}\{\sigma\})$$
  的线性性，然后**错误地假设** $\operatorname{rank}[P;Q]$ 也由两个独立的交维数决定。
* 专家 53 号的反例说明：两个交维数可以恒定，而 stacked rank 跳变——因为两个 $\sigma$ 必须来自**同一个**
  定义域向量（common preimage），这是特征向量条件，不是线性条件。

## 做法

**反例（专家 53 号）**：$k=3$，
$$Z_1=\begin{pmatrix}1&0\\0&1\\0&0\end{pmatrix},\qquad
Z_2=\begin{pmatrix}1&0\\0&2\\0&0\end{pmatrix}.$$
$\operatorname{im}Z_1=\operatorname{im}Z_2=U=\langle e_1,e_2\rangle$。对 $\sigma\in U$，
$$\dim(\operatorname{im}Z_1\cap\operatorname{span}\sigma)=\dim(\operatorname{im}Z_2\cap\operatorname{span}\sigma)=1$$
恒成立；但
$$\operatorname{rank}\begin{bmatrix}P\\Q\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}Z_1\\Z_2\end{bmatrix}
-\dim\Big(\operatorname{im}\begin{bmatrix}Z_1\\Z_2\end{bmatrix}\cap(\operatorname{span}\sigma\oplus\operatorname{span}\sigma)\Big).$$
共同原像存在 $\iff$ $T(s_1,s_2)^\top=\mu(s_1,s_2)^\top$，$T=\operatorname{diag}(1,2)$；
故只在两个特征向量 $[1:0]$、$[0:1]$ 处堆叠秩为 $1$，其余为 $2$。
所以 rank-$(1,1)$ 层是**两个点**，可约。

**正确的替代陈述**：
* $\operatorname{rank}Q$ 层由线性入射条件 $[\sigma]\in\mathbb P(\operatorname{im}Z_2)$ 控制；
* stacked-rank 层是 $M(\sigma)=\begin{bmatrix}B(\sigma)^\top Z_1\\B(\sigma)^\top Z_2\end{bmatrix}$ 的
  **determinantal locus**（全部 $(s+1)$-子式为零），是局部闭代数集，但**不必线性、不必不可约**；
* $e>0$ 时还要加 $\operatorname{rank}(\varphi_S|_{\widetilde E_S})$，因为
  $\dim(\widetilde E_S\cap X_S)=e-\operatorname{rank}(\varphi_S|_{\widetilde E_S})$；
* $k>3$ 时 $\operatorname{rank}Q=\operatorname{rank}Z_2-\dim(\operatorname{im}Z_2\cap T)$（$T$ 是 $S$ 的零化子），
  stacked 部分仍是 coupled 的 degeneracy locus，不是单个 Schubert 条件。

**引用**：Bruns–Vetter, *Determinantal Rings*；Fulton, *Intersection Theory* Ch. 14（degeneracy loci / Thom–Porteous）；
Fulton, *Young Tableaux* Ch. 9–10（Schubert）；Hartshorne II.3.19（Chevalley）。

## 进展

* 撤回已记录；反例已核对（$T=\operatorname{diag}(1,2)$ 的两个特征向量）。
* 112 的五个实例表**仍是逐实例精确数据**；每一行可能仍然正确，但旧的一般证明不再成立，
  需要逐实例直接计算（112 的枚举 + 104 的符号 gcd 就是这种逐例证据）。
* 正确的通用结论只有：秩层是**局部闭代数集**（determinantal），不是"射影子空间/开集"。

## 最终结论

* **一般断言撤回**：$k=3,e=0$ 时秩层**不一定**是不可约分量；反例给出可约的 rank-$(1,1)$ 层。
* 保留：$\operatorname{rank}Q$ 的线性公式、112 的逐实例表、$e>0$ 的秩指标、$k>3$ 的 Schubert 类比。
* 这条撤回直接影响 113：定理只能是 determinantal stratification，不能声称一般线性/不可约。

## 放弃原因

* 没有一般不可约分解；反例说明它本来就不成立。
* 112 的表没有逐行重算"不可约性"；只保留了枚举证据。

## 残留价值

* 一个清晰的反例，说明"两个独立交维数"不足以决定 stacked rank。
* 正确的 determinantal 框架与引用。
* 保留了 112 的逐实例数据（作为例子，不是定理）。

## 相关文件

* [attempts/112](112_incidence_table.md)（逐实例表）
* [attempts/113](../../decision_algorithms/attempts/113_projective_theorem_corrected.md)（改为 determinantal stratification）
* [attempts/114](114_lifting_lemma.md)（lifting）
* [attempts/104](104_p2_constrained_locus.md)（$d=1$ 的符号 gcd）

## 状态

* 一般断言：**[撤回]**（专家 53 号反例）。
* 逐实例表：**[精确验证 5 实例]**，不是一般定理。
* 正确框架：determinantal stratification（局部闭代数集）；不可约分量需逐例/一般理论。
