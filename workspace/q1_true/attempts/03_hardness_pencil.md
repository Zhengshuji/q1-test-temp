# 路线 03：矩形铅笔 rank-drop 作为 ∃R-hardness 的中间问题？

## 目标

按专家 QA10 §6.3 的建议：先证"抽象矩形铅笔 rank-drop"的硬度，再试着把它实现成观测器实例，
从而得到 $q1$（或至少 DEC(q)）的 ∃R-hardness。

## 设想与理由

专家建议的中间问题：给定 $(\iota,\bar A)$，问 $\exists\lambda\in\mathbb C:\operatorname{rank}(\lambda\iota-\bar A)<t$。

## 做法

1. 文献检索（2026-10-30，见 [literature/SEARCH_LOG.md](../../../literature/SEARCH_LOG.md)）；
2. 直接分析该中间问题的结构。

## 进展与判断

**该中间问题本身不太可能 ∃R-hard**：

- 对**方**铅笔（$\iota$ 可逆），$\lambda\iota-\bar A$ 奇异 $\iff\lambda$ 是 $\bar A$ 的特征值——代数闭域上**恒真**
  （这就是 Theorem D 的 $q=t$ 分支）。
- 对**矩形**铅笔，$\operatorname{rank}<t$ 等价于全部 $t\times t$ 子式的 $\gcd$ 有零点；这仍是"一个线性代数事实"，
  其判定是多项式时间可做的（gcd 次数 / 秩计算）。
- 也就是说：**抽象铅笔层面没有硬度**；硬度只能来自"这个铅笔必须能被 $(A,C,L_0)$ 实现"的**耦合约束**
  （$V=\ker[C;CA]$、$Z=\ker[C;L_0]$、功能可观测、$(A)$ 的秩条件）。

## 最终结论

**把"抽象铅笔 rank-drop"当作硬度中间问题不成立**——它是多项式可判的；
真正的硬度（若有）必须来自实现约束。这修正了专家建议的一个假设（他的建议在"抽象层面可能有硬度"上偏乐观）。

## 放弃原因

放弃"抽象铅笔 rank-drop 作为硬度中间问题"这一步：**具体卡在**——该问题是多项式可判的
（方铅笔：$\lambda$ 是 $\bar A$ 的特征值，代数闭域上恒真；矩形铅笔：判定全部 $t\times t$ 子式的 gcd 是否有零点，
多项式时间可做），因此**不可能**是 ∃R-hard（除非 P=∃R）。硬度必须来自 $(C,L_0)$ 对 $V,Z$ 的耦合约束。

## 残留价值

- 明确了硬度的来源：不是铅笔本身，而是 $(C,L_0)$ 对 $V,Z$ 的"钉住"；
- 与 R17 的教训一致：可行集的薄性来自实现约束，不来自铅笔。

## 相关文件

- [workspace/q1_true/attempts/02_hardness_skeleton.md](02_hardness_skeleton.md)（两段式骨架）
- [proof/h_bound/README.md](../../../proof/h_bound/README.md)（Theorem C/D/E）
- [archive/expert_correspondence/QA10_2026-10-30.md](../../../archive/expert_correspondence/QA10_2026-10-30.md) §6.3
