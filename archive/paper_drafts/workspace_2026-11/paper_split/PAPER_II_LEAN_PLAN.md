# Paper II 的 Lean 计划（2026-11-25 拟定）

> 目标：把 Paper II（`paper/current/paper_II_minorder.tex`，最小阶与最小阶构造）中**值得形式化**的陈述
> 做成可编译、可审计的 Lean，并按 artifact 仓库现有规范接入 CI。
> 规范依据：artifact 仓库 `docs/CONVENTIONS.md`、`Q1Paper/AGENTS.md`、本仓库 `CLAUDE.md §4/§5`。
> 本文件是**计划**，不是状态；状态以各模块的编译/审计结果和 `paper/LEAN_MAP.md` 为准。

---

## 0. 背景：上一轮的产出发生了什么

2026-11-23 曾在 WSL 工作树写过 5 个 Paper II 模块（`Wof`、`Sandwich`、`SandwichConverse`、
`Proposition2`、`Claim5`，约 700 行，全部编译通过）。2026-11-25 的 P1–P3 重组把它们**删除**了：
它们只存在于 `~/WorkSpace/lean4/Q1Paper/`，没有走 promote 流程，也没有进 artifact 仓库
（现在 `_attic/` 里只剩探针文件）。

**结论（流程教训）**：Paper II 的每个模块一编译通过就 promote 进 artifact 仓库并 commit，
不允许只在 WSL 里生长。

**好消息**：上一轮的数学内容大部分已被 Paper I 的新树覆盖，且换了更贴近论文的编码。
重做只需要补 Paper II 独有的部分，**不重写 sandwich**。

---

## 1. 复用地基（已核实存在的声明，不要重证）

| 声明 | 位置 | 在 Paper II 中的角色 |
|---|---|---|
| `Q1Paper.PaperI.DEC` / `DECℂ` / `MINDEC` / `MINDECℂ` | `PaperI/S00_Interface/Interface.lean:68,84,76,95` | 判定问题；Paper II 用 `DECℂ`（实设计、复秩） |
| `DEC_iff_compressed` | `PaperI/S01_Compression/CompressionMatrix.lean:258` | 原始条件 ↔ 压缩块 |
| `claim4_sandwich` | `PaperI/S02_Subspace/Claims38.lean`（约 190 行） | `W₀ ≤ W ≤ T` 且 `dim W ≤ dim W₀ + r`（正向） |
| `claim4_converse` / `claim4_converse_zero` | `PaperI/S02_Subspace/Claim4Converse.lean:52,143` | **逆命题已存在**：满足 sandwich 的 `W` 由某个 `R` 实现 |
| `pairRowSpace`、`pi1/pi2/piLam_pairRowSpace` | `PaperI/S02_Subspace/Claims38.lean:236,239,251,263` | 即上一轮的 `Wof` 与三条桥接（改名） |
| `claim5_conditions_depend_on_W` | 同上（约 277 行） | (5a)/(5b) 只依赖 `W` |
| `claim6_struct` | 同上（约 330 行） | `ω+1 ≤ dim W ≤ 2ω`（带 `IsAlgClosed`、`0 < ω`） |
| `claim7_DEC_succ` | 同上:586 | `DEC r → DEC (r+1)`（一般域 `K`） |
| `piLam`、`finrank_add_one_le_of_spectral` | `Q1Paper/BoundLower.lean:31,71` | 谱条件下界的一半 |
| `pi1`、`pi2` | `Q1Paper/SubspaceProjection.lean:27,31` | 两个投影 |
| `rowSpace`、`mem_rowSpan_iff_exists_vecMul`、`exists_rows_mul_eq` | `Q1Paper/RowSpaceAlgebraic.lean:24`、`Claims38.lean` | 行空间与提升 |

**由此，Paper II 真正缺的只有 6 件事**：`t = dim(W/W₀)` 这一层、`DECℂ` 的单调性、饱和、
最小阶 `q_min = r₀ + t_min`（含 `t_min ≤ 2ℓ`）、谱下界、紧性判据；外加 M2 的接口/算法正确性。

---

## 2. 决策（已经 ChatGPT 评审，见 §8）

