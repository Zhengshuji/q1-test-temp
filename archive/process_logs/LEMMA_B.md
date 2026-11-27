# 命题 B

## 记号

$A\in\mathbb{R}^{n\times n}$，$C\in\mathbb{R}^{p\times n}$，$L_0\in\mathbb{R}^{r\times n}$。

$$K:=\ker[C;CA]\quad(\dim K=d),\qquad N\in\mathbb{R}^{n\times d}\ \text{列满秩，}\ \operatorname{col}N=K,$$
$$A':=(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN\in\mathbb{R}^{d\times d},\qquad
R_0:=AN-NA'\in\mathbb{R}^{n\times d},$$
$$S:=\operatorname{row}(R_0)\subseteq\mathbb{R}^d\quad(\dim S=p),\qquad
V:=\big\langle S\big\rangle_{A'}\subseteq\mathbb{R}^d\ \ (S\ \text{的最小}\ A'\text{-不变超空间}).$$

称 $L\in\mathbb{R}^{q\times n}$（首行等于 $L_0$）为**解**，若

$$(\mathrm{a})\quad \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],$$
$$(\mathrm{b})\quad \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\qquad\forall\lambda\in\mathbb{C}.$$

对解 $L$，记

$$M:=LN\in\mathbb{R}^{q\times d},\qquad F:=LAN\in\mathbb{R}^{q\times d},\qquad
\rho:=\operatorname{rank}M,\qquad \mathcal A:=\operatorname{row}(M)\subseteq\mathbb{R}^d\ \ (\dim\mathcal A=\rho).$$

（注：$(\mathrm{a})\iff\exists\Lambda:F=\Lambda M$；$(\mathrm{b})\iff\operatorname{rank}(\lambda M-F)=\rho\ \forall\lambda$。）

## 命题

若 $p\le\dim V<d+1-p$，则对每个解 $L$ 都有

$$\rho\ \ge\ \dim V .$$

## 等价描述

1. 不存在满足 $(\mathrm{a})\wedge(\mathrm{b})$ 且 $\rho<\dim V$ 的 $L$。
2. 每个解的行空间 $\mathcal A$ 满足 $\dim\mathcal A\ge\dim V$。
3. 一个**更强的充分条件**：$S\subseteq\mathcal A$ 对每个解成立。
   （若 $S\subseteq\mathcal A$，则由 $(\mathrm{a})$ 有 $\mathcal A A'\subseteq\mathcal A+S=\mathcal A$，
   即 $\mathcal A$ 是 $A'$-不变的且含 $S$；由 $V$ 的极小性得 $V\subseteq\mathcal A$，故 $\rho\ge\dim V$。）
