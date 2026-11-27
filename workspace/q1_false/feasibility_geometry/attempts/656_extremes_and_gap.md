# 656 极端情形与中间缺口

> 2026-11-27。整理 655 的条件化充分性在两个极端情形的已知结论，并指出中间情形是缺口。
> 状态：**[已证-纸面]**（极端情形）+ **[开放]**（中间）。

## 极端情形一：$S=\mathbb C^k$（$s=k$）

$K=S^\perp=0$ ⇒ $K_\infty=0$、$T_\infty=0$、$d=k$。
$\mathcal G$ 的约束只剩 $U_0\subseteq U\subseteq\mathbb C^k$、$\dim U=k$ ⇒ $U=\mathbb C^k$、需要 $U_0=0$？

不要求 $U_0=0$：$U$ 是 $k$ 维全空间，总包含 $U_0$。
631 已证：$W$ 满行秩、$q>r_0$、$q-1\le k$ 时可行。所以条件化充分性在此成立（构造见 631）。

## 极端情形二：$S=0$（$s=0$）

$K=\mathbb C^k$ ⇒ $K_\infty=\mathbb C^k$ ⇒ $T_\infty=\mathbb C^k$、$d=0$。
$\mathcal G$ 只含 $U=0$；需要 $U_0=0$ 即 $H_0=0$。
此时可行（$L=0$），否则不可行（629）——条件化充分性成立。

## 中间情形（$0<s<k$）：缺口

$\mathcal G$ 非空需要 $U_0\subseteq U\subseteq T_\infty^\perp$、$\dim U=d$、$UZ'\subseteq U+S$。
条件化充分性要求每个这样的 $U$ 都能配上 $H,Z$ 满足扩展方程与避让。**未证明**。

## 维数观察

- $T_\infty=0$ 需要 $K_\infty=0$，即 $\bigcap_j(Z')^{-j}K=0$。对 $k=3$、$s=1$（$K$ 为 2 维）：
  两个 2 维子空间必相交 ⇒ $K_\infty\ge1$ ⇒ $T_\infty\ne0$。
  所以 $T_\infty=0$ 至少需要 $s\ge k/2$（粗略）。
- 这解释了为什么中间情形（$s$ 小）总被 $T_\infty$ 占去大部分空间。

## 小例子（待验证）

$k=2$、$q=3$、$S=\operatorname{span}\{e_1\}$、$Z'=\begin{bmatrix}0&0\\1&0\end{bmatrix}$：
$K=\operatorname{span}\{e_2\}$、$(Z')^{-1}K=\operatorname{span}\{e_1\}$、$K_\infty=0$ ⇒ $T_\infty=0$、$d=2$。
取 $H=\begin{bmatrix}1&0\\0&1\\0&0\end{bmatrix}$（$U=\operatorname{span}\{e_1,e_2\}$，$U+S=U$）：
$H_1Z'=0\in U$ ✓，$H_2Z'=e_1\in U$ ✓ ⇒ 逐行可解。
是否存在 $Z$ 使避让条件成立？待数值/构造验证。

## 下一步

1. 完成 $k=2$ 小例子的构造（或证明不存在）；
2. 若存在，作为中间情形的第一个正面证据；
3. 再尝试一般证明。

## 状态

- 极端情形：**[已证-纸面]**；
- 中间情形：**[开放]**。
