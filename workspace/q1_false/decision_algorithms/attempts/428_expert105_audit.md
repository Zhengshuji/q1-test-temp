# 428 专家 105 号审计：相容轨迹是一个 Grassmannian（新定理）；全局开性是下一个关键

> 送审件 [105](../../../for_expert/archive/105_active_subspace_tests.md)（已归档），
> 答复 [105-reply](../../../for_expert/archive/105_active_subspace_tests-reply.md)。
> **总评**：他认这条问法"比之前关于表达力的泛问精确得多"，并把它定为下一阶段的核心；
> 同时给出**一条新定理**、Q1–Q5 的明确裁决、以及**一条具体的计算路线**。

## 目标

1. 记录裁决与新增数学（Proposition 1–4、Theorem A–D）。
2. 记录他对我的五处更正。
3. 定下下一步：按他的顺序，先做 $k=2,\omega=1$ 的精确分类。

## 设想与理由

审计型回复：只记明确裁决与新增数学，不记客气话。

## 做法与结果

### 1. **新定理：相容轨迹永远是单个 Grassmannian**

令固定行张成
$$U=\operatorname{span}\{h_i^0,g_i^0\}\subseteq V,\qquad d=\dim U .$$
相容条件恰是 $U\subseteq W$，故
$$\boxed{\mathcal X_{\mathrm{comp}}=\{W\in\operatorname{Gr}(\omega,k):U\subseteq W\}\cong\operatorname{Gr}(\omega-d,k-d)}$$
（$d\le\omega\le k$ 时；$d>\omega$ 时为空），且
$$\dim\mathcal X_{\mathrm{comp}}=(\omega-d)(k-\omega).$$
三种情形：$d=\omega$ ⟹ $\operatorname{Gr}(0,k-\omega)$ **单点**（钉死，正是我 421 的结论）；
$d<\omega$ ⟹ 正维；$d=0$ ⟹ 整个 Grassmannian。

**重要推论**：相容轨迹在代数闭域上**不可约**——所以"把相容轨迹做成若干射影直线的积"这条路**不成立**（$\operatorname{Gr}(2,3)\cong\mathbb P^2$ 不可约）。

### 2. Q1（(iii) 的类型）：分三层，全局仍开

- 对**固定** $W$：谱正则性在纤维参数里 **Zariski 开**（可证）；
- 在**常秩层**上：活跃集**相对开**（可证）；
- **全局**：活跃集是构造性集，**开性与闭性都未证**；他明确说"现在断言开/闭/都不是都为时过早"，
  并建议把"证明或否证全局开性"当作**第一优先**。

### 3. Q2（分量编码）：Zariski 分量不行，实拓扑分量可行

- **Zariski 分量**：若活跃集是相容 Grassmannian 的非空 Zariski 开子集，则它**不可约** ⟹ 只有一个代数分量 ⟹ **编码不可能**；
- **实欧氏分量**：**可能**——例如 $\mathbb P^1(\mathbb R)\setminus\{P_0,P_1\}$ 有**两个**连通分量，而 $\mathbb C$ 上仍连通；
- **纤维级刚性不阻碍**只依赖 $W$ 的解码器 ✓（解码不加自由行的多项式限制）；
- 更关键的一条：**判决型归约不需要解码**——多一归约只要"可行性等价"，解码只在搜索型归约里才需要。

### 4. Q3（$2^s$ 个分量）：可能，但要靠谱条件切，且有维数下界

- 相容轨迹是**单个** Grassmannian，$\prod_i\mathbb P^1$ 不是它（$\dim$ 相同也不同构）；
- 可行做法：在坐标卡 $W=\operatorname{row}[I_\omega\ X]$（$X\in\mathbb R^{\omega\times(k-\omega)}$）里，
  让谱条件给出若干**分离超曲面** $g_i(X)=0$，用**符号** $\operatorname{sign}g_i$ 编码；
- **必要条件**：$(\omega-d)(k-\omega)\ge s$（$s$ 个独立连续参数）；
- 他建议的中间问题是：**谱可行性的多项式能否在 Grassmannian 的维数下实现指数多个符号区域**。

### 5. Q4（顶层）：值得单独做，但**不等于**方阵情形

- $\omega=k$ ⟹ $W=V$ 唯一，Grassmannian 退化成一个点；
- 相容自动；**秩补全自动**（$\pi_1(\mathcal S)=V$，只要 $m\ge1$）；
- 整个判定**只剩生成铅笔的谱正则性**；
- **方阵障碍只对 $r=k$ 适用**，不对 $\omega=k$ 适用（$r>k$ 时矩形铅笔可以处处满列秩，他给了 $H=\begin{pmatrix}1&0\\0&1\\0&0\end{pmatrix}$、$H_A=\begin{pmatrix}0&0\\0&0\\1&1\end{pmatrix}$ 的例子）；
- 结论：**"没有子空间选择"不等于"没有复杂度"**——数据仍可编码难的代数条件。

### 6. Q5（决定性计算）：先 $k=2,\omega=1$，再 $\operatorname{Gr}(2,3)$

他给了完整配方：

