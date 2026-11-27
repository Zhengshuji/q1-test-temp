# 740 Lean：734 的秩不等式内核与 739 的维数恒等式
> **已升级（741）**：`Q1RankCore.lean` 已并入构建图，`lake build MyProof` BUILD=0，公理审计干净；本文件的单文件状态由 741 取代。


> 2026-11-27。把 734/739 依赖的两条线性代数内核在 Lean 4（Mathlib）中机器检查。
> 状态：**[Lean 内核]**（EXIT=0）。

## 已形式化（Lean，内核检查）

文件：`~/WorkSpace/lean4/MyProof/MyProof/ChkRank6.lean`（WSL）。
编译：`lake env lean MyProof/ChkRank6.lean`，**EXIT=0，无 error**。

```lean
theorem rank_neg' (g : V →ₗ[K] W) : (-g).rank = g.rank
theorem rank_sub_le (f g : V →ₗ[K] W) : (f - g).rank ≤ f.rank + g.rank
theorem dim_sup_add_dim_inf (s t : Submodule K V) :
    finrank K ↥(s ⊔ t) + finrank K ↥(s ⊓ t) = finrank K ↥s + finrank K ↥t
```

其中 `rank_sub_le` 正是 734 的
$$\operatorname{rank}(HM-G)\le\operatorname{rank}(HM)+\operatorname{rank}G$$
的内核（取 $f=HM$、$g=G$）；`dim_sup_add_dim_inf` 是 739 中
$\dim(U+T)=\dim U+\dim T-\dim(U\cap T)$ 的维数恒等式。

## 覆盖范围

- **已 Lean 检查**：上述三条一般线性代数命题（$K$ 任意域、$V,W$ 任意模）；
- **未 Lean 检查**：734 的完整陈述（需要 $G$ 的行在 $T$、$Z$ 的存在性、$P(\mu)$ 的矩阵编码）与 739 的商空间同构部分（需要子空间/商空间的完整编码）；这两条目前是 **[已证-纸面]** + 精确验证；
- Lean 文件是 scratch 检查文件（`ChkRank6.lean`），未登记 `tools/lean/STATEMENT_MAP.md`，故此处只标 **[Lean 内核]**，不标整条命题的 `[Lean]`。

## 意义

- 734 与 739 的“代数骨架”已被机器确认，降低了这两条结论的记号风险；
- 剩余的纸面部分集中在“$G$ 的实现”（$G=LW$、$lN=0$）与商空间同构，这两块若要 Lean 化需要先建子空间/商空间的形式化接口。

## 下一步

1. 若继续 Lean 化：先形式化 $F_i=t_i+(U\cap T)$（仿射交），再形式化商空间同构 $\psi$；
2. 或者转向：把 733 的矩阵数据在 Lean 中编码（有限维矩阵、$\gcd$ 用多项式 API），验证 $\operatorname{rank}M=4$。

## 状态

- Lean 内核：**[Lean]**（`ChkRank6.lean`，EXIT=0）；
- 完整 734/739：**[已证-纸面]**；
- 733 的 Lean 编码：**[未做]**。
