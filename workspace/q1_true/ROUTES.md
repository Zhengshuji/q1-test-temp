> **历史版本**（2026-11-26 结构重整前的 README），保留原来的路线一览与链接。
> 现行入口见同目录 [README.md](README.md)；本文件只作路线索引的历史记录。

# 方向 q1_true：证 MIN-ROWS 是 NP-hard

> 目标：构造保持可行性与最优值的多项式归约，或证明某个明确的子问题是 NP-hard 且能传递过来。
> **现状：没有成立的结果。8 条路线全部死掉或卡在公开问题上。**

## 路线一览

| # | 路线 | 文件 | 状态 |
|---|---|---|---|
| 1 | 拟阵 / TAP（树增广）| [attempts/01_matroid_tap.md](../../archive/attempts_2026-10/q1_true/01_matroid_tap.md) | **死**（$(T)$ 有反例 + 圈空间不可实现）|
| 2 | min-rank / 覆盖 / 反馈设计 | [attempts/02_minrank_cover.md](../../archive/attempts_2026-10/q1_true/02_minrank_cover.md) | 死/受阻（落在公开的 min-rank $k{=}1$）|
| 3 | Z 形式 | [attempts/03_z_formulation.md](../../archive/attempts_2026-10/q1_true/03_z_formulation.md) | 未完成 |
| 4 | 谱切割 / 块结构 | [attempts/04_speccut.md](../../archive/attempts_2026-10/q1_true/04_speccut.md) | **死**（$\mathbb F_p$ 伪影）|
| 5 | 图/超图归约（CYCLIC-COVER）| [attempts/05_graph_reduction.md](../../archive/attempts_2026-10/q1_true/05_graph_reduction.md) | **死**（与 1 同源）|
| 6 | 混合情形（代数 ⊗ 谱）| [attempts/06_mixed_case.md](../../archive/attempts_2026-10/q1_true/06_mixed_case.md) | **死**（无额外组合结构）|
| 7 | 线性截面秩一（Lovitz 型）| [attempts/07_linear_section.md](../../archive/attempts_2026-10/q1_true/07_linear_section.md) | 受阻（公开问题）|
| 0 | 五次归约尝试总结 | [attempts/00_attempts_and_barriers.md](../../archive/attempts_2026-10/q1_true/00_attempts_and_barriers.md) | 记录 |

## 结论（诚实）

所有已知归约的落点都是同一个：**"线性截面里有没有秩一矩阵"（Lovitz，公开问题）**。

所以 q1 = 真 需要的**不是**技巧，而是先解决一个公开问题。见 [docs/03](../../docs/03_theorems_cited.md) 引用 5。

## 残留价值

- 坐标层 $(5b)$ 的**拟阵刻画**（并环集）——[attempts/01](../../archive/attempts_2026-10/q1_true/01_matroid_tap.md)
- 可实现 $\mathcal J$ 的**薄性**（Krylov 补丁）——同上 §7.7
- 反例（$(T)$ 为假）——同上 §7.9

## 相关

- 归约目标的形式化：[reduction_targets.md](reduction_targets.md)
- 方向总表：[../ATTEMPTS.md](../../ATTEMPTS.md)