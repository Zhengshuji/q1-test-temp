# 748 因子来源定理：$T^{\perp}$ 中的特征向量强制不可行（$d'=k$）

> 2026-11-27。解释 747 中 $B=0\Rightarrow$ 不可行的来源，并推广为一般定理。
> 状态：**[已证-纸面]**。

## 定理

设 $H$ 列满秩（$d'=k$）、$T=\{lW:lN=0\}$、$G=LW$ 的行在 $T$。若存在 $\mu$ 与 $v\ne0$ 使
$$(\mu I-Z')v=0\quad\text{且}\quad v\in T^{\perp}\ (\text{即 }Gv=0),$$
则对**任意** $H$ 与任意行在 $T$ 的 $G$，
$$P(\mu)v=H(\mu I-Z')v-Gv=0\ \Longrightarrow\ \operatorname{rank}P(\mu)\le k-1<d'=k .$$
故 $(5b)$ 在 $\lambda=\mu$ 处失败，**该实例不可行**。

**证明**：$P(\lambda)=\lambda H-HZ'-G=H(\lambda I-Z')-G$。在 $\mu$ 处两项都消掉 $v$：第一项因 $(\mu I-Z')v=0$，第二项因 $G$ 的行在 $T$ 而 $v\in T^\perp$（$Gv=0$）。故 $v\in\ker P(\mu)$，$v\ne0$ ⇒ 秩 $\le k-1$；又 $d'=k$ 要求秩 $=k$，矛盾。$\square$

## 推论：$(\lambda-\mu)\mid\gcd(\text{all }k\text{-minors})$

$\operatorname{rank}P(\mu)<k$ ⇒ 所有 $k$-子式在 $\mu$ 为零 ⇒ $(\lambda-\mu)$ 整除每个 $k$-子式 ⇒ $\gcd\ne1$。这就是 747 的“因子来源”。

## 例子

- **747 的 $B=0$**：$Z'=\begin{bmatrix}a&0\\c&d\end{bmatrix}$、$T=\operatorname{span}\{e_1\}$，故 $T^\perp=\{v:v_1=0\}\ni e_2$；且 $Z'e_2=(0,d)^{\mathsf T}=d\,e_2$ ⇒ $e_2$ 是特征向量 ⇒ 定理适用，$\gcd$ 含 $\lambda-d$（对任意 $g$）。与 747 的 120 例一致。
- **661**：$T=0$ ⇒ $T^\perp=\mathbb C^k$；$Z'$ 的任一特征向量都适用；$d'=k=2$ ⇒ 不可行（与 726/729 一致）。
- **733（可行）**：$Z'=\begin{bmatrix}1&2\\1&1\end{bmatrix}$ 的特征向量满足 $v_1\ne0$（$v=(1,(\lambda-1)/2)$），故 $v\notin T^\perp$；定理不适用，与可行一致。

## 适用范围与限制

- 要求 $d'=k$（$H$ 列满秩）；$d'<k$ 时，$\ker P(\mu)\ne0$ 只给 $\operatorname{rank}\le k-1$，不足以违反 $\operatorname{rank}=d'$；
- 对 $d'<k$ 的类似结论需要“秩降 $k-d'+1$ 维”的条件，尚未证明。

## 意义

- 747 的离散入口量 $B$ 的一般化：不是 $Z'_{12}$ 本身，而是“$Z'$ 是否有特征向量落在 $T^\perp$”；
- 与 705（$\rho_{d'}=1$）并列，构成两类结构性不可行：
  1. 秩/外幂退化（638）；
  2. $T^\perp$ 特征向量（661、747 的 $B=0$）。

## 待办

1. $d'<k$ 的版本：需要 $\dim(\ker P(\mu))\ge k-d'+1$ 的条件；
2. 把“$T^\perp$ 特征向量”写成纯数据判据（$Z'$ 与 $T$ 的可计算条件）；
3. 检验 738 的预筛选链能否加入该判据。

## 状态

- 定理：**[已证-纸面]**；
- 747/661 的解释：**[已证-纸面]**；
- $d'<k$：**[开放]**。
