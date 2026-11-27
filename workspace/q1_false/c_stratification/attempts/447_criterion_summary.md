> **判据已更正（448）**："$\dim\mathcal T_W=2\omega$"**假**——存在解析反例（$\dim=2\omega-1$ 且 $(E)$ 成立）。
> 正确判据是 $(E)$ + 行数（$m\ge\dim\mathcal T_W$）。见 [448](../../decision_algorithms/attempts/448_criterion_corrected.md)。

# 447 判据汇总：$\mathcal T_W=W\oplus W$（$21/21$ 数据一致，仍未证明）

> 收束 444 的判据。用修好的构造性判定（$m=\dim\mathcal T_W$，见 446）补测一批，
> 数据一致于：**可行 $\iff\dim\mathcal T_W=2\omega$**。

## 目标

汇总判据的全部数据与它的证明缺口。

## 设想与理由

$\mathcal T_W\subseteq W\oplus W$ ⟹ $\dim\le2\omega$，等号 $\iff\mathcal T_W=W\oplus W$。
等号时零配偶条件自动成立 ⟹ 可行（441 构造）。反向（$\dim<2\omega$ ⟹ 不可行）只有数据。

## 做法

- 构造性判定（446）：取 $\mathcal T_W$ 的基当自由行（$m=\dim\mathcal T_W$），算 $\omega$-子式 $\gcd$；
- 在 $n=5$、$p=1$、$k=3$、$\omega\in\{1,2\}$ 的随机实例上统计 $(\dim\mathcal T_W,2\omega,(F))$。

## 进展（数据）

| $\dim\mathcal T_W$ vs $2\omega$ | $(F)$ | 例数 | 来源 |
|---|---|---|---|
| $\dim=2\omega$ | **是** | 1 | [443](443_gray_band_has_feasible.md)（$\omega=1$、$\dim=4$） |
| $\dim<2\omega$ | **否** | 20 | [387](425_multi_active_found.md)/[446](../../decision_algorithms/attempts/446_bug_located.md) 的 10 + 本轮 10 |

**21/21 一致** ✓。

## 最终结论

1. **判据（未证）**：层 $\omega$ 在 $W$ 上可行 $\iff\mathcal T_W=W\oplus W$；
2. **充分**方向已证（零配偶构造，441）；**必要**方向只有数据；
3. 若判据成立，则中间层的判定化成一个**线性代数条件**：
$$\exists\,\omega\text{ 维 }W\supseteq U\ \text{使}\ W\oplus W\subseteq\mathcal S,$$
   而 $W\oplus W\subseteq\mathcal S\iff W\subseteq\pi_1(\mathcal S\cap(V\oplus0))$ 且 $W\subseteq\pi_2(\mathcal S\cap(0\oplus V))$——
   两个与 $W$ 无关的固定子空间 ⟹ **维数比较即可** ⟹ 多项式可判；
4. 与顶层（子式 $\gcd$）、$\omega=0$（闭式）合起来：**三层全部可算** ⟹ $q1$ 看起来在 $\mathrm P$，
   **硬度无立足点**。

## 放弃原因

- 必要方向**未证明**（这是本线最后一个技术缺口）；
- 数据只在 $n=5$、$p=1$、$k=3$ 上（$k\ge4$ 未测）；
- 固定行补一位的边界未处理。

## 残留价值

- **一条干净的判据 + 21 个一致样本**，把中间层化成线性代数；
- 明确最后一步是"证明必要方向"；
- 三层可算的整体图景（$\omega=0$ / 中间 / 顶层）现在都有具体判据（中间那条待证）。

## 下一步

证必要方向：若 $\mathcal T_W$ 是真子空间，证明对任何有限行集 $\mathcal P\subseteq\mathcal T_W$，
$\{\lambda:\operatorname{rank}E_\lambda(\mathcal P)=\omega\}$ 是**有限**集——但注意 446 表明
$(E)$（即 $\mathcal P=\mathcal T_W$ 全取）可以成立，所以正确提法要限制 $\mathcal P$ 的维数（$<\dim\mathcal T_W$？）或行数。

## 相关文件

- [444](444_threshold_criterion.md)（判据）、[446](../../decision_algorithms/attempts/446_bug_located.md)（bug 与等价性）
- [437](437_eval_map_criterion.md)（$(E)$ 必要）、[441](441_projection_not_sufficient.md)（零配偶充分）

## 状态

- 判据：**[未证，21/21 数据一致]**。
- 充分方向：**[已证-纸面]**。
- 必要方向：**[未证]**。
