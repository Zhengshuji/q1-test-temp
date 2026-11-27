# 410 更高阶的 $c$ 怎么处理

> 用户问：做完 $c=2$ 之后，$c\ge3$（乃至 $c$ 随输入变化）怎么办？
> 本文件把"哪些照搬、哪些变质、哪些是新的困难"分开写清。

## 目标

给出**一般 $c$** 的处理方案：结构层、算法层、复杂度层各差什么。

## 设想与理由

$c=2$ 的整套东西里，**只有一处真正用到 $c=2$**：406 的 $W$-消去中
$\dim D^\circ=c$ 是常数。其余（纤维分解、预设行限制、图卡、gcd、实点判据）都**只与 $c$ 是"固定参数"有关**。
所以一般 $c$ 的方案是"**照搬 + 承认代价**"，而不是重新发明。

## 做法

### 1. 结构层：全部照搬（把 $2$ 换成 $c$）

| $c=2$ 的陈述 | 一般 $c$ | 变化 |
|---|---|---|
| 方向 $D\in\operatorname{Gr}(2,K_0)$，$M(D)\subseteq D$ | $D\in\operatorname{Gr}(c,K_0)$，$M(D)\subseteq D$ | 底 $\mathcal I_c(M)$ |
| 底几何：主分量三分法 | 完全同形（不变子空间 = 链段直和） | 分量维数 $c(d_\lambda-c)$ |
| 纤维 $\operatorname{Gr}(t-w_0,T_D/W_0)$ | 同形 | $\dim T_D=(n-k)-r(D)$，$r(D)=\rank(A_{21}|_D)\in\{0,\dots,c\}$ |
| 预设行底条件 $P_{K_0}(V_0)\subseteq D^{\perp_{K_0}}$ | 同形 | 无 |
| **$W$-消去**：铅笔只通过 $\Phi(W)\subseteq D^\circ$ | **同形** | $\dim D^\circ=c$；有效纤维 $\operatorname{Gr}(r,D^\circ)$，维数 $\max_r r(c-r)=\lfloor c^2/4\rfloor$（专家 109 号 §6 的更准界） |
| 单谱 ⟹ 底有限 | 同形 | 孤立点数 \(\binom{k}{c}\)（指数！） |
| 固定 $c$ 的复杂度 $\mathrm{poly}$ | 同形（固定 $c$） | 每卡变量数 $\le\lfloor c^2/4\rfloor$ |

**结论**：结构定理（393/404/406/407）对一般 $c$ **逐字成立**，只要把"2"换成"$c$"、
把"$r\in\{0,1,2\}$"换成"$r\in\{0,\dots,c\}$"。这是 $c=2$ 工作的最大价值——它不是特例的技巧。

### 2. 算法层：同形，但图卡数与变量数随 $c$ 涨

- 底图卡：$\operatorname{Gr}(c,E_\lambda)$ 的标准图卡数 $\binom{d_\lambda}{c}$；
- 有效纤维图卡：$\operatorname{Gr}(\le c,D^\circ)$ 的图卡数 $\le\sum_{s\le c}\binom{c}{s}$（有限但随 $c$ 涨）；
- 每卡变量数：底 $c(d_\lambda-c)$ + 有效纤维 $\le\lfloor c^2/4\rfloor$。

所以"**固定 $c$ 可判**"照旧；只是常数随 $c$ 变大。

### 3. 复杂度层：三条不同的路，代价各不相同

**(a) 固定 $c$ + 单谱**：$\mathrm{poly}(n,\tau)$ ✓（408 的 $c=2$ 逐字推广，图卡数 $\binom{k}{c}$ 是
$k^{O(c)}$，固定 $c$ 仍是多项式）。

**(b) 固定 $c$、不假设单谱**：底可正维（$\operatorname{Gr}(c,E_\lambda)$ 维数 $c(d_\lambda-c)=O(cn)$），
得到 $n^{O(cn+c^2)}$——**固定 $c$ 但不是多项式**。这正是 408 说的"两条边界"之一。

