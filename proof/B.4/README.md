# B.4 · $V=\mathbb C^n$ 的判据

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `B.4` 条目（§0.1 归并表）。
> **状态：有缺口（专家复核）** —— 修订要求见文末的专家复核意见一节。
> 修订完成前，docs 里该条的等级按"待修"对待。

## 命题

**B.4（$V=\mathbb C^n$ 的可行性判据；按专家意见更正）** $\mathcal V=\mathbb C^n$ 满足 $(5b)$ $\iff$ **$A$ 在 $K=\ker[C;CA]$ 里没有（右）特征向量**，即

$$\nexists\,0\ne x:\quad Cx=0,\quad CAx=0,\quad \exists\lambda:\ (\lambda I-A)x=0 .$$

*更正说明*：原表述用 $A^{\mathsf T}$（对偶写法），与推导不符；见下方「约定与核验」。

## 纸面证明

*证明*：$V=\mathbb C^n$ 时 $[\lambda I-A;CA;C]$ 行满秩 $\forall\lambda$；其核为 $\{v:\ v(\lambda I-A)=0,\ vC=vCA=0\}$，非空即得左特征向量在 $K$ 里。
位置：[proof/top_layer_observability/](../top_layer_observability/README.md)。

## Lean

**无 Lean 内核（原内核已撤回）**：`B4FullSpace.b4_iff_no_eigenvector` 证的是**对偶写法 (D)**（$\dim(M\top+J)=n\iff\ker M^{\mathsf T}\cap J^{\perp}=0$），与铅笔秩降不等价（精确核验 3962 例，117 个反例）。它作为**独立辅助引理**保留，但不计入本条覆盖；按 (P) 重述的内核列为待办。

## 精确验证

* `b4_convention_test.py`：$n=3$、3962 个随机整数实例上比较 (P) 右特征向量 / (D) 对偶写法 与"铅笔降秩"；**(P) 3962/3962**、**(D) 3845/3962（117 个反例）**。验证的是**判据的取舍**，不是定理本身的证明。

## 状态与历史

**等级**：[已证]。
* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。





## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F1 |
| 导出等级 | **L2** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— **Lean 可行、尚未补**（四引理路线已定） |


## 支撑目录

[b4_full_space/](../b4_full_space/README.md)

（本卷宗只汇总证据；支撑目录里的脚本与文档保持原位。）

## 专家复核意见（有缺口（已定位并给出正确形式））

## 约定与核验（2026-11-06）

**两种写法必须区分**（专家指出的正是这一点）：

* **(P) 行约定（本项目、正确）**：铅笔行空间 $=\{(x)(\lambda I-A)\}+\mathcal J$，故
  $[\lambda\mathcal L-\mathcal LA;CA;C]$ 列满秩 $\iff\ker(\lambda I-A)\cap J^{\perp}=\{0\}$，
  即 **$A$ 的右特征向量不在 $K=\ker[C;CA]$ 里**。
* **(D) 对偶写法**：$\ker(\lambda I-A)^{\mathsf T}\cap J^{\perp}=\{0\}$（$A^{\mathsf T}$ 的左特征向量）。
  这是**另一条**陈述；它与铅笔的秩降**不等价**。

**精确核验**（`tools/verification/b4_convention_test.py`，$n=3$、随机整数实例 3962 个）：

| 判据 | 与"铅笔降秩"一致 | 反例 |
|---|---|---|
| (P) 右特征向量 | **3962 / 3962** | 0 |
| (D) 对偶写法 | 3845 / 3962 | **117** |

（降秩样本 70 个；(D) 在另外 117 个样本上给出与降秩相反的结论。）

**对现有 Lean 的处置**：`B4FullSpace.b4_iff_no_eigenvector` 编码的是 **(D)**（它证的是
$\dim(M\top+J)=n\iff\ker M^{\mathsf T}\cap J^{\perp}=0$，数学上正确但对应的不是本命题）。
因此该条**不再算作 B.4 的内核**；按 (P) 重述的 Lean 内核列为待办。

## (P) 版 Lean 内核：已尝试、卡在哪（2026-11-06）

**目标陈述**：设 $E$ 有限维、$J\le E^*$（行空间）、$M=\lambda I-A$，则
$$J\sqcup\operatorname{range}M^*=\top\iff\ker M\cap J^{\perp}=0 .$$
这正是 (P)（右特征向量判据）的行空间形式，证明只需零化子恒等式
$(J+\operatorname{range}M^*)^\perp=J^\perp\cap\ker M$ 与有限维对偶的维数公式。

**卡点**（两次编译后暂停，未提交内核）：
1. $J\le E^*$ 的零化子要用 `Submodule.dualCoannihilator`（不是 `J.dualAnnihilator`，后者落在 $E^{**}$）；
2. 需要 `(range M^*)^⊥ = ker M`（Mathlib 里对应 `LinearMap.ker_dualMap_eq_dualAnnihilator_range` 的对偶方向），
   以及 $E^{**}\cong E$ 的搬运；
3. 维数计算要在 $E^*$ 里做（`Subspace.finrank_add_finrank_dualAnnihilator_eq`），避免混用 $E$ 与 $E^{**}$。

**结论**：纸面形式（含 3962/3962 的判据核验）成立；Lean 化需要一个小的对偶搬运层，
列为本条唯一的待办（这也是它目前只能记 **L2** 而不能记 L4 的原因）。

## (P) 版 Lean：本轮 API 勘查结果（2026-11-07）

按专家的四引理路线逐条勘查 Mathlib 现有 API：

| 引理 | Mathlib 里有什么 | 还缺什么 |
|---|---|---|
| L1 和的零化子 | `Submodule.dualCoannihilator`、`Submodule.mem_dualCoannihilator`（$x\in\Phi^{\circ}\iff\forall\varphi\in\Phi,\varphi x=0$）、Galois 连接 `le_dualAnnihilator_iff_le_dualCoannihilator` | 需要 `dualCoannihilator_sup_eq`（和的零化子 = 交）——**未找到**，须自写（`ext` + `simp`，容易）|
| L2 $\operatorname{Ann}(\operatorname{range}M^\vee)=\ker M$ | （←）方向平凡 | （→）方向需要**对偶分离点**：$y\ne0\Rightarrow\exists\varphi,\varphi y\ne0$。可用 `Module.Dual.evalEquiv`（有限维双对偶同构）导出 |
| L3 $\operatorname{Ann}(H)=0\iff H=\top$ | 只有 $\operatorname{dualAnnihilator}$ 方向的维数恒等式 `Subspace.finrank_add_finrank_dualAnnihilator_eq` | **缺** $\operatorname{dualCoannihilator}$ 方向的维数恒等式；也**缺**双零化子恒等式 `dualAnnihilator_dualCoannihilator`（已 grep 确认不存在）|
| L4 合并 | — | 依赖 L1–L3 |

**结论**：L1 可立即写；L2 需要 `Dual.evalEquiv`；L3 需要自建"有限维下 $\operatorname{Ann}(H)=0\iff H=\top$"——
经由 `Dual.evalEquiv` 把 $H\le E^*$ 送到 $E^*$ 的**双**零化子，再用已有的
`finrank_add_finrank_dualAnnihilator_eq`。这是**一条可完成的路线**，但需要先把 `evalEquiv` 的 API 摸清，
预计 1–2 次会话。

因此 B.4 仍记 **M3/F1**，未升级。
