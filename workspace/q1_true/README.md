# q1_true —— 大方向：$q1$ 是“真”（NP-hard / $\exists\mathbb R$-hard）

> **定位（2026-11-26）**：本目录是**硬度侧**的总入口。上级只做协调与索引；具体推进在子目录。
> Paper I / Paper II 只给**上界**（固定参数、$\exists\mathbb R$），**没有**硬度结论；本方向独立于它们。

## 子方向

| 子目录 | 研究问题 | 状态 |
|---|---|---|
| [multiplication_gate/](multiplication_gate/README.md) | 构造 sound 的乘法门 $z=xy$，把 $\exists\mathbb R$-难问题归约到 $(5a)\wedge(5b)$ | **活跃**（唯一的在推方向） |
| [rank_gates/](rank_gates/README.md) | 用 $\operatorname{rank}H$ 的秩门编码布尔/算术条件（$q=4,5$） | **冻结**（q=5 结构化秩门，2026-11-27）：495–505 的 no-go 与实验；一般 $q=5$ 未解决 |
| [arm_reduction/](arm_reduction/README.md) | 用 Majumdar ARM(3) 的 gauge/composition 做翻译引理 | **关闭**：行包含接口 no-go（488）、谱机制无构造（489）；保留记录 |

## 本层文档

- [STATUS.md](STATUS.md) —— 现状 + 子方向状态表（含未尝试的）
- [RESULTS.md](RESULTS.md) —— 成果索引（本方向的“可借用”清单）
- [LESSONS.md](LESSONS.md) —— 跨子方向的经验与死路

## 与另一方向的关系

$q1$ 的两种结局都算答案：本方向证 **hard**，[q1_false/](../q1_false/README.md) 证 **tractable**。
两边共用压缩链、子空间语言与工具；任何一边的负结果都可能变成另一边的约束，**先查对方的 RESULTS/LESSONS**。
