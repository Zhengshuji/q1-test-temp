# 路线 2：min-rank / 覆盖 / 反馈设计

## 目标
把 MIN-ROWS 归约到已知 NP-hard 的矩阵/子空间问题（min-rank、集合覆盖、反馈设计），保持可行性与最优值双向。

## 设想与理由
$q_{\min}$ 是"最小行数"，而 min-rank 类问题也是"最小秩/最小维数"，形状最近。
相邻的 sensor placement 类问题**已知** NP-hard（[literature/notes/LITERATURE_COMPLEXITY.md](../../../literature/notes/LITERATURE_COMPLEXITY.md)）。

## 做法
20 条具体路线（项目早期 `ATTEMPTS_AND_BARRIERS.md` 与 `archive/attack_A2V0/` 记录），主要三类：
1. **min-rank 编码**：让 $q_{\min}$ 等于某个仿射族里矩阵的最小秩；
2. **覆盖编码**：让每条约束对应一个"集合"，$q$ = 覆盖大小；
3. **反馈设计编码**：让 $(5a)$ 对应"$\mathcal V$ 是某闭环的不变子空间"。

## 进展（结论性）
- 所有 min-rank 类编码最终都落在 **min-rank $k=1$**，即"线性截面里有没有秩一矩阵"——Lovitz 的**公开问题**（见 [07_linear_section.md](07_linear_section.md)）。
- 覆盖类编码死在：$C=I$ 时 $(5a)(5b)$ 自动成立（$\mathcal J=\mathbb C^n$、$K=0$），覆盖结构被抹平。
- 反馈设计类编码死在：$(5b)$ 是**开条件**，编码不出"必须选"的组合约束。

## 最终结论
**死/受阻**。不是缺技巧，而是落点本身是公开问题。

## 残留价值
- "相邻问题 NP-hard"的文献清单。
- 一个明确的**归约禁忌清单**（哪些编码方式必然失效）。

## 相关文件
- [literature/notes/LITERATURE_COMPLEXITY.md](../../../literature/notes/LITERATURE_COMPLEXITY.md)、[LITERATURE_COVER.md](../../../literature/notes/LITERATURE_COVER.md)
- [attempts/00_attempts_and_barriers.md](00_attempts_and_barriers.md)