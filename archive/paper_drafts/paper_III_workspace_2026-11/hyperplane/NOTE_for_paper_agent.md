# 给论文 agent：超平面层论文里两处需要修正的记号（附精确反例）

写这份说明的原因：$c=1$ 的论文在 $q=k$ 的实例上验证时，有两个"看起来显然"的等式恰好成立，
但它们**不是一般恒等式**。$c\ge2$ 的工作必须以正确的那一个为定义，否则后面全错。
以下每条都附精确核对（有理算术，无舍入）。

## 记号

$N$ 是 $K_0=\ker[C;CA]$ 的基，$H=LN$、$H_A=LAN$、$\omega=\rank H$；$q$ 是 $\mathcal L$ 的行数、
$V=\operatorname{row}\mathcal L$、$k=\dim K_0$、$\rho=\dim\pi_{K_0}(V)$。

## 结论一：$\omega=\rho$，不是 $\dim(V\cap K_0)$

$$\boxed{\ \omega=\rank(LN)=\dim(LK_0)=\dim\pi_{K_0}(V)=\rho\ }$$

而
$$\dim(V\cap K_0)=q+k-\rank[V;K_0],\qquad \dim(K_0\cap V^\perp)=k-\rho=q-\omega .$$

精确核对（4242 的实例，$n=8$、$k=4$、$\rho=4$；随机取满秩的 $q$ 行）：

| $q$ | $\rank H$ | $\dim(K_0\cap V^\perp)$ | $\dim(V\cap K_0)$ |
|---|---|---|---|
| 3 | 3 | 1 | 0 |
| 4 | 4 | 0 | 0 |
| 5 | 4 | 0 | **2** |
| 6 | 4 | 0 | 2 |

$q=5$ 那一行就是反例：$\omega=4$，而 $\dim(V\cap K_0)=2$。

**影响**：论文 §II/§III 里"$\omega=\dim(V\cap K_0)$"应改为
"$\omega=\rank H=k-\dim(K_0\cap V^\perp)$"。$c=k-\omega$ 这个定义本身是对的
（$c=\dim(K_0\cap V^\perp)$，与旧框架的 $\dim(\mathcal V\cap\mathcal J)$ 不同，见结论三）。

## 结论二：(S2) 即 $\dim(V\cap K_0)=k-1$ 不是 $(5a)$ 的推论

$c=1$ 的论文把它当作层的定义性正规化（"$V\cap K_0$ 的维数是 $k-1$"）。它不是自动的：

- 构造（$M=\operatorname{diag}(1,1,2,3)$、$K_0=\operatorname{span}\{e_5,\dots,e_8\}$、$D\le K_0$、$U=D+AD$、$V=U^\perp$）
- 取 $D=\operatorname{span}\{e_1+e_2,\ e_3+e_4\}$（**不是** $M$-不变）：则 $c=2$、$(5a)$ 成立，
  但 $\dim(V\cap K_0)=1\ne k-c=2$，且 $M(D)\not\subseteq D$。

**影响**：论文里凡是"由 $(5a)$ 得 $\dim(V\cap K_0)=k-1$"的句子要改成**假设**；
或者把层定义成"$c=\dim(K_0\cap V^\perp)$ 且 $V$ 与 $K_0$ 横截"。

## 结论三：旧框架的 $c$ 与本文的 $c$ 只在 $q=k$ 时相同

- 旧框架 $\mathcal J=\operatorname{row}[C;CA]=K_0^\perp$，$c_{\rm old}=\dim(V\cap\mathcal J)=q-\rho$；
- 本文 $c_{\rm new}=k-\omega=k-\rho$；
- 二者相差 $q-k$，$q=k$ 时相等（$c=1$ 的论文正好在此）。

若论文要与旧框架（`docs/04` 的 $q=\rho+c$）对话，必须写明用的是哪一个。

## 需要改的最小清单

1. §II 的 $\omega$ 定义：改成 $\omega=\rank H$，并写明 $\omega=\rho$；
2. §III 的 (S2)：改成显式假设（或改成横截条件），并注明 $c=1$ 时它由构造保证；
3. 摘要/引言里若出现"$\omega=\dim(V\cap K_0)$"一并改；
4. 附录若用 $\dim(V\cap K_0)=k-1$ 推导纤维维数，检查是否其实只用到了 $V\subseteq U_v^\perp$ 与
   $\dim(V\cap K_0)$ 的假设本身（若是，把假设写明即可）。

复现：`tools/verification/c392_language_alignment.py`（三量对照表）、
`tools/verification/c391_c2_direction_check.py`（$c=2$ 的四例）。
