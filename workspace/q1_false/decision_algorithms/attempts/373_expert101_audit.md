# 373 专家 101 号审计：三处必须修正；核心方向被确认

> 送审件 [101](../../../for_expert/archive/101_hyperplane_layer_complete.md)（已归档），
> 答复 [101-reply](../../../for_expert/archive/101_hyperplane_layer_complete-reply.md)（2111 行）。

## 目标

1. 记录 101 号的逐条裁决。
2. 落实三处必须修正（特征方向、Grassmannian 纤维、实 vs 复）与 Prop G 的降级。
3. 加代码守卫，保证"不完备"时不下结论。

## 设想与理由

101 号的总评是"有意义的扩展"，并明确说**核心想法**（超平面条件 ⟹ 可容许方向 = 压缩的特征向量）
是这条线最有价值的发现。但审计也指出：我与"完整参数化"之间还差三处几何事实，
而这三处恰好是 Prop G 的前提。所以本轮以"修正 + 降级 + 守卫"为主，不新增数学。

## 做法

逐条读裁决 → 映射到受影响的卷宗（350 的 Prop E、370 的 Prop G、357 的判定器）→ 改陈述/加守卫 →
重跑三个实例确认结论不变。

## 裁决总表

| 命题 | 裁决 |
|---|---|
| Theorem A（闭性 + 判据） | **成立**（代数假设下）；但"determinantal ⟹ 不可约"**不普遍成立**，须显式论证或直接参数化 |
| Theorem B（$p=1,q=n-2$） | **成立**（应表述为"满行空间模式"的定理） |
| Prop C（零频秩） | **正确且有用**；建议**前移**作快速剪枝 |
| Prop D（反例） | **重要且有效** |
| Prop E（可容许 $v$） | 非特征情形**正确**；**须扩展到特征情形**（Prop E′） |
| "层 = 有限个纤维" | **须修正**（见 §1、§2） |
| Prop F（左因子） | **正确**；但**等价于** Paper I 的 pivot-pencil 形式，不是新判据；术语应为"特征空间入射解释" |
| 双向算法 | 有前景；须补**实**参数化 |
| Prop G（固定 $p$ 多项式） | **未证**；$d_{\mathrm{fib}}\le2p$ 不够 |

## 三处必须修正

### 1. 特征值有限，但**特征方向**不必有限

若 $\dim E_\mu=d>1$，方向集是 $\mathbb P(E_\mu)\cong\mathbb P^{d-1}$——**无穷多**（例：$M=I_k$）。
所以层是
$$\bigcup_{\mu\in\operatorname{Spec}(M)}\ \mathbb P\bigl(\ker(M-\mu I)\bigr)\ \times\ \text{(纤维)},$$
而**不是**"有限个方向 × 纤维"。算法必须保留整个特征空间。

### 2. 纤维是 **Grassmannian**，不是 $\mathbb P^r$

记 $D_v=K_0\cap U_v^\perp$（$\dim=k-1$）。$V$ 由 $V/D_v\subseteq U_v^\perp/D_v$ 决定，故纤维为
$$\operatorname{Gr}\bigl(d_V-(k-1),\ \dim(U_v^\perp/D_v)\bigr);$$
只有 $q=k$（$V/D_v$ 一维）时才是 $\mathbb P^r$。我此前写 $\mathbb P^r$ **只在 $q=k$ 时正确**。

### 3. 实 vs 复

原始问题要**实**观测器：压缩的特征值必须**实**（否则无实特征向量），只取特征多项式的**实根**；
"generic gcd = 1 ⟹ 实可行点"还需**实点 Zariski 稠密**这一显式假设（对仿射/射影参数化成立）。

## 其余重要意见

- **Prop G 分两阶段**：① 几何参数计数（含 $\dim\mathbb P(E_\mu)$ 与 Grassmannian 参数）；② 每块**位**复杂度。
  有用事实：$q-\omega\le2p+1$、$\binom{k}{\omega}=k$ ⟹ 极大子式个数
  $k\binom{q}{q-k+1}\le k\sum_{j\le2p+1}\binom{n}{j}$，固定 $p$ 时是多项式（但**不足以**独证 Prop G）。
- **Q2**：正确定位是"参数化矩形铅笔对 $(G,X)$ 的 generic 广义特征值"（Paper I 的 pivot 分解 $H=XB$、$G=SX$）。
- **Q5**：加零频条件**不充分**（反例 $H=\binom10$、$S=\operatorname{diag}(2,3)$：零频通过但 $\operatorname{rank}P(2)=0$）。
- **Q3**：$q_0$ 不是对的参数；$\ell$ 随 $n$ 增长；**保留固定 $p$**。
- **§10.3**：不要声称"第一个反例"。
- **§10.4**：加自动化一致性检查（零多项式归一、gcd 整除每个子式、Bézout、非平凡公因子）。
- **§12**：Lean 优先序：Prop E′ → 纤维刻画 → 零频 → 射影闭性 → pivot/incidence 等价 → 判定流程。
- **§13/§17**：下一步**唯一目标** = "完整的超平面层参数化定理"（特征空间 + Grassmannian 纤维，实、有限不可约覆盖）。

## 进展

1. 已归档 101 号问答。
2. 350 的 Prop E 改为 **E′**（含特征情形），并写明"方向可为 $\mathbb P^{d-1}$"与"纤维是 Grassmannian、仅有 $q=k$ 时 $\mathbb P^r$"。
3. 370 的 Prop G 改为**条件性**（Stage 1 + Stage 2），补上极大子式计数的组合事实。
4. 判定器加两道守卫：$q=k$ 的适用性（实现即 $q=k$）、特征空间维数 $>1$ 时标"不完备"。
5. 重跑三实例：4242 可行、4245 可行、4246 不可行，结论**不变**（三实例的特征空间都是 1 维）。

## 最终结论

1. **核心方向被确认**：压缩特征向量刻画是这条线最有价值的想法。
2. **Prop G 降级**：固定 $p$ 的多项式结论仍需"完整参数化定理"（专家指定的下一步）。
3. 三实例的结论不受影响。

## 放弃原因

- 没有做"完整参数化定理"（本轮只做修正与守卫）；
- 没有处理重复特征值的一般情形（只在守卫里标"不完备"）；
- 没有补实根隔离与实参数化的实现。

## 残留价值

- 一份**逐条裁决**，把"哪些成立、哪些必须改"钉死；
- Prop E′ 与 Grassmannian 纤维的正确陈述；
- Prop G 的两阶段结构，以及可直接复用的子式计数事实。

## 相关文件

- [attempts/350](../../c_stratification/attempts/350_admissible_v_are_eigenvectors.md)（Prop E → E′）
- [attempts/370](../../c_stratification/attempts/370_c1_layer_complexity.md)（Prop G → 条件性）
- [attempts/357](../../c_stratification/attempts/357_rational_function_decider.md)（判定器）
- [attempts/372](../../c_stratification/attempts/372_decider_complete.md)（守卫的来源）
- [c355](../../../../tools/verification/c355_rf_gcd.py)

## 状态

- 核心方向：**被确认**。
- Prop G：**[未证]**（需两阶段）。
- 三实例结论：**[不变]**。
- 完整参数化定理：**[未做]**（下一步）。