1. **不照搬 Paper I 的 `S0x` 目录**。Paper II 初期用 `Q1Paper/PaperII/` 下约 6 个模块，
   按“证什么”命名；命名空间承载 API 名，文件路径可后移（`CONVENTIONS.md §4`）。
2. **不复述 Paper I 已覆盖的定理**；每个模块的 docstring 写明 `Reuses:` 清单。
3. **极小值用 `WithTop ℕ`**（不可行 = `⊤`），矩阵维度仍用 `ℕ`；不把 `⊤` 混进维度类型。
4. **文档、生成器、`Read/`、CI 放最后**（M3）。先稳定数学与声明，再冻结阅读材料。
5. **不做**：位复杂度、Renegar/BPR 等外部实代数算法的正确性、附录实例的数值证书（已在精确算术层）。

---

## 3. M1：核心最小阶数学（先做，一次会话一件事）

### M1.1 `PaperII/Interface.lean`
- `t (W₀ W) : ℕ`（商维数）、`t_eq_finrank_sub`（`W₀ ≤ W` 时 `t = dim W − dim W₀`）、
  `t_le_iff`：`t W₀ W ≤ r ↔ finrank W ≤ finrank W₀ + r`（与 `claim4_*` 的假设形式对接）；
- `decC`：把 `PaperI.DECℂ` 包装成 Paper II 的 `DecOrder`（含 `r0`），并证 `DecOrder ↔ DECℂ`。
- **验收**：`lake build Q1Paper.PaperII.Interface`；文件首行 docstring 是模块路径；无 `sorry`。

### M1.2 `PaperII/Monotone.lean`
- **风险 A**：`DECℂ` 的单调 `decC_succ`、`decC_mono`（`r ≤ r'`）。首选从 `claim7_DEC_succ` 桥接；
  若桥接比复制贵，就在 `DECℂ` 上重跑同一证明（同一数学，换定义），并在 docstring 说明。
- **饱和**：`decC_saturates : t W₀ T ≤ r → (DecOrder r ↔ DecOrder (t W₀ T))`。
  正向用 `claim4_converse`（`dim W ≤ dim W₀ + t`），反向是一行。
- **验收**：双向等价；与 `claim7_*` 无重复证明；`#print axioms` 只有三条。

### M1.3 `PaperII/MinOrder.lean`
- `tMin : WithTop ℕ`（`sInf` 升到 `WithTop`，空集 = `⊤`）、`qMin : WithTop ℕ`、`qMin_eq : qMin = r0 + tMin`；
- `tMin_le_two_mul_ell : tMin ≤ 2 * ℓ`，`ℓ = finrank (rowSpace (A * N))`；
  中间需要 `ω ≤ ℓ`：由 `rowSpace_mul_le` 得 `rowSpace (L*A*N) ⊆ rowSpace (A*N)`，再用
  `pi1_pairRowSpace`/`claim5`。
- **验收**：不可行时两者都 `⊤`；可行时 `qMin` 被取到（`WithTop` 的 `sInf_mem` 版本）。

### M1.4 `PaperII/LowerBound.lean`（Paper II 最有价值的新数学）
- 重写 `finrank_sup_pi_le`（`TightDim.lean` 已不存在）与 `finrank_pi1_mono`；
- `lowerBound_core : a + 1 ≤ s₀ + t`（`a = finrank (π₁ W₀ ⊔ π₂ W₀)`，`[IsAlgClosed K]`，`0 < ω`）；
- `lowerBound_sub`（`s₀ ≤ a` 时的减法形式）、`qMin_lower : r0 + (a + 1 - s₀) ≤ qMin`。
- **验收**：假设与论文 Prop 2 逐条对应；`a + 1 ≤ s₀ + t` 是主陈述（避免 ℕ 截断减法）。

---

## 4. M2：结构刻画与算法正确性

### M2.1 `PaperII/Tightness.lean`
- 论文 Prop 3 的 **(G,b) ⇒** 方向：构造 `W(G,b) = {(h, Gh + αb)}`，证 `dim = a+1`、`W₀ ⊆ W ⊆ T`、
  谱条件，从而 `tMin ≤ a − s₀ + 1`；与 `lowerBound_core` 合起来给出等式条件。
