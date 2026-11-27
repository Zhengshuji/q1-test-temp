# B.15 · 避免性引理

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `B.15` 条目（§0.1 归并表）。

## 命题

**B.15（阶差无界：$k$ 个同型副本的直和把阶差乘以 $k$）** 设单副本 $(A_1,C_1,L_{0,1})$ 满足
$$V_1\cap K_1=0\quad\text{且}\quad\exists\lambda_0:\ (\lambda_0I-A_1)V_1=K_1\qquad(\dim V_1=\dim K_1),$$
并设它在某阶 $q_1$ 有可行的增广 $\mathcal L_1$（如 $q_1=q_{\min}$），且 $d_1=n_1-p_1-q_1=0$。
取 $k$ 重直和 $(A,C,L_0)=(A_1,C_1,L_{0,1})^{\oplus k}$（于是 $n=kn_1$、$p=kp_1$）。则

1. $V=V_1^{\oplus k}$、$K=K_1^{\oplus k}$、$V\cap K=0$，且 $(\lambda_0I-A)V=K$（**同一个** $\lambda_0$）；
2. 由 B.13e，**每个**阶 $q$ 只要 $d=n-p-q\ge1$ 就整族不可行（无例外，因 $V\cap K=0$）；
3. 在 $q=kq_1$（即 $d=0$）处，块对角增广 $\mathcal L=\mathcal L_1^{\oplus k}$ 满足 $(5a)$ 与 $(5b)$
   （两者都按块相加）。

于是
$$\boxed{\ q_{\min}\big((A_1,C_1,L_{0,1})^{\oplus k}\big)=k\,q_{\min}(A_1,C_1,L_{0,1}),\qquad
\text{阶差}=k\cdot(\text{单副本阶差})\ }$$

## 纸面证明

*证明*：1 由分块对角结构直接得到；2 由 B.13e（例外集空）；3 因 $Q_{\mathcal L}$、$[\mathcal L;CA;C]$ 均分块对角，
秩按块相加，故 $(5a)/(5b)$ 逐块成立即整体成立。$\square$


$Z\le K$ 非零、$(\lambda_0I-A)|_V$ 满射，则 $\exists x\in V$ 使像在 $Z$ 内而 $x\notin Z$——即第 2 步的机制；
`LemmaB.finrank_range_prodMap`：直和映射的秩可加——即第 3 步的抽象核。**差异**：两个 Lean 文件都只证抽象核，
分块直和与矩阵 `fromBlocks`（Mathlib 无 `Matrix.rank_fromBlocks`）的实例化是纸面）
$+$ **[精确验证]**：单副本（$\lambda_0=-2$、$q_{\min}=4$、阶差 2）；
两副本（$q_0=4$、$q=4..7$ 的 1820 个候选无可行点、$q=8$ 块对角见证满足 $(5a)(5b)$）；
三副本（$\exists\lambda=-2:(\lambda I-A)V=K$；$q=12$ 的块对角见证：$\operatorname{rank}[C;\mathcal L]=18$、
$(5a)$ 真、B.12 可观性真）。
*意义*：**阶差可以任意大**（$k$ 个 gap-2 副本给阶差 $2k$）——这是"阶差不是一步病态"的严格版本，
也说明 $q_{\min}$ 与代数最小阶之间的差可随实例规模线性增长。

## Lean

* 等级行引用的 Lean 声明：`LemmaA.exists_witness_not_mem`
* 差在哪里：见等级行括注（内核一般只覆盖代数/维数骨架，矩阵实例化多为纸面）

## 精确验证

* 该条暂无独立精确验证脚本（纸面证明 + 支撑目录）。

## 状态与历史

*等级*：**[已证-纸面]** $+$ **[Lean-conditional]**（`LemmaA.exists_witness_not_mem` / `_not_mem'`：若 $V\cap K=0$、
* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。



## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F2 |
| 导出等级 | **L3** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— Lean 已覆盖（内核） |


## 支撑目录

无（证据全部在本卷宗内）。

## 专家复核意见（成立）

同一 $\lambda_0$ 在每块都成立是关键；例外集须证明是**真代数子集**（不能只凭有限计算没出现）。
