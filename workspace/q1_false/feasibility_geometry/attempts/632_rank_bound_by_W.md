# 632 猜想：可行 $\Rightarrow\ \operatorname{rank}H\le\dim\operatorname{row}(W)$

> **已推翻（638）**：存在 $\omega=2>s=1$ 的可行 q1 实例（具体 $n=6$ 实例，sympy 验证 (5a)(5b)）。本猜想不成立。
> 2026-11-27。继续 630/631，分析 $W$ 行空间为真子空间 $S$（$\dim S=s<k$）的情形。
> 状态：**[M2 猜想]**（有启发式论证与一个特例证明）。

## 设定

$H_A=HZ'+G$，$G$ 的行在 $S=\operatorname{row}(W)$ 内。$\omega=\operatorname{rank}H$。

## 特例证明：$H$ 取 $Z'$ 的左特征向量

设 $H$ 的每一行都是 $Z'$ 的、特征值 $\lambda_0$ 的左特征向量（即 $H Z'=\lambda_0 H$）。则
$$P(\lambda)=\lambda H-H_A=(\lambda-\lambda_0)H-G .$$
在 $\lambda=\lambda_0$：$P(\lambda_0)=-G$，其行都在 $S$ 内 ⇒ $\operatorname{rank}P(\lambda_0)\le\dim S=s$。
$(5b)$ 要求 $\operatorname{rank}P=\omega$，故
$$\omega\le s .$$
即在这个构造里，$W$ 的行空间维数给出秩上界。

## 猜想

对任意 $H$（不限于左特征向量），只要 $G$ 的行在 $S$ 内且 $(5b)$ 成立，就有
$$\boxed{\operatorname{rank}H\le\dim\operatorname{row}(W)}.$$

## 支持

- $W=0$（$s=0$）：629 证明只有 $\omega=0$，吻合；
- $W$ 满行秩（$s=k$）：631 构造出 $\omega=q-1\le k$ 的可行解，吻合；
- 左特征向量特例：已证；
- 直觉：$G$ 是唯一能“救”铅笔的项，但它的行被限制在 $S$ 内；在 $H(\lambda I-Z')$ 掉秩的谱点，需要 $G$ 提供 $k-s$ 个额外方向，而 $G$ 最多给 $s$ 维。

## 若猜想成立

- 可行 $\Rightarrow\omega\le s$；而 $\omega=\operatorname{rank}H\ge\operatorname{rank}H_0$；
- 于是 $s<\operatorname{rank}H_0$ ⇒ 不可行——**数据依赖的不可行**，这是 q1_true 的唯一入口；
- 也给出 $q_{\min}$ 的下界：$q\ge$ 使 $\omega\le s$ 且 $H_0$ 可扩展的最小 $q$。

## 下一步

1. 用随机数值实例检验：固定 $s$，搜索是否存在 $\omega>s$ 的可行 $H$；
2. 尝试证明一般情形（对 $P(\lambda)$ 在谱点做秩的维数计数）；
3. 与 629/631 合并为 q1 的分情形定理。

## 状态

- 特例：**[已证-纸面]**；
- 一般情形：**[M2 猜想]**。