- $W_{[s:t]}=\operatorname{span}\{(s,t)\}$，成员判据 $-tx_1+sx_2=0$；
- 相容性三分：$d=0$ ⟹ 全 $\mathbb P^1$；$d=1$ ⟹ 唯一点；$d=2$ ⟹ 无；
- $\mathcal T_z=\ker\left(\begin{bmatrix}-z&1&0&0\\0&0&-z&1\end{bmatrix}\big|_{\mathcal S}\right)$；
- 每行写成 $h_j=\alpha_j(1,z)$、$g_j=\beta_j(1,z)$，则
$$\boxed{\text{谱正则}\iff\gcd_j(\lambda\alpha_j-\beta_j)=1}$$
（**标量线性多项式**的 gcd，比一般矩阵铅笔简单得多）；
- 然后才上 $\operatorname{Gr}(2,3)$：$W_q=\ker q^{\mathsf T}$、$\mathcal T_{W_q}=\ker\left(\begin{bmatrix}q^{\mathsf T}&0\\0&q^{\mathsf T}\end{bmatrix}\big|_{\mathcal S}\right)$、
  $\gcd$ 在 $\overline{\mathbb F(z)}[\lambda]$ 上算、用结式消去 $\lambda$。

### 7. 他对我的五处更正

1. **"有限个连通分量"必须说清拓扑**（Zariski vs 实欧氏）；
2. **"$\prod\mathbb P^1$ 构造"只能当作实活跃集的**可能拓扑**，不是相容轨迹的结构**；
3. **顶层要区分 $\omega=k$ 与 $r=k$**（只有后者的方阵情形必坏）；
4. **"相对开"在 $\mathcal T_W$ 的维数跳跃点分析清楚前只是条件性的**；
5. **判决型归约与见证解码型归约要分开**。

### 8. 他给的一条形式化结论（可直接用）

> **（16）** 固定 $W$。$\mathcal P_W=\mathcal T_W^m$ 不可约；秩层条件 $\mathcal U^{rank}_W$ 与谱条件 $\mathcal U^{spec}_W$ 都是**开**集。
> 故
> $$\exists z\in\mathcal P_W\ \text{两者都成立}\iff\mathcal U^{rank}_W\ne\varnothing\ \text{且}\ \mathcal U^{spec}_W\ne\varnothing .$$
> 于是**"秩补全"与"谱条件"可以分开检验**，且 $\gcd$ 应当在**整个 $\mathcal T_W^m$** 上算，不必先强加秩补全。

### 9. 域约定（他提醒）

$R\in\mathbb R^{m\times n}$、$\lambda\in\mathbb C$；代数开性论证应在实参数空间的复化上做，实数点用于真见证。
**复可行 $\ne$ 实可行 $\ne$ 有理可行**，最终复杂度定理必须分清。

## 进展

- 五处更正全部记录；
- Proposition 1（相容轨迹）与 (16)（可分离检验）可直接用；
- 下一步按他的顺序：**Theorem A（相容几何，已备）→ B（分层开性，框架已有）→ C（全局开性，开放）→ D（分量复杂度，开放）**；
- Q5 的配方可直接实现。

## 最终结论

1. **相容轨迹 = 一个 Grassmannian**（新定理，$\dim=(\omega-d)(k-\omega)$）；
2. **(iii) 的全局开性是下一个关键**；(iii) 在固定 $W$ 与常秩层上已证开；
3. **分量编码只有走"实拓扑分量"才可能**；Zariski 分量不可能；
4. **顶层（$\omega=k$）值得单独做**：无 Grassmannian、相容与秩补全自动、只剩生成铅笔的谱正则性；
5. 判决型归约**不需要解码**——这条纠正了我此前的表述。

## 放弃原因

- 本轮没有开始 $k=2,\omega=1$ 的计算（下一步）；
- 全局开性没有推进（既未证也未构造反例）；
- 分量复杂度的符号区域计数没有开始。

## 残留价值

- **一条新定理 + 一条可分离性结论**（(16)）；
- 用户可执行的完整计算配方（$k=2$ 标量 gcd → $\operatorname{Gr}(2,3)$ 结式）；
- 明确的下一步优先级（先全局开性，再分量复杂度）。

## 下一步

1. **$k=2,\omega=1$ 的精确分类**（他的 #1）：$\gcd_j(\lambda\alpha_j-\beta_j)=1$ 的活跃集；
2. 若活跃集在 $\mathbb P^1$ 上只是空/点/稠密开，则全局开性在这一层成立；
3. 再看 $\operatorname{Gr}(2,3)$。

## 相关文件

- [105](../../../for_expert/archive/105_active_subspace_tests.md)、[105-reply](../../../for_expert/archive/105_active_subspace_tests-reply.md)
- [417](417_expert104_audit.md)（活跃子空间判据的来源）
- [421](../../c_stratification/attempts/421_omega1_excluded.md)（$\omega=1$ 钉死——现为 Proposition 1 的特例）
- [427](../../c_stratification/attempts/427_criterion_validated.md)（单 $W$ 判据与更正）

## 状态

- 裁决落实：**[完成]**。
- 相容轨迹定理：**[已证-纸面]**（他的证明，我复核）。
- $k=2,\omega=1$ 的精确分类：**[未做]**（下一步）。
- 全局开性：**[开放]**。
