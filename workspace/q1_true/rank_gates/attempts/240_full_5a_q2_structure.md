# 完整 $(5a)$ 的 $q=2$ 结构：$u\ne0$ 线性，$u=0$ 才是行列式门

> 2026-11-09。239 的漏行更正后，重新分析 $q=2$ 的完整 $(5a)$：
> $$u=[L_0A],\ x=[l],\ v=[lA]\in Q=(\mathbb C^n)^*/S,\qquad u,v\in\operatorname{span}\{x\}.$$
> 关键区分：$u\ne0$ 时 $x=\alpha u$，条件是**线性**的；只有 $u=0$（即 $L_0A\in S$）时，
> $(5a)$ 才等价于一个**二次行列式** $\det[S;l;lA]=0$。这解释了 234 为什么失败，也指出了正确的门。
> 状态：**M2（结构分析 + 精确实例）**。

## 目标

在完整 $(5a)$ 下找到能编码乘法的 $q=2$ 结构。

## 设想与理由

$S=\operatorname{row}[L_0;CA;C]$，$Q=(\mathbb C^n)^*/S$，$u=[L_0A]$、$x=[l]$、$v=[lA]$。
$(5a)$：$u,v\in\operatorname{span}\{x\}$。

### 1. $u\ne0$：线性

$u\in\operatorname{span}\{x\}$ 迫使 $x=\alpha u$（$\alpha\ne0$）。写 $l=\alpha l_u+s$，$s\in S$。
则
$$v=\alpha[l_uA]+[sA],$$
$[sA]$ 线性于 $s$；条件 $v\in\operatorname{span}\{u\}$ 是 $s$（和 $\alpha$）的**线性**方程。
所以 $u\ne0$ 时 $(5a)$ 是线性的，不能编码乘法。**234 正是这种情形**（专家算出 $b=0,d=0,c\ne0$）。

### 2. $u=0$：二次行列式

若 $L_0A\in S$，则第一个条件是 $0\in\operatorname{span}\{x\}$（自动），只剩
$$v\in\operatorname{span}\{x\}\iff \operatorname{rank}[S;l;lA]=\operatorname{rank}[S;l].$$
当 $\operatorname{rank}S=3$、$l\notin S$ 时，这是
$$\boxed{\det[S;l;lA]=0,}$$
即 $l$ 上的一个**齐次二次型** $D(l)$。在某个坐标归一化（如某坐标 $=1$）下，
$D=0$ 可以变成乘法关系 $z=xy$。

## 做法：一个 $u=0$ 的精确实例

随机搜索满足 $L_0A\in S$、$\operatorname{rank}S=3$ 的 $A,C,L_0$，找到一个：
$$A=\begin{bmatrix}
0&-1&1&0&-1\\
0&-1&-1&-1&0\\
0&-1&0&-1&1\\
-1&0&-1&-1&-1\\
1&1&-1&1&-1
\end{bmatrix},\quad
C=\begin{bmatrix}0&-1&1&-1&1\end{bmatrix},\quad
L_0=\begin{bmatrix}0&1&1&1&-1\end{bmatrix}.$$
则 $S=\operatorname{row}[L_0;CA;C]$ 秩 3，$L_0A\in S$，且
$$D(l)=\det[S;l;lA]=-2\bigl(4a^2+3ab-5ad-2ae+2b^2-bd+3be-de+e^2\bigr),$$
二次型秩 **3**（非零）。

## 进展

* 完整 $(5a)$ 的 $q=2$ 二分：$u\ne0$ 线性、$u=0$ 二次行列式；
* 找到 $u=0$ 的精确实例（二次型秩 3）；
* 明确 234 失败的结构原因（$u\ne0$）。

## 最终结论

* 正确的门必须取 $u=0$（$L_0A\in S$）；
* 门是 $D(l)=\det[S;l;lA]$，在归一化 chart 下可成为 $z=xy$；
* 秩 3 的二次型不足以给出 $z-xy$（后者需要 rank 4 的双曲平面 + 线性项）；需要构造 rank 4 的 $D$。

## 放弃原因

* 未构造 rank 4 的 $D$；
* 未处理 chart/边界（归一化坐标 $=0$ 的分支）；
* 未接 $(5b)$ 守卫。

## 残留价值

* 一个决定性的结构二分（线性 vs 行列式）；
* $u=0$ 的精确实例；
* 明确的 rank 4 目标。

## 相关文件

* [attempts/239](../../multiplication_gate/attempts/239_72_missing_L0A.md)（漏行更正）
* [attempts/234](../../multiplication_gate/attempts/234_explicit_gate.md)（$u\ne0$ 的失败例）
* [72 答复](../../../for_expert/archive/72_conditional_gate_anchored_request-answer.md)

## 状态

* 结构分析：**[M2]**。
* rank4 门：**[未做]**。
