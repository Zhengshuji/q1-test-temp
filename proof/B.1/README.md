# B.1 · 商铅笔等价

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `B.1` 条目（§0.1 归并表）。

## 命题

**B.1（商铅笔）** $(5b)\iff\operatorname{rank}Q_{\mathcal V}(\lambda)=\rho\ \forall\lambda$，$Q_{\mathcal V}(\lambda)=\lambda\pi(\mathcal L)-\pi(\mathcal LA)$。

## 纸面证明

*证明*：对 $\mathcal J$ 取商，秩条件变成 $\operatorname{rank}(\lambda\pi(\mathcal L)-\pi(\mathcal LA))=\dim\pi(\mathcal V)$。
位置：[proof/pencil_equivalence/](../pencil_equivalence/README.md)。

## Lean

* 等级行引用的 Lean 声明：`PencilEquivalence.pencil_rank_forall`、`pencil_rank_eq`、`finrank_sup_eq_add_quotient`、`AlphaBridge.alpha_matrix_rank_row`
* 差在哪里：见等级行括注（内核一般只覆盖代数/维数骨架，矩阵实例化多为纸面）

## 精确验证

* 该条暂无独立精确验证脚本（纸面证明 + 支撑目录）。

## 状态与历史

**等级**：[已证] $+$ **[Lean]**（`PencilEquivalence.pencil_rank_forall` = 本条原句；逐 $\lambda$ 版 `pencil_rank_eq`；核心恒等式 `finrank_sup_eq_add_quotient`：$\dim(W\sqcup J)=\dim J+\dim\pi_J(W)$。$\operatorname{rank}$ 用 $\dim$ 行空间写，依据 `AlphaBridge.alpha_matrix_rank_row`）。
* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。





## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F3 |
| 导出等级 | **L4** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— Lean 已覆盖（字面） |


## 支撑目录

[pencil_equivalence/](../pencil_equivalence/README.md)

（本卷宗只汇总证据；支撑目录里的脚本与文档保持原位。）

## 专家复核意见（成立）

在 $(5a)$ 下逐点成立，包括商铅笔可能退化的 $\lambda$；不需要 $q=t$。
