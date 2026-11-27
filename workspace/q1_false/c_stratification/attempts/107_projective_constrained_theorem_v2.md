# $k=\omega+1$ 投影约束定理：写实版

> **修正版见 [attempts/113](../../decision_algorithms/attempts/113_projective_theorem_corrected.md)**：admissibility 用 (4.2)，
> 底空间是 $\mathbb P((E+F_0)^\perp)$，genericity 作用在总 incidence 空间。本文件保留旧稿以记录修正过程。
>
> 2026-11-08。把 attempts/105 的骨架写成可检查的定理陈述 + 证明骨架，并以
> attempts/104 的 $\mathbb P^1$ 例作为实例化。状态：**M2（纸面草稿）**；结构部分依赖 B.24 的闭性/定理 A，
> 分层与算法部分是新的、未复核。

## 目标

固定数据 $(A,C,L_0)$，$q=\omega+1$，$k=\omega+1$，$m=q-r$。把 $S$ 写成超平面
$S_\sigma=\ker\sigma$，$\sigma\in\mathbb P^{k-1}$。目标是：

> **定理（投影约束纤维）**：incidence 空间
> $$\mathcal I=\{(\sigma,x_1,\dots,x_m,y_1,\dots,y_m):\ x_i,y_i\in S_\sigma,\ 
> x_iZ_1+y_iZ_2=0,\ \operatorname{rank}H=\omega,\ \ker H\subseteq\ker H_A\}$$
> 可分成**有限个局部闭层**，每层上 rank 数据（$\operatorname{rank}(B^\top Z_1)$、
> $\operatorname{rank}(B^\top Z_2)$、$\operatorname{rank}[B^\top Z_1;B^\top Z_2]$、$\dim X_S$、
> $\dim(E+X_S)$、$\operatorname{rank}L$）为常数；每层的每个不可约分量 $Z$ 上，坏谱集
> $$\mathcal B_Z=\{(\sigma,x,y)\in Z:\exists\lambda,\ \operatorname{rank}(\lambda H-H_A)<\omega\}$$
> 在 $Z$ 中**闭**。于是要么 $Z\subseteq\mathcal B_Z$（整分量全坏），要么 $Z\setminus\mathcal B_Z$ 非空
> Zariski 开稠密（好点开稠密）。两案由 $\mathbb C(Z)$ 上 $\omega$-子式的 **generic determinant divisor**
> $\Delta_Z(\lambda)$ 判定：$\Delta_Z$ 非常数 $\iff Z\subseteq\mathcal B_Z$；$\Delta_Z$ 是单位 $\iff$ 好点开稠密。

## 设想与理由

* 专家 51 号：先做 incidence 空间的**秩分层**，不要先分类投影到 $R$-空间的分量；$\rho$ 只是第一个不变量。
* 在常秩层上，$\dim X_S$、$\dim(E+X_S)$、兼容映射的秩都是常数；这些条件把 $\mathcal I$ 分成有限个
  **局部闭**层（每层由若干秩等式/不等式定义）。
* 每层上，坏谱集是"$\exists\lambda$ 使某个 $\omega$-子式为零"的投影；用齐次化到 $\mathbb P^1$ + 真映射，
  投影闭（B.24 闭性定理的逐层版本）。
* 层不可约 + 坏集闭 ⟹ 二分；generic gcd 判定（B.24 定理 A 的逐层版本）。

## 做法

**1. 坐标与矩阵。** 取 $S_\sigma$ 的基 $B$（$k\times2$，列），$x=aB^\top$、$y=bB^\top$（$a,b\in\mathbb C^2$）。
兼容条件写成
$$aP+bQ=0,\qquad P=B^\top Z_1,\ Q=B^\top Z_2\quad(2\times d).$$
$X_S=\{a:\exists b,\ aP+bQ=0\}$；其维数由 $\operatorname{rank}Q$ 与
$\operatorname{row}(P)\subseteq\operatorname{row}(Q)$ 决定。$E\subseteq S_\sigma$、$F_0\subseteq S_\sigma$
是 $\sigma$ 的线性条件；$E+X_S=S_\sigma$、$\operatorname{rank}H=\omega$ 是 $\sigma$ 与 $(x,y)$ 的多项式条件。

