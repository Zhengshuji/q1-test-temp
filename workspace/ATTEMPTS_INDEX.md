# attempts 分层索引（2026-11-26 第一版）

> 表：[ATTEMPTS_INDEX.tsv](ATTEMPTS_INDEX.tsv)（501 行，一行一个 attempt）。
> **2026-11-26 已按本表迁移**：文件现在位于 `workspace/q1_*/<subdirection>/attempts/`；
> 表里的 `file` 列是原始文件名，路径按 `direction/subdirection` 拼出。
> `proof/` 的对应目录已复制到各子方向的 `proof/`（不移动、不维护 `proof/` 本身）。

## 层级

| 层 | 取值 | 作用 |
|---|---|---|
| L1 方向 | `q1_true` / `q1_false` / `meta` | 两个大方向；`meta` 是论文/审计/规划等支撑工作 |
| L2 子方向 | `multiplication_gate`、`rank_gates`、`arm_reduction`；`c_stratification`、`decision_algorithms`、`feasibility_geometry`；`paper_support` | 具体研究路线 |
| L3 策略 | `prove`（定理/判据）、`experiment`（扫描/证书/构造）、`audit`（专家裁决/撤回/更正）、`plan`（路线/规划）、`paper`（论文/Lean） | 同类尝试共用一套做法与验收标准 |

## 计数（第一版）

| 方向 | 子方向 | 条数 |
|---|---|---|
| q1_false | c_stratification | 192 |
| q1_false | decision_algorithms | 103 |
| q1_false | feasibility_geometry | 94 |
| q1_true | multiplication_gate | 92 |
| q1_true | rank_gates | 12 |
| q1_true | arm_reduction | 8 |

| 策略 | 条数 |
|---|---|
| experiment | 270 |
| audit | 134 |
| prove | 80 |
| plan | 9 |
| paper | 8 |

## 读法

- `num` 是文件名前缀；目录里存在**两套编号**（如 `390_352_arm...`，前缀 390、内容编号 352），迁移时以 `file` 列为准。
- `title` 是文件第一行标题；`(no title)` 的条目按相邻块推断。
- `strategy` 是尝试类型，不是可靠性等级；可靠性仍看各 attempts 内的 `## 最终结论` 与等级标记。

## 复核建议

1. 先抽查 `q1_true`：`rank_gates` 与 `multiplication_gate` 的边界（$q=4/5$ 门 vs 乘法门）；
2. 再抽查 `meta/paper_support`：专家裁决类是否应归到对应方向，而不是统一进 meta；
3. `c_stratification` 与 `decision_algorithms` 的边界（层几何 vs 固定参数算法）。

复核后我再按表把 attempts 移入各子方向的 `attempts/`，并统一改 `ATTEMPTS.md` 与交叉链接。
