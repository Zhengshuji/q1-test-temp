# 路线 8：(5a) 地板 $\rho_{ci}$ 与真实 $\rho^*$ 的差距

## 目标

主线 Q1 的第一步：既然 $\rho_{ci}=P(T,B,U_0)$ 现已可算（$O(n^4)$，见 [../../../proof/p_is_polynomial/](../../../proof/p_is_polynomial/README.md)），
先测**地板离真值有多远**。若几乎总是相等，层扫描可塌成一层；若有稳定差距，必须搞清楚是哪一层被 $(5b)$ 毙掉。

## 设想与理由

$(5a)$ 只约束 $\rho$ 的下界；$(5b)$ 是余维条件，会把最小 ci 子空间毙掉。
所以"地板"$\rho_{ci}$ 是**下界**，真实 $\rho^*\ge\rho_{ci}$。差距的大小决定下一步该攻哪一层。

## 做法

新工具 [c199_floor_gap.py](../../../tools/layer_search/c199_floor_gap.py)（同一 $\mathbb F_p$ 上比较两者，内部一致）：

1. 用 `c192.setup` 取约化数据 $(T,B,U_0)$（$T$ 的矩阵是 `TW`，$B=\operatorname{span}(Bj)$，$U_0=\pi(S)$）；
2. $\rho_{ci}=P(T,B,U_0)$：把 [c195](../../../tools/p_algorithm/c195_P_q.py) 的递归在 $\mathbb F_p$ 上实现；
3. $\rho^*$：`c192.search` 穷举 $(U,H,\tau)$（$U$ 全枚举、$\tau$ 采样）；
4. 比较并统计 gap。

**加固**：$\tau$ 采样从 12 提到 40，gap 分布不变；对 $p=5$、$\tau$-维 $\le2$ 的情形，40 次采样已覆盖全部 $5^2=25$ 个 $\tau$ ⟹ **$\mathbb F_5$ 上是伪穷举**，gap 不是采样造成的。

## 进展

数据（$n\le5$、$d\le3$、$p=5,7$）：

| gap $=\rho^*-\rho_{ci}$ | 实例数 |
|---|---|
| 0（地板紧）| 7 |
| 1 | 8 |
| 2 | 1 |

典型：$d=2$、$\rho_{ci}=1$、可达集 $\{(2,1),(2,2)\}$ ⟹ $\rho^*=2$，地板 1 从未被达到。

**结构性观察**（$d=2$、$\rho=1$、$c=1$）：该层可行 $\iff$ 存在 ci 直线 $U\supseteq U_0$ 使 $U\cap B\ne0$。
因为 $\rho=1$ 时可控性 $\iff\beta|_H\ne0$，即 $U$ 要含一个非零的 $\beta(h)$；而 $\beta(h)\in B$。
> **2026-10-27 更正**：这条"可控性"论证后来被否决（$\beta(\mathcal H)\subseteq B$ ⟹ 输入恒为零，见 [docs/05](../../../docs/05_open_questions.md) Q5）；
> 本节的**测量数据**（gap 分布）不受影响，但"机制解释"这一句作废。
所以地板失败 $\iff$ **每条 ci 直线与 $B$ 只交于 0**。这是一个**线性**判据（不是搜索）。

## 最终结论

**地板不是紧的**（9/16 有正 gap），所以"层扫描塌成一层"不成立。
但 $(5b)$ 在地板层的失败有**线性/二次型的精确刻画**（$\rho=1$：$U\cap B\ne0$；$\rho=2$：$\det[b;S_\tau b]\not\equiv0$），
说明"逐层精确判定"仍是可行方向。

## 放弃原因

不适用（本路线未放弃，只完成了第一组测量）。

## 残留价值

- 工具 `c199_floor_gap.py`（可复跑，`--trials` 可调）；
- 地板层的**线性判据**（$\rho=1$）——下一步应把它写成一般 $\rho$ 的形式并证明；
- 数据：gap 分布 $\{0{:}7,\ 1{:}8,\ 2{:}1\}$（小 $n$，$\mathbb F_p$）。

## 相关文件

- [../../../tools/layer_search/c199_floor_gap.py](../../../tools/layer_search/c199_floor_gap.py)、[c192_reduced_search.py](../../../tools/layer_search/c192_reduced_search.py)
- [../../../proof/p_is_polynomial/algorithm.md](../../../proof/p_is_polynomial/algorithm.md)
- [../../../docs/05_open_questions.md](../../../docs/05_open_questions.md) Q1
