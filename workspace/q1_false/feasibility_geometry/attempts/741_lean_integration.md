# 741 Lean 集成：Q1RankCore 进入构建图

> 2026-11-27。把 740 的单文件内核并入 `MyProof` 构建图，跑通 `lake build MyProof` 与公理审计。
> 状态：**[Lean]**（内核层；`check_rules.sh` 仍有既有历史问题）。

## 文件与集成

`MyProof/Q1RankCore.lean`（带模块 docstring）：

```lean
theorem q1_rank_neg (g : V →ₗ[K] W) : (-g).rank = g.rank
theorem q1_rank_sub_le (f g : V →ₗ[K] W) : (f - g).rank ≤ f.rank + g.rank
theorem q1_dim_sup_add_dim_inf (s t : Submodule K V) :
    finrank K ↥(s ⊔ t) + finrank K ↥(s ⊓ t) = finrank K ↥s + finrank K ↥t
```

集成步骤（WSL）：

1. `scripts/in_build.txt` 追加 `Q1RankCore`；
2. `scripts/blocks.tsv` 追加 `A	Q1RankCore`；
3. `bash scripts/gen_blocks.sh`（GEN=0）；
4. `lake build MyProof` → **BUILD=0**（9116 jobs）；
5. `lake build MyProof.Q1RankCore` → **B=0**；
6. `#print axioms` 三条：
   `depends on axioms: [propext, Classical.choice, Quot.sound]`——**无 sorryAx**。

## 规则门

`bash scripts/check_rules.sh` 仍为 **RULES=1**，原因是仓库里**既有**的 scratch 文件缺模块 docstring（如 `CheckQ.lean`、`Probe6.lean`、`TestArith.lean` 等 20+ 个），与 `Q1RankCore.lean` 无关：

- `grep Q1RankCore /tmp/rules.log` 无命中；
- 模块头计数 `with module header: 30 / 209`，baseline 30，未下降；
- 本次已顺手删除自己产生的 6 个 scratch 文件（`ChkRank*.lean`），不再计入。

## 结论与等级

- 这三条**线性代数内核**：**[Lean]**（构建图内、公理干净）；
- 734/739 的**完整命题**仍为 **[已证-纸面]**：还差 \(G=LW\)、\(lN=0\) 的实现与商空间同构的形式化；
- 733 的矩阵实例：**[精确验证]** + 子 agent 复算，未 Lean 化。

## 下一步

1. 把 \(F_i=t_i+(U\cap T)\)（仿射交）形式化，推进 739 的完整陈述；
2. 或者形式化 733 的有限矩阵数据（\(\operatorname{rank}M=4\)、\(\gcd=1\)）；
3. 若要彻底转绿 `check_rules.sh`，需单独一轮清理历史 scratch 文件（不属于本轮范围）。

## 状态

- Q1RankCore：**[Lean]**（BUILD=0，axioms 干净）；
- check_rules.sh：**[既有失败，与本文件无关]**；
- 734/739 完整命题：**[已证-纸面]**。
