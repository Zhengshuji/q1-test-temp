# q1_false —— 大方向：$q1$ 是“假”（多项式可算）

> **定位（2026-11-26）**：本目录是**算法侧**的总入口。上级做协调与索引；具体推进在子目录。
> Paper I / Paper II 是本方向已冻结的两篇（判定与最小阶），**引用它们、不在这里复述**。

## 子方向

| 子目录 | 研究问题 | 状态 |
|---|---|---|
| [c_stratification/](c_stratification/README.md) | 按 $c=k-\omega$ 分级：$c=1$ 超平面层（Paper III）、$c=2$（Paper IV） | **活跃** |
| [decision_algorithms/](decision_algorithms/README.md) | 判定 $\mathrm{DEC}(q)$ 的算法与固定参数（Paper I 的本地支撑） | 已冻结（并入 Paper I） |
| [feasibility_geometry/](feasibility_geometry/README.md) | 增广族/子空间可行性、层公式、$q_0$ 扫描（001–098 一段） | 历史 |

## 本层文档

- [STATUS.md](STATUS.md) —— 现状 + 子方向状态表（含未尝试的）
- [RESULTS.md](RESULTS.md) —— 成果索引（论文 + 本地独立结果）
- [LESSONS.md](LESSONS.md) —— 跨子方向的经验与死路

## 与另一方向的关系

本方向证 **tractable**，[q1_true/](../q1_true/README.md) 证 **hard**；两边共用压缩链、子空间语言与工具。
Paper I/II 的结论是本方向的可靠基准，但**本地的进一步探索**（如 $c=1$ 的 S3 缺口）仍是独立结果。