- 反方向（`ker π₁|_W` 一维 + 截面）**明确列为可选**；若做，单独一个文件。

### M2.2 `PaperII/Opt.lean`
- 抽象二分引理：单调谓词 `P : ℕ → Prop`、`∃ n, P n` ⟹ 返回最小可行 `n`（用 `Nat.find`，与 DEC 后端解耦）。
- `opt_correct : DecOrder` 的二分返回 `qMin`（条件：`DecOrder` 单调 + 饱和，已在 M1 得到）。

### M2.3 `PaperII/Find.lean`
- 只证 **lifting**：`claim4_converse` 已经给出 `∃ R, rowSpace [L₀;R] * M = W`，
  把 `W` 反推成 `R` 的构造写成接口；**明确声明**未验证 BPR 采样算法。

---

## 5. M3：工程收尾（与 Paper I 对齐）

1. `PaperII/Audit.lean` + `scripts/check_paperII_axioms.py`（或给现有脚本加 `--paper` 参数）。
2. `PaperII/Claims.lean`（叙述）/ `ClaimsCheck.lean`（每条一个 `#check`）。
3. 生成器：`generate_paperII_claims.py`、`generate_paperII_modules.py`（或泛化现有脚本），
   `docs/PAPER_II_PROOF_MAP.md`、`docs/PAPER_II_MODULE_MAP.md`，`Read/` 入口。
4. `scripts/check.sh` 与 CI 加 Paper II 条目；`paper/LEAN_MAP.md` 与
   `paper/current/paper_II_minorder.tex` 的 `tab:evidence` 同步。
5. 收尾命令（与 `CONVENTIONS.md §6` 同构）：
   `lake build Q1Paper.PaperII.MainTheorems` → `Audit` → 生成器 `--check` → `check_consistency.py`。

---

## 6. 风险与待定

| # | 风险 | 处理 |
|---|---|---|
| A | `DECℂ`（复秩）与 `DEC`（一般域）的桥接成本未知 | M1.1 先做探针；贵就复制 `claim7` 的证明 |
| B | `WithTop ℕ` 的算术语（`r0 + tMin`）会有 coercion 摩擦 | 先只在 M1.3 用；若太痛退 `Option ℕ` + 非空假设 |
| C | `t ≤ r` 与 `finrank W ≤ finrank W₀ + r` 的等价需要 `W₀ ≤ W` | M1.1 的 `t_le_iff` 明确假设 |
| D | 名字冲突（`claim5_*`/`claim6_*`/`claim7_*` 已被 Paper I 占用） | Paper II 用 `prop1_*`、`prop2_*`、`sat_*`、`tight_*` 前缀 |
| E | 论文 `tab:evidence` 的等级与 Lean 实际强度可能不一致 | M3 逐行核对，只写 `[Lean]`/`[Lean-conditional]` |

**不做**：Theorem 4 的 `O(log(ℓ+2))` 次调用（复杂度计数）、Cor OPT/FIND 的位复杂度、附录实例的数值重算。

---

## 7. 下一步（按顺序，每步一次 commit）

1. **M1.1 探针**：在 WSL 建 `ScratchP2Interface.lean`，确认 `DECℂ → pairRowSpace → claim6_struct`
   这条链无额外假设；通了就 promote 成 `PaperII/Interface.lean`。
2. M1.2 饱和 + `DECℂ` 单调；M1.3 最小阶；M1.4 谱下界。
3. 每完成一个模块：`lake build` → `#print axioms` → promote → commit（artifact 仓库）。
4. M1 全绿后，再决定 M2 的取舍（Tightness 反方向是否值得）。
5. M3 收尾时再生成 `docs/PAPER_II_*` 与 `Read/`，避免过早冻结。

---

## 8.5 进展（2026-11-25 夜，M1 已开工）

