# q1_false · 现状

> 更新：2026-11-26。501 篇 attempts 已按分类表迁入各子方向的 `attempts/`（见
> [../ATTEMPTS_INDEX.tsv](../ATTEMPTS_INDEX.tsv)）。
>
> **优先级（2026-11-27，ChatGPT 评估；标准=推进 q1 的潜力）**：
> 3 `feasibility_geometry` → 5 `decision_algorithms` → 6 `c_stratification`（全局序）。
> 注：`c_stratification` 排名低是针对“解 q1”；它仍是 Paper III/IV 的当前论文线。

## 一句话

**固定参数的判定已闭合到论文级**（Paper I：固定 $q$ 的 XP、固定 $\ell$ 的 FPT、$\exists\mathbb R$）；
**最小阶与构造**在 Paper II；**一般 $q$（$q$ 随输入增长）仍开放**——这正是 $q1$。
当前唯一在推的算法侧方向是**按 $c$ 分级**：$c=1$（Paper III）与 $c=2$（Paper IV）。

| 子方向 | 状态 | 卡点 | 下一个里程碑 |
|---|---|---|---|
| c_stratification | 活跃 | $c=1$ 的 S3（移动根）= 唯一的 PIT 缺口；$c=2$ 的实点与位复杂度 | 补上 S3 或证明它是真障碍；$c=2$ 的实设计版本 |
| decision_algorithms | 已冻结 | 无（已成 Paper I） | 只做索引，不再推进 |
| feasibility_geometry | 历史 | 闭包/层公式已被反例修正 | 只作历史记录 |

## 子方向状态表（含未尝试）

| 子方向 | 是否尝试 | 是否有记录 |
|---|---|---|
| $c=1$ 超平面层 | 是 | 是（Paper III） |
| $c=2$ | 是 | 是（Paper IV） |
| 一般 $c$（固定 $c$ 多项式？） | 部分（$c=2$ 单谱） | 是 |
| 一般 $k>\omega$ 的分量描述 | 否（主峰） | 只有 $c=1$ 的定理 |
| 层单调性 | 否（有反例） | 是（Paper IV 的定理 16） |
| 位复杂度（固定 $c$） | 部分 | 是（$c=2$ 单谱） |
