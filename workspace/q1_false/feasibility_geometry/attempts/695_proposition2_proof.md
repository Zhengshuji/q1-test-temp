# 695 命题 2 的证明：$d'\le\dim(\operatorname{row}(H(\mu I-Z'))+T)$

> 2026-11-27。证明 ChatGPT 的“强化 690”：由行空间包含关系直接得到。
> 状态：**[已证-纸面]**。

## 定理

设 $\mu\in\mathbb C$（$Z'$ 的特征值或任意值），$M=\mu I-Z'$，$P(\mu)=HM-G$，可行（$\operatorname{rank}P(\mu)=d'$）。则
$$\boxed{d'\ \le\ \operatorname{rank}(HM)+t-\dim\big(\operatorname{row}(HM)\cap T\big)
=\dim\big(\operatorname{row}(HM)+T\big).}$$

**证明**：$G$ 的每一行在 $T$，而 $HM$ 的每一行在 $V:=\operatorname{row}(HM)$，故 $P(\mu)=HM-G$ 的每一行在 $V+T$ 中。于是
$$\operatorname{rank}P(\mu)\le\dim(V+T)=\dim V+t-\dim(V\cap T).\qquad\square$$

## 推论（强化 690）

因 $\operatorname{rank}(HM)\le\operatorname{rank}M=\operatorname{rank}(\mu I-Z')$ 且 $\dim(V\cap T)\ge0$，
$$d'\le\dim(V+T)\le\operatorname{rank}(\mu I-Z')+t,$$
即 690 的 $t$-版本；本定理是它的**子空间强化**（把“$\operatorname{rank}M$”换成“$HM$ 的行空间与 $T$ 的和”）。

## 检验

| 实例 | $\mu$ | $\operatorname{rank}(HM)$ | $\dim(V\cap T)$ | $t$ | 界 | $d'$ |
|---|---|---|---|---|---|---|
| 638 | 0 | 2（$V=\operatorname{span}\{e_2,e_3\}$） | 0 | 1 | 3 | 2 ✓ |
| 693（$Z'=0$） | 0 | 0 | 0 | 1 | 1 | $\le1$ ✓（$d'=2$ 被排除） |
| 661（$q=2$，$d'=1$） | 0 | 0（$HZ'=0$） | 0 | 1 | 1 | 1 ✓ |
| 661（$q=2$，$d'=2$） | 0 | 0 | 0 | 1 | 1 | 2 ✗（被排除） |

对 661 的核算：$Z'=\begin{bmatrix}0&1\\0&0\end{bmatrix}$，$H=\begin{bmatrix}0&1\\0&0\end{bmatrix}$（$d'=1$）或秩 2；
$HZ'=0$，故 $V=0$，界 $=0+t-0=1$，只能 $d'\le1$；秩 2 被排除（与 661 的 $m=1$ 一致）。

## 意义

- 这是“方向型”预筛选的第一个精确版本：不只数 $\operatorname{rank}M$，而是看 $HM$ 的行空间能否被 $T$ 补足；
- 它把 690 从“谱条件”强化为“谱 + 子空间位置”条件；
- 与 693 的机制一致：$HM=0$ 时界退化为 $t$。

## 下一步

1. 用本定理重写预筛选（把 690 换成本定理）；
2. 研究等号 $d'=\dim(V+T)$ 的横截性条件（ChatGPT 的“命题 3”）；
3. 测试更多实例，确认它是否排除 690 排除不了的不可行实例。

## 状态

- 定理：**[已证-纸面]**；
- 检验：**[已证-纸面]**（按表）。
