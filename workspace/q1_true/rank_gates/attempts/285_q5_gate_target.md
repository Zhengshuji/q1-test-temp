# $q=5$ 候选门：$H_0$ 秩 1、$Y$ 三行给 $z=xy$；但 $E=0$ 被 205 排除

> 2026-11-09。按 284 的最小窗口（$r=3,\\operatorname{rank}H_0=1,\\omega=2$）构造压缩门：
> $$H_0=[e_1;e_1],\\quad
> Y=\\begin{bmatrix}e_1\\\\(0,0,1,x)\\\\(0,0,y,z)\\end{bmatrix}.$$
> 则 $H$ 的 $3\\times3$ 子式
> $$\\det\\begin{bmatrix}1&0&0\\\\0&1&x\\\\0&y&z\\end{bmatrix}=z-xy,$$
> 所以 $\\operatorname{rank}H=3\\iff z\\ne xy$，门是 $z=xy$。
> 但若取 $E=0$（$A(K_0)\\subseteq K_0$），205 的刚性给出 $(5a)(5b)$ 不可行。
> 状态：**M2（构造目标 + 障碍）**。

## 目标

在 $q=5,r_0=2,r=3,\\operatorname{rank}H_0=1,\\omega=2$ 的窗口里构造门。

## 设想与理由

284 说二次门只可能在 $\\operatorname{rank}H_0<\\omega<r$。最小是 $r=3$、$\\operatorname{rank}H_0=1$、$\omega=2$。
取 $H_0$ 两行都是 $e_1$（秩 1），$Y$ 三行张成含 $e_1$ 的平面；平面条件给一个 $2\\times2$ 行列式。

## 做法

### 1. 压缩门

$$H=\\begin{bmatrix}
1&0&0&0\\\\
1&0&0&0\\\\
1&0&0&0\\\\
0&0&1&x\\\\
0&0&y&z
\\end{bmatrix}.$$
（这里 $Y_1=e_1$ 与 $H_0$ 重复，$H$ 的秩为 3 当且仅当 $z\\ne xy$；门是 $z=xy$。）

精确验证：$3\\times3$ 子式 $\\det[[1,0,0],[0,1,x],[0,y,z]]=z-xy$。

### 2. $E=0$ 的障碍

若 $A(K_0)\\subseteq K_0$，205 的定理说：$\\omega>0$ 时 $(5a)(5b)$ 不可行。
证明思路：可行 $V$ 必 $A$-不变，$\\operatorname{row}H=V^\\perp$ 含 $A^{\\mathsf T}$ 特征向量 $l$，
于是 $P(\\lambda)$ 行相关，$(5b)$ 失败。

所以本候选门的自然实现（$E=0$）被排除。

### 3. 需要 $E\\ne0$

要落地，必须让 $E=(I-NN^+)AN\\ne0$，同时：
- 固定行 $H_{A,0}$ 仍在 $\\operatorname{row}H$；
- 自由行 $H_{A,\\rm free}$ 逐行可提升（$r_iAN$）；
- $P(\\lambda)$ 在门 $z=xy$ 上秩恒为 2。

这是下一步的构造目标。

## 进展

* 最小窗口的显式压缩门 $z=xy$；
* $E=0$ 被 205 排除；
* 明确 $E\\ne0$ 的三个约束。

## 最终结论

* $q=5$ 窗口有干净的压缩乘法门；
* 但自然实现 $E=0$ 不可行；
* 下一步是 $E\\ne0$ 的逐行可提升构造。

## 放弃原因

* 未构造 $E\\ne0$ 的完整实例；
* 未验证 $(5b)$；
* 未处理 $E$ 对固定行/自由行的同时影响。

## 残留价值

* 一个干净的 $z=xy$ 压缩门；
* 明确 $E=0$ 的死因（205）；
* 下一步的约束清单。

## 相关文件

* [attempts/284](../../../q1_false/decision_algorithms/attempts/284_rank_window.md)
* [attempts/205](../../multiplication_gate/attempts/205_AinvK0_impossible.md)
* [attempts/281](281_q4_gate_not_liftable.md)

## 状态

* 压缩门：**[M2 + 精确恒等式]**。
* $E\\ne0$ 实例：**[未构造]**。
