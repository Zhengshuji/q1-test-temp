# 653 $Z$ 构造引理化为两个条件
> **审计注（729）**：$G=LW$ 的固定-$H$ 可达空间是 $T=\{lW:lN=0\}\subseteq S$；本文若把 $G\in S$ 当作可实现判据，需加 $T=S$ 或改用 $T$。


> 2026-11-27。把 652 的“$Z$ 构造引理”拆成可检验的线性条件。
> 状态：**[已证-纸面]**（逐行可解性与自由度分析）+ **[开放]**（第二条件）。

## 设定

固定 $H$（秩 $d$，$H|_T=0$，含 $H_0$），$U=\operatorname{row}(H)$（$\dim d$），$V=\operatorname{im}H$。
求 $Z\in\mathbb C^{q\times q}$ 使
$$ZH-HZ'=G,\qquad \operatorname{row}(G)\subseteq S .$$

## 逐行可解性

第 $i$ 行：$Z_iH=H_iZ'+s_i$（$s_i\in S$）。$Z_iH$ 随 $Z_i\in\mathbb C^q$ 取遍 $U$。所以
$$\text{第 }i\text{ 行有解}\iff H_iZ'\in U+S\quad\left(\iff HZ'\text{ 的每行}\in U+S\right).$$
记 $W=U+S$。

## 自由度

若逐行可解，$Z_i$ 确定到 $Z_i+\kappa_i$（$\kappa_iH=0$），共 $q(q-d)$ 维自由。
但 $\kappa H=0$ ⇒ $\kappa$ 在 $V=\operatorname{im}H$ 上为零：**这些自由不改变 $Z|_V$**。
而
$$Z(Hx)=HZ'x+Gx,$$
所以 $Z|_V$ 只由 $G$（行在 $S$ 内）决定。

## 第二条件（特征向量避让）

$$\forall x\ne0,\ \forall\lambda:\quad HZ'x+Gx\ne\lambda Hx .$$
$G$ 的自由度是 $q\cdot\dim S$ 维；这是开条件，通常非空，除非被第一条件强制。

## 检验：638

$T=\operatorname{span}\{e_3\}$、$U=\operatorname{span}\{e_1,e_2\}$、$S=\operatorname{span}\{e_2\}$、$Z'=\begin{bmatrix}0&0&0\\1&0&0\\0&0&0\end{bmatrix}$。
$e_1Z'=(0,0,0)\in U$ ✓；$e_2Z'=(1,0,0)=e_1\in U$ ✓。所以 $UZ'\subseteq U\subseteq U+S$ ✓，逐行可解。
638 的构造同时满足第二条件（gcd=1）。

## 与 $T_\infty$ 的关系（待证）

**猜想**：当 $U\subseteq T_\infty^\perp$、$\dim U=d=k-\dim T_\infty$ 时，
$$UZ'\subseteq U+S .$$
若成立，则第一条件自动；充分性只剩第二条件（开条件）。

## 下一步

1. 证明 $UZ'\subseteq U+S$（用 $T_\infty$ 的递推：$Z'(T_\infty\cap S^\perp)\subseteq T_\infty$ 之类）；
2. 证明第二条件在 $G\in S^q$ 中可满足（维数计数或显式构造）；
3. 合成充分性定理。

## 状态

- 逐行可解性与自由度：**[已证-纸面]**；
- $UZ'\subseteq U+S$ 的自动性：**[M2 猜想]**；
- 第二条件：**[开放]**。
