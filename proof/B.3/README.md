# B.3 · $\rho=0$ 层

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `B.3` 条目（§0.1 归并表）。

## 命题

**B.3（$\rho=0$ 层）** $\rho=0\iff\mathcal V\subseteq\mathcal J$；此时 $(5a)\iff S\subseteq\mathcal J$ 且 $SA\subseteq\mathcal J$，且 $(5b)$ 自动。

## 纸面证明

*证明*：$\rho=0\iff$ 商像为零；若 $S,SA\subseteq\mathcal J$ 取 $\mathcal V=S$ 即得 $(5a)$，而 $\lambda\mathcal L-\mathcal LA$ 的行全在 $\mathcal J$ 里，故 $(5b)$ 的秩恒为 $\dim\mathcal J$；反之 $(5a)$ 给 $SA\subseteq\mathcal V A\subseteq\mathcal J$。
位置：[proof/rho0_layer/](../rho0_layer/README.md)。

## Lean

* 等级行引用的 Lean 声明：`Rho0Layer.rho_zero_iff`、`Rho0Layer.five_a_of_le`、`Rho0Layer.five_b_auto`
* 差在哪里：见等级行括注（内核一般只覆盖代数/维数骨架，矩阵实例化多为纸面）

## 精确验证

* 该条暂无独立精确验证脚本（纸面证明 + 支撑目录）。

## 状态与历史

**等级**：[已证] $+$ **[Lean]**（`Rho0Layer.rho_zero_iff`：$\pi_J V=\bot\iff V\le J$；`Rho0Layer.five_a_of_le`：$V\le J$ 时 $(5a)\iff AV\le J$；`Rho0Layer.five_b_auto`：$V\le J$ 且 $AV\le J$ ⟹ 每个 $\lambda$ 的 $(5b)$ 自动）。
* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。





## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F3 |
| 导出等级 | **L4** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— Lean 已覆盖（字面） |


## 支撑目录

[rho0_layer/](../rho0_layer/README.md)

（本卷宗只汇总证据；支撑目录里的脚本与文档保持原位。）

## 专家复核意见（成立）

$\rho=0$ 的等价本身**不需要** $L_0\ne0$；该假设属全局观测器假设，与本论证无关。
