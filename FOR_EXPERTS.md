# FOR_EXPERTS · 阅读入口（公开快照）

这是一个 q1/MIN-ROWS 研究框架仓库的**公开快照**（自动整理，非逐次提交历史）。
目的：让专家不必访问原工作区即可直接阅读现状、结果与尝试记录。

## 先读什么（建议顺序）

1. [README.md](README.md) —— 问题、地图、目录语义；
2. [STATUS.md](STATUS.md) —— 一页纸现状（含文献定位与开放问题）；
3. [workspace/ATTEMPTS_INDEX.tsv](workspace/ATTEMPTS_INDEX.tsv) —— 全部 attempts 的编号/方向/子方向/策略索引；
4. [workspace/q1_false/feasibility_geometry/STATUS.md](workspace/q1_false/feasibility_geometry/STATUS.md) —— **当前主线**（编号 545–661）；
5. [workspace/q1_true/STATUS.md](workspace/q1_true/STATUS.md) —— 硬度侧（含已冻结的 rank_gates 与 multiplication_gate 的关闭结论）。

## 重要说明

- **Paper I / Paper II** 只维护在另一个仓库 `Zhengshuji/q1-functional-observer`；本仓库不复制、不复述它们的证明。
- **Paper III / IV** 位于 [paper/](paper/) 目录。它们**可靠性低于 Paper I/II**，仅作参考，不作为权威依据。
- 本快照**排除了** `archive/expert_correspondence/`（专家往来，含隐私）、`trash/` 与 `workspace/_exchange/`（临时文件）。
- 验证等级按 CLAUDE.md：`[Lean]` > `[已证-纸面]` > `[精确验证]` > `[数值]` > `[猜想]`；实验不计入证明。
- 部分早期文档可能含过时链接或已被撤回的结论；以 `STATUS.md`、`RESULTS.md` 与 `proof/refuted/` 为准。

## 复核入口

- 布局/一致性审计：`python tools/hygiene/audit_layout.py`（应 0 issue）；
- 各 attempts 附带的 `verify*.py` / `.lean` 为对应结论的机器检查；
- Lean 工程不在本仓库（在 WSL 的 `MyProof` 与 `Q1Paper` 中），此处只保留 `.lean` 源文件副本。
