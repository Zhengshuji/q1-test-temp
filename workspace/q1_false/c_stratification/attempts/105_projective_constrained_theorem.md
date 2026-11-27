# $k=\omega+1$ 的投影约束定理（草稿）

> 2026-11-08。落实专家 51 号答复的"下一目标"：$k=\omega+1$ 的投影约束定理。
> 本文件是**定理陈述 + 证明骨架**；完整的分量分解与算法未做。状态：M2（纸面草稿，待专家复核）。

## 目标

固定数据 $(A,C,L_0)$、$q=\omega+1$、$k=\omega+1$（故 $\operatorname{Gr}(\omega,k)=\mathbb P^{k-1}$）。
把 $S$ 写成超平面 $\ker\sigma$，$\sigma\in\mathbb P^{k-1}$。目标是：

> **定理（目标）**：在 incidence 空间（$\sigma$ + 兼容对）上按"兼容映射的秩 / $\dim X_S$ /
> $\dim(E+X_S)$ / $\operatorname{rank}L$"分层；每个常秩层的每个不可约分量上，坏谱集**闭**，
> 故要么整分量全坏、要么好点 Zariski 开稠密；由该分量函数域上的 **generic determinant divisor** 判定。

## 设想与理由

* 专家 51 号：先做 incidence 空间的分层，不要先分类投影到 $R$-空间的分量；$\rho$ 只是第一个不变量。
* 在常秩层上，$\dim X_S$、$\dim(E+X_S)$、兼容映射的秩都是常数；这些条件把 incidence 空间分成
  有限个**局部闭**层（每层由若干秩等式/不等式定义）。
* 每层上，坏谱集是"$\exists\lambda$ 使某个 $\omega$-子式为零"的投影；用齐次化到 $\mathbb P^1$ + 真映射，
  投影闭（B.24 闭性定理的逐层版本）。
* 层不可约 + 坏集闭 ⟹ 二分；generic gcd 判定（B.24 定理 A 的逐层版本）。

## 做法

**Incidence 空间**：
$$\mathcal I=\Big\{(\sigma,\ x_1,\dots,x_m,\ y_1,\dots,y_m):\ \sigma\in\mathbb P^{k-1},\ x_i,y_i\in S_\sigma,\ 
x_iZ_1+y_iZ_2=0,\ \operatorname{rank}H=2,\ \ker H\subseteq\ker H_A\Big\},$$
其中 $H=[U_0;x_1;\dots;x_m]$、$H_A=[V_0;y_1;\dots;y_m]$。

**分层数据**（每项在 $\mathcal I$ 上局部常值/局部闭）：
1. $r_{\rm comp}=\operatorname{rank}$ 的兼容映射 $(x,y)\mapsto xZ_1+yZ_2$；
2. $x_S=\dim X_S$；
3. $e_S=\dim(E+X_S)$；
4. $\operatorname{rank}L$（full-row-rank 是开条件，单独一层）。

**定理（草稿）**：固定一个常秩层 $\mathcal I_\alpha$，设 $X\subseteq\mathcal I_\alpha$ 是不可约分量。
则
$$\text{要么 }X\subseteq\mathcal B,\qquad\text{要么 }X\setminus\mathcal B\ \text{非空 Zariski 开稠密},$$
其中 $\mathcal B$ 是"某 $\lambda$ 处铅笔秩 $<2$"的集合；两案由 $\mathbb C(X)$ 上
$\gcd_\lambda\{2\text{-子式}\}$ 是否为常数判定。

*证明骨架*：在常秩层上，$\sigma$ 与 $(x,y)$ 的约束都是多项式等式/不等式；坏集是
$\{(\sigma,x,y,\lambda):\text{全部 }2\text{-子式}=0\}$ 到 $X$ 的投影。齐次化 $\lambda\in\mathbb P^1$，
$[1:0]$ 处由 $\operatorname{rank}H=2$ 排除，投影真 ⟹ 像闭。$X$ 不可约 ⟹ 闭集要么全 $X$、要么补开稠密。
generic gcd 的判定与 B.24 定理 A 同。$\square$

## 进展

* 定理陈述与证明骨架已写；**部分**：开层 generic gcd 已算出（attempts/104：gcd $=\lambda t$，$t\ne0$），
  例外点已完见证（显式 $R$）；**未做**：一般分层的参数化、其它层的 gcd、$k-\omega>1$ 的归纳。
* **一个测试例**（attempts/104）：$k=3,\omega=2,q=3$ 的实例，$\mathbb P^1$ 可容许轨迹分成两层：
  * 开层（$\sigma\ne(1,0,0)$）：$y$ 被限制在 $\langle V_0\rangle$，公共 $\lambda_0=0$ 使整层全坏；
  * 例外点（$\sigma=(1,0,0)$）：$y$ 在 $S$ 中 2 维自由，显式好点（gcd $=1$）。
  这正好说明：**同一 $\mathbb P^1$ 的不同秩层可以一坏一好**；不按秩分层就会得出错误结论。

## 最终结论

* 投影约束定理的**结构部分**（分层 + 逐层二分 + generic gcd）是 B.24 闭性/定理 A 的直接逐层化；
  新内容是"把兼容秩/纤维维数放进分层"。
* **算法部分**：已有第一个实例——开层 gcd $=\lambda t$（符号证书）、例外点完见证（显式 $R$）；
  一般分层的参数化、其它层的 gcd、$k-\omega>1$ 的归纳仍未做。
* 硬度仍推迟（专家 51 号）。

## 放弃原因

* 没有把定理写成"可判定判据"：分层是集合层面的，尚未给出每层的多项式参数化。
* 没有证明分层的有限性（虽然秩只有有限个取值，但 incidence 空间的连通性/不可约性未逐一处理）。

## 残留价值

* 一个清晰的定理骨架 + 一个反例式的测试（同一 $\mathbb P^1$ 一坏一好），可直接寄专家复核。
* 把专家 51 号的"incidence 分层"建议落成了可写的命题。
* 为 $k-\omega=d>1$ 的归纳提供了正确的分层语言（不是 $\mathbb P^1$-丛的朴素剥皮）。

## 相关文件

* [attempts/104](104_p2_constrained_locus.md)（$\mathbb P^1$ 测试例：开层全坏、例外点好）
* [proof/B.24/README.md](../../../../proof/B.24/README.md)（闭性定理、定理 A、块判据）
* [workspace/ROADMAP.md](../../../ROADMAP.md) §5（专家 51 号优先级）

## 状态

* 定理：**[草稿，M2]**；结构部分依赖 B.24 闭性/定理 A（M3）；算法部分是新的、部分完成（104 开层 gcd + 例外点）。
* 测试例：attempts/104（开层 gcd $=\lambda t$；例外点显式好 $R$）。
* 下一步：一般分层参数化；其它层的 gcd。
