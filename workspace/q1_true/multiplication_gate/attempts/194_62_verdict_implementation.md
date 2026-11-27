# 专家 62 号裁决落实：O1 判据更正、O2 限定、无界 $c$ 硬度路线

> 2026-11-09。汇总 62 号答复：O1 的“可对角化⇒好”**错误**，正确判据是特征空间上的单射；
> O2 的特征线不必有限、188 只给个别提升、开性不决定空；硬度首选 ARM(3)。状态：**M2（记录）**。

## 目标

把 62 号裁决逐条落实，明确更正、限定与下一步。

## 设想与理由

专家指出 191 的一个**实质错误**：坏只需一个特征向量被 $\ker B_*$ 吞，不是全部；可对角化 + $B_*\ne0$ 不够。
正确判据是 $\ker(A_*-\lambda I)\cap\ker B_*=\{0\}\ \forall\lambda$，即 $B_*$ 在每个特征空间上单射；
广义特征向量不产生额外坏情形。

## 做法：逐条落实

### 1. O1 更正

- 删除“$B_*\ne0$ 且可对角化 ⇒ 好”；
- 采用正确判据：
  $$\operatorname{rank}P(\lambda)=\omega\ \forall\lambda\iff
  \ker(A_*-\lambda I)\cap\ker B_*=\{0\}\ \forall\lambda;$$
- 反例：$A_*=\operatorname{diag}(0,1)$、$B_*=[1\ 0]$，$e_2$ 被吞 ⇒ $\lambda=1$ 秩降；
- 非对角化分支删去；改为“每个特征空间上 $B_*$ 单射”；
- 已改 191；190 的判定树同步。

### 2. O2 限定

- 特征线集合是 $\bigcup_\lambda\mathbb P(U\cap\ker(A-\lambda I))$，**不必有限**（特征空间维数 $>1$ 时是正维射影子空间）；
- Lemma 188 只证“每个 $h$ 有个别可容许提升”，不等于“能同时拼出满足秩与行独立约定的 $L$”；
  提升层仍需单独检查；
- 开性不决定投影的空/非空；结果式消元要用完整系统（$v\notin U$、秩、提升、谱），并做饱和。

### 3. 无界 $c$ 硬度（Q3 的答复）

专家的排序：
1. **仿射秩最小化（ARM）**：2026  preprint 证其在 rank $=3$ 时已 $\exists\mathbb R$-完全；
   与 $H=LN$、$\operatorname{rank}H=\omega$ 的结构接近；固定 $\omega=3$、$k$ 增长 ⇒ $c=k-3$ 无界；
   主要障碍：$H$ 与 $H_A$ 必须来自同一个 $L$。
2. **静态输出反馈**：Liu 2026 证 $\exists\mathbb R$-完全；但 Hurwitz 条件与“所有 $\lambda$ 的铅笔满秩”不同，
   需构造性转化。
3. **ETR 算术电路**：最直接的源问题；chart 公式的二次项 $XA_{12}X$ 可作乘法 gadget。

**两阶段路线**：$\mathrm{ETR}\to$ 结构化秩/incidence 问题 $\to\mathrm{DEC}(q)$。
**设计原则**：让 $B_*|_{\ker(A_*-\lambda I)}$ 单射（谱条件自动满足），把硬度隔离在核几何与秩条件。

### 4. 优先级（Q4 的答复）

并行两条工作流：
- **A 固定 $c$**：更正 O1、补 O2（含正维特征空间）、审计 188、完成 $c=2$、验证求解器；
- **B 无界 $c$ 硬度**：先做“表达力引理”——观测器数据能否在 Grassmannian chart 上实现足够一般的仿射/二次 incidence，
  同时让谱条件自动满足。不要等固定 $c$ 全部完成。

### 5. 文献（Q5 的答复）

- Fernando 2010、Darouach–Fernando 2025、Fernando 2026（刻画）；
- Liu 2026（static output feedback，$\exists\mathbb R$-完全）；
- Majumdar 2026（affine rank minimization，$\exists\mathbb R$-完全，rank 3）；
- 2025 功能可观测性/传感器放置的 NP-hardness（相邻但不同）。
专家未找到直接针对本项目 $\exists\Theta$ 的复杂度分类。

## 进展

* O1 的错误已更正（191/190）；
* O2 的三个限定已写入 193；
* 硬度路线与优先级已记录；
* 62 已归档，README 标 Reviewed。

## 最终结论

* 60–62 三轮的核心更正都已落实；
* 固定 $c$ 与无界 $c$ 硬度应并行；
* 首个硬度实验：ARM(3) 的表达力引理。

## 放弃原因

* 未重跑求解器的 O1 测试（需把 gcd 检查换成特征空间单射）；
* 未开始 ARM(3) 的 gadget 构造；
* 未审计 188 的“个别 vs 同时”提升。

## 残留价值

* 正确的 O1 判据；
* 硬度路线的清晰排序；
* 两工作流的计划。

## 相关文件

* [attempts/191](../../../q1_false/c_stratification/attempts/191_c1_pencil_criterion.md)（已更正）
* [attempts/190](../../../q1_false/c_stratification/attempts/190_c1_decision_tree.md)、[193](../../../q1_false/c_stratification/attempts/193_c1_O2_reduction.md)（限定）
* [attempts/192](../../../q1_false/decision_algorithms/attempts/192_c1_pencil_block_algorithm.md)（小算法）
* [attempts/186](../../../q1_false/c_stratification/attempts/186_61_verdict_implementation.md)（上一轮裁决）

## 状态

* 裁决落实：**[完成，M2]**。
* 求解器 O1 测试 / ARM gadget / 188 审计：**[未做]**。
