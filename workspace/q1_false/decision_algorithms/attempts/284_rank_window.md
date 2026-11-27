> **295 降级**：依赖 282 的吸收性，后者未证；秩窗口只是启发式。

# 可行实例的秩窗口：$\\operatorname{rank}H_0<\\omega<r$ 才可能有二次秩门

> 2026-11-09。由 282（$\\omega\\le r$）与 283（$q=4$ 二分）进一步分析 rank 门的可能性。
> 结论：可行实例必须 $H_0\\subseteq\\operatorname{row}Y$；于是
> $$\\operatorname{rank}H=\\operatorname{rank}Y.$$
> - 若 $\\operatorname{rank}Y=r$（满行秩），$\\omega=r$ 是**开条件**，没有行列式门；
> - 若 $\\operatorname{rank}Y=\\omega<r$，门是 determinantal；
> - 若 $\\operatorname{rank}H_0=\\omega$，则 $H_0\\subseteq\\operatorname{row}Y$ 且 $\\operatorname{rank}Y=\\omega$
>   迫使 $\\operatorname{row}Y=\\operatorname{row}H_0$，条件是**线性**的；
> - 因此二次秩门只可能在
>   $$\\boxed{\\operatorname{rank}H_0<\\omega<r.}$$
> 状态：**M2（结构分析）**。

## 目标

确定 Route A 的 rank 门在哪些秩窗口可能非平凡。

## 设想与理由

282 给 $\\omega\\le r$，并证明可行 ⇒ $H_0\\subseteq\\operatorname{row}Y$。
$H=[H_0;Y]$，故 $\\operatorname{rank}H=\\operatorname{rank}Y$。

## 做法：窗口分类

### 1. $\\omega=r$

$\\operatorname{rank}Y=r$ 是开条件（$Y$ 的某个 $r\\times r$ 子式非零）。
没有“$\\det=0$”型门；$(5b)$ 只能作为谱 guard。

### 2. $\\omega<r$ 且 $\\operatorname{rank}H_0=\\omega$

$H_0\\subseteq\\operatorname{row}Y$ 且 $\\operatorname{rank}H_0=\\omega=\\operatorname{rank}Y$ ⇒
$\\operatorname{row}Y=\\operatorname{row}H_0$。
这等价于 $Y$ 的每一行都在固定 $\\omega$-平面 $\\operatorname{row}H_0$ 内，是**线性**条件，
不是二次门。

### 3. $\\operatorname{rank}H_0<\\omega<r$

此时 $\\operatorname{row}Y$ 是含 $H_0$ 的 $\\omega$-平面，$H_0$ 的秩严格小于 $\\omega$；
在商空间 $\\mathbb C^k/\\operatorname{row}H_0$ 中，$Y$ 的像张成一个 $(\\omega-\\operatorname{rank}H_0)$ 维子空间。
这是 Grassmannian 条件，可能给二次/高次门。

**最小窗口**：
$$r=3,\\ \\operatorname{rank}H_0=1,\\ \\omega=2.$$
例如 $q=5,r_0=2$ 但 $H_0$ 秩 1；或 $q=4,r_0=1$ 但 283 的独立/吸收二分已排除（$q=4$ 时 $\\omega=3$ 或 $\\omega$ 满）。

## 对 Route A 的含义

- 之前 275/281 的 $q=4,\\omega=3$ 落在 $\\omega=r$ 或 $\\operatorname{rank}H_0=\\omega$ 的坏窗口；
- 新设计应取 $q\\ge5$、$r_0$ 使 $\\operatorname{rank}H_0=1$、$\\omega=2<r$；
- 门的次数由商空间 Plücker 坐标决定，可能是二次。

## 进展

* 可行实例的秩窗口分类；
* 明确二次门只可能在 $\\operatorname{rank}H_0<\\omega<r$；
* 最小候选 $r=3,\\operatorname{rank}H_0=1,\\omega=2$。

## 最终结论

* Route A 的 rank 门没有被 282/283 完全排除，但窗口很窄；
* 下一步应在 $r=3,\\operatorname{rank}H_0=1,\\omega=2$ 构造压缩门；
* 若该窗口也只能给线性/开条件，则 rank 门整体关闭。

## 放弃原因

* 未构造窗口内的门；
* 未检查 $q=5,r_0=2$ 的 $H_0$ 秩 1 实现。

## 残留价值

* 一个清晰的秩窗口；
* 把搜索空间从 $q=4$ 移到 $q\\ge5$；
* 与 282/283 一致。

## 相关文件

* [attempts/282](282_omega_le_r.md)
* [attempts/283](../../../q1_true/rank_gates/attempts/283_q4_r1_dichotomy.md)
* [attempts/275](275_rankone_section_gate.md)

## 状态

* 窗口分类：**[M2 纸面]**。
* 最小窗口构造：**[未做]**。
