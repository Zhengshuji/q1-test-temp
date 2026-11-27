# 587 584 的判据错误：$\omega=2$ 时 $\det P$ 必须恒为零

> 2026-11-27。复查 584：那里按“$\det P$ 恒非零”分析，但 $\omega=2$、$q=3$ 时判据是
> $\operatorname{rank}P=2$，即 $\det P\equiv0$ **且** 某个 $2\times2$ 子式恒非零。
> **结论：584 的构造恒不可行（$\det P\equiv0$ 需要 $1=0$）。**
> 状态：**[已证-纸面]**。

## 584 的 $P$

$$P(\lambda)=\begin{bmatrix}\lambda r_1-1&\lambda z&0\\\lambda&\lambda r_2-1&0\\0&0&-1\end{bmatrix},\qquad
\det P=-\big[\lambda^2(r_1r_2-z)-\lambda(r_1+r_2)+1\big].$$

## 正确判据（$\omega=2$）

$\operatorname{rank}P=2$ 对所有 $\lambda$ $\iff$
1. $\det P\equiv0$（$\operatorname{rank}\le2$）；
2. 某个 $2\times2$ 子式的 gcd 为常数（$\operatorname{rank}\ge2$）。

$\det P\equiv0$ 要求
$$r_1r_2=z,\qquad r_1+r_2=0,\qquad 1=0 .$$
第三式不可能 ⇒ **584 的构造恒不可行**。

## 教训

- 对 $3\times3$ 的 $P$、$\omega=2$：$\det P$ 必须**恒为零**（不是“恒非零”）；
- 584/585 的分析基于“$\det$ 恒非零”，只适用于 $\omega=3$（而 $q=\omega=3$ 已被 586 排除）；
- 正确的 3×3 路线是：让 $\det P\equiv0$ 的系数条件中**一个**成为门（如 $r_1r_2-z=0$），
  其余系数条件恒为零（由 $a_i$ 的设计保证）。

## 下一步

取 $a_3=0$（则 $\det(a)=0$，常数项自动为零），计算
$$\det P=\lambda^3\det H-\lambda^2\big(\det(h_1,h_2,a_3)+\cdots\big)+\lambda\det(a_1,a_2,h_3),$$
设计 $a_1,a_2,h_i$ 使 $\lambda$ 与 $\lambda^2$ 系数都恒为零、只剩 $r_1r_2-z$ 进入某个 $2\times2$ 子式。

## 状态

- 584 的判据错误：**[已证-纸面]**；
- 正确路线：**[未做]**。
