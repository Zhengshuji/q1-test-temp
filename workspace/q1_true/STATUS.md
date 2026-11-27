# q1_true · 现状

> 更新：2026-11-26。501 篇 attempts 已按分类表迁入各子方向的 `attempts/`（见
> [../ATTEMPTS_INDEX.tsv](../ATTEMPTS_INDEX.tsv)）。
>
> **路线状态（2026-11-27 更新）**：`arm_reduction` 关闭、`rank_gates` 冻结、`multiplication_gate` 的自由行 gadget 路线关闭（627/628）。
> 本方向目前**没有可用的 hardness 归约**；仅剩 $W\ne0$ 的数据层结构分析（与 q1_false 主线的 629/631/639/651 相接）。
> （旧优先级“1 arm_reduction → 2 rank_gates → 4 multiplication_gate”已失效，保留在历史记录中。）

## 一句话

**没有成立的归约。** 2026-11-27 关闭“自由行 gadget”路线（627/628：自由行是存在量词，门条件可由求解者满足）。 已落地的只有 sound 的“非零门”（$f\ne0$）与“输入非零门”（$x\ne0$），
乘法门 $z=xy$ 仍不 sound；wiring/port 有条件的 no-go。

| 子方向 | 状态 | 卡点 | 下一个里程碑 |
|---|---|---|---|
| multiplication_gate | 活跃但**自由行 gadget 路线关闭**（627/628） | 自由行可任意满足门条件；598/601/613 只是“某个 $H$ 可行”的描述 | 只剩 $W\ne0$ 的数据层分析（与 q1_false 的 629/631/639/651 相接） |
| rank_gates | **冻结**（q=5 结构化秩门） | $q=2$ 完整 no-go；$q=4$ 不可提升；$q=5$ 仅搜索边界 | 495–505 的 no-go 与实验；重启入口见 505/503 |
| arm_reduction | **关闭**（no-go 已写） | 载体界、仿射控制、行包含接口 no-go、谱机制无构造 | 仅保留记录；若有人提出谱秩强制 gadget 再重开 |

## 子方向状态表（含未尝试）

| 子方向 | 是否尝试 | 是否有记录 |
|---|---|---|
| 乘法门（sound，逐行可提升） | 是 | 是（gadget/wiring/port） |
| rank 门 | 是 | 是（已撤回/搜索边界） |
| ARM(3) 翻译 | 否 | 只有计划 |
| 拟阵/TAP 归约 | 是 | 是（已死） |
| min-rank / 覆盖 | 是 | 是（受阻于公开问题） |
| 图归约 / CYCLIC-COVER | 是 | 是（已死） |
| 双向量（bivector）硬度 | 否（只列必要条件） | 是（blueprint） |
