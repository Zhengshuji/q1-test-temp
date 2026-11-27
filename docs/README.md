# docs/ — 严谨内容

> **规则**：本目录只放**定义**与**已证命题**（纸面证明或 Lean 检查）。
> Python 实例复核**不算证明**，一律放在 `proof/<claim>/verify.py`，不在本目录。

> **docs 与 proof 的分工（2026-11-06 确立）**
> * `docs/` 对**整个项目**负责（尤其 $q1$）：陈述、结论、等级、以及论文/note 级的整理；
>   条目里给"陈述 + 一句思路 + 等级 + 指针"，不再承载长篇证明细节。
> * `proof/<条目>/README.md` 是对应命题的**卷宗**：纸面证明全文、Lean（模块 + 声明 + 差异）、
>   精确验证（脚本 + 数字）、状态与历史，四类证据在**同一处**汇总，便于逐条检验。
> * 闸门：`tools/hygiene/audit_proof_map.py`（卷宗必备小节、索引登记、待建基线）。

| 文件 | 内容 | 等级 |
|---|---|---|
| [00_problem.md](00_problem.md) | 问题、$(5a)/(5b)$、已确认的等价形式、与文献的对应 | 定义 / 已证 |
| [01_notation.md](01_notation.md) | 全部记号 + 术语表（原 06_glossary 已合并） | 定义 |
| [02_theorems_proven.md](02_theorems_proven.md) | 已证命题索引（含证明与等级） | 已证 / Lean |
| [03_theorems_cited.md](03_theorems_cited.md) | 引用的文献定理 | 引用 |
| [04_structure.md](04_structure.md) | 主分解、算术侧（$P$）、已证的层结论、与 $q1$ 的关系 | 已证 |
| [05_open_questions.md](05_open_questions.md) | 开放问题（Q1 主问题；后续主线） | 开放 |
| [07_literature_review.md](07_literature_review.md) | 研究进展综述（文献面；不含本项目新结论） | 文献 |
| [08_results.md](08_results.md) | 结果汇总（按叙述组织；只收仍成立的陈述） | 已证 / 验证 / 引用 |

**docs/ 的定位**：只放**可靠成果**（定义、已证命题、引用定理、开放问题、文献综述），
合起来就是论文骨架；按文件分块只是为了相对独立地维护。

**不在本目录的**：管理/总览文档在 `workspace/support/project_management/`（工作清单 09、项目叙事 10、
资产盘点/路线 11）；经验数据、被推翻命题、尝试记录、Python 复核分别见
`workspace/`、`proof/refuted/`、`workspace/*/attempts/`、`proof/<claim>/verify.py`。
**不在本目录的**：经验数据（在 `workspace/q1_false/notes_data_shapes.md`）、
被推翻的命题（在 `proof/refuted/`）、尝试记录（在 `workspace/*/attempts/`）、
Python 复核（在 `proof/<claim>/verify.py`）。

- [`07_literature_review.md`](07_literature_review.md) — **研究进展综述**（最小阶功能观测器的文献面；含记号对照、五条研究线、时间复杂度现状）
