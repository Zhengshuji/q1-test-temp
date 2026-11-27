# $k=\omega+1$ 投影约束定理（修正版 v2，按专家 52/53 号）

> **适用范围（专家 54 号）**：本文件的射影参数化 $S=\ker\sigma$、$\sigma\in\mathbb P^{k-1}$ 要求
> $\dim S=k-1=\omega$，即 **$\omega=k-1$（超平面情形）**。一般 $\omega$ 的底空间是
> $\operatorname{Gr}(\omega,k)$，见专家 54 号 §5.3 与 attempt 121 的对照。
>
> 2026-11-08。按专家 52/53 号重写：坐标修正 $\widetilde E_S$；**lifted incidence space**（把 $R$ 作为变量）；
> determinantal 分层；genericity 作用在 lifted 分量的不可约分量上。
> 状态：**M2（纸面草稿）**；超平面情形的分量数见 121（$\le\delta+1$）。

## 目标

固定数据 $(A,C,L_0)$，$q=\omega+1$，$k=\omega+1$（故 $\omega=k-1$，$S=\ker\sigma$ 是超平面），
$m=q-r$，$N=N_K$，$M=AN_K$，$E=U_0=L_0N$，$F_0=V_0=L_0AN$，$e=\dim E$。目标是下面的定理（修正版 v2）：

> **定理**：令 $\mathcal B=\mathbb P((E+F_0)^\perp)=\{[\sigma]:\sigma|_{E+F_0}=0\}$。对 $\sigma\in\mathcal B$，
> $S=\ker\sigma$，$B$ 为基，$P=B^\top Z_1$，$Q=B^\top Z_2$，$X_S=\{a:aP\in\operatorname{row}Q\}$，
> $$\widetilde E_S=\{a\in\mathbb C^\omega:aB^\top\in E\}.$$
> 定义**lifted incidence space**
> $$\mathcal I=\{(\sigma,R):\ \operatorname{row}(L_0N)\subseteq S,\ \operatorname{row}(L_0AN)\subseteq S,\ 
> \operatorname{row}(RN)\subseteq S,\ \operatorname{row}(RAN)\subseteq S,\ 
> \operatorname{row}(L_0N;RN)=S,\ \operatorname{rank}[L_0;R]=q\}.$$
> 它等价于 $\operatorname{rank}H=\omega$、$\ker H\subseteq\ker H_A$、$\operatorname{row}H=S$、$\operatorname{rank}[L_0;R]=q$。
> 块分解要写对：$Z=(A_W;B_\perp)$，$A_W\in\mathbb C^{\omega\times\omega}$、$B_\perp\in\mathbb C^{(q-\omega)\times\omega}$，
> bad $\iff\exists0\ne y\in\ker B_\perp,\ A_Wy\in\mathbb Cy$。
> 在压缩层，admissibility 是
> $$E+F_0\subseteq S,\qquad \widetilde E_S+X_S=\mathbb C^\omega\ 
> \Big(\iff e+\dim X_S-\dim(\widetilde E_S\cap X_S)=\omega\Big),\qquad m\ge\omega-e.$$
> 按
> $$\big(\operatorname{rank}Q,\ \operatorname{rank}[P;Q],\ \operatorname{rank}(\varphi_S|_{\widetilde E_S}),\ \operatorname{rank}H\big)$$
> 分层，其中 $\varphi_S(a)=aP\bmod\operatorname{row}Q$。每个常秩层上，坏集
> $$\mathcal B_{\mathcal I}=\{(\sigma,R):\exists\lambda,\ \operatorname{rank}(\lambda H-H_A)<\omega\}$$
> 在层中**闭**。每个不可约分量 $X$ 上，要么全坏，要么好点 Zariski 开稠密；由 $\mathbb C(X)$ 上
> $\omega$-子式的 generic determinant divisor 判定。

## 设想与理由

* 专家 52 号：$X_S\not\subseteq E$ 不是 admissibility；精确条件是 $\widetilde E_S+X_S=\mathbb C^\omega$。
* 专家 53 号：$E\subset\mathbb C^k$、$X_S\subset\mathbb C^\omega$ 是**不同空间**；必须经 $\widetilde E_S$ 的坐标表示。
* 专家 53 号：总 incidence 空间最好**把 $R$ 作为变量**。若只保留压缩对 $(H,H_A)$，lift 条件是投影，
  只保证 constructible（Chevalley），不必局部闭；保留 $R$ 后 full-row-rank 是开条件，集合局部闭，可直接分解。
* 专家 53 号：$k=3$ 的"秩层=不可约分量"**不成立**（115 已撤回）；一般框架只能是**determinantal stratification**，
  不是线性/不可约。

## 做法

