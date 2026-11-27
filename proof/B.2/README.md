# B.2 · 顶层可观测与 PBH

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `B.2` 条目（§0.1 归并表）。

## 命题

**B.2（a）〔原 B.2〕（顶层）** 若 $\rho=d$，则 $(5b)\iff(D_W^{\mathsf T},T_W)$ **可观测**。

## 纸面证明

*证明*：$\rho=d$ 时 $Q_{\mathcal V}(\lambda)=\begin{pmatrix}-D_W^{\mathsf T}\\ \lambda I_d-T_W\end{pmatrix}$；秩恒为 $d$ $\iff$ 不存在 $\ker D_W$ 里的特征向量 $\iff$ PBH $\iff$ 可观测。
位置：[proof/top_layer_observability/](../top_layer_observability/README.md)。

**B.2（b）〔原 B.5〕（$c_0=1$、$\rho=d$：循环向量判据）** 设 $c_0=1$（$S=\operatorname{span}\{j_0\}\subseteq\mathcal J$），$W$ 为 $\mathcal J$ 的补、$\mathcal V=\operatorname{span}\{j_0\}\oplus W$（此时 $(5a)$ 自动）。记 $T_W$ 为 $A$ 沿 $\mathcal J$ 的压缩、$v_W=\pi_W(j_0A)$。则
$$\mathcal V\ \text{满足}\ (5b)\iff v_W\ \text{是}\ T_W\ \text{的循环向量}\quad(\operatorname{rank}[v_W;v_WT_W;\dots;v_WT_W^{d-1}]=d).$$
*证明*：$(5b)$ 失败 $\iff\exists\lambda,\ 0\ne\psi\in\mathcal J^\perp:\ \psi(\lambda\ell-\ell A)=0\ \forall\ell$；由 $j_0\in\mathcal J$ 得 $\psi(j_0)=0$，故 $\psi(j_0A)=0$，而 $\psi|_W$ 是 $T_W$ 的左特征向量 ⟹ 其核是含 $v_W$ 的真不变子空间。
位置：[proof/cyclic_vector_criterion/](../cyclic_vector_criterion/README.md)（[精确验证 35/35]，负侧待构造）。

## Lean

* 等级行引用的 Lean 声明：`PBH.pbh_iff`、`PBH.Observable`、`B2Block.block_on_J`、`block_on_W`、`CyclicVector.isCyclic_iff`、`not_cyclic_of_left_eigen`、`exists_left_eigen_of_not_cyclic`、`CyclicStructural.b5_five_b_fails_imp_not_cyclic`、`ProjW`、`exists_functional_of_rank_drop`、`b5_five_b_fails_imp_not_cyclic`、`b5_converse`
* 差在哪里：见等级行括注（内核一般只覆盖代数/维数骨架，矩阵实例化多为纸面）

## 精确验证

* 该条暂无独立精确验证脚本（纸面证明 + 支撑目录）。

## 状态与历史

**等级**：[已证]（**完整证明**：[proof/top_layer_observability/theorem.md](../top_layer_observability/theorem.md)）$+$ **[Lean-conditional]**（`PBH.pbh_iff` = 第三步 PBH；`PBH.Observable` = 可观测性定义。**差异**：分块形式已有**逐点版**（`B2Block.block_on_J`/`block_on_W`）；未做的是"组装成矩阵 + 接秩条件"的建模）。
**等级**：[已证] $+$ **[Lean-conditional]**（`CyclicVector.isCyclic_iff` = 事实 1（循环 $\iff$ 无含 $v$ 的真不变子空间）；`not_cyclic_of_left_eigen` + `exists_left_eigen_of_not_cyclic` = **双向**；`CyclicStructural.b5_five_b_fails_imp_not_cyclic` = **$(5b)$ 秩降 $\Rightarrow$ $v_W$ 不循环**（经 `ProjW` 的桥梁与 `exists_functional_of_rank_drop`））。**双向都已 Lean**：`b5_five_b_fails_imp_not_cyclic`（$(5b)$ 失败 $\Rightarrow$ 不循环）$+$ `b5_converse`（不循环 $\Rightarrow$ 存在 $\lambda$ 使秩降）。"循环"写成 $\operatorname{span}\{T_W^kv_W\}=W$，秩形式由 $\alpha$ 桥翻译）。
* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。





## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F2 |
| 导出等级 | **L3** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— Lean 已覆盖（内核） |


## 支撑目录

[top_layer_observability/](../top_layer_observability/README.md)、[xw_decomposition/](../xw_decomposition/README.md)、[cyclic_vector_criterion/](../cyclic_vector_criterion/README.md)、[controllability_equivalence/](../controllability_equivalence/README.md)

（本卷宗只汇总证据；支撑目录里的脚本与文档保持原位。）

## 专家复核意见（成立）

只对**顶层**（$\rho=d$）成立，不可沿用同一块记号外推到低层；零维/零行的退化情形应单列一段。
