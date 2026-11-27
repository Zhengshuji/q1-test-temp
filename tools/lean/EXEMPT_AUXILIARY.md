# Lean 辅助内核的**文件级豁免**清单

> 背景：`tools/lean/MyProof/Theorems/`（16 个文件、**78 条声明**）是早期会话留下的"论文核心内核"，
> 属**辅助/工具**性质；`STATEMENT_MAP.md` 按**命题**登记，不逐一登记这类声明。
> 本文件是豁免白名单：`audit_lean_statements.py` 会**跳过**这里列出的文件，
> 但要求①文件真实存在；②每个文件在本表里有理由；③命题级声明必须点名。

## 规则

1. 新增辅助文件 → 必须在本表加一行（文件、声明数、理由）；
2. 文件里若有**命题级**声明（对应 docs/02 的条目），必须在该行的"命题级声明"列点名，
   并在 `STATEMENT_MAP.md` 里单独登记（豁免只覆盖辅助声明，不覆盖命题级声明）；
3. 文件被删除或移走时，本表同步删行。

## 清单

| 文件 | 声明数 | 命题级声明（须在 STATEMENT_MAP 单列）| 理由 |
|---|---|---|---|
| `Theorems/ABridge.lean` | 4 | 无（含 `rank_eq_iff_ker`、`decomp_iff_rank`：$(5a)$ 的秩/核等价，属工具） | 早期 $(5a)$ 桥接工具 |
| `Theorems/B2.lean` | 3 | 无 | 顶层 $B_2$ 的辅助维数引理 |
| `Theorems/Bridge.lean` | 1 | 无 | 分解→像包含的桥 |
| `Theorems/C6.lean` | 20 | 无 | $C\circ A\circ A=0$ 情形的论文核心（多支） |
| `Theorems/C6A.lean` | 4 | 无 | C6 的一支 |
| `Theorems/C6Mech.lean` | 8 | 无 | C6 的机制引理 |
| `Theorems/CaseII.lean` | 1 | 无 | Case II 的秩界 |
| `Theorems/CriterionCore.lean` | 3 | 无 | 判据的序关系工具 |
| `Theorems/D4.lean` | 6 | 无 | D.4 的分解工具 |
| `Theorems/Decomp.lean` | 2 | 无 | 分解的像/桥 |
| `Theorems/DimCount.lean` | 4 | 无 | 维数计数工具 |
| `Theorems/Factor.lean` | 8 | **`decomp_iff_ker`**（$=\,$L1：$(5a)\iff\exists(\Lambda,G_0,G_1)$ 分解，**已核**） | $(5a)$ 的因子化核心；其余 7 条为工具 |
| `Theorems/PaperCore.lean` | 5 | 无 | 早期论文核心的通用引理 |
| `Theorems/Pencil.lean` | 2 | 无 | 铅笔秩的通用引理 |
| `Theorems/Spectral.lean` | 2 | 无 | 秩-复合等价（B.1 的辅助） |
| `Theorems/UpperBound.lean` | 5 | 无 | 铅笔上界工具 |

**合计：16 文件 / 78 声明**；其中命题级 1 条（`decomp_iff_ker`）。

## 与 docs/02 的关系

* `decomp_iff_ker` → 对应 **B.17 的 $(\ast)$ 分解** 与 **L1**（专家第五轮的里程碑）；
* 其余 77 条为工具，**不单独**计入任何命题的 Lean 覆盖。
