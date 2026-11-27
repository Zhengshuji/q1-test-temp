> **295 降级**：依赖 282 的 $\omega\le r$，后者未证；本文件只是条件性观察。

# $q=4,r_0=1,\\omega=3$：固定行独立则谱失败，固定行被吸收则秩门消失

> 2026-11-09。检查满足 $\\omega\\le r$ 的最小候选 $q=4,r_0=1,r=3,\\omega=3$。
> 结论：两种情形都不支持 275 型 rank-one 行列式门：
> - $H_0$ 与 $Y$ 独立：$\\operatorname{rank}H=1+\\operatorname{rank}Y$，$\\omega=3$ 迫使 $\\operatorname{rank}Y=2$，
>   在固定行特征值处 $\\operatorname{rank}P\\le2<3$；
> - $H_0$ 被 $Y$ 吸收：$\\operatorname{rank}H=\\operatorname{rank}Y\\le3$，$\\omega=3$ 是**开条件**（$Y$ 行满秩），
>   没有行列式门；任何门只能来自 $(5b)$ 的谱分支。
> 状态：**M2（结构分析）**。

## 目标

判断 $q=4,r_0=1,\\omega=3$ 能否承载 rank-one 行列式门。

## 设想与理由

282 给 $\\omega\\le r$；$q=4,r_0=1$ 时 $r=3$，所以 $\\omega=3$ 是允许的边界。
$H=[H_0;Y]$，$H_0$ 是 $1\\times k$，$Y$ 是 $3\\times k$。

## 做法：两种情形

### 1. $H_0\\notin\\operatorname{row}Y$（独立）

$$\\operatorname{rank}H=1+\\operatorname{rank}Y.$$
$\\omega=3$ ⇒ $\\operatorname{rank}Y=2$。
$H_{A,0}=\\alpha H_0$（$1\\times1$），在 $\\lambda=\\alpha$ 处固定行 $P$ 为零；
自由行 $\\lambda Y-H_{A,\\rm free}$ 秩 $\\le\\operatorname{rank}Y=2$。所以
$$\\operatorname{rank}P(\\alpha)\\le2<3,$$
$(5b)$ 失败，与 282 的独立情形一致。

### 2. $H_0\\in\\operatorname{row}Y$（吸收）

$$\\operatorname{rank}H=\\operatorname{rank}Y\\le3.$$
$\\omega=3$ 等价于 $Y$ 行满秩（$3\\times k$ 的秩 3），这是一个**开条件**，不是行列式方程。
所以在压缩层上：
- 没有由 $\\operatorname{rank}H=3$ 产生的行列式门；
- $(5a)$ 也因 $H_0\\subset\\operatorname{row}Y$ 而自动；
- 唯一的约束是 $(5b)$ 的谱条件。

因此 275 型“rank-one 行列式门”在 $q=4,r_0=1,\\omega=3$ 下不存在：
要么独立（谱失败），要么吸收（秩门消失）。

## 进展

* $q=4,r_0=1$ 的二分；
* 独立情形被 282 排除；
* 吸收情形没有秩门，只能做谱门。

## 最终结论

* $q=4$ 的 rank-one 行列式门（$r_0=1$ 或 $2$）都不成立：
  - $r_0=2$：$\\omega\\le2<3$（282）；
  - $r_0=1$：独立失败，吸收则无秩门（283）。
* 下一档是 $q\\ge5$；或者放弃“秩门”，改做 $(5b)$ 的谱门。

## 放弃原因

* 未构造 $q\\ge5$ 的门；
* 未构造谱门；
* 未处理 $k>4$ 的 rank-one 截面。

## 残留价值

* 关闭 $q=4$ 的 rank-one 门；
* 明确“吸收 ⇒ 无秩门”的机制；
* 下一步的 $q\\ge5$ 约束。

## 相关文件

* [attempts/282](../../../q1_false/decision_algorithms/attempts/282_omega_le_r.md)
* [attempts/275](../../../q1_false/decision_algorithms/attempts/275_rankone_section_gate.md)
* [attempts/281](281_q4_gate_not_liftable.md)

## 状态

* 分析：**[M2 纸面]**。
* $q\\ge5$ 门：**[未构造]**。
