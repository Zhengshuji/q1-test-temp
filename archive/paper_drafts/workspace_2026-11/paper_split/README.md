# 论文拆分计划（Paper I / Paper II）

> 2026-11-15。依据：专家对拆分方案的评审（`paper/current/新建 文本文档 - 副本 - 副本.md`）+ 依赖图。
> 原则：**能复用就复用**——两份新稿都从现有 `q1_parametric_algorithms.tex` 剪裁，而不是重写。

## 0. 文件

| 文件 | 内容 | 状态 |
|---|---|---|
| `paper/current/others/q1_parametric_algorithms.tex` | 合并版（16 页，当前唯一事实源） | **保留为历史基线**，拆分完成后移入 `archive/paper_drafts/` |
| `paper/current/paper_I_dec.tex` | Paper I：判定复杂度 | 新建（剪裁自合并版） |
| `paper/current/paper_II_minorder.tex` | Paper II：最小阶与构造 | 新建（剪裁自合并版） |

`\label` 全部沿用现有名字（`sec:compressed`、`lem:struct` 等），所以剪裁**不需要改任何 `\ref`**。

## 1. Paper I —— *Deciding functional observer feasibility: compression, certificates, and parameterized algorithms*

```
I    Introduction                          （复杂度缺口 + 五条贡献 + roadmap）
II   Preliminaries and the problem         （记号 / (5a)(5b) / DEC, MINDEC, 阶范围）
III  The reduction                         （L1, L2, L3+L4, L6 结构界）
IV   The finite certificate                （L10, L11, L12, P13 + Cauchy–Binet）
V    The fixed-order algorithm             （Thm + 退化情形）
VI   The fixed-parameter algorithm         （Algorithm 2 + 六步证明，分正确性/计数两组）
VII  The zero-free-row case                （L21, P22 + Kronecker 注）
VIII Membership in ∃R                      （Thm23, Cor24）
IX   Conclusions
A    Bit sizes and the coefficient bound   （从现 §VII-C 移入）
B    The existential-real encoding
```

**从合并版删除**：P9 谱下界、§VII-A OPT/FIND（Cor OPT / Algorithm 3 / Procedure FIND / Cor FIND / two remarks）、附录 C 实例。
**从合并版移动**：现 §VII-C 的位模型与系数界（L19, L20, Renegar 规范化）→ 附录 A。
**重写**：标题、摘要、§I（贡献按专家给的 5 条顺序）、§II-C 末尾加"OPT/FIND 见 companion paper"一句。

## 2. Paper II —— *Minimum order and minimum-order construction for functional observers*

```
I    Introduction                          （最小阶问题、阶差现象、三条核心定理）
II   Setting and the reduction we use      （压缩、W、沙包+可实现性、条件只依赖 W、结构界）
III  Monotonicity, saturation and the minimum order
     A 单调与饱和  B q_min = r0 + t_min  C 谱下界（Theorem 2）
IV   Computing the minimum order           （接口定理 + 二分，O(log ℓ) 次 DEC）
V    Constructing a minimum-order observer （W → R 提升；采样点；位复杂度 open）
VI   An incorrect published minimum-order value （实例、四行见证、q_min = 4）
VII  Conclusions
```

**从合并版保留**：L1–L7、P8、P9、OPT/FIND 的全部内容、附录 C 实例（成为 §VI + 附录）。
**删除**：证书（L10–L13 + Cauchy–Binet）、Thm14、Thm15（改为接口定理引用）、zero-free-row、∃R、两个附录。
**新增（必须自足）**：接口定理；§II 的精简归约叙述（换叙述焦点）。

## 3. 依赖图（谁证什么）

| 条目 | Paper I | Paper II |
|---|---|---|
| L1 秩恒等式 | 完整（引 HJ13） | 精简重述 |
| L2 压缩与铅笔判据 | 完整 | 精简 |
| L3 可达行对 | 完整 | 完整 |
| L4 沙包与可实现性 | 完整 | 完整 |
| L5 条件只依赖 W | 完整 | 完整 |
| L6 结构界 | 完整（图的维数界） | 完整（t ≤ 2ℓ） |
| L7 单调 / 饱和 | 仅单调 | 完整 |
| P8 q_min = r0 + t_min | — | 完整（Theorem 1） |
| P9 谱下界 | — | 完整（Theorem 2） |
| L10–L12, P13 证书 | 完整 | — |
| Thm14 固定阶 | 完整 | 作为 oracle |
| Thm15 FPT(ℓ) | 完整 | 接口定理引用 |
| OPT / FIND | — | 完整（Theorem 3） |
| zero-free-row、∃R | 完整 | — |
| 实例与纠正 | — | 完整 |

共享部分：L1–L6，约 2 页；Paper II 里约占 22%。

## 4. 执行顺序（每步编译 + 提交）

1. **Paper I**：复制 → 删 Paper II 块 → 位模型移入附录 A → 重写标题/摘要/引言 → 编译核对（目标 ≈13 页，TAC ≤16）
2. **Paper II**：复制 → 删证书与两算法 → 写接口定理 → 重写引言与 §II → 实例化 → 编译核对（目标 ≈9 页；若 >8 需减或改投 Automatica）
3. **细节**：两篇的术语/符号一致性、交叉引用、参考文献去重、CI 与产物仓

## 5. 已知风险

- Paper I 若 >16 页：优先把 L19/L20（位尺寸）压成附录里的一页，或删去退化情形小节。
- Paper II 若 >8 页（TAC Technical Note 上限）：显式观测器参数进附录；或投 Automatica。
- 两篇同期投稿需在 cover letter 说明 companion papers，并附本文件的依赖图。
