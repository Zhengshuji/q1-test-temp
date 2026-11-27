# H.1 · 商等价、方阵条件与 $d=0$ 边界

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `H.1` 条目（§0.1 归并表）。

## 命题

**H.1（a）〔原 H.1〕（商等价定理 Theorem Q）** 设 $Z\subseteq H$、$S=Z\cap V$、$A(S)\subseteq Z$、$U=Z/S$、
$P(\lambda)=(A-\lambda I)|_{V/S}$。则
$$\operatorname{rank}\big[(\lambda I-A)V\mid Z\big]=\dim(V+Z)
\iff \operatorname{rank}\big[U\mid P(\lambda)\big]=r+t .$$

## 纸面证明

*证明*：$S\subseteq Z$ ⟹ $\operatorname{rank}M=s+\dim(\operatorname{col}M/S)$；模 $S$ 后列空间 $=[U\mid P(\lambda)]$（需 $(A)$ 才良定义）；
$\dim(V+Z)=s+r+t$。

内核 `qe_colspace` / `qe_finrank` / `qe_well_defined`。差异：$r+t$ 写成 $\dim((V+Z)/S)$，二者的相等是纸面记账）。
**位置**：[proof/quotient_equivalence](../quotient_equivalence/README.md)。

**H.1（b）〔原 H.2〕（方阵条件）** $[U\mid P(\lambda)]$ 是 $w_m\times(r+t)$；它方阵 $\iff q=t$。
而 $m=r+t\iff h=w$（$L_0\subseteq\operatorname{row}C$）——与 $q=t$ 无关。
*证明*：$r+t=w-q+v-2s$、$t=v-s$、$w_m=w-s$。
**注**：这更正了旧文档的 $r+t=w-q$（笔误）与"$h-s=w_m\iff q=t$"（错）。

**H.1（c）〔原 H.3〕（$d=0$ 边界）** $d=0$ 时 $(A)$ 自动；$(S)\iff V\cap\ker(\lambda I-A)=0\ \forall\lambda$
$\iff A$ 在 $V$ 里没有特征向量。加行满秩条件：$q_{\min}=w$ 可行 $\iff$
$\operatorname{rank}[C;L_0]=p+r_0$ 且 $V$ 无特征向量。
*证明*：$Z=0\Rightarrow S=0$，$(S)$ 即 $(\lambda I-A)|_V$ 单射。

内核 `d0_rank_nullity` / `d0_rank_iff`。差异：未形式化"$A$ 在 $V$ 里没有特征向量"这一说法）。
**推论**：第二实例 $e_1..e_4\in V$ 是 $\lambda=1$ 的特征向量 ⟹ $q=w$ 也不可行 ⟹ $q_{\min}=\infty$
（"$q=w$ 时 $(5b)$ 平凡"是错的）。

## Lean

* 等级行引用的 Lean 声明：`QuotientEquivalence.qe_full`、`DimArithmetic.r_add_t`、`square_iff`、`m_iff_h`、`no_truncation`、`D0Boundary.d0_forall`
* 差在哪里：见等级行括注（内核一般只覆盖代数/维数骨架，矩阵实例化多为纸面）

## 精确验证

* 见等级行给出的精确验证数字。

## 状态与历史

**等级**：[已证-纸面] $+$ [精确验证 18 个 $Z$] $+$ **[Lean]**（`QuotientEquivalence.qe_full` = 本条陈述；
**等级**：[已证-纸面] $+$ 精确验证 $+$ **[Lean]**（`DimArithmetic.r_add_t`、`square_iff`、`m_iff_h`；$\mathbb N$ 无截断前提 `no_truncation`）。归档：[proof/h2_dim_arithmetic/](../h2_dim_arithmetic/README.md)。
**等级**：[已证-纸面] $+$ [精确验证 40/40] $+$ **[Lean]**（`D0Boundary.d0_forall` = 本条陈述的 $\forall\lambda$ 版；
* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。





## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F3 |
| 导出等级 | **L4** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— Lean 已覆盖（字面） |


## 支撑目录

[quotient_equivalence/](../quotient_equivalence/README.md)、[h2_dim_arithmetic/](../h2_dim_arithmetic/README.md)、[d0_boundary/](../d0_boundary/README.md)

（本卷宗只汇总证据；支撑目录里的脚本与文档保持原位。）

## 专家复核意见（成立）

$A(S)\subseteq Z$ 必须作为**显式假设**保留（虽然 $(5a)$ 可推出它：$x\in S\Rightarrow LAx=CAx=0\Rightarrow Ax\in Z$）；并强调 $[U\mid P(\lambda)]$ 一般不必方阵，方阵性对应 $q=t$。
