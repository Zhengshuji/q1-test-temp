# 769 阶段整理：ABCD 进度与 Paper I/II 的 Lean 复用

> 2026-11-28。盘点 ABCD 当前状态；核查 Paper I/II 的 Lean 工程可复用内容；并实际移植了 Bézout 家族模块。
> 状态：**[整理]** + **[Lean]**（移植模块）。

## 1. ABCD 进度（截至 768）

| 项 | 内容 | 等级 | 文件 |
|---|---|---|---|
| A | 固定 $U$ 存在性定理（$\mathcal F_U$、$L=[H|M]$ 构造、基不变性） | 已证 | 761 |
| A | 非退化实例（$n=6,k=2,d'=1$，$W_{\mathrm{top}}\ne0$，秩 5<6，$\gcd=1$） | 精确验证 | 764 |
| A | $d'=k$ ⇒ $(5a)$ 自动；非退化 $\iff d'<k$ | 已证 | 767 |
| A | $\mathcal F_U$ 仿射几何（$\dim=q\,a$）与坏集 $\mathcal B_U$ | 已证 | 768 |
| B | Bézout 接口：$\gcd=1\iff\exists u_j\sum u_jf_j=1$；$K(x)$ 陷阱 | 已证/整理 | 765 |
| C | 独立审计：733/747/739/753 通过；两处笔误已修 | 精确验证 | 758/759 |
| D | Lean：$({\star\star})$ row(HA)⊆row A | Lean | 762 |
| D | Lean：$({\star})$ 的抽象正交补部分 | Lean | 766 |
| D | Lean：Bézout 家族（移植 Paper I） | Lean | 769（本文） |

## 2. Paper I/II 的 Lean 可复用清单

（Paper I/II 的 Lean 工程在独立仓库，Mathlib 版本与本仓库不同，但数学接口兼容。）

### 2.1 行空间 / 秩（可直接支撑 761/767 的矩阵层）

- `rowSpace_eq_range_transpose`：行空间 $=\operatorname{range}(A^{\mathsf T})$；
- `rowSpace_mul_le`、`rowSpace_mul_eq_map`、`rowSpace_pencil_eq_map`：行空间在乘法/铅笔下的像；
- `rank_eq_finrank_rowSpace`、`rank_eq_finrank_rowSpan`：秩 = 行空间维数；
- `mulVecLin_range_eq_ker`：核的基矩阵 $\Rightarrow$ range = ker；
- `rank_vstack_add_rank_mul`、`rank_fromRows_add_map`、`rank_neg_eq`：堆叠秩恒等式；
- `rank_le_rank_fromRows_right`、`exists_mulVec_eq_iff_mem_rowSpace`：行空间/可解性判据。

### 2.2 gcd / Bézout（直接支撑 B 与 677 的判定链）

- `exists_bezout_family`：$\deg f_i\le\omega$、无公共根 ⇒ $\exists g_i$，$\sum g_if_i=1$ 且 $\deg g_i<\omega$（Paper I Lemma 4；**已移植**）；
- `exists_bezout_deg_lt`、`bezout_of_gcd_eq_one`：两多项式的 Bézout 与次数界；
- `gcd_isConst_iff_no_common_complex_root`：$\gcd$ 为常数 $\iff$ 无公共复根（$\mathbb Q[\lambda]$ 族）；
- `pencilMinors_gcd_isConst_iff_no_common_complex_root`：铅笔子式族的同一判据；
- `exists_leftInverse_pencil_of_gcd_isConst`、`rank_eq_of_leftInverse_pencil`：$\gcd$ 常数 ⇒ 多项式左逆 ⇒ 每个 $\lambda$ 满秩（正是 $(5b)$ 的代数形式）；
- `exists_bezout_iff_mem_rowSpace_window`、`mem_rowSpace_window_iff_no_common_complex_root`：Bézout 与行空间窗口的等价（Paper I 的窗口判据）。

### 2.3 铅笔 / 常数秩 / 子空间

- `hasConstantRank_iff_rankIndependent`：常数秩与“秩无关”的等价；
- `finrank_sup_eq_iff_le`、`finrank_ker_add_finrank_range`、`finrank_add_one_le_of_spectral`：维数/核-秩工具；
- `rank_fromRows_zero*`、`GramRankAugmented.*`：块矩阵与 Gram 秩。

### 2.4 不能直接借的部分

- Paper I/II 的 Lean 工程中**没有**正交补（`orthogonal`）相关引理；
- 因此 $({\star})$ 的 $\operatorname{row}A^{\perp}=\ker A$ 桥接仍需自写（766 已备好抽象部分）；
- Paper I 的定理多限定在 $\mathbb Q$ 或 $\mathbb R$，用到我们 $\mathbb C$ 的情形时需要复化映射（`rank_map_ofReal`、`Complexify` 一类可复用）。

## 3. 本次实际移植（已验证）

从 Paper I 的 Lean 工程复制三个模块到 `MyProof`（保持 `Q1Paper` 命名空间）：

- `Q1BezoutDeg`（Bézout 次数界的基础）；
- `Q1HyperplaneAvoid`（超平面回避）；
- `Q1BezoutFamily`（`exists_bezout_family`）。

结果：

| 项 | 结果 |
|---|---|
| 三个模块单独编译 | 0 |
| 并入构建图后 `lake build MyProof` | **BUILD=0（9123 jobs）** |
| `#print axioms Q1Paper.exists_bezout_family` | `[propext, Classical.choice, Quot.sound]`，无 sorryAx |

**意义**：B 的“存在有界 Bézout 系数”这一步现在有机器检查的现成定理，不必从零形式化。

## 4. 下一步

1. **继续移植** Paper I 的 `Claim16_Gcd`/`MinorRank`/`SpectralCertificate` 相关模块，把 677 的“$\gcd$ 常数 $\iff$ 每个 $\lambda$ 满秩”接到 Lean；
2. 自写 $({\star})$ 的桥接（$\operatorname{row}A^{\perp}=\ker A$，实数域逐坐标），完成 753 的完整 Lean；
3. B：在 764 的非退化实例上验证 Bézout 系统的确有解（数值/精确）。

## 状态

- 移植：**[Lean]**（BUILD=0，公理干净）；
- 复用清单：**[整理]**；
- $({\star})$ 桥接：**[待自写]**。
