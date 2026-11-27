# q1_true · 现状

> 更新：2026-11-26。501 篇 attempts 已按分类表迁入各子方向的 `attempts/`（见
> [../ATTEMPTS_INDEX.tsv](../ATTEMPTS_INDEX.tsv)）。
>
> **优先级（2026-11-27，ChatGPT 评估；标准=推进 q1 的潜力）**：
> 1 `arm_reduction` → 2 `rank_gates` → 4 `multiplication_gate`（全局序；本方向内按此顺序尝试）。

## 一句话

**没有成立的归约。** 已落地的只有 sound 的“非零门”（$f\ne0$）与“输入非零门”（$x\ne0$），
乘法门 $z=xy$ 仍不 sound；wiring/port 有条件的 no-go。

| 子方向 | 状态 | 卡点 | 下一个里程碑 |
|---|---|---|---|
| multiplication_gate | 活跃 | 复制整行 $H_2=(H_A)_1$ 会强制 $y_1=1$；单坐标复制无机制 | 一个 copy/format gadget $(0,y,z)\to(0,1,z)$，或证明其不可能 |
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
