# 669 Theorem U 的两个直接推论：$d=1$ 的重推与 $d=2$ 的 $M$ 结构

> 2026-11-27。用 666/667 的统一判据重推 663，并写出 $d=2$ 时 Bézout 矩阵的显式结构。
> 状态：**[已证-纸面]**。

## 一、$d=1$：Theorem U ⇒ 663

$H=u v^{\mathsf T}$，$H_A=ZH$，$P(\lambda)=(\lambda I-Z)H=(\lambda u-Zu)\,v^{\mathsf T}$。

- 所有 2 阶子式恒为零（$P$ 是秩 $\le1$ 的外积）；
- $P$ 的条目为 $(\lambda u_i-z_i)v_j$，其中 $z=Zu$。因为某个 $v_j\ne0$，条目族的 gcd 等于
  $$\gcd_i(\lambda u_i-z_i)\quad(\text{差非零常数}) .$$
- 该 gcd 为 1 $\iff$ 不存在 $\lambda$ 使 $\lambda u=Zu$ $\iff$ $u$ 不是 $Z$ 的特征向量（$Zu=0$ 时 $\lambda=0$ 是根）。

由 Theorem U：
$$\boxed{(5b)\iff u\ \text{不是}\ Z\ \text{的特征向量}} .$$
$q=1$ 时 $Z$ 是标量、必有特征值 ⇒ 不可行；$q\ge2$ 可取 $Zu=w\notin\operatorname{span}\{u\}$。

再叠加 $(5a)$ 的分析（663 的情形 A/B：$v\in S$ 且 $Z'^{\mathsf T}v\in S$）即得 663 的完整分类。

## 二、$d=2$：$M(H)$ 的显式结构

设 $d$ 阶子式为 $f_i(\lambda)=a_i\lambda^2+b_i\lambda+c_i$（$i=1,\dots,m$），取 $g_i=g_{i0}+g_{i1}\lambda$。则
$$\sum_i g_if_i
=\sum_i\Big[c_ig_{i0}\Big]
+\lambda\sum_i\Big[b_ig_{i0}+c_ig_{i1}\Big]
+\lambda^2\sum_i\Big[a_ig_{i0}+b_ig_{i1}\Big]
+\lambda^3\sum_i\Big[a_ig_{i1}\Big].$$
于是 $M(H)$ 是 $4\times2m$ 的块矩阵，第 $i$ 组两列为
$$\begin{bmatrix}c_i\\ b_i\\ a_i\\ 0\end{bmatrix},\qquad
\begin{bmatrix}0\\ c_i\\ b_i\\ a_i\end{bmatrix},$$
右端 $e_0=(1,0,0,0)^{\mathsf T}$。

$(5b)\iff e_0\in\operatorname{col}M(H)\iff \operatorname{rank}[M\mid e_0]=\operatorname{rank}M$。

## 三、$d=2$ 验证（668）

| 实例 | $m$ | $\operatorname{rank}M$ | $\operatorname{rank}[M\mid e_0]$ | 可解 |
|---|---|---|---|---|
| 638（可行） | 3 | 4 | 4 | 是 |
| 641B（不可行） | 4 | 2 | 3 | 否 |

## 四、结构性观察

- $d=2$ 的 $M$ 是 $4\times2m$，其列成对出现（移位结构），这是“乘以 $g$ 的系数”的 Sylvester 型矩阵；
- 因此 $(5b)$ 是“$e_0$ 是否在 Sylvester 型矩阵的列空间”的线性问题（对固定 $H$）；
- 对变动的 $H$（即 $R$），$a_i,b_i,c_i$ 是 $R$ 的多项式（次数 $\le2$），$e_0$ 的列空间条件是一个行列式条件；
- 这正是 667 的统一系统，不需要为 $d=2$ 单独建立理论。

## 五、下一步

1. 把 $M(H)$ 的列空间条件写成关于 $R$ 的行列式/结式条件（固定 $d$，统一处理）；
2. 检验 663/665 是否能完全由 Theorem U + 结构约束推出（已部分完成）；
3. 研究该条件在 $R$ 上的消元复杂度（这是统一路线的真正瓶颈）。

## 状态

- $d=1$ 重推：**[已证-纸面]**；
- $d=2$ 的 $M$ 结构：**[已证-纸面]**；
- 消元复杂度：**[未做]**。
