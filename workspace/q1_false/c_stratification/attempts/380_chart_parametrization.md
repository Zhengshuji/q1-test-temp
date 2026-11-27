# 380 图卡参数化：纠正 379 的"未找到"；$L_0=e_6,\ q=4$ 其实可行

> 承接 379（带 $L_0$ 的实现：NO 证书跑通、YES 侧未成）。本轮补上 $\operatorname{Gr}(m,R)$ 的**图卡参数化**，
> 结果推翻了 379 情形 2 的结论。

## 目标

把纤维 $\operatorname{Gr}(s-\delta,\ \mathcal Q_v/\overline V_{0,v})$ 按图卡参数化（而不只是取一个点），
并据此重判 379 的情形 2。

## 设想与理由

379 的构造是"从 $U_v^\perp$ 的基里贪心补向量到 $q$ 维"——那只是 Grassmannian 里的**一个点**。
若好点集在纤维里是开的（Theorem A），一个点坏**不能**推出整条纤维坏；反之一个点好就够。
所以正确做法是：用图卡把 $m=s-\delta$ 维子空间**符号化**，算 generic gcd。

## 做法

[c359](../../../../tools/verification/c359_chart_parametrization.py)：

1. $D_v=K_0\cap U_v^\perp$、$V_0$ 模 $D_v$ 的补（$\delta$ 维）、$\mathcal Q_v/\overline V_0$ 的补（$R$ 维）；
2. $m=q-(k-1)-\delta$；若 $m=0$ 纤维是单点，$m=1$ 是 $\mathbb P^{R-1}$（符号 $t$）；
3. 行空间 $=$ 基 $+$（$m$ 个图卡行），算铅笔子式的 gcd（$t$ 为符号）。

## 进展

| 实例 | 结果 |
|---|---|
| $L_0=e_6$、$q=4$ | **$m=1$，符号 gcd $=1$** ⟹ **该纤维生成好** ⟹ **实例可行** |
| $L_0=e_6$、$q=5$ | $m=2$，本脚本未实现 |

**379 情形 2 的"未找到"是错的**：贪心构造只测了纤维里的一个点，而正确的图卡参数化显示
**整条（$\mathbb P^{R-1}$）纤维的 generic gcd 就是 1**。所以 $L_0=e_6$、$q=4$ 的实例是**可行**的。

## 最终结论

1. **图卡参数化是必需的**：只测一个点会漏（379 的教训）。
2. 带预设行时：$\delta=\dim V_0-\dim(V_0\cap K_0)$（本例 $\delta=0$，因为 $e_6\in K_0$），
   $m=q-k+1-\delta$；$m\le1$ 已实现。
3. 379 的 NO 证书（情形 1，$L_0$ 全 1 行）不受影响——那是方向筛，与纤维无关。

## 放弃原因

- $m\ge2$ 的图卡未实现（需要 $m\times(R-m)$ 个符号参数）；
- 只处理有理特征值；
- 没有把 $L_0\neq0$ 接入主判定器（仍是独立脚本）。

## 残留价值

- **一个正确的带 $L_0$ 判定路径**（$m\le1$），并纠正了 379 的错误结论；
- 明确了 $\delta$ 在实际实例里的计算（本例 $\delta=0$）。

## 相关文件

- [attempts/379](379_prescribed_row_implementation.md)（被纠正）
- [attempts/378](378_parameterization_with_L0.md)（定理）
- [attempts/377](../../decision_algorithms/attempts/377_expert103_audit.md)（103 号要求）
- [c359](../../../../tools/verification/c359_chart_parametrization.py)

## 状态

- 图卡参数化（$m\le1$）：**[可用]**。
- $L_0=e_6,q=4$ 可行：**[精确验证]**（符号 gcd = 1）。
- $m\ge2$ / 数域：**[未做]**。
