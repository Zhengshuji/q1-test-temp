# F.1 · 秩屏障

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `F.1` 条目（§0.1 归并表）。

## 命题

**F.1（a）〔原 F.1〕（秩屏障）** 设 $\mathcal L$ 是层 $(\rho,c)$ 的任一候选（$\rho=\dim\pi(\mathcal V)$、$c=\dim(\mathcal V\cap\mathcal J)$）。
对 $\lambda_0\in\mathbb C$ 记
$$r(\lambda_0):=\dim\pi\big(\mathbb C^n(\lambda_0I-A)\big)=\operatorname{rank}[\lambda_0I-A;\,C;\,CA]-j .$$
则：**若 $(5b)$ 在 $\lambda_0$ 处成立，必有 $\rho\le r(\lambda_0)$。**
特别地，若 $\rho>\min_{\lambda}r(\lambda)$，该层**不可行**。

## 纸面证明

*证明*：$\lambda_0\mathcal L-\mathcal LA=\mathcal L(\lambda_0I-A)$，故其行空间含于 $\mathbb C^n(\lambda_0I-A)$，于是
$\operatorname{rank}[\lambda_0\mathcal L-\mathcal LA;CA;C]=\dim(\operatorname{row}(\mathcal L)(\lambda_0I-A)+\mathcal J)\le j+r(\lambda_0)$；
而 $(5b)$ 在该处要求左端 $=\operatorname{rank}[\mathcal L;CA;C]=j+\rho$。$\square$

即本条陈述；内核 `RankBarrier.rank_barrier`。差异：$r(\lambda)$ 在 Lean 里写成 $\dim\pi_J(\operatorname{range}(\lambda I-A))$，
未与"$\operatorname{rank}[\lambda I-A;C;CA]-j$"显式等同——见 [STATEMENT_MAP](../../tools/lean/STATEMENT_MAP.md)）。
**位置**：[proof/rank_barrier/](../rank_barrier/README.md)；

**F.1（b）〔原 F.2〕（无解判据）** 若 $\min_{\lambda}r(\lambda)<\rho_{ci}$，则原问题**没有解**。
*证明*：任何解满足 $\rho\ge\rho_{ci}$（E.1）与 $\rho\le\min_\lambda r(\lambda)$（F.1），矛盾。$\square$


**注**：$\lambda\notin\operatorname{spec}(A)$ 时 $r(\lambda)=d$，故 $\min_\lambda r$ 只在**特征值**上取到；
实践中常取 $\lambda_0=0$ 做快速筛。用途：①过滤层（$\rho>\min_\lambda r$ 的全部不看）；
②约束 hardness gadget（必须 $r(\lambda)\ge\rho$ 对所有 $\lambda$）；③§82 反例即 $r(0)=1<3=\rho$。

## Lean（2026-11-06 已同步登记）

**[Lean-conditional]** —— 内核只覆盖代数/维数骨架，矩阵实例化与其余分部为纸面。

* 内核：`RankBarrier.rank_barrier` + `F1_Matrix.mul_pencil`、`rowSpace_one`、`rowSpace_eq_range`、`finrank_sup_eq_add_quotient`
* 均在 `tools/lean/MyProof/` 下，已登记进 `tools/lean/STATEMENT_MAP.md`；WSL 侧 `lake build MyProof` exit=0。
* 差异：矩阵实例化/行空间翻译与其余分部仍为纸面（详见 `## 状态与历史` 的等级行）。

## 精确验证

* 见等级行给出的精确验证数字。

## 状态与历史

**等级**：[已证-纸面] $+$ [精确验证 1484+113] $+$ **[Lean]**（`RankBarrier.rank_barrier_full`：$(5b)$ ⟹ $\rho\le\dim\pi_J(\operatorname{range}M)$，
**等级**：[已证-纸面]（由 E.1 + F.1）。
* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。






## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F2 |
| 导出等级 | **L3** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— Lean 已覆盖（内核） |


## 支撑目录

[rank_barrier/](../rank_barrier/README.md)

（本卷宗只汇总证据；支撑目录里的脚本与文档保持原位。）

## 专家复核意见（成立）

秩屏障只是**必要条件**，不得在无其它定理时当充分条件用；论文里须明写。
