# C.1 · 特殊族的精确值

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `C.1` 条目（§0.1 归并表）。

## 命题

**C.1（$S=\mathcal J$ 闭包族）** 若 $\operatorname{row}(L_0)=\mathcal J$ 且 $\langle\mathcal J\rangle_A=\mathbb C^n$，则唯一可行解是 $\mathbb C^n$，$q_{\min}=n$。

## 纸面证明

*证明*：$(5a)$ 强制 $\mathcal V$ 是 $A$-不变且 $\supseteq\mathcal J$，故 $\supseteq\langle\mathcal J\rangle_A=\mathbb C^n$。
**用途**：严格推翻 $\dim V+1$（R1）与 $\max(r,\rho^*+1)$（R3）；**不**推翻 $F_3$（R4）。**完整证明** + 用途表：[proof/s_j_family/theorem.md](../s_j_family/theorem.md)；复核 `tools/certificates/c190_invariant_family.py`（$8/8$）。

## Lean

* 等级行引用的 Lean 声明：`C1Closure.c1_of_closure_top`、`c1_finrank`
* 差在哪里：见等级行括注（内核一般只覆盖代数/维数骨架，矩阵实例化多为纸面）

## 精确验证

* 该条暂无独立精确验证脚本（纸面证明 + 支撑目录）。

## 状态与历史

**等级**：[已证] $+$ **[Lean]**（`C1Closure.c1_of_closure_top`：$A$-不变闭包 $=\top$ ⟹ $V=\top$；`c1_finrank` 给 $q_{\min}=n$；闭包用"所有含 $J$ 的 $A$-不变子空间的交"定义）。
* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。



## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F3 |
| 导出等级 | **L4** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— Lean 已覆盖（字面） |


## 支撑目录

[s_j_family/](../s_j_family/README.md)、[layer_31_theorems/](../layer_31_theorems/README.md)、[layer_program/](../layer_program/README.md)、[rho1_layer/](../rho1_layer/README.md)

（本卷宗只汇总证据；支撑目录里的脚本与文档保持原位。）

## 专家复核意见（成立）

闭包论证对 $r\ge2$ 同样成立，不需要标量输出假设。
