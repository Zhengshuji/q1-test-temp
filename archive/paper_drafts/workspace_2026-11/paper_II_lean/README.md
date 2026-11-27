# Paper II Lean 工作树镜像

这里存放 WSL 工作树 `~/WorkSpace/lean4/Q1Paper/Q1Paper/PaperII/` 的**只读镜像**，
用途只有一个：防止再次发生 2026-11-25 那样的"重组时把未 promote 的模块删掉"。

- **真源**：WSL 工作树（`lake build` 在那里跑）。
- 每次改动后手动同步：`wsl -e bash -c "cp <wsl 路径> /mnt/c/.../workspace/paper_II_lean/"`。
- 不要在这里编辑；改名/移动以 WSL 为准。

当前内容（2026-11-25 夜）：

| 文件 | 内容 | 状态 |
|---|---|---|
| `Interface.lean` | `Mcol`/`Φ` 列分裂、`map_rowSpace_Mcol`、`t`/`t_eq_finrank_sub`/`t_le_iff`、`DecOrder`、`IsFeasible` + `isFeasible_pairRowSpace_iff` | 编译通过；公理审计 = 三条 |
| `Sandwich.lean` | `Ac/L0c/Rc/Lc`、`W0/TR/WR`、三条 `*_eq_map`、`decC_to_feasible`（正向 sandwich） | 编译通过；公理审计 = 三条 |
| `Monotone.lean` | `pairRowSpace_fromRows`、`pairRowSpace_pad`、`decC_mono_add`、`decC_mono`（Claim 5 单调半） | 编译通过；公理审计 = 三条 |
| `LowerBound.lean` | `finrank_sup_pi_le`、`finrank_pi1_mono`、`lowerBound_core`（`a+1 ≤ s₀+t`）、`lowerBound_sub`（Prop 2） | 编译通过；公理审计 = 三条 |
| `MainTheorems.lean` | 聚合入口 | `lake build` 通过（9173 jobs） |
| `Converse.lean` | `WRc`、`WRc_eq_map`、`map_symm_map`、`feasible_to_DEC`（反向 sandwich，复设计） | 编译通过；公理审计 = 三条 |
| `Saturate.lean` | `DEC_to_feasible_c`、`t_le_t_of_le`、`dec_saturates`、`dec_mono_complex` | 编译通过；公理审计 = 三条 |
| `MinOrder.lean` | `tMinSet`、`tMin`、`tMin_le_iff_dec`（`t_min ≤ r ↔ DEC (r₀+r)`）、`ell`、`omega_le_ell`、`t_le_two_ell`、`tMin_le_two_ell` | 编译通过；公理审计 = 三条 |
| `Audit.lean` / `Claims.lean` / `ClaimsCheck.lean` | 48 条声明的公理审计；论文条目 ↔ 声明对照 | `lake env lean` 通过 |

当前：`DEC`（复设计）上 Claim 5、Prop 1、Prop 2 全部完成；`DECℂ` 的正向与单调完成。
唯一规格缺口：`DECℂ` 的饱和/最小阶需要"实压缩引理"，见计划 §8.5。
这些文件已 promote 到 artifact 仓库 `Q1Paper/PaperII/`（commit `feb5b06`），并接入 CI。

注意：artifact 仓库的 `paper_lean_index.py` 扫描 `Q1Paper/**/*.lean`，所以在完成生成器改造
（M3）之前，这些文件**不能**直接放进 artifact 仓库，否则 `--check` 会报 stale。
计划见 [`../paper_split/PAPER_II_LEAN_PLAN.md`](../paper_split/PAPER_II_LEAN_PLAN.md) §8.5。