**2. 分层。** 令 $\mathcal I$ 按元组
$$\big(\operatorname{rank}P,\ \operatorname{rank}Q,\ \operatorname{rank}[P;Q],\ \dim X_S,\ 
\dim(E+X_S),\ \operatorname{rank}L\big)$$
分层。每个分量由 $\sigma$ 与 $(x,y)$ 的**确定性秩条件**定义，故是局部闭的；秩只取有限个值，故分层有限。
在每个常秩层上，$X_S$ 的维数与 $E+X_S$ 的维数不变。

**3. 闭性。** 固定常秩层 $Z$。把 $\lambda$ 齐次化到 $\mathbb P^1$，考虑
$$\mathcal W=\{(\sigma,x,y,[\lambda_0:\lambda_1])\in Z\times\mathbb P^1:\ 
\text{全部 }\omega\text{-子式 of }(\lambda_0H-\lambda_1H_A)\text{ 为零}\}.$$
$\mathcal W$ 是闭的。在 $\lambda_1=0$（无穷远）处，$\lambda_0H-\lambda_1H_A=\lambda_0H$，其秩
$=\operatorname{rank}H=\omega$，故 $\mathcal W$ 与无穷远纤维不交。投影 $\pi:\mathcal W\to Z$ 是紧合映射
（$\mathbb P^1$ 紧合）的复合，故像 $\mathcal B_Z$ 闭。$\square$

**4. 二分与 gcd。** 设 $Z$ 不可约。闭集 $\mathcal B_Z$ 要么 $=Z$，要么是 $Z$ 的真闭子集；后者补集非空
Zariski 开稠密。在函数域 $\mathbb C(Z)$ 上，$\Delta_Z(\lambda)=\gcd$ 全部 $\omega$-子式；
$\Delta_Z$ 非常数 $\iff$ 一般点有公共根 $\iff Z\subseteq\mathcal B_Z$；$\Delta_Z$ 是单位 $\iff$ 一般点无公共根
$\iff$ 好点开稠密。$\square$

**5. $k=3,\omega=2,q=3$ 的显式分层。** 此时 $\sigma\in\mathbb P^2$，$P,Q$ 是 $2\times1$（向量 $p,q$）。
分层由 $q=0$ 与否、$p=0$ 与否、$E\subseteq S_\sigma$、$F_0\subseteq S_\sigma$、$E+X_S=S_\sigma$ 决定：
* 开层 $q\ne0$：$X_S=\mathbb C^2$，$E+X_S=S_\sigma$ 自动；
* 层 $q=0,p\ne0$：$X_S$ 是一条线；$E+X_S=S_\sigma$ 需 $E$ 不在这条线里（若 $E=0$ 则不可容许）；
* 层 $q=0,p=0$：$X_S=\mathbb C^2$，但 $q=0$ 是 $\sigma$ 的线性条件（通常是点或线）。
每层是 $\mathbb P^2$ 的局部闭子集（点/线/开集），故分层有限、每层不可约分量的 gcd 可算。

**6. 实例化（attempts/104）。** 数据 $U_0=0$、$V_0=(0,-1,-4)$、$Z_1=0$、$Z_2=e_1$、$d=1$。
$p=0$；$q=B^\top e_1$。$q=0\iff e_1\in\operatorname{span}\sigma\iff\sigma=(1,0,0)$。
故分层只有两个：
* 开层 $\sigma\ne(1,0,0)$（$q\ne0$）：符号 gcd $=\lambda t$，$t\ne0$ 即 $\lambda$ ⟹ **全坏**；
* 点 $\sigma=(1,0,0)$（$q=0$）：gcd $=1$ ⟹ **好点**（显式 $R$ 过七条检查）。
这与定理的二分完全一致：开层不可约、坏集闭且 $=$ 全层；点是零维分量、好点开稠密（整点）。

