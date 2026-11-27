# A4：双向量问题的硬度（blueprint，未启动归约）

## 目标

判定"线性空间 $L\subseteq\Lambda^2\mathbb C^N$ 是否含非零可分解元"（及带线性/开条件的变体）的**复杂度**：
多项式算法，或从已知 hard 问题归约。若后者成立，它就可以作为 $\mathrm{DEC}(q)$ 硬度的中间问题。

## 设想与理由

专家 2026-11-01 §5.5 把两件事分开：

- **Problem G**（一般）：$L\subseteq\Lambda^2E$ **任意**线性子空间；
- **Problem O**（observer 诱导）：$L=K=\bigcap_j\ker a_j$ 由铅笔记号给出。

**G 的硬度不自动传递到 O**——必须证明 observer 能实现任意 $L$。这与项目此前的教训一致（11c：Bad 不可设计）。

## 做法（计划）

1. 先把 G 写成标准形：$\exists p\in L:\ p\wedge p=0$（$\mathrm{rank}\,M(p)\le2$）；
2. 候选归约源：ETR/二次可行性（Mnëv 型 universality）、determinantal assignment、矩阵 pencil 秩条件；
3. 对 O 的**结构缺口**做定量：$K$ 的维数 $\ell$ 能否随 $n$ 增长？（A2 表明 $\ell$ 大时可分解性免费）

## 进展

本轮（A2）只得到**必要条件**，没有归约：

- 命题 K.1–K.3（[proof/bivector_r2](../../../proof/bivector_r2/README.md)）：$m\le4$、或 $\ell\ge N-(2m-4)$ 时**恒有**可分解元
  ⟹ 这些区域**没有**硬度空间；
- 算法 K.4：固定 $\ell\le3$ 时判定是常数规模 ⟹ **硬度必须让 $\ell$ 随 $n$ 增长**，且 $m\ge5$。

## 最终结论（当前）

**未启动归约**。可得的两条硬性条件：

$$\boxed{\ \text{硬度必须（i）发生在 }m\ge5\text{，（ii）且 }\ell=\dim K\text{ 随 }n\text{ 增长（}\ell<N-(2m-4)\text{）}\ }$$

## 放弃原因（若失败）

不适用（尚未启动）。已知的失败模式（来自 11c）：Bad 不可设计、正维数族要统一覆盖、$\mathbb F_p$ 构造不可提升到 $\mathbb Q/\mathbb C$。

## 残留价值

- 把"哪里**不可能**有硬度"钉死了（$m\le4$ 与 $\ell$ 大的区域），这本身排除了大量无效尝试；
- 与 A2 的接口：K.3 的阈值 $N-(2m-4)$ 是"可分解性免费"的精确边界。

## 相关文件

- [proof/bivector_r2/README.md](../../../proof/bivector_r2/README.md)（命题 K.1–K.4）
- [tools/verification/bivector.py](../../../tools/verification/bivector.py)（判定实现）
- [workspace/q1_true/attempts/10_hardness_attempt.md](10_hardness_attempt.md)（11c 的失败记录）
- [docs/05_open_questions.md](../../../docs/05_open_questions.md)（Q1）
