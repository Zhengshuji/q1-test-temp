# 651 定理：$T_\infty$ 零化与秩界（比 $K_\infty$ 更强）

> 2026-11-27。按 ChatGPT 的建议，把“沿 $S^\perp$ 内轨道前向传播”的零空间闭包形式化。
> 状态：**[已证-纸面]**。

## 定义

$K=S^\perp$。$T_0=K_\infty$（639），
$$T_{j+1}=T_j+Z'\,(T_j\cap K).$$
有限维 ⇒ 序列稳定，记 $T_\infty$。

## 定理

若 $(5a)(5b)$ 成立，则
$$\boxed{H|_{T_\infty}=0,\qquad \omega=\operatorname{rank}H\le k-\dim T_\infty,}$$
从而固定行满足
$$\boxed{H_0|_{T_\infty}=0,\qquad \operatorname{rank}H_0\le k-\dim T_\infty .}$$

## 证明

对 $j$ 归纳证明 $H|_{T_j}=0$：

- $j=0$：639（$H|_{K_\infty}=0$）；
- 设 $H|_{T_j}=0$。取 $x=a+Z'y$，$a\in T_j$、$y\in T_j\cap K$。
  $Ha=0$；又 $y\in K$ ⇒ $Gy=0$（$G$ 行在 $S$ 内）⇒ $ZHy=HZ'y$。
  由 $Hy=0$ 得 $HZ'y=0$，故 $Hx=0$。✓

于是 $T_\infty\subseteq\ker H$，$\operatorname{rank}H\le k-\dim T_\infty$。

## 检验

| 实例 | $K$ | $K_\infty$ | $T_\infty$ | 界 $\omega\le$ | 已知 |
|---|---|---|---|---|---|
| 629（$S=0$） | $\mathbb C^k$ | $\mathbb C^k$ | $\mathbb C^k$ | 0 | ✓ |
| 631（$S=\mathbb C^k$） | 0 | 0 | 0 | $k$ | ✓ |
| 638（$S=e_2$） | $\operatorname{span}\{e_1,e_3\}$ | $\operatorname{span}\{e_3\}$ | $\operatorname{span}\{e_3\}$ | 2 | ✓ 达到 |
| 648/650（$S=e_1$，$Z'$ 循环） | $\operatorname{span}\{e_2,e_3\}$ | $\operatorname{span}\{e_3\}$ | $\mathbb C^3$ | 0 | ✓（$H_0\ne0$ 不可行；$H_0=0$ 时 $\omega=0$ 可行） |

650 的 $T_\infty=\mathbb C^3$ 精确解释了“$H_0=e_1^{\mathsf T}$ 必矛盾”：任何可行 $H$ 必须为零。

## 猜想（充分性）

$$\text{可行}\iff H_0|_{T_\infty}=0\ \wedge\ \operatorname{rank}H_0\le k-\dim T_\infty\ \wedge\ (q\ \text{足够}).$$

- 已知：629、631、638、648/650 全部吻合；
- 待证：$H_0\ne0$ 且满足条件时，总能构造出满足铅笔条件的扩展。

## 下一步

1. 对 $T_\infty$ 给定、$H_0$ 非零且满足条件的小族做构造/穷举，寻找反例；
2. 若找不到，尝试证明充分性（用商空间 $C^k/T_\infty$ 上的构造，类似 631 的 $Z$ 选择）；
3. 与 ChatGPT 核对 $T_\infty$ 的充分性思路。

## 状态

- 定理：**[已证-纸面]**；
- 充分性：**[M2 猜想]**。