| 模块 | 内容 | 状态 |
|---|---|---|
| `Q1Paper/PaperII/Interface.lean` | 列分裂 `Mcol`/`Φ`、`Φ_vecMul`、`map_rowSpace_Mcol`（row(M) 编码 ↔ pair 编码）；`t`、`t_eq_finrank_sub`、`t_le_iff`；`DecOrder`；`IsFeasible` + `isFeasible_pairRowSpace_iff` | 编译通过，10 条声明公理审计只有 `propext/Classical.choice/Quot.sound` |
| `Q1Paper/PaperII/Sandwich.lean` | `Ac/L0c/Rc/Lc`、`W0/TR/WR`、`W0_eq_map/TR_eq_map/WR_eq_map`、**`decC_to_feasible`**（`DECℂ r → ∃W, W₀≤W≤T ∧ feasible ∧ t≤r`） | 编译通过，审计三条 |
| `Q1Paper/PaperII/Monotone.lean` | `pairRowSpace_fromRows`（行堆叠分裂）、`pairRowSpace_pad`（补零行不动 `W`）、**`decC_mono_add`**（`DECℂ r → DECℂ (r+c)`）、`decC_mono`（`r ≤ r'`） | 编译通过，审计三条 |
| `Q1Paper/PaperII/LowerBound.lean` | `finrank_sup_pi_le`（`rank[U₀;V₀] ≤ ω`）、`finrank_pi1_mono`、**`lowerBound_core`**（`a + 1 ≤ s₀ + t`）、`lowerBound_sub`（`s₀ ≤ a` 时的减法形式） | 编译通过，审计三条 |
| `Q1Paper/PaperII/Converse.lean` | `WRc`（复设计）、`WRc_eq_map`、`map_symm_map`、**`feasible_to_DEC`**（反向 sandwich，复设计） | 编译通过，审计三条 |
| `Q1Paper/PaperII/Saturate.lean` | **`DEC_to_feasible_c`**（正向，复设计）、`t_le_t_of_le`、**`dec_saturates`**（`DEC r ↔ DEC m`）、`dec_mono_complex` | 编译通过，审计三条 |
| `Q1Paper/PaperII/MinOrder.lean` | `tMinSet`、`tMin : WithTop ℕ`、**`tMin_le_iff_dec`**（`t_min ≤ r ↔ DEC (r₀+r)`）、`ell`、`omega_le_ell`、`t_le_two_ell`、**`tMin_le_two_ell`**（Prop 1） | 编译通过，审计三条 |
| `Q1Paper/PaperII/Audit.lean` / `Claims.lean` / `ClaimsCheck.lean` | 48 条声明的公理审计；论文条目 ↔ 声明对照（ClaimsCheck 逐条 `#check`） | `lake env lean` 通过；审计全部 `propext/Classical.choice/Quot.sound` |
| `Q1Paper/PaperII/MainTheorems.lean` | 聚合入口（import 上面七个） | `lake build` 通过（9174 jobs） |

**已接入 artifact 仓库**（commit `feb5b06`）：`Q1Paper/PaperII/` 11 个文件；`paper_lean_index.py`
跳过 PaperII（Paper II 有独立 Claims 表）；`.github/workflows/build.yml` 与 `scripts/check.sh`
增加 Paper II 的 build + ClaimsCheck + Audit 步骤；本地 `check_consistency.py` 与四个生成器
`--check` 全绿。

关键做法：Paper II 的 `W` 用 pair 编码（Claim 5/6 的语言），而 Claim 4 的 sandwich 在
row(`[N AN]`) 编码里；两者用一列分裂同构 `Φ` 连接（`LinearEquiv.sumArrowLequivProdArrow`
+ `finSumFinEquiv`），于是 sandwich 的两个方向都**直接复用** `claim4_sandwich` /
`claim4_converse`，不重证。

**发现的集成约束（M3 必须先处理）**：artifact 仓库的 `scripts/paper_lean_index.py` 扫描
`Q1Paper/**/*.lean` 生成 `docs/PAPER_I_MODULE_MAP.md`；把 `PaperII/` 放进 artifact 仓库会让该
`--check` 变红（"stale"）。所以 Paper II 的 promote 必须和生成器改造（加 `--paper` 参数或独立
`docs/PAPER_II_MODULE_MAP.md`）同批提交，不能只拷文件。

当前备份：`workspace/paper_II_lean/` 是 WSL 工作树 `PaperII/` 五个文件的镜像（防再次丢失）。

