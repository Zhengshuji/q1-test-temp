# 384 专家 105 号审计：$L_0$ 的秩是硬错误；缺"满秩首项系数引理"

> 送审件 [105](../../../for_expert/archive/105_hyperplane_prescribed_rows_and_complexity.md)（已归档），
> 答复 [105-reply](../../../for_expert/archive/105_hyperplane_prescribed_rows_and_complexity-reply.md)（994 行）。
> 总评：**"substantial mathematical progress"**、**"sound and potentially publishable mathematical core"**；
> 但有一处**硬错误**（$L_0$ 的秩）与一处**关键缺失引理**（满秩首项系数）。

## 目标

1. 记录逐条裁决。
2. 落实：$L_0$ 秩问题（Lemma C / $q_{\text{eff}}$）、满秩首项系数引理、结式的"充分非必要"、Theorem 1′ 的三处细化。
3. 明确实现范围的诚实表述（只到有理特征值）。

## 设想与理由

105 号是"报告 + 请求审计"的混合件。我预期它主要回答位复杂度；实际它同时做了三件事：
确认主体（三步链）、指出一处**硬错误**（$L_0$ 的秩）、补一个**我完全没意识到的引理**（满秩首项系数）。
所以本轮的落实重点是"改正"，不是"新增"。

## 做法

逐条读裁决 → 分成"确认 / 硬错误 / 缺失引理 / 建议" → 硬错误与缺失引理写进 378 的更正块，
结式的"充分非必要"写进 381，位复杂度的七步路线记录在本文（作为下一轮的工作清单）。

## 裁决总表

| 组件 | 裁决 |
|---|---|
| Lemma A（预设行相容） | **正确**（建议把 $E_\mu^0$ 显式写成"与预设行相容的方向空间"） |
| Lemma B（纤维） | **正确**（建议显式写出 $\delta\le s\le\rho$ / $\rho-1$ 两个可行性不等式） |
| **Lemma C（全行秩）** | **前提不足**：需要 $\operatorname{rank}L_0=r_0$，否则目标维数应是 $q_{\text{eff}}$ |
| **Theorem 1′** | 结构正确、维数正确、不可约正确；三处细化（范畴、空层、方向层面的划分） |
| **图卡 gcd 判据** | 需要**满秩首项系数引理**才能从"generic gcd 正次数"推出"每个点都坏" |
| 结式检验 | **充分非必要**（反例 $f_1,f_2,f_3$：两两有公因子但三者 gcd $=1$） |
| 反例 | 有前景，但需**完整数据**（含 $q$）与**覆盖每个图卡**的证书 |
| Paper II 对偶 | 方向对应正确；$V\mapsto W$ 的纤维需用 $\overline\Phi$ 的满射条件刻画 |
| 固定 $p$ 位复杂度 | **可行但未证**；给了完整的证明路线（§4） |

## 硬错误：$L_0$ 的秩

原问题 $L=[L_0;R]$，$L_0\in\mathbb Q^{r_0\times n}$。记 $t_0=\operatorname{rank}L_0=\dim V_0$，则
$$\dim V\le t_0+(q-r_0).$$
所以除非 $\operatorname{rank}L_0=r_0$，行空间**不可能**达到 $q$ 维——**Lemma C 的结论不成立**。

**两条修法**（按专家的建议）：
- **Route A**：把 $\operatorname{rank}L_0=r_0$ 写成显式假设；
- **Route B**：令 $q_{\text{eff}}=t_0+q-r_0$、$s_{\text{eff}}=q_{\text{eff}}-(k-1)$，纤维改为
  $$\operatorname{Gr}\bigl(s_{\text{eff}}-\delta,\ \mathcal Q_v/\overline V_{0,v}\bigr),\qquad \dim=(s_{\text{eff}}-\delta)(r(v)-s_{\text{eff}}).$$

我们所有实例里 $L_0$ 为空或单行（秩=行数）⟹ 不受影响；但**一般陈述必须改**。

## 关键缺失引理：满秩首项系数

> **引理（满秩首项系数）.** 设图表上 $\operatorname{rank}H\equiv\omega$。则每个点处至少有一个极大子式的 $\lambda$-次数**恰为 $\omega$**；
> 于是若 $K(X)[\lambda]$ 上的 gcd 次数**为正**，则**每个**特化点都有非平凡公因子 ⟹ 整个图卡全坏。

*证明（专家的）.* 去掉内容后的非常数公因子 $g\in K[X,\lambda]$ 整除每个子式；若在某点 $g(X_0,\cdot)$ 为**常数**，则每个 $m_i(X_0,\cdot)$ 的次数 $<\omega$，与"某子式次数 $=\omega$"矛盾；若 $g(X_0,\cdot)\equiv0$，则所有子式恒零，同样矛盾。$\square$

