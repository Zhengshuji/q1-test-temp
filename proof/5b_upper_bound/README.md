# (5b) 的上界：$\operatorname{rank}(\lambda H-F)\le \operatorname{rank}H$

> **对应 docs 条目**：B.8（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

> 归档日期：2026-10-21
> 状态：**数学证明 ✅；Lean 形式化 ✅（本次新增）；数值验证 ✅（本次修正）**
>
> **2026-10-31 补充**：本目录证的是 $(5b)$ 的**上界**（$\le$，由 $(5a)$ 免费得到、不含谱信息）。
> $(5b)$ 的**下界**（$=$，即谱条件 $\operatorname{rank}(\lambda H-F)=h\ \forall\lambda$）是**另一个问题**，
> 它的判定复杂度（$\mathrm{DEC}(q)\in\exists\mathbb R$）见 [../dec_q_existsR/](../dec_q_existsR/README.md)。
> 两者合起来才是 $(5b)$：上界说"不会超"，下界说"不会掉"；**真难度在下界**。

## 一句话

$(5b)$ 是一个**秩等式**

$$\operatorname{rank}(\lambda H-F)=\operatorname{rank}H\quad(\forall\lambda),$$

它拆成**上界**和**下界**两个方向：

$$\underbrace{\operatorname{rank}(\lambda H-F)\le h}_{\text{上界：免费，已证}}\quad\wedge\quad
\underbrace{\operatorname{rank}(\lambda H-F)\ge h}_{\text{下界：真正的谱条件，未证}}.$$

**上界是 $(5a)$ 的推论**（$F=\Lambda H$ 或行包含），对一切 $\lambda$ 自动成立；它不提供任何硬度。**所有困难都在下界**：下界等价于 $\gcd$ 判据 / “$\operatorname{im}H$ 不含 $\Lambda$ 的特征向量” / PBH 可控性。

## 位置

本目录只是 $(5b)$ 的**上界**（$\le$，由 $(5a)$ 免费）；**下界**（$=$）的判定复杂度在
[../dec_q_existsR/](../dec_q_existsR/README.md)，命题间的整体关系见 [../README.md](../README.md)。

## 文件地图

| 文件 | 内容 |
|---|---|
| [`README.md`](README.md) | 本文件：结论、状态、入口 |
| [`01_描述与意义.md`](01_描述与意义.md) | 上界是什么、为什么免费、控制论意义、与 NP-hard 的关系 |
| [`02_证明.md`](02_证明.md) | 数学证明（原始 4 块形式 + 约化铅笔形式）+ Lean 形式化说明 |
| [`03_验证.md`](03_验证.md) | 本次修正了什么、如何复现、测试结果、遗留问题 |
| [`lean/README.md`](lean/README.md) | Lean 归档说明：依赖链、如何编译 |
| [`lean/MyProof/Theorems/UpperBound.lean`](../../trash/lean_removed_2026-11-19/proof/5b_upper_bound/lean/MyProof/Theorems/UpperBound.lean) | 本次新增的 5 条上界定理 |
| [`lean/MyProof/Theorems/Pencil.lean`](../../trash/lean_removed_2026-11-19/proof/5b_upper_bound/lean/MyProof/Theorems/Pencil.lean) | T5′ 恒等式（依赖） |
| [`lean/MyProof/Theorems/Factor.lean`](../../trash/lean_removed_2026-11-19/proof/5b_upper_bound/lean/MyProof/Theorems/Factor.lean) | `tuple` / `tuple_apply` / `decomp_iff_ker`（依赖） |
| [`lean/MyProof/Theorems/ABridge.lean`](../../trash/lean_removed_2026-11-19/proof/5b_upper_bound/lean/MyProof/Theorems/ABridge.lean) | $(A)$ 秩形式 $\iff$ 分解（依赖） |
| [`lean/MyProof/Theorems.lean`](../../trash/lean_removed_2026-11-19/proof/5b_upper_bound/lean/MyProof/Theorems.lean) | 归档用的**最小**根文件（只 import 上面四个模块） |
| [`scripts/verify_upper_bound.py`](scripts/verify_upper_bound.py) | 数值/符号验证脚本（含 `cond_5b` 回归） |

> **Lean 不是“一个文件”**：`UpperBound.lean` 依赖 `Pencil.lean`、`Factor.lean`、`ABridge.lean` 和 `Mathlib`。
> 归档里把自写的依赖一起复制了（`lean/MyProof/`）；`lean/README.md` 有依赖链和编译方法。

## 核心结论

