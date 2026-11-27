> **295 撤回（78 审计）**：$L_0A$ 可在 row[L0;R;CA;C] 中（含 R），故 $H_{A,0}=M H_0$ 不成立；相交情形推理也错。$\omega\le r$ 未证，$q=4$ 不可能性未证。

# 必要条件 $\\omega\\le r=q-r_0$：固定行必须被自由行“吸收”

> 2026-11-09。由 $H_{A,0}=M H_0$ 与谱判据得到一个一般性必要条件：
> $$\\boxed{\\omega=\\operatorname{rank}H\\ \\le\\ r=q-r_0.}$$
> 也就是说，固定行 $L_0$ 不能在 $H$ 中独立于自由行；否则在 $M$ 的特征值处 $(5b)$ 必失败。
> 推论：$q=4,r_0=2,\\omega=3$ **不可能**，275/281 的架构不能落地。
> 状态：**M2（纸面）**。

## 目标

给出 $(5a)(5b)$ 对固定行/自由行秩的必要条件。

## 设想与理由

$(5a)$ 给 $H_A=FH$。固定行 $L_0A\\in S=\\operatorname{row}[L_0;CA;C]$，右乘 $N$（$N$ 张成 $\\ker[C;CA]$）：
$$H_{A,0}=M H_0.$$
于是 $\\operatorname{row}H_0$ 在 $M$ 下不变；$M$ 在 $\\mathbb C$ 上有特征值。

## 做法：定理

设 $H=[H_0;Y]$，$H_0=L_0N$，$Y=RN$，$r=q-r_0$，$\\omega=\\operatorname{rank}H$。

**定理**：若 $(5a)(5b)$ 同时成立，则
$$\\omega\\le r.$$

*证明*：分两种情形。

**情形 1：$\\operatorname{row}H_0\\cap\\operatorname{row}Y=0$（独立）**。
则 $\\operatorname{rank}H=\\operatorname{rank}H_0+\\operatorname{rank}Y$。
$H_{A,0}=M H_0$，$M$ 在 $\\operatorname{row}H_0$ 上有特征值 $\\lambda$，故
$$\\operatorname{rank}(\\lambda I-M)H_0\\le\\operatorname{rank}H_0-1.$$
自由行的 $P$ 行为 $\\lambda Y-H_{A,\\rm free}$，秩 $\\le\\operatorname{rank}Y$。
所以
$$\\operatorname{rank}P(\\lambda)\\le(\\operatorname{rank}H_0-1)+\\operatorname{rank}Y
=\\operatorname{rank}H-1<\\omega,$$
与 $(5b)$ 矛盾。

**情形 2：$\\operatorname{row}H_0\\cap\\operatorname{row}Y\\ne0$（相关）**。
则
$$\\operatorname{rank}H=\\operatorname{rank}(\\operatorname{row}H_0+\\operatorname{row}Y)\\le\\operatorname{rank}Y\\le r.$$
所以 $\\omega\\le r$。$\\square$

**推论 1**：$q=4,r_0=2$ 时 $r=2$，故 $\\omega\\le2$；$\\omega=3$ 不可能。
275/281 的 $q=4,\\omega=3$ 架构不能落地。

**推论 2**：$q=2,r_0=1$ 时 $r=1$，故 $\\omega\\le1$；$\\omega=2$ 不可能（与 245 一致）。

**推论 3**：固定行必须被自由行“吸收”：
$$\\operatorname{row}H_0\\subseteq\\operatorname{row}Y.$$
否则独立情形给矛盾。

## 与已有结果的关系

- 245 的 $q=2$ no-go 是 $\\omega\\le r$ 的特例；
- 244 的 $q=3,r_0=1,\\omega=2$ 满足 $\\omega\\le r=2$；
- 228 的 10 维族 $q=3,r_0=1,r=2,\\omega=2$ 也满足；
- 275/281 的 $q=4,r_0=2,\\omega=3$ 被排除。

## 进展

* 一个一般的必要条件 $\\omega\\le q-r_0$；
* 解释了 275/281 为什么不可落地；
* 统一了 $q=2$ 与 $q=4$ 的障碍。

## 最终结论

* Route A 必须满足 $\\omega\\le r$，即固定行被自由行吸收；
* $q=4,r_0=2,\\omega=3$ 关闭；
* 新设计应在 $\\omega\\le r$ 的范围内（例如 $q=5,r_0=2,r=3,\\omega\\le3$）。

## 放弃原因

* 未构造满足 $\\omega\\le r$ 的新门；
* 未检查 $\\omega=r$ 的边界。

## 残留价值

* 一个强必要条件；
* 排除了 275/281 架构；
* 为 Route A 的新维度给出约束。

## 相关文件

* [attempts/275](275_rankone_section_gate.md)
* [attempts/281](../../../q1_true/rank_gates/attempts/281_q4_gate_not_liftable.md)
* [attempts/245](../../../q1_true/rank_gates/attempts/245_q2_no_gate_theorem.md)

## 状态

* 定理：**[M2 纸面]**。
* 新门：**[未构造]**。
