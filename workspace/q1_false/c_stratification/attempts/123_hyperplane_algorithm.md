# 超平面情形的判定算法：每个分量一个随机点

> 2026-11-08。把 121 的向量丛分解 + 113 的 genericity 拼成一个**端到端**的判定过程：
> 对固定的 $(q,\omega)$、$k=\omega+1$，分量数 $\le\delta+1$，每个分量取一个随机点算 gcd；
> 全坏分量永远不会被接受，好分量以概率 1 被接受。状态：**M2（算法 + 概率界）**。

## 目标

给定 $(A,C,L_0)$、$q=\omega+1$、$k=\omega+1$（超平面情形），判定：是否存在好的满行秩
$R\in\mathbb C^{m\times n}$（$m=q-r$），即 $(5a)\wedge(5b)$。

## 设想与理由

* 121：lifted incidence 的非空不可约分量 $\le\delta+1$；每个分量是某底片上向量丛的开子集。
* 113：每个不可约分量上，坏集闭；要么全坏，要么好点 Zariski 开稠密。
* 所以：**每个分量取一个随机点**——
  * 若分量全坏，任何点都坏，不会误接受；
  * 若分量有好的开集，随机点以概率 1 落在好集里（坏集是 proper closed）。
* 这是一侧错误（只会假阴性），和 RP 的结构一致。

## 做法

**算法（固定 $(q,\omega)$、$k=\omega+1$）**：

1. 算 $K=\ker[C;CA]$、$N=N_K$、$K_0=\{N\sigma^\top:\sigma E^\top=0,\ \sigma F_0^\top=0\}$、
   $D_A=K\cap A^{-1}K$、$\delta=\dim D_A$。
2. 枚举底片：
   * 特征片：对每个 $\lambda\in\operatorname{spec}(A)$ 且 $K_0\cap\ker(A-\lambda I)\ne0$，取非零
     $v\in K_0\cap\ker(A-\lambda I)$；
   * 非特征开片：取随机 $v\in K_0$，若 $v$ 是特征向量则重取。
3. 对每个底片：
   * 取 $U=\operatorname{span}\{v,Av\}$（$\rho=\dim U\in\{1,2\}$），取 $U^\perp$ 的基；
   * 对 $m$ 行随机取 $R$（每行是 $U^\perp$ 的随机组合）；
   * 检查 $\operatorname{rank}H=\omega$、$\operatorname{rank}[L_0;R]=q$（开条件；失败则重取）；
   * 算 $\lambda H-H_A$ 的全部 $\omega$-子式的 gcd；若 gcd $=1$（常数）则**接受**。
4. 所有片都不接受则**拒绝**。

**正确性**：由 121，每个点落在某个分量；由 113，分量上坏集闭。若存在好分量，随机点以概率 1
落在其好开集；若所有分量全坏，任何点都坏，算法不接受。故**永不假阳性**，只有假阴性。

**概率界**：在好分量上，坏集是 proper closed；若用大小 $N$ 的有理网格抽样，由 Schwartz–Zippel，
假阴性概率 $\le D/N$，其中 $D$ 是坏集定义多项式的次数上界（$\omega$-子式的次数 $\le\omega$，
故 $D\le\omega$ 量级；精确常数可写）。取 $N=2D$ 即 $\le1/2$；重复 $T$ 次得 $\le2^{-T}$。

**复杂度**：分量数 $\le\delta+1$；每片一次 gcd（$\omega$-子式，$(m+1)\times k$ 的 1 次多项式矩阵），
用矩形 Hermite/行列式因子（[attempts/106](106_rectangular_determinantal_divisor.md)）多项式时间；
总复杂度是“$(\delta+1)\times$ gcd”的多项式。

## 进展

* 算法框架与正确性已写；概率界是标准的 Schwartz–Zippel。
* 对 104/109 的 $d=1$ 族：开片（非特征）全坏，特征点好——算法会在特征片接受，
  与 104 的“开层坏、例外点好”一致。
* 对 110 的 138（$U_0=0$）：特征点全坏（两个特征点），算法在 $q=3,\omega=2$ 拒绝；
  但 $q_{\min}=2$（$\omega=1$ 层），所以完整 DEC 要对 $\omega$ 取并。
* 对 116 的 $e=1$：1081/1327/1491 有好点（特征片），算法接受；753 全坏，拒绝。

## 最终结论

* 超平面情形（$k=\omega+1$）有一个**端到端的一侧随机算法**：分量数 $\le\delta+1$，
  每分量一个随机点 + gcd；永不假阳性，假阴性 $\le2^{-T}$。
* 这是目前对一般 $k=\omega+1$ 最完整的判定过程；它把 121（分量）、113（genericity）、
  106（gcd）三块接起来了。
* 完整 DEC(q) 还要对 $\omega=0,\dots,q$ 取并；实点问题另算；$c>1$ 不覆盖。

## 放弃原因

* 不是确定性算法；没有 derandomization。
* 只覆盖 $k=\omega+1$；$c>1$ 的 Grassmannian 情形未做。
* 实点（实输入）未处理；复数判定不等于实可行性。
* 每片的 gcd 仍要符号/精确计算，复杂度未逐项优化。

## 残留价值

* 第一个把“分量分解 + genericity + gcd”接成可执行判定的版本。
* 分量数 $\le\delta+1$ 让算法只跑常数多片，不是逐 $k$ 枚举。
* 为论文的“算法”一节与 $c=2$ 的推广提供模板。

## 相关文件

* [attempts/121](121_hyperplane_vector_bundle.md)（分量定理）
* [attempts/113](../../decision_algorithms/attempts/113_projective_theorem_corrected.md)（genericity）
* [attempts/106](106_rectangular_determinantal_divisor.md)（gcd/矩形 Hermite）
* [attempts/104](104_p2_constrained_locus.md)（$d=1$ 例子）
* [attempts/110](110_d2_all_bad_example.md)（$d=2$ 例子）

## 状态

* 算法：**[M2，纸面 + 概率界]**。
* 正确性：一侧（无假阳性）；假阴性 $\le2^{-T}$。
* 未做：确定性版本、$c>1$、实点、复杂度优化。
