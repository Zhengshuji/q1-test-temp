# 764 非退化 $(5a)$ 实例（$n=6,k=2$，$d'=k-1$）

> 2026-11-28。子 agent `nondeg-5a` 找到 $W_{\mathrm{top}}\ne0$、$\operatorname{rank}[L;CA;C]<n$、$(5a)$ 非平凡成立的可行实例；本文独立复核并提炼结构事实。
> 状态：**[精确验证]**。

## 实例（$q=k=2$，最小）

$n=6$、$k=2$、$N=[I_2;0]$，
$$A=\begin{bmatrix}1&1&0&0&0&0\\1&0&0&0&0&0\\0&0&0&0&1&0\\0&0&0&0&0&1\\1&0&0&0&0&0\\0&1&0&0&0&0\end{bmatrix},\quad
C=\begin{bmatrix}0&0&1&0&0&0\\0&0&0&1&0&0\end{bmatrix},$$
$$W=\begin{bmatrix}1&0\\0&0\\0&0\\0&0\\1&0\\0&1\end{bmatrix}\ (W_{\mathrm{top}}=\begin{bmatrix}1&0\\0&0\end{bmatrix}\ne0),\quad
Z'=\begin{bmatrix}0&1\\1&0\end{bmatrix},\quad
L=\begin{bmatrix}1&0&1&0&-1&-1\\1&0&0&1&0&-1\end{bmatrix}=[H_2|M_2].$$

独立复核（sympy，有理精确）：

| 检查 | 结果 |
|---|---|
| $AN=NZ'+W$ | ✓ |
| $K_0=\ker[C;CA]=\operatorname{im}N$ | ✓（dim 2） |
| $LN=H_2$（$\operatorname{rank}H_2=1$） | ✓ |
| $\operatorname{rank}[L;CA;C]$ | **5 < 6 = n**（非退化） |
| $\operatorname{rank}[LA;L;CA;C]$ | 5（与上式相等，$(5a)$ 非平凡成立） |
| $(5b)$：$[\lambda L-LA;CA;C]$ 的 5×5 子式 | 6 个非零，**$\gcd=1$**；$\lambda=0,1,2,\tfrac12$ 处秩均为 5 |

同一 $(A,C,W,Z')$ 下还有 $q=3$ 的版本（$L=[H|M]$，$H$ 三行、$\operatorname{rank}H=1$，$G'=MW_{\mathrm{bot}}$），同样 $\operatorname{rank}[L;CA;C]=5<6$、$\gcd=1$。

## 结构事实（子 agent 的发现，本文复核）

在标准块形 $N=[I_k;0]$、$CN=0$、$CW=0$、$\operatorname{rank}[C;CA]=n-k$ 下，$C=[0|C_2]$、$CA=[0|C_2D]$，$[C;CA]$ 的行张成 $\{0\}\times\mathbb C^{n-k}$，故
$$\boxed{\operatorname{rank}[L;CA;C]=(n-k)+\operatorname{rank}(LN)=(n-k)+\operatorname{rank}(H).}$$
**推论**：非退化（$<n$）$\iff \operatorname{rank}H<k$，即 $d'=\dim U<k$。

这解释了：
- 733/747 的 $d'=k=2$ ⇒ 必然退化（$(5a)$ 自动成立），所以它们只检验了 $(5b)$；
- 761 的“$H$ 行满秩”应理解为 $\operatorname{rank}H=d'$（行满秩于 $U$），本实例 $d'=1<k$，**不矛盾**；
- 真正的非退化区域是 $d'<k$。

## 对 761 的意义

761 的定理对任意 $d'=\dim U\le k$ 成立（$H$ 行满秩指 $\operatorname{rank}H=d'$）；本实例正是 $d'=1<k$ 的非退化验证：

- $F_U=\prod_i(T\cap(U-H_iZ''))$，$T=\operatorname{row}(W_{\mathrm{bot}})$；
- $G'=MW_{\mathrm{bot}}$ 行在 $T$；
- $\gcd=1$ ⇒ 可行。

## 限制

- 仍是**有限实例**（精确验证），非一般命题；
- $d'<k$ 的一般理论（非退化区域）仍待发展；
- 子 agent 的“结构筛 10/10 通过”是经验统计，未证明。

## 状态

- 实例：**[精确验证]**（独立复核通过）；
- 结构恒等式：**[已证-纸面]**（块形下）；
- 非退化区域 $d'<k$：**[下一步]**。
