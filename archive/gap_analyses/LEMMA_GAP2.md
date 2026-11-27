# 命题 C（上界）

## 记号

$A\in\mathbb{R}^{n\times n}$，$C\in\mathbb{R}^{p\times n}$，$L_0\in\mathbb{R}^{r\times n}$。

$$K:=\ker[C;CA]\quad(\dim K=d),\qquad N\in\mathbb{R}^{n\times d}\ \text{列满秩，}\ \operatorname{col}N=K,$$
$$A':=(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN\in\mathbb{R}^{d\times d},\qquad
R_0:=AN-NA'\in\mathbb{R}^{n\times d},$$
$$S:=\operatorname{row}(R_0)\subseteq\mathbb{R}^d\quad(\dim S=p),\qquad
V:=\big\langle S\big\rangle_{A'}\subseteq\mathbb{R}^d\ \ (S\ \text{的最小}\ A'\text{-不变超空间}),$$
$$\alpha_0:=L_0N\in\mathbb{R}^d,\qquad \beta_0:=L_0AN\in\mathbb{R}^d .$$

称 $L\in\mathbb{R}^{q\times n}$（首行等于 $L_0$，$q$ 为行数）为**解**，若

$$(\mathrm{a})\quad \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],$$
$$(\mathrm{b})\quad \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\qquad\forall\lambda\in\mathbb{C}.$$

对解 $L$，记

$$M:=LN,\qquad F:=LAN,\qquad \rho:=\operatorname{rank}M,\qquad \mathcal A:=\operatorname{row}(M)\ \ (\dim\mathcal A=\rho).$$

（注：$(\mathrm{a})\iff\exists\Lambda:F=\Lambda M$；$(\mathrm{b})\iff\operatorname{rank}(\lambda M-F)=\rho\ \forall\lambda$。）

## 命题

设 $\alpha_0\in V$。则存在解 $L$ 使

$$\rho=\min\big(d+1-p,\ \dim V\big).$$

## 等价描述

1. 存在解 $L$ 使 $\rho\le\min(d+1-p,\dim V)$。（结合命题 A、B 得等式。）
2. 存在解的行空间 $\mathcal A$ 使 $\dim\mathcal A=\min(d+1-p,\dim V)$。
3. 分两种情形：

   **(C1)** $\dim V<d+1-p$：取 $\mathcal A=V$（因 $V$ 是 $A'$-不变的，故 $\mathcal A A'\subseteq\mathcal A+S=\mathcal A$），
   存在 $q$ 行 $L$ 满足 $(\mathrm{a})\wedge(\mathrm{b})$ 且 $\rho=\dim V$。

   **(C2)** $\dim V\ge d+1-p$：取任一满足
   $$\dim\mathcal A=d+1-p,\qquad \mathcal A\supseteq\operatorname{span}\{\alpha_0,\beta_0\},\qquad \dim(\mathcal A\cap S)=1$$
   的 $\mathcal A$（存在性由维数计数给出），存在 $q$ 行 $L$ 满足 $(\mathrm{a})\wedge(\mathrm{b})$ 且 $\rho=d+1-p$。

4. 记 $q_{\min}:=\min\{q:\ \text{存在 } q \text{ 行的解}\}$，则
$$q_{\min}\ \le\ \min(d+1-p,\ \dim V)+1$$
（用 $\rho\le q-1$，即 $q\ge\rho+1$，对所有解成立）。

5. $(\mathrm{b})$ 可等价地写为：设 $F=M\Lambda+l\,c^{\mathsf T}$（$\Lambda$ 为 $\mathcal A$ 上的线性映射、$l$ 张成 $\mathcal A\cap S$、$c\ne0$），则
$$l\ \text{是}\ \Lambda^{\mathsf T}\ \text{的循环向量}\iff
\big[l;\ l\Lambda;\ \cdots;\ l\Lambda^{\rho-1}\big]\ \text{满秩}\iff
l\notin(\lambda I-\Lambda)(\mathcal A)\ \ \forall\lambda\in\mathbb{C}.$$
