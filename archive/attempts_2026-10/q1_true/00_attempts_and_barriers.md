# 路线总清单（重建版）

> **背景**：本清单原来在旧 `q1_true/README.md` §2（20 条死路线），该文件在 2026-10-27 重构时被我**覆盖**，
> 无法恢复（见 [trash/README.md](../../../trash/README.md)）。以下是**从多处档案重建**的版本：
> `archive/handovers/STATUS_2026-10-25.md` §3、`STATUS_2026-10-26.md` §8、
> `archive/session_history/54_handoff.md`、`archive/attack_A2V0/TECHNICAL_QUESTIONS.md` §5、
> `archive/attack_A2V0/OPEN_PROBLEM.md` §2.4、`THE_MISSING_PIECE.md` §3.3、以及本目录 01–07。
> **若有遗漏，以档案为准。**

## 目标

把 MIN-ROWS 归约到已知 NP-hard 问题（证 $q1$ = 真），或给出多项式算法（证 $q1$ = 假）。

## 设想与理由

$q_{\min}$ 是"最小行数"，与 min-rank / 覆盖 / 低秩补全同形；且 $(5b)$ 会在候选集里"切点"，
天然像"截面与 Grassmannian 相交"这类几何存在性问题。

## 做法

三类做法：**归约**（把已知 NP-hard 编码成 $(A,C,L_0)$）、**构造/压缩**、**公式/结构**。逐条见下表。

## 进展（逐条，含死因与出处）

### A. 归约类

| # | 路线 | 死因 / 状态 | 出处 |
|---|---|---|---|
| A1 | 拟阵 / CYCLIC-COVER → TAP | **死**：$(T)$ 有显式反例（$n{=}6$，$q_{\min}{=}2<3=q_{\rm coord}$）+ 可实现 $\mathcal J$ 很薄 | [01_matroid_tap.md](01_matroid_tap.md) |
| A2 | 图 / 超图归约 | **死**：与 A1 同源 | [05_graph_reduction.md](05_graph_reduction.md) |
| A3 | min-rank（斜倍增）编码 | **死**：$q{=}2$ 时可行集的 Plücker 张成满（定理 $+$ 数值），真子空间不可实现 | [STATUS_2026-10-26](../../../archive/handovers/STATUS_2026-10-26.md) §8、§4.2 |
| A4 | 覆盖 / 反馈设计 | **死/受阻**：全部落在 Lovitz 型 | [02_minrank_cover.md](02_minrank_cover.md) |
| A5 | Z 形式（$q_{\min}$ = 最大化子空间维数）| **未完成**：$(8c)$ 有缺项，已被一个实例打假 | [03_z_formulation.md](03_z_formulation.md) |
| A6 | 线性截面秩一（Lovitz）| **受阻**：公开问题 | [07_linear_section.md](07_linear_section.md) |
| A7 | 谱切割 / 块结构 | **死**：$\mathbb F_3$ 上的"组合结构"是伪影 | [04_speccut.md](04_speccut.md) |
| A8 | 混合情形（代数 ⊗ 谱）| **死**：没有可用的组合对象 | [06_mixed_case.md](06_mixed_case.md) |
| A9 | "一般位置"上界 | **死**：不能控制整条参数族 | STATUS_2026-10-26 §8 |

### B. 构造 / 压缩类

| # | 路线 | 死因 / 状态 | 出处 |
|---|---|---|---|
| B1 | $\mathcal V'\subseteq\mathcal V+\mathcal J$ 压缩 | **死**：要求 $\dim(\mathcal V'\cap\mathcal J)=1$，但 $\mathcal V'\supseteq L_0\subseteq\mathcal J$ 迫使 $\ge r$ | STATUS_2026-10-26 §8 |
| B2 | $\mathcal V^{\rm ci}(L_0)$ 作压缩目标 | **死**：实测可只有 1–2 维 | 同上 |
| B3 | $P\to q_{\min}$ 的"自动桥" | **死**：$E\cap K$ 不可行时 spec_cut 仍可 $>0$ | 同上 |
| B4 | $(T)$ 保坐标（坐标解不劣于非坐标）| **死**：$n{=}6$ 反例 | 同上 |

### C. 公式 / 结构类（多为 $(5a)$/层公式）

