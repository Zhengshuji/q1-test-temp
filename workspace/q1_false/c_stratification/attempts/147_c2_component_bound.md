> **专家 57 号意见**：$c=2$ 的分量上界“plausible，可在写出不可约性证明后接受”；
> 本文件的逐层不可约性论证即该证明，待专家复核。另：$c=3$ 的对应上界被暂停（见 148）。

# $c=2$ 可容许层的不可约性与分量数上界

> 2026-11-08。补 143 的缺口：每个可容许层是**不可约**的（或按特征值分成有限个不可约块），
> 由此得到 $c=2$ 可容许 locus 的分量数上界
> $$\boxed{\binom{s}{2}+3s+2},\qquad s=\#\{\text{$A$ 的不同特征值}\}\le n.$$
> 状态：**M2（纸面）**。

## 目标

证明：$c=2$ 的可容许 locus
$$\mathcal A=\{V\in\operatorname{Gr}(2,K_0):\ \operatorname{rank}\Phi_V=2-t,\ t=\dim(V\cap A^{-1}V)\}$$
的不可约分量数 $\le\binom{s}{2}+3s+2$；好 locus（可容许层的开子集）同样不超过这个数。

## 设想与理由

143 已把 $\mathcal A$ 分成六个互斥的层：
$$(2a),\ (2b),\ (2c),\ (1A),\ (1B),\ (0).$$
若每层是不可约的（或按特征值拆成有限个不可约块），则分量数 = 各层块数之和。

**不可约性工具**：
* Grassmannian $\operatorname{Gr}(k,E)$、射影空间 $\mathbb P(E)$ 不可约；
* 不可约簇的乘积不可约；有限群作用下的商（如 $(\mathbb P\times\mathbb P)/S_2$）不可约；
* 不可约簇的开子集不可约（若非空）；闭子簇不必不可约，但**射影线性子空间**不可约；
* 纤维丛的底与纤维都不可约 ⟹ 全空间不可约（代数簇的纤维化；底不可约 + 几何纤维不可约）。

## 做法

逐层：

**(2a) $\lambda\ne\mu$。** 对每对不同的特征值 $\{\lambda,\mu\}$，参数空间
$$\big(\mathbb P(E_\lambda\cap K_0)\times\mathbb P(E_\mu\cap K_0)\big)/S_2$$
是射影空间的乘积的有限商，不可约。不同 $\{\lambda,\mu\}$ 的层互不相交（特征空间不同）。
故 (2a) 贡献 $\le\binom{s}{2}$ 个分量。

**(2b) 标量 $\lambda$。** 参数 $\operatorname{Gr}(2,E_\lambda\cap K_0)$，不可约；每个 $\lambda$ 一块，
贡献 $\le s$ 个分量。

**(2c) Jordan $\lambda$。** 底
$$\mathcal B_{2c,\lambda}=\{\ell\in\mathbb P(E_\lambda\cap K_0):\ \ell\subseteq(A-\lambda I)(K_0)\}$$
是射影空间中的**线性子空间**（条件“线落在子空间 $(A-\lambda I)(K_0)$ 中”是线性的），故不可约；
纤维是仿射空间（或空），不可约；故每 $\lambda$ 一块，贡献 $\le s$。

**(1A) $AL\subseteq L$。** 底
$$\mathcal B_{1A}=\{\ell:A\ell\subseteq\ell\}=\bigcup_{\lambda}\mathbb P(E_\lambda\cap K_0).$$
不同 $\lambda$ 的特征空间交为零，故这是**互不相交的并**，每个 $\mathbb P(E_\lambda\cap K_0)$ 不可约；
纤维是 $\mathbb P(K_0/L)$ 的开子集，不可约或空。故贡献 $\le s$。

**(1B) $AL\not\subseteq L$。** 参数
$$\{v\in D:\operatorname{rank}[v,Av,A^2v]=3\}/\mathbb C^\times.$$
“某个 $3\times3$ 子式 $\ne0$”是开条件，故这是 $\mathbb P(D)$ 的开子集，不可约或空；贡献 $\le1$。

**(0) $t=0$。** $\operatorname{Gr}(2,K_0)$ 的开子集，不可约或空；贡献 $\le1$。

**求和**：
$$\#\text{components}\le\binom{s}{2}+s+s+s+1+1=\binom{s}{2}+3s+2.$$
（(2a) $\binom{s}{2}$；(2b)(2c)(1A) 各 $s$；(1B)(0) 各 1。）

**好 locus**：每层的好条件是开条件（块判据的补是闭的），故好 locus 是上述每个不可约块的开子集；
开子集不可约或空，故分量数不超过同一上界。

## 进展

* 六层的不可约性/块数逐层核对；得到 $\binom{s}{2}+3s+2$ 的严格上界。
* 与 131 的界一致，但这里给出的是**不可约性证明**，不是组合计数。
* $s\le n$，故界与 $k$ 无关（只要 $n$ 固定）。

## 最终结论

* $c=2$ 可容许 locus 的分量数 $\le\binom{s}{2}+3s+2$；好 locus 同界。
* 每个分量是某个（特征值标号）块的开子集。
* 这把 143 的“未证不可约性”补上，且与 121 的 $c=1$ 界（$\delta+1$）同一风格。

## 放弃原因

* 未证各层的**非空性**（空层的块不贡献分量；上界仍成立）；
* 未给下界/精确分量数；
* 实点/算法未做。

## 残留价值

* $c=2$ 的第一个严格分量上界（M2）；
* 可直接用于 Q9 的“分量数”部分与论文的 $c=2$ 一节。

## 相关文件

* [attempts/143](143_c2_rigorous_parameterization.md)（六层参数化）
* [attempts/131](131_c2_d3_nilpotent_subtype.md)（旧界 $\binom{s}{2}+3s+2$）
* [attempts/121](121_hyperplane_vector_bundle.md)（$c=1$ 的 $\delta+1$）

## 状态

* 不可约性/分量上界：**[已证-纸面，M2]**。
* 非空/下界/实点：**[未做]**。
