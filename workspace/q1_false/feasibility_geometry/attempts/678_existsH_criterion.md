# 678 可行性的 $\exists H$ 判据：$D_{d'}$ 在 $G$ 空间上不恒为零
> **更正（685）**：$G\in S^q$ 不自由；$(5a)$ 还要求 $H_iZ'+G_i\in\operatorname{row}(H)$（等价 $G_i\in S\cap(U-H_iZ')$）。本文件的判据应加此仿射约束；$661$ 的 $q=2$ 不可行正是该约束导致 $G=0$。


> 2026-11-27。把 677 的满秩判据与 $(5a)$ 的自由度结合，写出 q1 可行性的统一代数判据。
> 状态：**[已证-纸面]**。

## 自由度回顾

$H=LN$、$H_A=LAN$，$AN=NZ'+W$，$S=\operatorname{row}(W)$。令 $G=LW$，则
$$H_A=HZ'+G,\qquad \operatorname{row}(G)\subseteq S .$$
反之，任给 $H$（$q\times k$）与 $G\in S^q$，可取 $L$ 使 $LN=H$、$LW=G$（逐行：$lW$ 取遍 $S$），故 $(H,G)$ 与 $(H,L)$ 的可行组合一一对应。

于是变量是
$$H\in\mathbb C^{q\times k}\ (\text{前 }r_0\text{ 行}=H_0),\qquad G\in S^q .$$

## 定理（可行性判据）

设 $d'=\operatorname{rank}H$（$d'\ge\operatorname{rank}H_0$），$f_i$ 为 $\lambda H-H_A=\lambda H-HZ'-G$ 的全部 $d'$-子式，$M(H,G)$ 为对应的 Bézout 矩阵（$2d'\times md'$），
$$D_{d'}(H,G)=\sum_{|I|=2d'}\big|\det M(H,G)_I\big|^2 .$$
则
$$\boxed{\text{可行}\iff\exists H\ (\operatorname{rank}H=d',\ \text{前 }r_0\text{ 行}=H_0):\ D_{d'}(H,\cdot)\not\equiv0\ \text{on }S^q .}$$

**证明**：固定 $H$，由 677，$(5b)$ 成立 $\iff$ $\operatorname{rank}M(H,G)=2d'$ $\iff$ $D_{d'}(H,G)\ne0$。
$G$ 在仿射空间 $S^q$ 自由；存在 $G$ 使 $D\ne0$ $\iff$ 多项式 $D_{d'}(H,\cdot)$ 不恒为零。再对 $H$ 取存在。$\square$

## 两种情形

1. **$q=r_0$（无自由行）**：$H=H_0$、$G=L_0W$ 都固定，判据退化为单点检查
   $$D_{d'}(H_0,L_0W)\ne0,$$
   即对固定铅笔算一次 $\operatorname{rank}M=2d'$——多项式时间可做；
2. **$q>r_0$（有自由行）**：$H$ 的自由行与 $G$ 都可变，判据是“$D_{d'}$ 在秩 $d'$ 的确定簇上不恒为零”。

## 检验

- **661**：$k=q=2$、$d'=2$、$m=1$；$M$ 为 $4\times2$，$\operatorname{rank}\le2<4$，故 $D_2\equiv0$ 对一切 $H,G$ ⇒ 不可行 ✓；
- **638**：$D_2\not\equiv0$（668：$\operatorname{rank}M=4$）⇒ 可行 ✓；
- **629**（$S=0$）：$G=0$，判据退化为固定 $H$ 的检查；$W=0$ 时 $m$ 结构与 629 的结论一致（$H_0\ne0$ 不可行）。

## 意义

- 可行性从“逐 $d$ 的几何分类”化为**一个多项式在确定簇上是否恒为零**；
- 无自由行时是多项式时间；有自由行时是代数几何/消元问题；
- 这与 672 的“一般层/退化层分裂”一致：$D\not\equiv0$ 即一般层可行。

## 仍未解决

1. 判定“$D_{d'}$ 在秩 $d'$ 的确定簇（含 $H_0$ 行约束）上是否恒为零”的复杂度；
2. $d'$ 的选取（从 $\operatorname{rank}H_0$ 到 $\min(q,k)$）；
3. 实可行性与位长；
4. 与 Paper III/IV 的层化对接。

## 状态

- 判据：**[已证-纸面]**；
- 恒零判定的复杂度：**[未做]**。