| # | 路线 | 死因 / 状态 | 出处 |
|---|---|---|---|
| C1 | $q_{\min}=\dim V+1$ | **死**：$n{=}5$ 反例 | `proof/refuted/README.md` R1 |
| C2 | $q_{\min}=\max(r,\rho^*+1)$ | **死**：$S=\mathcal J$ 族 $q_{\min}=n$ | R3 |
| C3 | $q_{\min}=\max(r+\varepsilon,\rho^*+1)$ | **死**：同上 | R3 |
| C4 | $F_3=\max(r+\varepsilon,\rho^*+\max(c_0,1))$ | **死**：$n{=}4$ 反例 | R4 |
| C5 | 两值假设 $\rho^*\in\{\rho_0,\dim V\}$ | **死**：中间层证书 | `archive/attempts_2026-10/q1_false/06_two_values.md` |
| C6 | $\rho_{ci}$ 闭式 / "最小 ci 唯一" | **死**：极小元不唯一、$\rho$ 不恒定 | `archive/attempts_2026-10/q1_false/04_rho_ci.md` |
| C7 | 贪心闭包 | **死**：20/24 | `archive/attempts_2026-10/q1_false/05_greedy_closure.md` |
| C8 | 层紧性 $q(\rho)=\rho+1$ | **部分**：70 对中 69 紧，1 例外已解释 | `archive/attempts_2026-10/q1_false/00_the_lemma.md` |

### D. $(5b)$ 的局部 / 代数尝试

| # | 路线 | 死因 / 状态 | 出处 |
|---|---|---|---|
| D1 | 商的谱 | **死** | `archive/session_history/54_handoff.md`（9 条之一）|
| D2 | $\forall y$ 平行 | **死** | 同上 |
| D3 | $\alpha_0A'\notin$ 某空间 | **死** | 同上 |
| D4 | $\Lambda$ 算子化 | **死** | 同上 |
| D5 | $H(V)$ 不变 | **死** | 同上 |
| D6 | $S_0$ 迭代 | **死** | 同上 |
| D7 | $w\cdot\gamma_0$ | **死** | 同上 |
| D8 | 只用 $\ker M^{\mathsf T}$ 的像 | **死** | 同上 |
| D9 | 逐 $\lambda$ 维数不等式 | **死** | 同上 |
| D10 | $A(\operatorname{col}N)\subseteq\operatorname{col}N$ | **死**：$1/3,1/4,2/4$ 违例 | `archive/attack_A2V0/OPEN_PROBLEM.md` §2.4 |
| D11 | $A(\ker L\cap\ker C)\subseteq\ker(CA)$ | **死**：2160 解中 2579 违例 | 同上 |
| D12 | 封闭性递推（$v\to Av\to A^2v$）| **死**：同 D11 | 同上 |
| D13 | 块对角扩展 | **死**：$q\ge\rho+\#\{\text{块}\}$，给不出紧中间层 | `archive/attack_A2V0/TECHNICAL_QUESTIONS.md` §5 |
| D14 | 不可见块（增维使 $C=0,A=0$）| **死**：保持中间层但不改 $\rho$–$q$ 关系 | 同上 |
| D15 | $k{=}2$ 的 $V$ 被 $L_0$ 定死 | **死**：$\Sigma$ 不被线性结构钉住 | 同上 |
| D16 | "自由方向"给出 $Z$ | **死**：实测 $\dim\le1$ | 同上 |
| D17 | 符号消元（$\Sigma(t)$ 代入）| **死**：退化轨迹使符号 gcd 不可读 | 同上 |
| D18 | 随机搜索中间层 $k{=}2$ | **0 命中**（8 随机 + 48 定向）| 同上 |

## 最终结论

**没有成立的结果**（$q1$ 仍开放）。项目的自我总结：硬度链只可能落在三个地方：

| 落点 | 状态 |
|---|---|
| "线性空间里是否存在秩一矩阵"（Lovitz）| 公开问题 |
| "线性截面与 $\mathrm{Gr}(k,n)$ 相交" | 活跃方向，无定论 |
| $k{=}2$：$\exists c\ne0,\ \operatorname{Pf}(\sum c_i\Phi_i)=0$ | 未定（与 copositivity 相邻）|

## 放弃原因

各条见上表。共同模式：归约的落点要么是**公开问题**，要么被**可实现性 / Plücker 张成满**这类结构障碍挡住。

## 残留价值

- A1 的**拟阵刻画**（坐标层 $(5b)\iff$ 并环集）与**可实现 $\mathcal J$ 的薄性**（Krylov 补丁）；
- A3 的 **Plücker 张成定理**（$\operatorname{span}\{p(\mathcal V)\}\le\binom{n-1}{q-1}$，且数值上总满）——结构性排除 min-rank；
- 三个落点清单（上表）——任何新归约必须落在其中一个之外。

## 相关文件

- 各路线：[01_matroid_tap](01_matroid_tap.md)、[02_minrank_cover](02_minrank_cover.md)、[03_z_formulation](03_z_formulation.md)、[04_speccut](04_speccut.md)、[05_graph_reduction](05_graph_reduction.md)、[06_mixed_case](06_mixed_case.md)、[07_linear_section](07_linear_section.md)
- 归约目标形式化：[../reduction_targets.md](../reduction_targets.md)
- 主线开放问题：[../../../docs/05_open_questions.md](../../../docs/05_open_questions.md)
