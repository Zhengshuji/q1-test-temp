# 压缩铅笔对所有可容许 $V$ 都下降：块判据的统一形式（专家 57 号更正）

> 2026-11-08。专家 57 号指出：$P(\lambda)$ 在 $V=\ker H$ 上为零**不依赖 $t=2$**，而是由 $(5a)$
> 直接推出；因此块判据对所有可容许 $V$ 成立，不需要 $t<2$ 的两分支系统。
> 本文件写出统一形式，并撤回 145 的两分支作为“谱判据”的地位。状态：**M2（纸面）**。

## 目标

证明：若 $(5a)$ 成立、$H=LN_K$、$H_A=LAN_K$、$V=\ker H$，则 $P(\lambda)=\lambda H-H_A$ 在 $V$ 上为零，
下降为
$$\overline P(\lambda):K_0/V\longrightarrow\mathbb C^q,$$
并在适当基下等于
$$\begin{bmatrix}\lambda I_\omega-A_*\\-B_*\end{bmatrix};$$
于是
$$\operatorname{rank}P(\lambda)<\omega\iff\exists\,0\ne y\in\mathbb C^\omega:\ A_*y=\lambda y,\ B_*y=0.$$

## 设想与理由

$(5a)$ 等价于 $\ker[L;CA;C]\subseteq\ker LA$。对 $v\in K_0$、$Lv=0$：$v\in\ker[L;CA;C]$（因为 $Cv=CAv=0$），
故 $LAv=0$。用 $N_K$ 坐标：$Hv=0\Rightarrow H_Av=0$，即 $\ker H\subseteq\ker H_A$。
于是对 $v\in V=\ker H$：$P(\lambda)v=\lambda Hv-H_Av=0$。

## 做法

**下降**：$P(\lambda)$ 在 $V$ 上为零，故诱导 $\overline P(\lambda):K_0/V\to\mathbb C^q$。
$\dim(K_0/V)=k-c=\omega$；$\overline H$ 单射（$H$ 的核恰为 $V$）。取 $K_0/V$ 与 $\mathbb C^q$ 的基使
$$\overline H=\begin{bmatrix}I_\omega\\0\end{bmatrix},\qquad
\overline H_A=\begin{bmatrix}A_*\\B_*\end{bmatrix},\quad A_*\in\mathbb C^{\omega\times\omega},\ B_*\in\mathbb C^{(q-\omega)\times\omega}.$$
则
$$\overline P(\lambda)=\lambda\overline H-\overline H_A=\begin{bmatrix}\lambda I_\omega-A_*\\-B_*\end{bmatrix}.$$
$\operatorname{rank}P(\lambda)<\omega$ $\iff$ 这个 $q\times\omega$ 矩阵秩 $<\omega$ $\iff$ 存在 $0\ne y\in\mathbb C^\omega$ 使
$(\lambda I-A_*)y=0$、$B_*y=0$。$\square$

**$q=\omega+1$ 的特殊化**：$B_*$ 是一行；好 $\iff$ 这一行在每个特征子空间上都不为零
（即 $\ker B_*$ 不含 $A_*$ 的特征向量）。

## 与 144/145 的关系

* 144 的 $t=2$ 判据是上述一般判据在 $t=2$（$V$ 不变，$P$ 直接下降）的特例——**正确**。
* 145 的两分支 $(x,\alpha)$ 系统来自另一个消元（把 $H$ 当作 $(\omega+1)\times k$ 的**行相关**分析），
  它**不是**谱判据 (8)；专家 57 号明确指出：在没有写出变换与等价证明前，不能把它当作
  “谱好性”的判据。**本文件撤回 145 的谱判据地位**；两分支若有用，只可能是“提升附加条件”，需另行推导。
* 144 的“只对 $t=2$”限定也撤回：判据对所有可容许 $V$ 成立。

## 进展

* 统一块判据的证明已写出（一行 $(5a)$ 推出 $\ker H\subseteq\ker H_A$）。
* 145 的两分支已明确降级；144 的适用范围扩大到所有 $t$。

## 最终结论

* 谱判据就是块判据 $(8)$，对所有可容许 $V$ 成立；
* 不需要 $t<2$ 的两分支系统来判 $(5b)$；
* 这是专家 57 号 Q2/Q6 的落实。

## 放弃原因

* 两分支是否对应“提升附加条件”未证（不排除有用，但不再是谱判据）；
* 未 Lean 化（专家建议形式化一般块判据；见下一步）。

## 残留价值

* 把 $c=2$ 的好性判据统一为一条，与 144 一致、与 145 的过度推广切割；
* 为 Lean 化“一般块判据”提供正确陈述。

## 相关文件

* [attempts/144](../../c_stratification/attempts/144_c2_good_locus.md)（$t=2$ 特例）
* [attempts/145](../../c_stratification/attempts/145_c2_good_locus_corrected.md)（两分支，已降级）
* [lean/BlockIff](../../../../trash/lean_removed_2026-11-19/augmentation_lean/BlockIff.md)（块判据的 Lean 形式）

## 状态

* 统一块判据：**[已证-纸面，M2]**。
* 145 两分支作为谱判据：**[撤回]**。
