# $q=4$ 的全部四层排除：16/21 的 $q_{\min}\ge5$

> 2026-11-08。补上 $q=4$ 的 $\omega=1$（$c=3$）与 $\omega=4$（$c=0$）两层，结合 165/172/182/183，
> 得到 **16/21 的 $q=4$ 完全不可行**。状态：**M2（纸面 + 精确计算）**。

## 目标

对 seeds 16/21，排除 $q=4$ 的所有 $\omega\in\{1,2,3,4\}$，从而 $q_{\min}\ge5$。

## 设想与理由

$q=4$ 时 $\omega\in\{1,2,3,4\}$ 四种可能；逐一用已有工具（$W_L$ 约束、行空间判据、$c=1$ 引理）
或简单的行列式论证排除。$\omega=1$ 与 $\omega=4$ 是之前漏掉的两层。

## 做法：四层

| $\omega$ | $c=k-\omega$ | 结论 | 依据 |
|---|---|---|---|
| 1 | 3 | 不可行 | $V\subseteq W_L$，$\dim W_L=2<3$ |
| 2 | 2 | 不可行 | 行空间判据（$b$ 全强制 0）|
| 3 | 1 | 不可行 | 182 非特征线 + 183 特征线（全部秩 1）|
| 4 | 0 | 不可行 | 行列式论证（见下）|

### $\omega=1$（$c=3$）

$H$ 是 $4\times4$ 秩 1，$V=\ker H$ 是 3 维。由 $W_L$ 约束 $V\subseteq W_L$，但两个 seed 的
$\dim W_L=2<3$，矛盾。$\square$

### $\omega=4$（$c=0$）

$H$ 是 $4\times4$ 满秩（$V=0$）。有
$$P(\lambda)=\lambda H-H_A=L(\lambda I-A)N,$$
$\det P(\lambda)$ 是次数 $\le4$ 的多项式，首项系数
$$\det(LN)=\det H\ne0,$$
故 $\deg\det P=4$，在 $\mathbb C$ 上有 4 个根。在任一根 $\lambda_0$ 处 $\operatorname{rank}P(\lambda_0)<4=\omega$，
与 $(5b)$ 矛盾。$\square$

**一般化**：只要 $c=0$（即 $\omega=k=q$，$H$ 满秩），$\det P$ 是 $k$ 次非零多项式，必有根，
故 $c=0$ 层在 $\mathbb C$ 上**恒不可行**。

## 结论

$$\boxed{\text{seeds 16/21 的 } q=4 \text{ 不可行；结合 } q=3 \text{ 不可行，} q_{\min}\ge5.}$$

这是两个实例的**下界**；$q=5$ 及以上未判定。

## 进展

* $q=4$ 的四层全部排除（其中 $\omega=1$ 与 $\omega=4$ 是新增的简单论证）；
* $c=0$ 的恒不可行性是一个可复用的一般结论；
* 16/21 的 $q_{\min}\ge5$。

## 最终结论

* $q_{\min}(16),q_{\min}(21)\ge5$；
* $c=0$ 层对任意 $(q=k)$ 恒不可行；
* $q\ge5$ 的层（$\omega=1..5$，$c=4..0$）未判定。

## 放弃原因

* 未判定 $q=5$ 及以上；
* 未把 $c=0$ 的结论写进一般 $c$ 的界（它会让某些层为空）；
* 未 Lean 化。

## 残留价值

* 两个实例的 $q_{\min}$ 下界从 3 提到 5；
* $c=0$ 恒不可行的简单证明。

## 相关文件

* [attempts/165](165_c2_forced_plane_criterion.md)（$q=3$）
* [attempts/179](../../decision_algorithms/attempts/179_c2_scope.md)（$q=4,\omega=2$）
* [attempts/182](182_c1_infeasibility_lemma.md)、[183](183_c1_eigenlines.md)（$q=4,\omega=3$）

## 状态

* $q=4$ 排除：**[已证-纸面 + 精确计算，M2]**。
* $q\ge5$：**[未做]**。