**规格决定（2026-11-26 夜，ChatGPT 复核）**：坚持 `DECℂ`（实设计、复秩），不改用 field-generic
`DEC`。反向 sandwich 因此不能直接套 `claim4_converse`（它返回 K 上的 `R`）。需要补一条**实压缩引理**：

1. `realification_of_feasible_W`：Paper II 构造的可行 `W` 是某个实子空间的复化
   （`W = W_ℝ ⊗_ℝ ℂ`，`W0_ℝ ⊆ W_ℝ ⊆ T_ℝ`，`dim_ℝ W_ℝ ≤ dim_ℝ W0_ℝ + r`）；
2. `real_sandwich_converse`：对 `W_ℝ` 用 K = ℝ 的 `claim4_converse`，再复化，得到**实** `R`。

这是唯一的规格缺口；`decC_to_feasible` 与 `decC_mono` 已经按 `DECℂ` 完成。

**当前状态（2026-11-27 深夜）**：**Paper II 的全部论文 math 条目已在实设计规格上闭合**——
Claim 4、Claim 5（`DECℂ` 单调 + 饱和）、Prop 1（`q_min`、`t_min ≤ 2ℓ`、`qmin-lb`，以及
`DECℂ` 版 `tMinC ≤ r ↔ DECℂ r`）、Prop 2、Theorem 4 顺序部分、Prop 3 双向；实压缩链
（`real_compress`→`feasible_to_decC`→`decC_saturates`→`tMinC_le_iff_decC`）全部 Lean 化。
**剩余仅 M3/论文层**：接口计数、OPT/FIND 推论、附录实例（已在 proof map 登记）；以及
`Read/` 入口与 STATUS 一致性。artifact 仓库 commit `f1b934e`→`f8fe881`→`9bf8e64`（90 条审计）。

**并发提醒（2026-11-27）**：artifact 仓库出现来自另一会话的提交（`1453560`、`e6622c4`），
`Q1Paper/PaperII/` 与 `paper/` 的本次改动已在其提交中；后续只 `git add` 本会话的路径。

**实压缩引理的下一步（本轮尝试过，已回退）**：需要先证
`rowSpace (M.map f) = span_ℂ (phi '' rowSpace M)`（重述为 ℂ-span 形式，用 `Submodule.span_span`）
与 `Mcol (N.map f) (Ac A) = (Mcol N A).map f`（`Fin.addCases` 的索引形式 `j.addNat k` 与
`Fin.natCase_right` 不匹配，需要先 `show` 或改 `Mcol` 的定义）。这两条通过后，压缩本身是
`claim4_converse`（K=ℝ）+ 复化 + 维数恒等式。

## 8. 与 ChatGPT 的往返（2026-11-25，短提示词 + 让它自己读仓库）

问的是三点：Paper II 该不该照搬 `S0x` 结构、哪 6–8 条值得形式化并排序、文档/产物何时生成。
答复要点（已采纳）：

- 不照搬 `S0x`；初期 6 个数学模块，按证明内容命名。
- 不复述 Paper I 已覆盖的定理（尤其 Claim 4 的逆命题已存在）。
- **优先做谱条件下界**（Paper II 最有价值的新数学）。
- 把 Tightness 保留为正式目标（下界 → 结构刻画的关键）。
- OPT 只证算法正确性；FIND 只证精确提升，不声称验证外部采样算法。
- 文档、生成器、`Read/` 最后做。
- 两个技术风险：`DECℂ` 的单调桥接、无解时的 `+∞`（建议 `WithTop ℕ`）。

## 8.6 新一轮（2026-11-26 晚，目标：继续完善 + ChatGPT 终检）

**已完成**：PaperII/Tightness.lean（94 条审计）——
- pi1_eq_sup_of_finrank：可行、W₀ ≤ W、dim W = a+1 时 π₁W = U₀+V₀；
- 	Min_eq_of_graph：(G,b) + pencil 秩条件 ⇒ 	_min = a+1−s₀（⇐）；
- exists_graph_of_tMin_eq：	_min 饱和 ⇒ 存在 V = W(G,b)、 ≠ 0、π₁V = U₀+V₀ 与秩条件（⇒）。

