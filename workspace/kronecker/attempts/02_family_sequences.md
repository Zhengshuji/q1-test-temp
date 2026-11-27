# 固定 $(A,C,L_0,q)$ 的增广族内：指标序列与 $(5b)$ 是否变化？

## 目标

回答专家 2026-11-02 答复 §12 第 4 步（他称为**最重要的实验**）：

> 在**同一个固定 $(A,C,L_0,q)$** 的增广族内，是否出现不同的左指标序列（从而不同的 $\sum\varepsilon$
> 与不同的 $(5b)$ 判定）？

若是，则 $\mathrm{DEC}(q)$ 是**真正的存在性**问题；若在样本内唯一，只能说明候选族不全（专家 §6.1）。

## 设想与理由

* 早先的 [partition_determinacy.py](../../../tools/verification/partition_determinacy.py) 按 $(q,p,h,r)$ 分组，
  混合了不同实例与不同 $L$，**不能**回答这个问题；正确分组是 $(\text{instance},q)$；
* 有了 [Toeplitz 判据](../../../proof/toeplitz_criterion/README.md)，每个 $L$ 的整条序列只需一个块 Toeplitz
  矩阵的零度，可以对每个 $(instance,q)$ 扫很多候选；
* 关键是**生成器**：启发式候选（链、闭包、模 $\mathcal J$ 提升）太窄；应改用 P1 §V 的族在阶 $q$ 上的推广
  （$k=q-r$ 的图卡 $Y_J(\Theta)$），这才是"所有 $q$ 维、含 $L_0$ 的候选"的参数化。

## 做法

脚本：[tools/verification/family_sequences.py](../../../tools/verification/family_sequences.py)，
生成器：[tools/verification/p1_family.py](../../../tools/verification/p1_family.py) 的 `sample_q`（$k=q-r$）。

1. 用 `c208_q0_lower_bound.eta_and_q0` 算 $q_0=\sum_j\eta_j$；
2. 对 $q\in\{q_0,q_0+1,q_0+2\}$，在 P1 族的**所有图卡**上抽样 $\Theta$（每图卡 5 点，$0$ 与小整数），
   过滤条件：**行满秩**、$\operatorname{row}L_0\subseteq\operatorname{row}L$、$(5a)$（`linalg_q.condA`）；
3. 对每个通过的 $L$ 用 Toeplitz 判据算 $(\varepsilon,\sum\varepsilon,d_{\rm fin},(5b))$，并断言与 Smith 一致；
4. 按 $(\text{instance},q)$ 分组统计。

## 进展

$n=5,6,7$ 各 3 个 seed：9 个实例、**127 个合格铅笔**、23 个 $(\text{instance},q)$ 组。
数据：[workspace/kronecker/data/family_sequences.tsv](../data/family_sequences.tsv)。

| 现象 | 组数 |
|---|---|
| 同族内出现 **≥2 种指标序列** | **11** / 23 |
| 同族内 $\sum\varepsilon$ 取 **≥2 个值** | **11** |
| 同族内 $(5b)$ 判定**不一致** | **3** |

**决定性的单例**（$n=5$、seed 1000、$q=3$；两组 $A,C,L_0$ 相同、都含 $L_0$、都满足 $(5a)$）：

| $L$（$3\times5$）| $h$ | $s$ | $m$ | $d_{\rm fin}$ | $\varepsilon$ | $(5b)$ |
|---|---|---|---|---|---|---|
| $\begin{pmatrix}0&1&0&0&0\\0&0&1&0&2\\0&0&0&1&0\end{pmatrix}$ | 5 | 3 | 0 | 3 | $[]$ | **False** |
| $\begin{pmatrix}0&1&0&0&0\\0&0&1&0&0\\0&0&0&0&1\end{pmatrix}$ | 4 | 3 | 1 | 0 | $[3]$ | **True** |

同一个 $(A,C,L_0,q=3)$：一族成员使 $(5b)$ 失败、另一族成员使 $(5b)$ 成立。

## 最终结论

* **同族内 $(5b)$ 会变**（3/23 组有直接证据）：$\mathrm{DEC}(q)$ 是真正的 $\exists$ 问题，
  可行性**不能**从 $(A,C,L_0,q)$ 或聚合数据（$q,p,h,\operatorname{rank}\mathcal L$）读出；
* 同族内指标序列也会变（11/23 组），$\sum\varepsilon$ 亦然（11/23 组）；
* 这支持专家的建议：研究增广族的几何（WP2），而不是按图卡盲目枚举。

**边界（必须一起读）**：我们在**图卡内抽样**，不是穷尽；因此"某些组内唯一"**不是**"被决定"的证据。
只有"同族内出现不同判定"是硬结论。

## 放弃原因

不适用（实验完成，且得到与预期相反但确凿的结论）。

## 过程中的两次更正（记录在案）

1. **漏检 $\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$**：第一版 `push` 只查 $(5a)$，
   于是把"可观性链 $L=C$"当成候选 $\mathcal L$——而 $C$ 的行空间一般不含 $L_0$。
   修正：显式检查（CLAUDE 纪律 5）。
2. **包含性检查写错**：把 `rank([L;L0]) == len(L)` 当成"$L_0\subseteq L$"——它只说明 $L$ 与 $L_0$ 的
   行空间是**不同的**两个子空间（秩恰为 $\dim L$ 时反而说明 $L_0\not\subseteq L$）。
   正确形式：`rank([L;L0]) == rank(L)`。
   同时加上"行满秩"（否则有冗余行，去掉后 $q$ 更小，不可能是最小 $q$ 的解）。
   **修正前后结论从"11/13 组有差异"变成"3/23 组有差异"**——若不做这次自查，会把无效候选当成反例。

## 残留价值

* 一个可复用的"P1 族 × Toeplitz 判据"按 $(\text{instance},q)$ 分组的实验框架；
* 3 个实例上"同族内 $(5b)$ 既真又假"的显式证据，使 $\mathrm{DEC}(q)$ 的难度来源明确；
* 两个候选筛选的错误模式，可写进 CLAUDE §10.1（"包含性检查写反"）。

## 相关文件

- [tools/verification/family_sequences.py](../../../tools/verification/family_sequences.py)
- [tools/verification/p1_family.py](../../../tools/verification/p1_family.py)
- [tools/verification/toeplitz_criterion.py](../../../tools/verification/toeplitz_criterion.py)
- [proof/toeplitz_criterion/](../../../proof/toeplitz_criterion/README.md)
- [workspace/kronecker/data/family_sequences.tsv](../data/family_sequences.tsv)
- [archive/expert_correspondence/answer_2026-11-02_notes.md](../../../archive/expert_correspondence/answer_2026-11-02_notes.md)
