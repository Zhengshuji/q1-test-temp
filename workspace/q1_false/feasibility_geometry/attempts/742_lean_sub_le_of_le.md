# 742 Lean 内核收尾：rank_sub_le_of_le 入构建图

> 2026-11-27。按“关键内核用 Lean、其余以推进为主”的要求，把 734 所需的最终形式（`rank_sub_le_of_le`）并入构建图。
> 状态：**[Lean]**（内核层）。

## 文件与定理

`MyProof/Q1RankCore5.lean`（导入 `MyProof.Q1RankCore`）：

```lean
theorem q1_rank_sub_le_of_le {a : Cardinal} (f g : V →ₗ[K] W) (h : g.rank ≤ a) :
    (f - g).rank ≤ f.rank + a
```

证明：`q1_rank_sub_le` + `add_le_add_left`（`rank` 在 Mathlib 中是 `Cardinal` 值，需 `add_comm` 调整）。

## 验证

| 项 | 结果 |
|---|---|
| 注册（`scripts/blocks.tsv`、`in_build.txt`，替换掉先前误写的 `Q1RankCore3/4` 条目） | 完成 |
| `bash scripts/gen_blocks.sh` | GEN=0 |
| `lake build MyProof` | **BUILD=0（9118 jobs）**，`Q1RankCore5` 已构建 |
| `#print axioms q1_rank_sub_le_of_le` | `[propext, Classical.choice, Quot.sound]`，无 sorryAx |

（过程中 `Q1RankCore3/4` 因 `Cardinal` 加法方向与注册行被误写，已删除并回退；当前只保留 `Q1RankCore` 与 `Q1RankCore5`。）

## 覆盖范围与等级

- **[Lean]**：`q1_rank_neg`、`q1_rank_sub_le`、`q1_rank_sub_le_of_le`、`q1_dim_sup_add_dim_inf`；
- **[已证-纸面]**：734/739 的完整陈述（\(G=LW\)、\(lN=0\)、商空间同构 \(T/(U\cap T)\cong(U+T)/U\) 尚未 Lean 化）；
- 按用户 2026-11-27 的指示：Lean 只保证“推导内核无误”，不再为完整命题的每个细节做形式化。

## 当前数学进展（摘要）

- 733：\(d'=2>s=t=1\) 可行（\(\omega>s\) 有效例），子 agent 独立复算；
- 734：\(d'\le\operatorname{rank}(HM)+\dim E_H\)；
- 737/739：\(\dim E_H=\dim(U\cap T)+\operatorname{cls}\)（等式）；
- 735：665 的 \(T\)-版本；736：商空间方向性（已被 739 取代）。

## 下一步

1. 数学：用 739 的等式重新审视 \(t=1\) 与 \(t=2\) 的方向性判据，寻找“等式取等但不可行”的 733 型边界；
2. 子 agent：`eq-search` 正在搜索 739 等式的反例（\(k=5/6\)、\(\operatorname{cls}\ge2\)）；
3. 文档：把 732（\(d'\le t\)）的“推翻”与 733 的边界例子统一进预筛选链说明。

## 状态

- Lean 内核：**[Lean]**（BUILD=0，axioms 干净）；
- 完整 734/739：**[已证-纸面]**；
- eq-search：**[进行中]**。