**1. 底空间与 $\dim X_S$。** 由 108 的秩公式，
$$\dim X_S=\omega-\big(\operatorname{rank}[P;Q]-\operatorname{rank}Q\big).$$
另外 $\dim(\widetilde E_S\cap X_S)=e-\operatorname{rank}(\varphi_S|_{\widetilde E_S})$。

**2. 坐标修正。** $E\subseteq S$ 时，$\widetilde E_S$ 是 $E$ 在基 $B$ 下的坐标，$\dim\widetilde E_S=e$。
于是
$$\widetilde E_S+X_S=\mathbb C^\omega\iff e+\dim X_S-\dim(\widetilde E_S\cap X_S)=\omega.$$
按 $\operatorname{rank}(\varphi_S|_{\widetilde E_S})$ 细分（秩条件，局部闭），每片上
$\dim(\widetilde E_S\cap X_S)$ 常值。另需 $m\ge\omega-e$。

**3. lifted incidence space。** $\mathcal I$ 的坐标是 $(\sigma,R)$；前五个条件是秩/包含条件，
$\operatorname{rank}[L_0;R]=q$ 是开条件（某个 $q\times q$ 子式非零）。所以 $\mathcal I$ 是**局部闭**的；
按秩分层后每层局部闭，可分解为不可约分量。
与压缩对的关系：$(\sigma,R)\mapsto(\sigma,H,H_A)$ 的像是投影，按 Chevalley 只保证 constructible；
这就是为什么要把 $R$ 保留在空间里。

**4. 闭性。** 固定常秩层 $Z$。把 $\lambda$ 齐次化到 $\mathbb P^1$，坏集是
$\{(\sigma,R,[\lambda_0:\lambda_1]):\text{全部 }\omega\text{-子式为零}\}$ 的投影；在无穷远处
$\lambda_0H-\lambda_1H_A=\lambda_0H$ 的秩 $=\operatorname{rank}H=\omega$，故不与无穷远纤维相交；
投影紧合，像闭。

**5. 二分与 gcd。** 不可约分量上闭集要么全、要么真闭；真闭的补开稠密。
在 $\mathbb C(Z)$ 上算 $\omega$-子式的 gcd：非常数 $\iff$ 全坏；单位 $\iff$ 好点开稠密。

## 进展

* 修正版 v2 的陈述与五步骨架已完成：坐标修正、lifted incidence space、determinantal 分层、闭性/二分/gcd。
* $k=3$ 的实例表（112）保留为**逐实例**的精确数据；其"一般线性性"解释已撤回（见 115）。
* **未做**：一般分量分解；$e>0$ 的完整处理（已给 rank 指标，但未算分量）；$k>3$；实点。

## 最终结论

* 定理现在是**坐标正确**、**以 lifted incidence space 为中心**、**determinantal 分层**的版本；
  不再声称 $k=3$ 的一般线性/不可约性。
* 结构部分（闭性/二分/gcd）仍是 B.24 的逐层化；新内容是坐标修正与 lifted 空间。
* 算法部分（分量分解、每分量 gcd）仍未完成；112 是逐实例数据，不是一般定理。

## 放弃原因

* 没有做一般 determinantal 分量的不可约分解。
* $e>0$ 只给了秩指标（$\operatorname{rank}(\varphi_S|_{\widetilde E_S})$），没有逐例计算。
* $k>3$ 与实点未处理。

## 残留价值

* 一条按 52/53 号裁决修正的、可寄的定理陈述；把 $\widetilde E_S$、lifted incidence space、
  determinantal 分层写进了正式框架。
* 与 112（逐实例数据）、114（lifting）、115（撤回与反例）配套。
* 为论文包的“投影约束定理”一节提供正确版本。

## 相关文件

* [attempts/107](../../c_stratification/attempts/107_projective_constrained_theorem_v2.md)（旧稿）
* [attempts/108](../../c_stratification/attempts/108_layer_constancy.md)（$\dim X_S$ 与 $\widetilde E_S$）
* [attempts/112](../../c_stratification/attempts/112_incidence_table.md)（$k=3$ 逐实例表）
* [attempts/114](../../c_stratification/attempts/114_lifting_lemma.md)（lift 引理）
* [attempts/115](../../c_stratification/attempts/115_k3_component_decomposition.md)（$k=3$ 线性性撤回 + 反例）
* [proof/B.24/README.md](../../../../proof/B.24/README.md)（闭性、定理 A）

## 状态

* 定理：**[草稿，M2]**；按专家 52/53 号修正；结构部分依赖 B.24（M3）。
* 实例：112 的表（逐实例）；115 的反例说明一般线性性不成立。
* 未做：一般分量分解、$e>0$ 逐例、$k>3$、实点。