**ChatGPT 复核（同日）**：分解正确；两点改进——①ω > 0 应从数据推出（dim W ≤ 2ω 且 dim W ≥ 1），
不要作为假设；② = s₀ = 0 的退化情形要显式排除（此时 W=0 可行、	_min=0 ≠ a+1−s₀=1）。
建议顺序：omega_pos 引理 → A → B（在  ≠ 0 之后推全称 hω）→ C（处理退化）→ 最后打包成
↔（需要把 G 从 π₁W 搬到 U₀+V₀ 的 transport）。

**下一轮**：先证 omega_pos_of_finrank 与 omega_pos_of_nonzero（去掉 	Min_eq_of_graph 的 hω
假设），再处理 (C) 的退化分支。注意 Submodule.eq_bot_of_finrank_eq_zero 在此 Mathlib 不存在，
用 y_contra + Submodule.finrank_pos_iff（同样不存在，改用 inrank_eq_zero/eq_bot 的可用名）。

## 8.7 进展（第 2 轮）

**已完成并推送（artifact main `12d1ec5`，96 条审计）**：`Tightness.lean` 去掉 Prop 3 两方向的非退化假设——
- `omega_pos_of_nonzero`：`W₀ ≠ ⊥` ⇒ 每个可行 `V ≥ W₀` 的 `ω > 0`（由 `dim V ≤ 2ω` + `V ≠ ⊥`）；
- `W0_ne_bot_of_pos`；`pi1_eq_sup_of_finrank` 内部由 `dim W ≤ 2ω` 推出 `ω > 0`；
- `tMin_eq_of_graph` 由 `b ≠ 0` 推出 `W₀ ≠ ⊥`（用 `Subsingleton` 处理 `U = ⊥`），再取全称 `hω`；
- `exists_graph_of_tMin_eq` 不再需要 `hω`。这正是 ChatGPT 指出的改进方向。

**卡点（未提交，已回退）**：把两方向打包成单一 `↔`（RHS 用 `π₁V = U₀+V₀` 的 V-形式）。
`tMin_eq_of_graph_gen`（对一般 `U : Submodule ℂ (Fin k → ℂ)` 的 (⇐)）在
`hmem : t W₀ (graphExt U G b) ∈ tMinSet` 这一步触发 whnf 心跳超时（800k 也不够）。
下次可试：①先证一个小的 `tMin_le_of_feasible` 辅助引理（一次性消化大项），再复用；
②把 `graphExt U G b` 用 `let` 绑定成局部定义以减少展开；
③或接受「两方向分开陈述」作为最终形态（论文的 iff 由两句合成）。

## 8.8 第 3 轮进展

**已完成（本地 commit `4996a05`；97 条审计，build 9179 jobs）**：`tMinC_le_two_ell`——
实设计的最小商维数 `t_min^ℝ ≤ 2ℓ`，由 `tMinCSet` 的达到者 + `WR ≤ TR`（`rowSpace_mul_le`）
+ `t_le_two_ell` 得到。这补上了 proof map 里「实设计 t_min ≤ 2ℓ」这一条。

**未推送**：GitHub SSH（443）连接超时（`ssh_dispatch_run_fatal: Connection timed out`），
`4996a05` 只在本地；网络恢复后 `git push origin main` 即可。

**Prop 3 打包成单一 `↔` 仍卡在精化成本**：直接写（V-形式的 RHS）在 `t_eq_of_graph`/`tMin_le_of_feasible`
的实例化处反复 whnf 超时（800k 心跳）。下一步的有效办法应是**把图数据做成谓词/结构**：
`def HasGraph (V) : Prop := ∃ U G b, V = graphExt U G b ∧ ...`，让 Lean 不必反复展开
`graphExt (π₁ V) G b`；或者把 `t_eq_of_graph` 的结论预先特化到 `π₁ V` 的形状上。

## 8.9 第 4 轮进展

**已完成并推送（artifact main `3b533fb`，101 条审计，build 9179 jobs）**：`Tightness.lean` 新增
`UV`（`U₀+V₀` 的短名）、`UV_eq`、`mem_tMinSet`、`tMin_le_of_feasible`
（`t_min` ≤ 任意可行 `W` 的商维数；把大项一次性消化，供后续复用）。

