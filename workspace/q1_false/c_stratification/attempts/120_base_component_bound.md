# $k=\omega+1$、$d=2$：底空间分量个数的常数上界

> 2026-11-08。Q9 第一项的第一小步：对 $k=\omega+1$、$d=2$，证明**底空间**（$\sigma$-空间）的秩层
> 只有**常数个**不可约分量，与 $k$ 无关。总量 incidence 空间的纤维分量另计（未证）。
> 状态：**M2（纸面）**。

## 目标

设 $k=\omega+1$、$q=\omega+1$、$d=2$，$Z_1,Z_2\in\mathbb C^{k\times2}$。证明：底空间
$\mathbb P((E+F_0)^\perp)$ 上按
$$\big(\operatorname{rank}Q,\ \operatorname{rank}[P;Q]\big)$$
分层的不可约分量个数有一个**与 $k$ 无关的常数上界**。

## 设想与理由

* $B^\top:\mathbb C^k\to\mathbb C^\omega$ 的核是 $\operatorname{span}\{\sigma\}$，所以
  $$\operatorname{rank}Q=\operatorname{rank}Z_2-\dim(\operatorname{im}Z_2\cap\operatorname{span}\{\sigma\}),$$
  只依赖 $\sigma$ 是否落在固定子空间 $U_2=\operatorname{im}Z_2$ 里——线性条件。
* 堆叠秩：令 $W=\operatorname{im}\begin{bmatrix}Z_1\\Z_2\end{bmatrix}\subseteq\mathbb C^k\oplus\mathbb C^k$，
  $$\operatorname{rank}\begin{bmatrix}P\\Q\end{bmatrix}=\operatorname{rank}W-\dim\big(W\cap(\operatorname{span}\sigma\oplus\operatorname{span}\sigma)\big).$$
  $d=2$ 时 $W$ 的维数 $\le4$；$\Delta_\sigma=\operatorname{span}\sigma\oplus\operatorname{span}\sigma$ 是 2 维。
  “$\dim(W\cap\Delta_\sigma)\ge1$”是 $\Delta_\sigma\to(\mathbb C^k\oplus\mathbb C^k)/W$ 的核非零，
  即某个 $2\times(\operatorname{codim})$ 矩阵的**全部 $2\times2$ 子式为零**——$\sigma$ 的**二次**条件。
* 所以秩元组只依赖：$\dim(U_1\cap\operatorname{span}\sigma)$、$\dim(U_2\cap\operatorname{span}\sigma)$、
  以及上面那个二次条件；前者是线性条件，后者是二次曲面（在 $\mathbb P^{k-1}$ 中至多 2 个不可约分量）。

## 做法

**引理 1**：$\operatorname{rank}Q$ 由 $\dim(U_2\cap\operatorname{span}\sigma)\in\{0,1,2\}$ 决定；
固定这个维数的 locus 是“$\sigma$ 在某个子空间 $V$ 中且不在更小子空间 $V'$ 中”，是射影子空间之差，不可约。

**引理 2**：$\operatorname{rank}[P;Q]$ 由 $\dim(W\cap\Delta_\sigma)\in\{0,1,2\}$ 决定；
条件 $\dim(W\cap\Delta_\sigma)\ge1$ 是 $\sigma$ 的二次方程（所有 $2\times2$ 子式为零），
在 $\mathbb P^{k-1}$ 中是一个二次超曲面，至多 2 个不可约分量（若可约则为两张超平面）。
条件 $\dim\ge2$ 更强，是线性条件（存在两个独立向量）。

**定理（底空间常数界）**：底空间的秩层不可约分量个数 $\le 2^3\cdot2=16$（粗界），与 $k$ 无关。

*证明*：秩元组由三个“$\dim\ge s$”条件决定（$U_1$、$U_2$、$W\cap\Delta$）；
每个是线性或二次条件；布尔组合至多 $2^3$ 种，二次条件至多 2 个分量。$\square$

**与 $k=3$ 的例子核对**：$d=1$ 时 $\operatorname{rank}Z_2=1$，$U_2$ 是一维，$\operatorname{rank}Q$ 的跳变是一个点；
$d=2$ 的 138/261 也只有线/开集/点——都远小于 16。

## 进展

* 底空间的常数上界已证（$\le16$，粗界）。
* **总量 incidence 空间**：每个底分量上的纤维是仿射空间，被 $\operatorname{rank}H=\omega$、
  $\ker H\subseteq\ker H_A$、$\operatorname{row}H=S$ 切割；这些纤维的不可约分量个数**未界定**，
  可能依赖 $\omega$。所以本文件只给“底空间”的界。
* 这个界已经说明：**底空间的 k-枚举没有必要**；需要小心的是纤维。

## 最终结论

* $k=\omega+1,d=2$ 时，底空间的秩层分量个数 $\le16$，与 $k$ 无关。
* 总量 incidence 空间的分量界仍未解决；它依赖纤维上的秩条件，是 Q9 的真正难点。
* 这符合 Q9 的定位：结构是常数/多项式的，难点在纤维与 gcd。

## 放弃原因

* 只证了底空间；纤维的 $\operatorname{rank}H=\omega$ 条件可能把分量数增大。
* 16 是粗界，没有优化；也没有处理 $e>0$ 的 $\widetilde E_S$ 条件（它是线性/秩条件，可加进同一框架）。

## 残留价值

* 一个与 $k$ 无关的底空间界，直接回应“不能逐 $k$ 枚举”。
* 把难点定位到纤维（$\operatorname{rank}H=\omega$ 的 determinantal 条件），这是 Q9 的下一步。
* 引理 1/2 可复用到任意 $d$（把 2 换成 $d$，二次换成 $d$ 次）。

## 相关文件

* [docs/05 Q9](../../../../docs/05_open_questions.md)（分量分解复杂度）
* [attempts/112](112_incidence_table.md)（$k=3$ 例子）
* [attempts/118](118_k_omega_plus_1_d2_attempt.md)（$k>3$ 充分定理）
* [attempts/113](../../decision_algorithms/attempts/113_projective_theorem_corrected.md)（一般定理）

## 状态

* 底空间常数界：**[已证-纸面，M2]**（$\le16$，粗界）。
* 总量 incidence 空间：**[开放]**（纤维的 rank H 条件）。
* 未做：优化界；$e>0$；$d>2$ 的对应界。
