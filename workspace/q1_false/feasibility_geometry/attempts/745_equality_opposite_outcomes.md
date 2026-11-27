# 745 取等但相反：638（不可行）vs 733（可行）

> 2026-11-27。回答“方向性维数取等是否足以判定”的问题：两个实例都取等，结论相反。
> 状态：**[已证-纸面]** + **[精确验证]**。

## 两个实例的方向性数据（在 $Z'$ 的特征值 $\mu$ 处）

| 实例 | $d'$ | $\operatorname{rank}(H(\mu I-Z'))$ | $\dim(U\cap T)$ | $\operatorname{cls}_\mu$ | 和 | 结论 |
|---|---|---|---|---|---|---|
| 638 | 2 | 1 | 0 | 1 | $2$ | **不可行**（709） |
| 733 | 2 | 1 | 1 | 0 | $2$ | **可行**（$\gcd=1$） |

即 744 的第 6 条在两个实例上**都取等**：
$$d'=\operatorname{rank}(HM)+\dim(U\cap T)+\operatorname{cls}_\mu=2 .$$

## 为什么结论相反

- **638**：$U=\operatorname{span}\{e_2,e_3\}$（$e_1\notin U$），$T=\operatorname{span}\{e_1\}$，$\dim(U\cap T)=0$；$Z'$ 3-循环、$\mu=1$ 时 $\operatorname{rank}(M)=2$，$HM$ 的秩 1，$\operatorname{cls}=1$。  
  709 证明 $P$ 的行全部落在 $U$ 内 ⇒ 所有 2-子式成比例 ⇒ $\rho_2=1$ ⇒ $\operatorname{rank}M\le2<4$ ⇒ 不可行。
- **733**：$U=\mathbb C^2$、$T=\operatorname{span}\{e_1\}$，$Z'=\begin{bmatrix}1&2\\1&1\end{bmatrix}$ 的特征值 $\mu=1\pm\sqrt2$；$\operatorname{rank}(HM)=1$、$\dim(U\cap T)=1$、$\operatorname{cls}=0$，取等。  
  但 $P$ 的三个 2-子式
  $$-9(\lambda-3),\quad -2\lambda^2+\lambda+5,\quad \lambda^2+4\lambda-25$$
  的 $\gcd=1$ ⇒ $\operatorname{rank}M=4$ ⇒ 可行。

## 区分量

- 638：$\rho_{d'}=1$（子式空间一维），$P$ 的行落在同一个 $d'$ 维子空间内；
- 733：$\rho_{d'}=3$（子式张成三维），$\gcd=1$。

因此**方向性维数取等不是判定依据**；需要代数量（$\rho_{d'}$ 或 $\gcd$ / $\operatorname{rank}M$）来区分。

## 待办

1. 用 $\rho_{d'}$ 与 $\operatorname{cls}$ 组合，寻找“取等 + $\rho_{d'}=1$”的不可行判据（这是 705 的直接应用）；
2. 检查是否还有“取等 + $\rho_{d'}\ge2$ 但 $\gcd\ne1$”的不可行实例；
3. 把 744 的 1–7 与 $\rho_{d'}$ 一起写成筛选脚本。

## 状态

- 两个实例：**[已证-纸面]** + **[精确验证]**；
- 区分量：$\rho_{d'}$（638 为 1，733 为 3）。
