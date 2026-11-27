# 命题 A

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

若 $\dim V\ge d+1-p$，则对每个解 $L$ 都有

$$\rho\ \ge\ d+1-p .$$

## 等价描述

1. 不存在满足 $(\mathrm{a})\wedge(\mathrm{b})$ 且 $\rho<d+1-p$ 的 $L$。
2. 存在解的行空间 $\mathcal A$ 满足 $\dim\mathcal A\ge d+1-p$。
3. 一个**更强的（充分不必要）形式**：$\dim(\mathcal A+S)=d$。
   （由 $\dim(\mathcal A+S)=\rho+p-|\mathcal A\cap S|$：饱和仅当 $|\mathcal A\cap S|=1$ 时才等价于 $\rho=d+1-p$；
   一般地饱和给出 $\rho=d-p+|\mathcal A\cap S|\ge d+1-p$，故饱和 ⟹ 本命题，但本命题**不蕴含**饱和。）