1. **原始 4 块形式**：由 $(5a)$，$\operatorname{row}(LA)\subseteq\operatorname{row}(L,CA,C)$，故
   $\operatorname{row}(\lambda L-LA)\subseteq\operatorname{row}(L,CA,C)$，于是
   $$\operatorname{rank}[\lambda L-LA;CA;C]\le \operatorname{rank}[L;CA;C].$$
2. **约化铅笔形式**：$P(\lambda)=\lambda H-F=(\lambda I-\Lambda)H$，故
   $\operatorname{rank}P(\lambda)\le\operatorname{rank}H$。
3. **没有 $(5a)$ 时上界会失败**：$M=\operatorname{diag}(1,0)$、$F=\begin{pmatrix}0&0\\0&1\end{pmatrix}$ 给出
   $\operatorname{rank}M=1$ 而 $\operatorname{rank}(1\cdot M-F)=2$。

## 本次修正（2026-10-21）

| 问题 | 修正 |
|---|---|
| Lean 里 **没有** 上界定理 | 新增 [`UpperBound.lean`](../../trash/lean_removed_2026-11-19/proof/5b_upper_bound/lean/MyProof/Theorems/UpperBound.lean)：矩阵形式、线性映射形式、原始 4 块形式、端到端（抽象 (5a) ⟹ 上界） |
| Lean 的 `T2_pencil_rank` 只是同义反复（两边是同一矩阵） | 保留为恒等式辅助引理；真正的内容移到 `UpperBound.lean`，并在 `03_验证.md` 说明 |
| `exact_gcd.cond_5b` **只查下界**（$\rho$ 阶子式 gcd），会假阳性 | `cond_5b` 现在同时检查 $(ρ+1)$ 阶子式（上界）与 $\rho$ 阶子式 gcd（下界）；$\rho=0$ 时等价于 $F=0$ |
| 缺少回归用例 | 新增假阳性用例、$\rho=0$ 用例、合法 $(5b)$ 用例 |

## 如何复现

```bash
# 数值/符号验证（含 cond_5b 回归）
python proof/5b_upper_bound/scripts/verify_upper_bound.py
python scripts/core/exact_gcd.py

# Lean（WSL）
export PATH="$HOME/.elan/bin:$PATH"
cd ~/WorkSpace/lean4/MyProof && lake build
```

## 与 NP-hard 的关系

**上界对硬度没有直接贡献**：它不限制解集，只是把 $(5b)$ 从“秩等式”归约为“不降秩”。因此

$$\text{NP-hard 的难度（若存在）只能来自下界，不可能来自上界。}$$

但它是**问题表述的必要前提**：没有上界，$(5b)\iff\gcd=1$ 不成立，项目的 $(S)$ 判据、V1（给定 $L$ 的多项式验证）以及所有基于 gcd 的讨论都会失去依据。所以不能说“完全无关”。

## 本次改动文件（2026-10-21）

| 文件 | 改动 |
|---|---|
| `scripts/core/exact_gcd.py` | `cond_5b` 加上上界检查（$(ρ+1)$ 阶子式）；新增 `cond_5b_diagnose`；5 个回归用例 |
| `scripts/lean/Theorems/UpperBound.lean` | **新增**：4 条上界定理（矩阵 / 线性映射 / 原始 4 块） |
| `scripts/lean/Theorems/Pencil.lean` | 更正 `T2_pencil_rank` 的 docstring：它只是恒等式，不是完整 T2 |
| `scripts/lean/Factor.lean` | `tuple` 加 `@[expose]`；新增 `tuple_apply` |
| `scripts/lean/Theorems.lean` | 新增 `import MyProof.Theorems.UpperBound` |
| `proof/00_证明索引.md` | 新增本归档条目；给 S 的“下界已证”加条件性提醒 |
| `scripts/core/README.md` | 更新 `cond_5b` 的说明 |
| `scripts/lean/README.md` | 更新状态横幅（8 条 → 70+ 条） |
| `README.md` | 新增复现命令与目录说明 |
| `proof/5b_upper_bound/lean/MyProof/` | 归档快照：`Pencil.lean` / `Factor.lean` / `ABridge.lean` / `UpperBound.lean` + 最小根 `Theorems.lean` |

## 相关文档

- 原始讨论：[`docs/04_形式化验证方法.md`](../../archive/methodology/04_形式化验证方法.md#L143-L151)（案例 3：只检查一个方向是错的）
- 推导记录：[`history/proof/12_命题q的数学推导.md`](../../archive/session_history/proof/12_命题q的数学推导.md#L88-L97)（“上界条件自动满足”）
- 下游结论：[`problems/q4.md`](../../archive/problem_statements/q4.md)（$d_{CA}$ 与 $q_0$ 的三情形）、[`proof/S`](../../archive/proof_notes_dimV_line/S_维数下界定理_2026-10-21.md)（下界方向的另一条线）
