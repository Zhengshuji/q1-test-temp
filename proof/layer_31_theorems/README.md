# `(3,1)` 层：格子级定理包

> **对应 docs 条目**：C.1（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

> **状态**：C.1–C.5 全部 **【已证-纸面】**；其中三处有 **【Lean】** 支撑（见 §3）。
> **范围**：只覆盖 $(\\rho,c)=(3,1)$ 层、**单个格子**（给定 $(\\mathcal U,\\mathcal H)$）。
> **不含**层级别的判定（那仍是开放问题，见 [admissibility.md](admissibility.md) §4）。

## 文件清单

| 文件 | 内容 |
|---|---|
| [theorem.md](theorem.md) | 记号、引理 0（谱判据）、C.1–C.5 的陈述与证明、验证等级 |
| [admissibility.md](admissibility.md) | 可允许格子的**精确规格** A1–A7、层归约定理、开放问题 |
| [verification.md](verification.md) | 验证矩阵、复现命令、未形式化清单 |

## 一句话

$$\\boxed{\\ \\text{固定格子后，$(3,1)$ 层的"是否被覆盖"由 }\\mu=\\dim(B\\cap\\mathcal U)\\text{ 完全决定}\\ }$$

| $\\mu$ | 结论 | 依据 |
|---|---|---|
| 3 | $w\\ne0$ 时**不被覆盖** | C.1 |
| 2 | $w\\ne0$ 时**不被覆盖** $\\iff$ $T$ 无 $E^{\\perp}$ 内特征向量 | C.3 |
| 1 | $w\\ne0$ 时**不被覆盖** $\\iff$ $T$ 无 $a^{\\perp}$ 内特征向量 | C.2 |
| 0 | **恒被覆盖** | C.4（= C.5 的特例）|
| 任意 | $w=0$ 时**恒被覆盖** | C.5 |

## 权威索引

本目录是**定理包**（按 `proof/<claim>/` 惯例）✓；逐条的工作记录、撤回清单与后续分析在
[../../proof/layer_program/RESTRICTED_COMPLETION_MODEL.md](../layer_program/RESTRICTED_COMPLETION_MODEL.md)（§44 为总表）。
两者若有冲突，**以本目录的陈述为准**（它是冻结版本），撤回记录仍以 RCP 为准。

### 文件清单（2026-10-30 更新）

| 文件 | 内容 |
|---|---|
| `theorem.md` | C.1–C.5（格子级判据）+ 引理 0 + 独立性表 |
| `admissibility.md` | A1–A7 规格、层归约定理、P1/P2/P3 |
| `verification.md` | 验证矩阵、复现命令、未形式化清单 |
| **`criterion.md`** | **覆盖判据的权威表述**：行/列约定显式、基无关性（30/30）、充分条件、我写错的地方 |
| **`d4_classification.md`** | **$d=4$ 的充要分类**：四条引理 + 定理 6.1 + 谱步可判边界 + 覆盖范围 |
| **`edci.md`** | **EDCI**（定维数条件不变子空间存在性）的独立表述：与经典三问的区别、MIN-ROWS 多的约束、三条路线 |
| `verify_dichotomy_fp.py` | $\mathbb F_p$ 上的完整枚举（仅作找候选，语义不对 ✗）|
