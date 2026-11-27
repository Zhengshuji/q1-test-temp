# 449 专家 107 号：中间层命题漏了 (R)（秩补全）；其余认可

> 送审件 [107](../../../for_expert/archive/107_layer_decision.md)（已归档），
> 答复 [107-reply](../../../for_expert/archive/107_layer_decision-reply.md)。
> **总评**：三处更正方向都对（撤回"中间层恒不可行"、改用 $E_\lambda$、承认 $W$ 搜索未解决），
> 中间层重构"是真正的结构进展"；**但命题不完整**——漏了**秩补全** $\operatorname{rank}H=\omega$。

## 目标

落实裁决：补上 (R)，记录他给的正确命题与证明。

## 设想与理由

他的反例说明为什么 $(E)$ 不够：
$$\mathcal T_W=\{0\}\oplus W\ \Longrightarrow\ E_\lambda(\mathcal T_W)=W\ \forall\lambda\ \text{✓但}\ \pi_1(\mathcal T_W)=\{0\}\ \text{✗}$$
于是 $H$ 的第一分量全零 ⟹ $\operatorname{rank}H=0<\omega$ ⟹ **不可行**。
所以 $(E)$ 能"全靠第二分量"成立，与秩补全**独立**。

## 做法

复核他给的反例与命题证明。

## 进展

> **命题（固定纤维，$m\ge D_W=\dim\mathcal T_W$）.** 层 $\omega$ 在 $W$ 的纤维上可行 $\iff$
> $$\textbf{(R)}\ \operatorname{span}\bigl(\{h_i^0\}\cup\pi_1(\mathcal T_W)\bigr)=W,
> \qquad\textbf{(E)}\ E_\lambda(\mathcal T_W)=W\ \ \forall\lambda\in\mathbb C .$$

**必要性**：可行 ⟹ 第一分量张成 $W$（秩 $\omega$）⟹ (R) ✓；铅笔的每一行都是某个对在 $E_\lambda$ 下的像，
秩 $\omega$ ⟹ 这些像张成 $W$ ⟹ (E) ✓。
**充分性**：取 $\mathcal T_W$ 的基当自由行（每个 $\mathcal S$ 的元素都可由某行实现）⟹ (R) 给 $\operatorname{rank}H=\omega$；
(E) 给铅笔处处满秩 ⟹ 可行 ✓。

## 其他裁决

1. **$\gcd$ 检验对 $(E)$ 是对的**：$M_W(\lambda)=(\lambda x_j-y_j)_j$ 的极大子式 $\gcd=1\iff(E)$ ✓
   （他确认了这个等价），但**必须**配套查 (R)；
2. 他给出一个**计算简化**：不必先算 $\mathcal T_W$ 的基，可直接用 $\mathcal S$ 的基矩阵（§3.1）；
3. $\lambda=\infty$ 需要齐次化处理（§3.2）；
4. **反例（$\dim=2\omega-1$ 满足 $(E)$）被认可"有效且重要"** ✓；
5. **顶层**：$K_0$ 无特征向量只是**点态**必要，**充分性未证**——他没有给证明，只说"未建立" ✗；
6. **$W$ 的搜索**仍是主要未解问题（§6：Grassmann 参数化不能消除搜索）；
7. **$m$ 的阈值**：他说 $m\ge\omega+1$ 是"看起来的泛型阈值"（§5.2），未证。

## 最终结论

1. **中间层命题已修正**（加 (R)）——这是本轮最实质的收获；
2. 于是"层可判"的说法**要重新表述**：给定 $W$ 时可行 $\iff$ (R) ∧ (E)，两者都是**线性/$\gcd$ 计算** ✓；
   但"$\exists W$"仍是**未解的搜索** ✗；
3. 顶层的充分性**退回未证**；
4. 所以 $q1$ 的方向性判断应写为"**若 $\exists W$ 的搜索可解，则 $q1\in\mathrm P$**"，
   而不是我之前写的"三层全可算 ⟹ $q1$ 看起来在 $\mathrm P$" ✗（这句撤回）。

## 放弃原因

- 没有处理 $W$ 的搜索（他明确说这是主要未解问题）；
- 没有做 $\lambda=\infty$ 的齐次化；
- 顶层的充分性仍未证。

## 残留价值

- **正确的中间层命题**（(R) ∧ (E)，含证明）；
- 明确了 $q1$ 的真正剩余障碍：**$\exists W$ 的搜索**（而不是层的判定）；
- 反例被专家认可，保留。

## 下一步

1. 把 (R) ∧ (E) 写成对 $W$ 的**Grassmann 条件**，看"$\exists W$"是否可判（这是他 §6 指的方向）；
2. 顶层充分性：试着造"无特征向量 + $L_0$ 挡路"的反例，或补证明。

## 相关文件

- [107](../../../for_expert/archive/107_layer_decision.md)、[107-reply](../../../for_expert/archive/107_layer_decision-reply.md)
- [448](../../decision_algorithms/attempts/448_criterion_corrected.md)（被本文件补全）
- [437](437_eval_map_criterion.md)（$(E)$）

## 状态

- 中间层命题（含 (R)）：**[已证-纸面]**（他给的证明，我复核）。
- $\exists W$ 的搜索：**[未解]**。
- 顶层充分性：**[未证]**。