**7. 更正（专家 52 号）。** 原稿把 $E+X_S=S$ 说成“$X_S\subseteq E$ 的补”；当 $e<\omega-1$ 时这是错的。
精确条件是
$$E+F_0\subseteq S,\qquad e+\dim X_S-\dim(E\cap X_S)=\omega,\qquad \omega-e\le m=q-r .$$
射影底空间是 $\mathbb P((E+F_0)^\perp)$，不是整个 $\mathbb P^{k-1}$。并且 genericity 定理必须应用在
**总 incidence 空间**（$S$ + 兼容对 + 张成条件 + full-row-rank）的不可约分量上，不能只对底空间 $\sigma$ 施加；
$d=1$ 例的纤维维数跳变正说明底空间不足以决定好坏。

## 进展

* 定理陈述与证明骨架已写实（分层、闭性、二分、gcd 四步）。
* $k=3,\omega=2,q=3$ 的显式分层已给出；测试例（104）完全落在定理框架内。
* **分层常值性已闭合**（[attempts/108](108_layer_constancy.md)）：$\dim X_S=\omega-(\operatorname{rank}[P;Q]-\operatorname{rank}Q)$
  （秩-零化度）；$E+X_S$ 的维数经有限细分常值。
* **未做**：
  * 每层的**不可约分量**没有一般算法（$k=3$ 时是点/线/开集，可手算；一般 $k$ 需要计算代数几何）；
  * generic gcd 的**可计算表示**没有一般算法（$k=3$ 时可符号算）；
  * 实点问题（实输入时好点是否含实点）未处理。

## 最终结论

* 投影约束定理的**结构部分**（分层 + 逐层闭性 + 二分 + generic gcd）是 B.24 闭性/定理 A 的直接逐层化；
  新内容是"把兼容秩/纤维维数放进分层"。
* **算法部分**：$k=3,\omega=2,q=3$ 已有显式分层与一个完整实例（104）；一般 $k$ 的
  分层参数化、分量枚举、gcd 计算仍未做。
* 这不是 $q1$ 的算法；它是把 $q1$ 的约束情形**结构化**的一步。

## 放弃原因

* 分层常值性已由 [attempts/108](108_layer_constancy.md) 闭合；剩余是分量枚举、程序验证、一般 $k$。
* 一般 $k$ 的分量枚举超出本轮；$k=3$ 的显式分层是手算的，未写成程序对所有 $\sigma$ 验证。
* 实点问题按专家建议单独处理，本轮不碰。

## 残留价值

* 一个可检验的定理框架 + 一个完整实例（104）；任何后续 $k=\omega+1$ 的例子都可按同一模板分析。
* 把专家 51 号的"incidence 分层"建议落成了四步证明骨架。
* 为 $k-\omega=d>1$ 的归纳提供了正确的分层语言（不是 $\mathbb P^1$-丛的朴素剥皮）。

## 相关文件

* [attempts/104](104_p2_constrained_locus.md)（$\mathbb P^1$ 测试例：开层 gcd $\lambda t$、例外点完见证）
* [attempts/105](105_projective_constrained_theorem.md)（骨架版）
* [attempts/106](106_rectangular_determinantal_divisor.md)（矩形行列式因子，RP 用）
* [proof/B.24/README.md](../../../../proof/B.24/README.md)（闭性定理、定理 A、块判据）
* [workspace/ROADMAP.md](../../../ROADMAP.md) §5（专家 51 号优先级）

## 状态

* 定理：**[草稿，M2]**；结构部分依赖 B.24 闭性/定理 A（M3）；分层常值性见 [attempts/108](108_layer_constancy.md)；
  **admissibility 已按专家 52 号改为 (4.2)**（$e+\dim X_S-\dim(E\cap X_S)=\omega$），并加 $E+F_0\subseteq S$、$\omega-e\le m$。
* 实例：attempts/104（开层符号 gcd $\lambda t$；例外点显式好 $R$）。
* 下一步：建**总 incidence 空间**（$S$ + 兼容对 + 张成 + full-row-rank）的不可约分量；$k=3$ 的分层写成程序验证；一般 $k$。
