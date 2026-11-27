# 路线 7：线性截面里的秩一矩阵（Lovitz 型）

## 目标
把 MIN-ROWS 的可行性在 $q=1$ 或小 $q$ 时化为"某个线性截面里是否存在秩一（或低秩）矩阵"，从而用已知的公开问题做"归约即失"。

## 设想与理由
$q$ 很小时，$\mathcal V$ 是低维子空间，其生成矩阵 $R$ 低秩；$(5a)$ 给**线性**约束（$R$ 的条目），$(5b)$ 给**行列式/铅笔**条件。
这个形状与"线性截面里找低秩矩阵"完全同构。

## 做法
- 写出 $q=1$ 时的完整约束系统（见 `archive/expert_correspondence/` 的相关推导与 `archive/old_scripts/q1_true_routes/`）；
- 检查是否存在"线性截面 + 秩一"的等价实例族。

## 进展
- 形状确认：约束确实落在"线性截面 + 低秩"上；
- 但 **min-rank $k=1$（线性截面里有没有秩一矩阵）是公开问题**（Lovitz；项目 `archive/process_logs/REVIEW_LOG.md` 记录）。
- 因此本路线的"归约"若成立，等于同时解决一个公开问题。

## 最终结论
**受阻**（不是死，是被公开问题挡住）。

## 若未来要走
需要的不是新技巧，而是：
1. 一个已知 NP-hard 的"线性截面 + 秩一"变体（例如限制在 $\{0,1\}$ 或特定结构的截面上）；
2. 或直接证明 min-rank $k=1$ 的复杂度（公开问题）。

## 相关
- [attempts/02_minrank_cover.md](02_minrank_cover.md)
- [docs/05](../../../docs/05_open_questions.md) Q3

## 相关文件
- [02_minrank_cover.md](02_minrank_cover.md)
- [../../../docs/05_open_questions.md](../../../docs/05_open_questions.md) Q3
