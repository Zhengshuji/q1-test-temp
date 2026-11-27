# workspace/ —— 目录地图

> **规则（2026-11-26 起）**：一个目录 = **一个研究方向**；目录名用研究对象/问题命名，不用内部代号。
> 按用途划分的内容（对外文档、管理、工具、讨论、审计）放 [support/](support/README.md)；
> 临时文件放 `_exchange/`。结论仍进 `proof/` + `docs/02`，工具进 `tools/`，文献进 `literature/`。

## 研究方向

| 方向 | 研究问题 | 子方向 | 状态 |
|---|---|---|---|
| [q1_true/](q1_true/README.md) | 证 $q1$ 为真：NP-hard / $\exists\mathbb R$-hard 归约（硬度侧） | `multiplication_gate`（活跃）、`rank_gates`（历史）、`arm_reduction`（规划） | **活跃**（乘法门） |
| [q1_false/](q1_false/README.md) | 证 $q1$ 为假：$\mathrm{DEC}(q)$ 的多项式判定（算法侧） | `c_stratification`（活跃）、`decision_algorithms`（冻结）、`feasibility_geometry`（历史） | **活跃**（$c$ 分级） |
| [kronecker/](kronecker/README.md) | 观测器铅笔的 Kronecker 结构（B.6/B.7 的实验与数据） | — | 历史（被 `proof/kron_null_module` 引用） |

> `augmentation_family/` 已于 2026-11-26 解散：501 篇 attempts 按表迁入
> `q1_true/*/attempts/` 与 `q1_false/*/attempts/`（索引见 [ATTEMPTS_INDEX.tsv](ATTEMPTS_INDEX.tsv)）；
> 其旧 README 与阶段索引保存在 `archive/attempts_2026-11_augmentation_family_README.md`。

**每个方向（及其子方向）固定四件套**：`README.md`（总体介绍）、`STATUS.md`（现状 + 子级状态）、
`RESULTS.md`（成果汇总：上级索引、下级详细）、`LESSONS.md`（经验记录，给子 agent）。
`q1_true/`、`q1_false/` 与 6 个子方向的四件套均已建。

## 方向优先级（2026-11-27，ChatGPT 评估）

> 排序标准是**推进 $q1$ 的潜力**（不是论文产出价值）。外部意见，实施时仍需结合项目判断。

| 序 | 子方向 | 一句理由 | 可行性 / 风险 |
|---|---|---|---|
| 1 | q1_true/arm_reduction | ARM(3) 是最接近目标的现成硬度框架 | 中 / 可能无法忠实表达仿射约束 |
| 2 | q1_true/rank_gates | 秩约束可能绕过乘法门的部分障碍 | 中低 / 秩跳跃与自由变量可能不够强 |
| 3 | q1_false/feasibility_geometry | 可行域几何是归约与不可能性证明的共同基础 | 高 / 可能只得结构刻画 |
| 4 | q1_true/multiplication_gate | 自然路线，但已有多项 no-go | 低 / 需先找到绕开 no-go 的机制 |
| 5 | q1_false/decision_algorithms | 固定参数结果有独立价值，但难推一般情形 | 中高 / 参数随规模增长时失效 |
| 6 | q1_false/c_stratification | 分层可成独立论文，但与硬度问题联系较弱 | 高 / 风险在工作量与新颖性 |

## 对外材料（功能目录，暂在顶层）

| 目录 | 功能 | 说明 |
|---|---|---|
| [for_expert/](for_expert/README.md) | 对外自包含文档（每次一份；109、110 待回复）| 238 个文件、内部链接多；迁移到 `support/` 需要整体加深一层链接，放在第 2 步 |

## 支撑（功能目录）

| 目录 | 功能 |
|---|---|
| [support/](support/README.md) | `project_management`（管理）、`fer26b_example_audit`（审计）、`chatgpt_notes`（讨论）|
| `_exchange/` | 跨 Windows/WSL 的临时交换区；会话结束清理构建产物，脚本可留 |

## 主线与缺口（一屏）

$q1$ = 固定阶判定 $\mathrm{DEC}(q)$ 的复杂度：

$$\mathrm{DEC}(q):\ \text{给定 }(A,C,L_0)\text{ 与 }q,\ \text{判定 }\exists\,\mathcal L\ (q\times n,\ \operatorname{row}L_0\subseteq\operatorname{row}\mathcal L)\ \text{使 }(5a)\wedge(5b).$$

* 存在性刻画与 $(5a)$ 的通式/完备族：文献已解决（Fernando 2026 两篇），**不由本项目承担**；
* 复杂度上界：$\mathrm{DEC}(q)\in\exists\mathbb R$；固定 $q$ 的 XP 与固定 $\ell$ 的 FPT 见 **Paper I**；
* 最小阶与构造见 **Paper II**；本仓库的 Paper III（超平面层）与 Paper IV（$c=2$）是后续两篇；
* 缺口：**一般 $k>\omega$ 的分量描述与约束纤维判据**、硬度（$\exists\mathbb R$-hard 归约）、编码规模。

详见 [docs/05 Q1](../docs/05_open_questions.md)；$(5b)$ 工作总图在
[archive/project_reports/5b_map.md](../archive/project_reports/5b_map.md)。

## 放置规则

| 内容类型 | 去处 |
|---|---|
| 结论 / 引理（要给别人用的）| `docs/`（登记）+ `proof/<claim>/`（证明）|
| 可复用工具、脚本 | `tools/<类别>/` |
| 文献与阅读笔记 | `literature/` |
| 对外文档、管理、讨论、审计、工具配置 | `workspace/support/<功能>/` |
| 独立成篇、有留存价值但不是结论 | `archive/<内容类>/` |
| 无用 / 被取代 | `trash/`（登记后移入，不删除）|

`workspace/` 只留**正在推进的研究方向**与 `support/`、`_exchange/`；任务结束后材料按上表分派出去。
