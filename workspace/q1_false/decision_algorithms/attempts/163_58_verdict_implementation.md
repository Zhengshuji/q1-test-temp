# 专家 58 号裁决落实与两处待裁定分歧

> 2026-11-08。汇总 58 号答复的裁决、已落实项、以及两处我们与专家判断不一致、
> 需要下一次送审裁定的点。状态：**M2（记录）**。

## 目标

把 58 号答复逐条落进项目记录，并明确哪些已关闭、哪些待裁定。

## 设想与理由

58 号答复是一份长审计，确认了多数结构，但**没有回答** 58 号的 Q1（$W_L$ 约束），
并且在 $S_{2,3}$ 与 $p(c)n^c$ 上与我们的新证明有出入。

## 做法：逐条裁决

| 58 号问题 | 专家裁决 | 落实 |
|---|---|---|
| Q2 提升完成 | **确认**，并给出更强形式：$\Psi(\bar g)=(gN,gAN)$、$Z_{\rm pair}$、$d'_C\ge\dim\ker Z_{\rm pair}$（$(5a)$ 下即 $q-\omega\le d'_C$）| 已写入 152 |
| Q3 $c=2$ 算法 | 架构正确；完整算法未证；需 nonempty fibres 与 good locus 的逐分量检验 | 156 已记；seed10 见证是数据点；16/21 仍开放 |
| Q4 $c=3$ | 11 层需逐个不可约性证明；$S_{2,3}$ 最高优先；界暂停 | 我们的 158/159 与专家判断有出入（见下）|
| Q5 一般 $c$ | $p(c)n^c$ 不是分量界；建议条件性定理 | 161 的不变部分给出逐块不可约的分量界（专家可能未细看）；待裁定 |
| Q6 $\exists\mathbb R$ | **确认**；建议直接对原铅笔 $Q(\lambda)=[\lambda L-LA;CA;C]$ 做证书（$\deg Y\le2s-2$、normal rank、局部 Smith 逆命题）| 已写成 162 |
| Q7 文献/路线 | 提升 → $c=2$ → 分量；$\exists\mathbb R$ 并行 | 采纳 |

**直接原铅笔证书**（162）：$s=\operatorname{rank}[L;CA;C]$，
$$(5b)\iff\exists Y,\ \deg Y\le2s-2,\ QYQ=Q\ \text{且 normal rank}=s.$$
逆命题用局部 Smith 形；编码 $O(n^3)$ 变量/方程。

## 两处待裁定分歧

### 分歧 1：$W_L$ 约束（Q1 未答）

58 号的 Q1 问 $V\subseteq W_L=\ker[L_0N;L_0AN]$ 是否正确、六层是否应解释为
“单个 $V$ 的类型”。**答复未涉及**。我们的论证是：$H$ 与 $H_A$ 的顶部 $r$ 行固定，
$V=\ker H\subseteq\ker H_A$，故 $V\subseteq W_L$；当 $\dim W_L=c$ 时 $V$ 被唯一确定。
这直接影响 $c=2$ 算法的“枚举六层”：若 $V$ 唯一，六层只是类型判定，不是参数族枚举。
**需要下一次送审确认**。

### 分歧 2：$S_{2,3}$ 是否开

专家 58 号 §14.2 说 $S_{2,3}$ 是 rank-exact、可能可约；我们 158 证明：
$$S_{2,3}=\{W:\dim(W+A_0(W))=3\}=\{W:A_0(W)\not\subseteq W\}$$
是 $A_0(W)\subseteq W$（闭条件）的补，故**开**、不可约。
专家的“rank$(f|_W)=1$”条件（当 $W\cap A_0(W)$ 一维时）是**充分**的，不是等价的：
$W\cap A_0(W)=0$ 时 $\dim(W+A_0W)=3$ 也成立。
**需要专家裁定**：若我们的开性论证正确，则 159 的界应恢复；若专家坚持，请指出我们漏掉的
“$W$ 只在 $W\cap A_0W$ 一维时才算 $S_{2,3}$”的定义。

### 次要：$p(c)n^c$ 与 161

专家说 $p(c)n^c$ 不是分量界；我们同意（149 已降级）。但 161 的不变部分用“每块不可约”
给出 $\sum_{\lambda\vdash c}s^{b(\lambda)}$ 的分量界（不是 $p(c)n^c$ 的标签数），
这一点专家可能未细看。**待裁定**：每块不可约性论证是否成立。

## 进展

* 58 号裁决已逐条落实；162 是新增的直接 $\exists\mathbb R$ 证书；
* 两处分歧（$W_L$、$S_{2,3}$）已定位，需要下一次送审；
* $c=2$ 算法：专家确认架构、不确认完整算法；seed10 见证保留、16/21 开放。

## 最终结论

* 58 号关闭了提升与 $\exists\mathbb R$ 两块；$c=2$ 算法与 $c=3$ 界仍开放；
* 需要一封短送审（59）专门问 $W_L$ 与 $S_{2,3}$ 两处分歧。

## 放弃原因

* 未写 59 号（下一步）；
* 未把直接证书接进 G.1 的主证明（162 是独立版本）。

## 残留价值

* 一份裁决落实表与两处分歧的清晰陈述；
* 162 的原铅笔证书可直接作为复杂度部分的独立定理。

## 相关文件

* [attempts/152](../../c_stratification/attempts/152_lift_completion_fixed_l0.md)（$\Psi/Z_{\rm pair}$）
* [attempts/156](../../c_stratification/attempts/156_c2_algorithm_spec.md)（$c=2$ 算法）
* [attempts/158](../../c_stratification/attempts/158_c3_s23_audit.md)、[159](../../c_stratification/attempts/159_c3_component_bound_corrected.md)（$S_{2,3}$）
* [attempts/161](../../c_stratification/attempts/161_general_c_invariant_and_rank_strata.md)（一般 $c$）
* [attempts/162](162_direct_original_pencil_certificate.md)（直接证书）

## 状态

* 裁决落实：**[完成，M2]**。
* 两处分歧：**[待 59 号裁定]**。
