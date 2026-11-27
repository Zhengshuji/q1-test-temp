# 572 冗余行引理（草稿）：新行落在 $P_0(\lambda)$ 行空间里 ⇒ 它是已有行的组合

> 2026-11-27。为 571 的猜想给出证明草稿。
> 状态：**[M2 纸面草稿]**（系数依赖 $\lambda$ 的情形尚未完全排除）。

## 陈述

设 $H_0$（$r_0\times k$）、$H_{A,0}$ 固定，$P_0(\lambda)=\lambda H_0-H_{A,0}$。
若存在 $r$ 使
$$\lambda\,rN-rAN\in\operatorname{row}P_0(\lambda)\qquad\forall\lambda,$$
则 $rN\in\operatorname{row}H_0$ 且 $rAN\in\operatorname{row}H_{A,0}$。
于是新增行 $(rN,rAN)$ 是已有行 $(h_i,a_i)$ 的线性组合，$\operatorname{rank}H$、$\operatorname{rank}P$ 都不变。

## 证明草稿（常数系数情形）

若 $\lambda rN-rAN=\sum_i c_i(\lambda)\,p_i(\lambda)$，$p_i=\lambda h_i-a_i$。
把 $c_i$ 写成 $\mathbb C(\lambda)$ 的元素；比较 $\lambda\to\infty$ 的首项：
$$rN=\sum_i c_i(\infty)\,h_i,$$
即 $rN\in\operatorname{row}H_0$。再比较常数项：
$$-rAN=-\sum_i c_i(\infty)\,a_i,$$
即 $rAN\in\operatorname{row}H_{A,0}$。$\square$（常数系数）

## 未闭合处

若 $c_i(\lambda)$ 有极点或首项抵消，需要更细的论证（例如在 $P_0$ 的每个有限点/无穷远做局部展开）。
当前只对“$c_i$ 为常数”的干净情形成立；571 的枚举（小整数 $r$）都在这个情形里。

## 对 571 猜想的意义

- 在干净情形下，可行的自由行必然冗余——与 571 的 3/27（全为重复行）一致；
- 若存在非冗余的可行行，它必须对应“$\lambda$-依赖系数”的退化，这是下一步要排除或找到的。

## 下一步

分析 $P_0(\lambda)$ 的 Smith 形/最小多项式，判断 $\lambda$-依赖系数是否可能产生非冗余解；
或直接在 $r$ 的更大范围（含 $r_4,r_5\ne0$）搜索反例。

## 状态

- 冗余行引理（常数系数）：**[M2 草稿]**；
- 一般情形：**[未闭合]**。
