# 762 Lean：753 的 $({\star\star})$ 已入构建图

> 2026-11-27。把 753 的两条恒等式中的 $({\star\star})$（$\operatorname{row}(HA)\subseteq\operatorname{row}A$）形式化并并入构建图。
> 状态：**[Lean]**。

## 文件与声明

`MyProof/Q1RowSpace2.lean`（带模块 docstring）：

```lean
def q1_rowSpace' (A : Matrix n p K) : Submodule K (p → K) :=
  Submodule.span K (Set.range A.row)

theorem q1_rowSpace'_mul_subset (H : Matrix m n K) (A : Matrix n p K) :
    q1_rowSpace' (H * A) ≤ q1_rowSpace' A
```

证明：$(HA).\mathrm{row}_i=\sum_j H_{ij}\cdot A.\mathrm{row}_j$，故在行空间张成中。

## 验证

| 项 | 结果 |
|---|---|
| 注册（`in_build.txt`、`blocks.tsv`） | 完成 |
| `bash scripts/gen_blocks.sh` | 0 |
| `lake build MyProof` | **BUILD=0（9119 jobs）** |
| `#print axioms q1_rowSpace'_mul_subset` | `[propext, Classical.choice, Quot.sound]`，无 sorryAx |

## 覆盖范围

- **已 Lean**：$({\star\star})$（对任意矩阵、任意域）；
- **未 Lean**：$({\star})$ $\dim(\operatorname{row}A+T)=k-\dim(\ker A\cap T^\perp)$（需要行空间/核/正交补的维数恒等式，Mathlib 无现成组合），以及 753 的“749 ⇒ 695 失败”推论（依赖 $({\star})$ 与维数比较）；
- 这三条仍为 **[已证-纸面]** + 精确验证（子 agent 400 组）。

## 下一步（D 的剩余部分）

1. 形式化 $({\star})$：可用
   - $(\operatorname{row}A+T)^{\perp}=(\operatorname{row}A)^{\perp}\cap T^{\perp}$；
   - $(\operatorname{row}A)^{\perp}=\ker A$（列核）；
   - `Submodule.finrank_quotient_add_finrank` 或 `finrank_sup_add_finrank_inf_eq`。
2. 再形式化 753 的推论（维数不等式）。

## 状态

- $({\star\star})$：**[Lean]**；
- $({\star})$：**[待形式化]**；
- 完整 753：**[已证-纸面]**。
