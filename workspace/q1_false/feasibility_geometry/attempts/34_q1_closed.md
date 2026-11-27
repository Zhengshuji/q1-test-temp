# Q1 闭合：零空间铅笔判据（专家 2026-11-03 §1）已核验；并修掉一个"抽样 λ"的 bug

## 目标

专家对 Q1（$r\ge2$、$h<n$ 时的遮蔽判据）给出了**精确**回答，并指出它就在 2026 preprint 的 Theorem 4 里。
本档：把他给的形式**实现并核验**，同时记录过程中发现的自身 bug。

## 设想与理由

专家给的判据（原文 Q1.1）：设 $V$ 是 $\\ker[C;CA]$ 的满列秩基、$Z$ 是 $\\mathcal Z=\\ker[C;\\mathcal L]$ 的满列秩基，则
$$(5b)\\iff \\operatorname{rank}\\bigl[(\\lambda I-A)V\\ \\ Z\\bigr]
=\\operatorname{rank}\\bigl[V\\ \\ Z\\bigr]\\quad\\forall\\lambda\\in\\mathbb C .$$
等价形式：$\\operatorname{rank}\\bigl(\\pi_Z\\circ(\\lambda I-A)|_V\\bigr)=\\operatorname{rank}\\bigl(\\pi_Z|_V\\bigr)$，
以及核形式 $\\{v\\in V:(\\lambda I-A)v\\in\\mathcal Z\\}=V\\cap\\mathcal Z\\ \\forall\\lambda$。
它**不需要 $h=n$**，也**不需要**标量 $\\lambda(x)=L_0Ax/L_0x$。

实现要点：必须用**极大子式 gcd**（对 $\\lambda$ 恒等），不能只抽若干 $\\lambda$ ——否则会漏掉复根/非有理根。

## 做法

[verify_Q1_nullspace.py](../../../../tools/verification/verify_Q1_nullspace.py)：

1. `nullspace_gcd`：构造 $P_Z(\\lambda)=[(\\lambda I-A)V\\ |\\ Z]$（线性铅笔），枚举所有 $s\\times s$ 极大子式
   （$s=\\operatorname{rank}[V|Z]$），用**多项式行列式**精确算出，再求 gcd；常值非零 $\\iff (5b)$；
2. 与两条既有判据比对：Toeplitz 零度判据、$Q_{\\mathcal L}$ 的极大子式 gcd；
3. 另核验 C4 实例（$r=2$）的**比例性**（专家 §8.5）。

## 进展

| 候选 | Toeplitz | 零空间 gcd 判据 | $Q_{\\mathcal L}$ gcd 常数 | 一致 |
|---|---|---|---|---|
| C4 #1 | 失败 | **失败**（抽样版误报成功）| 否 | ✓ |
| C4 #2 | 失败 | 失败（掉秩 $\\lambda=3$）| 否 | ✓ |
| 专家给的 $\\mathcal L_*$ | 成立 | 成立 | 是 | ✓ |
| rand 6/2/1、7/2/2、5/2/1 | 成立 | 成立 | 是 | ✓ |

**6/6 一致**。

**C4 的比例性**（专家 §8.5 要求）：$\\det\\begin{pmatrix}L_{0,1}Ax&L_{0,1}x\\\\ L_{0,2}Ax&L_{0,2}x\\end{pmatrix}$
是 $x$ 的二次型，在 $V$ 的基上（2 个）与基和上（1 个）**全为零**，由极化恒等式得它在整个 $V$ 上恒零
⟹ $L_0Ax$ 与 $L_0x$ 总成比例，$\\lambda(x)$ 合法。

**发现的自身 bug**：我最初把零空间判据实现成"在有限个有理 $\\lambda$ 上比较秩"，对 C4 的第一个候选
**误报为 $(5b)$ 成立**（真实的掉秩发生在非有理 $\\lambda$）。这与 CLAUDE §10.1"用有限个实 $\\lambda$ 采样代替
$\\forall\\lambda$"是同一个陷阱。已改为精确的极大子式 gcd，并保留抽样版作为快速预筛（输出里会标注）。

## 最终结论

1. **Q1 闭合**：专家给的零空间铅笔判据是精确形式，且已在 6/6 上与 Toeplitz / $Q_{\\mathcal L}$-gcd 一致；
2. 它同时覆盖 $h<n$ 与 $r\\ge2$，因此**取代**了遮蔽判据作为主判据（遮蔽判据降为特例/充分条件）；
3. C4 的 $r=2$ 比例性已证，满足专家 §8.5 的收紧要求；
4. 术语按专家建议改用：**dimension obstruction**（$h\\ge q+r_1$）、**spectral obstruction**（$h<q+r_1$ 且 $d_{\\rm fin}>0$）、
   **uniform spectral infeasibility**（整族失败）、**incidence obstruction**（原"occlusion"）；
5. 阶区间 $[q_0,n_0-p]$ 由 preprint 的 Theorem 7 确认（终点阶谱可行、$q_{\\min}\\le n_0-p$；且代数可行在整个区间无空隙，谱可行**可以**有）。

## 放弃原因

不适用（核验与更正完成）。

## 残留价值

* 一个**精确**、覆盖 $h<n$ 与 $r\\ge2$ 的谱判据实现（三判据交叉验证 6/6）；
* 修掉一个会静默误报的 bug（抽样 $\\lambda$），并把它作为反例记入；
* C4 证明所需的比例性闭合，使整族不可行论证在专家要求的标准下完整；
* 术语与阶区间的权威依据。

## 相关文件

- [tools/verification/verify_Q1_nullspace.py](../../../../tools/verification/verify_Q1_nullspace.py)
- [workspace/for_expert/06_state_corrections_and_assessment-answer.md](../../../for_expert/archive/06_state_corrections_and_assessment-answer.md)（专家答复 §1、§8）
- [proof/refuted/C4_type3_counterexample.md](../../../../proof/refuted/C4_type3_counterexample.md)
- [workspace/q1_false/feasibility_geometry/attempts/32_occlusion_applicability.md](32_occlusion_applicability.md)（被取代的遮蔽判据）