**打包仍卡住**：`tMin_eq_of_graph_gen`（一般 `U` 的 ⇐）在 `t_eq_of_graph`/`tMin_le_of_feasible`
实例化处仍 whnf 超时（`UV` 短名 + 800k 心跳都不够）。已回退，保持树绿。
**新思路（待试）**：沿 `hpi : π₁V = U₀+V₀` 用 `▸` 把 `G`/`b` transport 到 `U₀+V₀`，再套现成的
`tMin_eq_of_graph`（U-形式）；或把 RHS 写成谓词 `IsTightExtension V` 让 Lean 不必展开。

**已向 ChatGPT 提问**（2026-11-26 晚）：打包是否值得继续、哪种实现最省力、下一步补哪块覆盖最值。
下一轮先读回复再动手。

## 8.10 第 5 轮进展（按 ChatGPT 的决定转向）

**ChatGPT 的裁定**：复域 iff 打包**不值得**继续（"主要增加接口便利性，不增加实质覆盖"）；
若要打包，用谓词 `IsTightExtension V` 且 `G,b` 定义在 `π₁V` 上，**不要把 transport 放进主定理**。
优先级：①实↔复设计等价桥梁；②实域 Prop 3；③FIND 见证系统；④复域 iff 打包。

**已落地（artifact main `9ad5e07`，103 条审计）**：
- proof map 冻结复域打包（写明原因与将来做法），并新增「实域 Prop 3 未形式化」一行；
- `Realification.lean` 新增 `UC`（实子空间 `U ≤ (Fin k → ℝ)` 的 ℂ-span）与
  **`finrank_UC`：`finrank ℂ (UC U) = finrank ℝ U`**（把 `U` 写成矩阵行空间 +
  `rowSpace_map_complex` + `rank_map_ofReal_any`）。

**实域 Prop 3 的路线（已想清，待实现）**：设 `U = U₀+V₀` 为实子空间、`b ∈ U` 实、`G : U → U` 实，
满足 `W(G,b) ⊆ T` 与复域 pencil 秩条件。则
- 上界：`W(G,b)` 是实子空间，`claim4_converse`（K=ℝ）给出实设计 `R` 使 `rowSpace = W(G,b)`，
  于是 `t_min^ℝ ≤ dim W(G,b) − s₀ = a+1−s₀`；
- 下界：`tMin ≤ tMinC`（实设计 ⊆ 全部复可行 W），再用 `le_tMin_of_lowerBound_max`。
需要的新件：把实线性 `G`/`b` 复化到 `UC U` 上（baseChange of a linear map），约 20–30 行；
然后 `graphExt_feasible`/`graphExt_piLam` 在 `UC U` 上套用。

## 8.11 第 6 轮进展

**已落地（artifact main `42d8974` + `350a8cd`，106 条审计）**：`Realification.lean` 新增
- `WR_le_TR`：任意实设计的 `W` 都在 `T` 内（`rowSpace_mul_le`）；
- **`tMin_le_tMinC`**：复域最小 ≤ 实域最小（实设计是可行复 `W` 的子集）；
- **`le_tMinC_of_lowerBound`**：Prop 1 的 `qmin-lb` 在实设计上的形式 `a + 1 − s₀ ≤ t_min^ℝ`
  （由 `le_tMin_of_lowerBound_max` + `tMin_le_tMinC`）。

至此实设计（`DECℂ`）的 Prop 1 三条界齐了：`tMinC_le_two_ell`（上界）、`le_tMinC_of_lowerBound`
（下界）、`tMinC_le_iff_decC`（最小阶刻画）。Claims 与 proof map 已同步（proof map 的
"Prop 1 实设计 2ℓ 未形式化" 一行改为 resolved，并指向三条声明）。

**下一轮**：实域 Prop 3 的 (⇐)——需要先把实 `G`/`b` 复化到 `UC U`（矩阵层面用
`(Gm.map (algebraMap ℝ ℂ)).mulVecLin`，子空间层面用 `phi` 的像），再用 `graphExt_feasible`。

## 8.12 第 7 轮：ChatGPT 终检与收尾（2026-11-26）