**这是"generic gcd 正次数 ⟹ 整图卡坏"的唯一正确理由**——不是 gcd 的一般性质（$X\lambda+1$ 在 $X=0$ 退化为 $1$）。

## 其它修正

1. **结式充分非必要**：$f_1=\lambda(\lambda-1)$、$f_2=\lambda(\lambda-2)$、$f_3=(\lambda-1)(\lambda-2)$ 两两有公因子但 $\gcd(f_1,f_2,f_3)=1$。所以"所有结式为零"**不能**推出坏，只能"未判定"。
2. **Theorem 1′ 三处细化**：① 说明是"局部闭实代数底上的代数相对丛"；② 空层显式（$h_\mu^0=0$ / $d_\mu^0=0$）；③ 先在方向层面说划分（两支不相交且覆盖）。
3. **迭代/数域**：无理特征值时纤维基与铅笔系数落在 $\mathbb Q(\mu)$，gcd 必须在 $\mathbb Q(\mu)(X)[\lambda]$ 上算；我目前只做有理 ⟹ **诚实的定理只覆盖"所有相关实特征值都有理"的子类**，比"几何单谱"窄得多。
4. **位复杂度的路线**（专家 §4，可直接照做）：
   - 压缩高度引理（分数自由消元 + 清分母 + 本原整数列 + Hadamard 界）；
   - 特征多项式/特征值高度（标准根高度界；$[\mathbb Q(\mu):\mathbb Q]\le n$、$h(\mu)\le\mathrm{poly}(n,\tau)$）；
   - 特征向量与商丛基（同一数域上做精确消元）；
   - 图表变量 $d\le p^2$、图卡数 $\binom{r-\delta}{s-\delta}$ 常数；
   - 子式 $\le n^{O(p)}$ 个、$\lambda$ 与 $X$ 的次数 $\le\omega$；
   - **无分数子结式**（不是朴素欧几里得）；且要界**多多项式** gcd，不是一对结式。
5. **Paper II 对偶**：应立为命题（专家给了完整陈述）；$V\mapsto W$ 的纤维：
   $\ker\Phi=(K_0+AK_0)^\perp$、$T_W=\Phi^{-1}(W)$、$\overline\Phi:T_W/S\to W/\Phi(S)$，
   提升 = 满足 $\overline\Phi(\overline V)=W/\Phi(S)$ 的子空间——**是满射轨迹，不是整个 Grassmannian**。
6. **否定证书的层级**：方向筛（已用）→ 纤维维数证书（$\delta>s$ 或 $s>\rho$）→ 普遍谱障碍（$\exists z,\lambda_0$: $\lambda_0 z-Az\in U_v$）→ 精确代数证书（逐图卡）。

## 进展与落实

1. 本文件记录裁决；$L_0$ 秩问题与满秩引理**已写入 378 的更正块**。
2. 结式的"充分非必要"已记入 381。
3. 位复杂度的路线已记录（可作为下一轮的工作清单）。

## 最终结论

1. **核心成立**：预设行融入方向空间（$E_\mu^0$）+ 相对 Graßmann 纤维 + 逐图卡铅笔证书，
   这条三步链被专家称为"the most valuable result"。
2. **必须改**：$L_0$ 秩（Route A 或 B）、缺满秩首项系数引理。
3. **诚实范围**：实现只到有理特征值 ⟹ 定理只覆盖"有理特征值"子类。

## 放弃原因

- 没有实现 $q_{\text{eff}}$（Route B）；
- 没有把数域接到图卡 gcd；
- 没有按专家 §4 的路线写位复杂度证明。

## 残留价值

- 一份逐条裁决与两处硬修正；
- 满秩首项系数引理的完整陈述与证明（专家给的）；
- 位复杂度的七步证明路线。

## 相关文件

- [attempts/378](../../c_stratification/attempts/378_parameterization_with_L0.md)（定理 1′，已加更正）
- [attempts/381](../../c_stratification/attempts/381_m_ge_2_chart.md)（结式，已注明充分非必要）
- [attempts/382](../../c_stratification/attempts/382_general_m_two_way.md)（双向判定）
- [attempts/357](../../c_stratification/attempts/357_rational_function_decider.md)（generic gcd 判据）

## 状态

- 核心三步链：**被确认**。
- $L_0$ 秩 / 满秩引理：**[已记录，待写入正文]**。
- 位复杂度：**[未证]**（路线已明确）。
