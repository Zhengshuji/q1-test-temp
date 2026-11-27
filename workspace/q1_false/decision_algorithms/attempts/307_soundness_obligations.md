# sound q1 gate 的三条证明义务；rank forcing 不足以救 303

> 2026-11-10。80 号把问题定位到 soundness。本文件把“sound q1 gadget”写成三条明确义务，
> 并说明一个自然的补救（用固定行强迫自由行非零）为什么不够。
> 状态：**M2（结构分析）**。

## 目标

把 soundness 拆成可检查的义务，并判断“rank forcing”能否救 303。

## 设想与理由

303 的乘法门在 $R=0$ 时仍可行，因为固定行 $H_0,H_{A,0}$ 已在同一个低秩层里，
自由行可以被选为零而不违反 $(5a)(5b)$。
一个自然的补救是：让固定 $H_{A,0}$ 含一个**不在** $\\operatorname{row}H_0$ 的方向，
迫使自由行非零。

## 做法

### 1. sound q1 gate 的三条义务

固定 $A,C,L_0$。称一个压缩模式 $\\mathcal P$ 是 **sound** 的，如果：

- **C（completeness）**：源问题的每个解都能提升为某个可行 $R$；
- **S（soundness）**：每个可行 $R$（包括额外非零行、跨块分量、任意秩层）都解码为源问题的解；
- **R（rank stratum）**：可行 $R$ 的 $\\omega=\\operatorname{rank}H$ 被固定数据强制在预期层，
  或其它层已被证明不可能/不解码。

303 满足 C，但不满足 S；也没有 R。

### 2. rank forcing 的机制

取
$$H_0=\\begin{bmatrix}e_1\\\\e_2\\end{bmatrix},\\qquad
H_{A,0}=e_3.$$
若自由行全零，$H=H_0$，$\\operatorname{row}H=\\operatorname{span}(e_1,e_2)$，
而 $H_{A,0}=e_3\\notin\\operatorname{row}H$，
所以 $(5a)$ 失败。因此 $R=0$ 被排除。

这确实排除了“全零见证”，但**不强制乘法**：自由行可以选择 $e_3$（或含 $e_3$ 的向量），
使 $\\operatorname{row}H=\\mathbb C^3$，于是 $(5a)$ 对所有 $H_A$ 自动成立。
这时 $H_A$ 的任意行都在行空间中，乘法关系不再被强制。

### 3. 结论：rank forcing 只是把“零行”换成“满行”

- 固定行可以排除一个低秩层；
- 但自由行可以跳到更高秩层，使 $(5a)$ 变成空条件；
- $(5b)$ 只要求“ pencil 的秩等于当前的 $\\operatorname{rank}H$”，不要求是预期层；
- 所以“强迫非零”不等于“强迫解码关系”。

## 进展

* 三条义务的明确表述；
* rank forcing 的机制与失败模式；
* 303 的 S 义务缺失被具体化。

## 最终结论

* soundness 不能靠排除 $R=0$ 解决；
* 必须控制**所有**自由行方向和秩层，或者设计局部子空间使只有预期行空间可行；
* 这正是 80 号说的 global incidence realization。

## 放弃原因

* 未构造满足 S 的乘法门；
* 未证明 rank forcing 不可能；
* 未接硬度。

## 残留价值

* 三条义务的检查表；
* rank forcing 的负结果；
* 下一步 global incidence 的入口。

## 相关文件

* [attempts/306](../../../q1_true/multiplication_gate/attempts/306_80_soundness_correction.md)
* [attempts/303](303_79_verdict_lifts.md)
* [attempts/305](../../../q1_true/multiplication_gate/attempts/305_wiring_obstruction.md)

## 状态

* 义务：**[M2 纸面]**。
* sound 乘法门：**[未解决]**。
