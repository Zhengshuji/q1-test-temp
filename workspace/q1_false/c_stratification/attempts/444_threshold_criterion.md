> **判据已更正（448）**：见 [448](../../decision_algorithms/attempts/448_criterion_corrected.md)。

# 444 阈值数据支持判据：可行 $\iff\mathcal T_W=W\oplus W$（$\mathcal S\supseteq W\oplus W$）

> 承接 443（灰色带可行侧非空，$\dim\mathcal T_W=4=2\omega$）。本轮测阈值，
> 得到的全部数据都指向一条**很干净**的判据。

## 目标

定出"$\dim\mathcal T_W$ 多大才可行"。

## 设想与理由

$\mathcal T_W\subseteq W\oplus W$，故 $\dim\mathcal T_W\le2\omega$，且等号 $\iff\mathcal T_W=W\oplus W$
（即 $\mathcal S\supseteq W\oplus W$）。而等号时**零配偶条件 $(Z)$ 自动成立** ⟹ 可行（441 的构造）✓。

所以只需检验反向：$\dim\mathcal T_W<2\omega$ 时是否**永不**可行。

## 做法

[c387](../../../../tools/verification/c387_threshold.py)：随机实例（$n=5$、$p=1$、$k=3$），
对每个相容 $W$ 与 $\omega\in\{1,2\}$ 记录 $(\omega,\dim\mathcal T_W,(E),(F))$，
其中 $(F)$ 用 $m=2\omega$ 个可用对精确判（$\tau$-符号 $\gcd$）。

## 进展（数据）

| $\omega$ | $\dim\mathcal T_W$ | $2\omega$ | $(E)$ | $(F)$ | 例数 |
|---|---|---|---|---|---|
| 2 | **3** | 4 | **假** | **假** | 10/10 |
| 1 | **4** | 2 | 真 | **真** | 1（443 的实例，$\dim=2\omega$） |

**全部数据一致于**：

$$\boxed{(F)\iff \dim\mathcal T_W=2\omega\iff \mathcal T_W=W\oplus W\iff \mathcal S\supseteq W\oplus W}$$

（$\dim<2\omega$ ⟹ 不可行：10/10；$\dim=2\omega$ ⟹ 可行：1/1。）

## 推论：中间层**多项式可判**

"$\exists\,\omega$ 维 $W\supseteq U$ 且 $W\oplus W\subseteq\mathcal S$" 是可算的：

- $W\oplus W\subseteq\mathcal S$ 等价于 $W\subseteq\pi_1(\mathcal S\cap(V\oplus0))$ 且
  $W\subseteq\pi_2(\mathcal S\cap(0\oplus V))$——**两个固定子空间**（与 $W$ 无关）✓；
- 故存在这样的 $W$ $\iff$ $\operatorname{span}\{U\}\cup$ 那两个子空间**合起来维数 $\le\omega$**，
  且可扩到 $\omega$ 维（在 $\mathcal S$-闭的方向上）✓。

于是：

$$\text{层 }\omega\text{ 的可行性}=\text{一个线性代数条件，多项式时间可判}$$

## 最终结论

1. **判据（数据支持，尚未证明）**：可行 $\iff\mathcal S\supseteq W\oplus W$；
2. 于是**每一层的判定都是线性的**（$\omega=0$ 闭式、顶层子式 $\gcd$、中间层 $\mathcal S\supseteq W\oplus W$）⟹
   **$q1$ 的判定看起来在多项式时间内**；
3. **硬度仍无立足点**——但这次不是靠被推翻的层表，而是靠这条有数据支持的干净判据。

## 放弃原因

- **没有证明**"$\dim\mathcal T_W<2\omega$ ⟹ 不可行"（只有 10/10 的样本）；
- 样本很小（10 个实例、1 个可行例）；
- 没有处理 $\mathcal S\supseteq W\oplus W$ 与固定行相容性的联合条件；
- 固定行补一位的边界仍未处理。

## 残留价值

- **一条极干净的候选判据**（$\mathcal S\supseteq W\oplus W$），把中间层化成线性代数；
- 它的**多项式可判性**（两个固定子空间的维数条件）；
- 至此**三层都有了可算判据**，硬度侧的证据链完整。

## 下一步

证明"$\dim\mathcal T_W<2\omega$ ⟹ 不可行"：思路是——若 $\mathcal T_W$ 是真子空间，
则存在非零的线性泛函在 $\mathcal T_W$ 上为零；用它构造一个"必然为零"的组合，
从而某个 $\lambda_0$ 处秩不满（这正是 $(E)$ 失败的形式）。

## 相关文件

- [443](443_gray_band_has_feasible.md)（$\dim=2\omega$ 的可行例）
- [442](442_three_conditions.md)（三条件图景）
- [441](441_projection_not_sufficient.md)（零配偶构造）
- [437](437_eval_map_criterion.md)（$(E)$）

## 状态

- 判据（数据支持）：**[未证，样本 11/11 一致]**。
- 多项式可判性：**[已证-纸面]**（给定判据成立时）。
- 硬度：**[无立足点]**。
