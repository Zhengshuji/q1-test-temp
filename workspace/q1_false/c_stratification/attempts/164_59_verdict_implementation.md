# 专家 59 号裁定落实：$W_L$ 接受、$S_{2,3}$ 条件恢复、不变界降级、$c=2$ 行列式判据

> 2026-11-08。汇总 59 号答复的裁定、已落实项、以及下一步（含专家给的 $q=3,\omega=2$ 精确判据）。
> 状态：**M2（记录 + 计划）**。

## 目标

把 59 号的裁决与三项“请求的交付物”落进项目，明确下一步。

## 设想与理由

59 号回答了三处争议，并给出一个可立即使用的精确判据（$q=3,\omega=2$ 的 $\det[b;bA_*]\ne0$）。

## 做法：逐条裁决

| 59 号点 | 裁决 | 落实 |
|---|---|---|
| $W_L$ 约束 | **正确**；$\dim W_L=c$ 时 $V=W_L$ 被迫；$\dim W_L>c$ 时在 $\operatorname{Gr}(c,W_L)$ 上分类；$\omega\ge\operatorname{rank}D_L$ | 158/153 已记；作为“固定行压缩引理” |
| $S_{2,3}$ | **条件正确**：需 $\dim(W+A_0W)\le3$ 对所有 $W$；在 $c=3,t=2$ 自动（$U\subseteq V$、$\dim V=3$）| 158 已补维度引理；159 的界在基空间层面恢复 |
| 不变部分计数 | **未证**：长链的正确底是 $\mathbb P(\ker T\cap T^{c-1}(K_0))$；链→子空间的商映射未控制 | 161 已降级为标签数；单块问题列为 Deliverable 2 |
| $c=2$ 精确判据 | $q=3,\omega=2$：$Z=\binom{A_*}{b}$，好 $\iff b\ne0$ 且 $\det[b;bA_*]\ne0$ | 下一步实现（Deliverable 1）|
| $\exists\mathbb R$ 直接证书 | **sound**；normal rank 必须单独加；$s=0$ 单独 | 162 已含；补 $s=0$ 的明确处理 |
| 十一层 | 需要精确清单（定义、$(t,u)$、Jordan 数据、非空、互斥、穷尽）| 146 已有清单；整理成 Deliverable 3 |
| 优先级 | $W_L$ → 归一化 $c=2$ → 提升 → $\exists\mathbb R$ → $c=2$ 界 → $c=3$ → 一般 $c$ | 采纳 |

## 专家给的 $q=3,\omega=2$ 精确判据（可直接实现）

$Z:\operatorname{im}H\to\mathbb C^3$，$Z=\binom{A_*}{b}$（$A_*\in\mathbb C^{2\times2}$、$b\in\mathbb C^{1\times2}$）。
则
$$\operatorname{rank}P(\lambda)=2\ \forall\lambda\iff \ker b\ \text{不含}\ A_*\ \text{的特征向量}\iff b\ne0\ \text{且}\ \operatorname{rank}\binom{b}{bA_*}=2.$$
坐标下即一个 $2\times2$ 行列式非零：
$$\boxed{\det\begin{bmatrix}b\\ bA_*\end{bmatrix}\ne0.}$$
在自由参数 $\theta$ 下，$A_*(\theta),b(\theta)$ 有理；在 $2\times2$ 主 minor 非零的 chart 上通分得多项式 $g(\theta)$：
* $g\equiv0$（所有 chart）⇒ 该实例不可行；
* 否则好 locus 是非空 Zariski 开集，可取精确有理点。

**下一步（Deliverable 1）**：对 16/21 做符号参数化（$V=W_L$ 被迫、admissibility 线性系统），
在每个 chart 上算 $g(\theta)$，判定恒零或给出精确好点。

## 进展

* $W_L$、$S_{2,3}$、不变界三处已按裁决更新；
* $q=3,\omega=2$ 判据已记录，实现列为下一步；
* 十一层清单已在 146，按 59 号的表格式整理为 Deliverable 3（待做）。

## 最终结论

* 59 号确认 $W_L$ 与 $S_{2,3}$（在自动维度假设下），否定了不变部分的分量界；
* $c=2$ 的下一步是**符号行列式判据**，不是随机搜索；
* 优先级：$W_L$ → $c=2$ 符号判据 → 提升 → $\exists\mathbb R$ → $c=2$ 界 → $c=3$。

## 放弃原因

* Deliverable 1/2/3 未完成（下一步）；
* 159 的界能否恢复取决于提升纤维条件（专家提醒不要混同三个空间的分量数）。

## 残留价值

* 59 号裁决的落实表与精确判据；
* 明确的下一步交付物。

## 相关文件

* [attempts/158](158_c3_s23_audit.md)、[159](159_c3_component_bound_corrected.md)
* [attempts/161](161_general_c_invariant_and_rank_strata.md)（降级）
* [attempts/162](../../decision_algorithms/attempts/162_direct_original_pencil_certificate.md)
* [attempts/146](146_c3_rigorous_parameterization.md)（十一层清单）

## 状态

* 裁决落实：**[完成，M2]**。
* 三项交付物：**[未做]**。