**(c) $c$ 随输入变化**：底的分量数 $\binom{k}{c}$ 可指数（$c=\lfloor k/2\rfloor$ 时 $\Theta(2^k/\sqrt k)$），
所以"枚举分量"这一步就指数。**这一步是 $q1$ 的真正瓶颈。**

### 4. 一般 $c$ 上值得问的三个结构问题（按价值排序）

**Q-A（最有希望）**：$\mathcal I_c(M)$ 的分量数能否**不必枚举**？
例如：能否把"$\exists$ 分量"改写成对 $M$ 的一个**代数条件**（如某矩阵的秩），
从而一次判定、不枚举？这与"$\exists$ 不变子空间"的经典问题同型，但也可能因为 $M$ 固定而变简单。

**Q-B**：**$\Phi$ 的量化能否消掉**？$c=2$ 时 $\Phi$ 只是 ℙ^1 的点；一般 $c$ 时是
$\operatorname{Gr}(\le c,D^\circ)$ 的点。能否把"存在 $\Phi$ 使铅笔满秩"化成一个
**秩/分离条件**（专家 108 号 §14 的原话："rank, controllability, observability, or subspace-separation
condition involving only the induced maps on $T_D/W_0$"）？若能，则整个纤维消失，只剩底。

**Q-C**：**底与纤维能否对偶互换**？449 的字典说 $c=k-\dim U$（$U=\pi_1(W)$）——
大 $c$ 对应小 $\dim U$。若 $\dim U$ 一侧有更好的结构（例如 $\rho$ 侧已有多项式算法 $P(T,B,U_0)$），
也许该**在对偶侧做层分解**，让"层号"变成 $\dim U$ 而不是 $c$。

## 进展

- 结构层的"逐字推广"已核对：393/404/406 的证明只用到"$\dim D=c$"与"$M(D)\subseteq D$"，与 $c=2$ 无关；
- 算法层的计数已写出；
- 三个结构问题记下（Q-A 分量数、Q-B 消 $\Phi$、Q-C 对偶换层号）。

## 最终结论

1. **结构照搬**：把 2 换成 $c$ 即可，$c=2$ 的工作不是特例技巧；
2. **算法照搬**：固定 $c$ 可判，代价随 $c$ 涨；
3. **复杂度分层**：固定 $c$+单谱 ⟹ poly；固定 $c$ ⟹ $n^{O(cn+c^2)}$；$c$ 可变 ⟹ 枚举分量指数；
4. **下一步的正题**是 Q-A / Q-B / Q-C 三条之一，其中 Q-B（消 $\Phi$）是 $c=2$ 已成一半（$\Phi$ 只剩 ℙ^1）
   的自然延伸，也最可能产出新的结构定理。

## 放弃原因

- 没有证明任何 Q-A/Q-B/Q-C；
- 没有把一般 $c$ 的图卡计数写成显式公式（只给了量级）；
- 没有检查 $\operatorname{Gr}(\le c,D^\circ)$ 的图卡在 $c$ 大时的实际数量（$\sum_{s\le c}\binom{c}{s}$ 是指数的）。

## 残留价值

- 一张"$c=2$ → 一般 $c$"的**对照表**，说明哪些结论逐字推广、哪些代价变质；
- 三个结构问题（Q-A/Q-B/Q-C）的明确表述，可直接作为下一阶段的研究计划；
- 明确"$c$ 可变时枚举分量是指数的"这一点是 $q1$ 的真正瓶颈。

## 相关文件

- [attempts/393](393_c2_fibre_and_base.md)（纤维与底）、[404](../../decision_algorithms/attempts/404_expert108_audit.md)（预设行与底分类）
- [attempts/406](406_eliminate_W.md)（$W$-消去，逐字推广）、[407](../../decision_algorithms/attempts/407_effective_charts.md)（可实现图卡）
- [attempts/408](408_c2_complexity.md)（两条边界）、[409](../../../q1_true/multiplication_gate/attempts/409_hardness_plan.md)（硬度规划）
