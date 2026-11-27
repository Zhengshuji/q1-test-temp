# 761 固定行空间 $U$ 的仿射存在性定理

> 2026-11-27。把 678/687/697/739/755 合并为“$U$ 层”的判据，全部使用中心化对象 $(Z'',G')$。
> 状态：**[已证-纸面]**（在 $N$ 标准化的约定下）。

## 约定

- 取 $N=\begin{bmatrix}I_k\\0\end{bmatrix}$（$n\times k$ 列满秩）。一般 $N$ 可通过状态空间的可逆换基化到此形；秩条件在该换基下不变。
- $W=\begin{bmatrix}W_{\mathrm{top}}\\W_{\mathrm{bot}}\end{bmatrix}$，$T=\operatorname{row}(W_{\mathrm{bot}})$，$Z''=Z'+W_{\mathrm{top}}$。
- 固定 $U\subseteq\mathbb C^k$、$\dim U=d'$，$U_0=\operatorname{row}(H_0)\subseteq U$；取 $q\times k$ 的行满秩矩阵 $H$ 使 $\operatorname{row}H=U$。
- 定义**仿射纤维**
$$\boxed{\mathcal F_U=\prod_{i=1}^{q}\big(T\cap(U-H_iZ'')\big).}$$

## 定理

存在 $L$（$q\times n$，$LN=H$）与 $Z$ 使 $(5a)(5b)$ 成立，且 $\operatorname{row}H=U$，当且仅当

1. $\mathcal F_U\ne\varnothing$（等价地 $H_iZ''\in U+T$ 对所有 $i$）；
2. 存在 $G'\in\mathcal F_U$，使 $P_{G'}(\lambda)=\lambda H-HZ''-G'$ 的全部 $d'$-子式的 $\gcd=1$（即 $\operatorname{rank}M=2d'$）。

## 证明

**（⇒）** 设 $L,Z$ 可行。令 $G=LW$、$G'=G-HW_{\mathrm{top}}\in T^q$（757），$Z''=Z'+W_{\mathrm{top}}$。由 $ZH=HZ'+G=HZ''+G'$ 与 $Z_iH\in U$：
$$G'_i=Z_iH-H_iZ''\in U-H_iZ'',\qquad G'_i\in T,$$
故 $G'\in\mathcal F_U$。$(5b)$ 给 $\operatorname{rank}P_{G'}(\lambda)=d'$ 对所有 $\lambda$，由引理 S 得 $\gcd=1$。

**（⇐）** 设 $G'\in\mathcal F_U$ 且 $\gcd=1$。逐行 $H_iZ''+G'_i\in U$，取 $Z_i$ 使
$$Z_iH=H_iZ''+G'_i\quad(\text{存在，因 } H \text{ 行满秩、}z\mapsto zH\text{ 满射到 }U).$$
逐行拼接得 $Z$，且 $ZH=HZ''+G'$。

再构造 $L$：$G'\in T^q=\operatorname{row}(W_{\mathrm{bot}})^q$，取 $M$（$q\times(n-k)$）使 $MW_{\mathrm{bot}}=G'$；令
$$L=\big[\,H\ \big|\ M\,\big]\quad(q\times n).$$
则 $LN=H$，且
$$LW=H\,W_{\mathrm{top}}+M\,W_{\mathrm{bot}}=HW_{\mathrm{top}}+G'=G .$$
于是 $ZH=HZ''+G'=HZ'+G$，$(5a)$ 成立；$\gcd=1$ 给 $(5b)$。$\square$

## 基选择不变性

若 $H$ 换成 $SH$（$S$ 可逆），则 $F_U$ 逐行作线性组合、$P$ 左乘 $S$，$\gcd$ 与 $d'$-子式空间不变；故“$U$ 可行”与 $H$ 的选取无关。

## 推论（实例级判据）

实例可行 $\iff$ 存在 $U$（$\dim U=d'$、$U_0\subseteq U$）使 $\mathcal F_U\ne\varnothing$ 且 $\exists G'\in\mathcal F_U$ 使 $\gcd=1$。

这仍然是 $\exists U$（Grassmann）+ $\exists G'$（仿射）的两层存在性；第二层正是 PIT 缺口的所在。

## 检验：733

733：$W_{\mathrm{top}}=0$（$W=e_3e_1^{\mathsf T}$），$U=\mathbb C^2$、$T=\operatorname{span}\{e_1\}$、$Z''=Z'$。
$$F_U=\prod_i\big(T\cap(\mathbb C^2-H_iZ')\big)=T^q\ni G'=(-3,0)\text{ 的行},$$
$\gcd=1$ ⇒ 定理判定可行 ✓（与 733 一致）。

## 与旧结果的关系

- 678 是“固定 $H$”的版本；本定理把它提升为“固定 $U$”，并显式分离 $\mathcal F_U$；
- 687 的 $Z$ 消去在本定理的 $(\Leftarrow)$ 中体现为“取 $Z_i$ 使 $Z_iH=\cdots$”；
- 755 的相容性即 $\mathcal F_U\ne\varnothing$；
- 739 的 $\dim E_H$ 等式用于分析 $\mathcal F_U$ 的维数（$\dim E_H=\dim(U\cap T)+\operatorname{cls}$）。

## 状态

- 定理：**[已证-纸面]**（$N$ 标准化约定下）；
- 733 检验：**[精确验证]**；
- 一般 $N$ 的换基说明：**[待补严格化]**。