**ChatGPT 终检结论**：三项低成本清理后即可**冻结 Paper II 的 Lean 覆盖**；不再投入
复域单一 `↔` 打包与实设计 Prop 3。它同时声明：本轮它只核对仓库声明与审计清单，
**没有独立重跑 `lake build`**（构建证据来自提交记录）。

**三项清理已落地并推送（artifact main `cf58299`）**：
1. `ClaimsCheck.lean` 补 6 条 `#check`：`tMinC_le_two_ell`、`WR_le_TR`、`tMin_le_tMinC`、
   `le_tMinC_of_lowerBound`、`UC`、`finrank_UC`；
2. 清理过时范围说明：`Claims.lean`（实设计 converse 已由 `real_compress` 打通）、
   `Realification.lean` 文件头（已从"为 real-compression 做准备"改为"实设计桥梁已完成"）；
3. `docs/PAPER_II_PROOF_MAP.md` 的审计数 `48 declarations` → `106 declarations`。

**最终验证（2026-11-26 19:xx）**：
- `lake build Q1Paper.PaperII.MainTheorems Q1Paper.PaperII.Read` = **9180 jobs**，0 error；
- `lake build Q1Paper.PaperI.S00_Interface.MainTheorems` = 9167 jobs（未被我改动破坏）；
- `ClaimsCheck` 0 error；`Audit.lean` = **106 条声明**，`check_paperI_axioms.py` → 106/0（只允许
  `propext`、`Classical.choice`、`Quot.sound`），全树无 `sorry`；
- `check_consistency.py`（144 模块）consistent；四个生成器 `--check` 全部 exit 0。

**冻结后的边界（写进 proof map）**：复域 Prop 3 两方向 + `π₁W = U₀+V₀` 识别已证，单一 `↔` 打包冻结；
实设计 Prop 3（紧性判据）未形式化（只有 `UC`/`finrank_UC` 的维数桥）；FIND 见证系统、`O(log)` 计数、
附录实例仍是论文/数值层。

## 8.13 第 8 轮：按 Paper I 的可读性重排 Paper II 仓库（2026-11-26）

**已完成（artifact `430b4b0`、`56c8b9e`）**：
1. 新增生成器 `scripts/generate_paperII_modules.py`（→ `Q1Paper/PaperII/MODULES.md`）与
   `scripts/generate_paperII_claims.py`（→ `Q1Paper/PaperII/CLAIMS.md`，并校验表中每个声明都在
   `ClaimsCheck.lean` 里）。两者 `--check` 已接入 CI 与 `scripts/check.sh`。
2. `Read.lean` 拆成 `Read/`：`S01_Standing`、`S02_Sandwich`、`S03_MinOrder`、`S04_LowerBound`、
   `S05_Tightness`、`S06_RealDesigns`、`All`（按论文章节，逐步骤 `#check`，与 Paper I 的 `Read/` 同形）；
   CI 改为构建 `Q1Paper.PaperII.Read.All`。
3. `ClaimsCheck.lean` 补 Paper I 复用声明（`claim3_attainable`、`DEC_iff_compressed`）；
   `docs/START_HERE.md` 的 Paper II 段改成入口表；`docs/PAPER_II_MODULE_MAP.md` 加生成物指引。

**论文修正（同批）**：
- 证据表补 7 行：tightness 的识别与合成两方向、实压缩（`real_compress`/`feasible_to_decC`）、
  实设计 `t_min^ℝ ≤ 2ℓ`、实设计 `qmin-lb`；
- 删掉过时句"剩下边界 = 实设计规格"，改为准确表述（两方向已合成、未打包成单一 ↔、实设计紧性未证）；
- Prop 3 证明补上 `ω > 0` 的由来（`dim W ≤ 2ω`，`dim W = a+1 > 0`），使 `eq:qmin-lb` 的前提成立；
- 新增 `scripts/verify_paperII_example.py`（附录实例的精确有理证书：k=4、d_0=6、s_0=2、ℓ=4、
  (5a) 两秩=7、铅笔 det=0 且 64 个 7×7 子式 gcd=1），论文 reproducibility 段改为点名该脚本。
  **此前正文声称"exact rational arithmetic 验证"但仓库里没有脚本，这是实质缺口。**
