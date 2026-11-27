# 635 证明尝试：为什么“单式行列式”论证不适用
> **审计注（729）**：$G=LW$ 的固定-$H$ 可达空间是 $T=\{lW:lN=0\}\subseteq S$；本文若把 $G\in S$ 当作可实现判据，需加 $T=S$ 或改用 $T$。


> 2026-11-27。尝试证明 $\omega\le s$（632 猜想）。
> 状态：**[M2 分析]**（指出一个看似可行的证明为何失败，并定位真正的障碍）。

## 看似可行的论证（以及它为何失败）

取 $L:\mathbb C^q\to\mathbb C^k$ 使 $LH$ 在 $\operatorname{im}H$ 的补上可逆；则
$$LT_\lambda=L(\lambda H-H_A)=\lambda LH-LHZ'-LG .$$
若 $LH$ 是恒等（$\omega\times\omega$），这就是单式 $\lambda I-\cdots$，必有根 ⇒ 矛盾。
但 $LH$ 只是 $H$ 在某个补空间上的逆，$LT_\lambda$ 作用在 $\mathbb C^k$ 上，**不是 $\omega\times\omega$ 方阵**；
限制到 $R$（$\dim\omega$）后像也不落在 $R$ 内。所以单式行列式论证不成立。

这正是 ChatGPT 的“$\omega=0$”结论出错的地方（633）：$(\lambda I-Z)|_V$ 不是方阵。

## 真正的障碍

$(5b)$ 等价于：$V=\operatorname{im}H$（$\dim\omega$）中**没有** $Z$ 的特征向量
（否则 $\lambda H-H_A=(\lambda I-Z)H$ 在 $V$ 上掉秩）。

而 $Z$ 受约束：
$$ZH=HZ'+G,\qquad \operatorname{row}(G)\subseteq S .$$
于是对 $v=Hx\in V$：
$$Zv=HZ'x+Gx\in V+\operatorname{im}G,\qquad \dim(V+\operatorname{im}G)\le\omega+s .$$

## 关键结构

- $G$ 的秩 $\le s$（因为 $G=C\,S_{\rm basis}^{\mathsf T}$，$C$ 是 $q\times s$）；
- 若 $Z$ 把 $V$ 映入 $V+\operatorname{im}G$ 且 $V$ 没有特征向量，则 $V$ 的像在 $\omega+s$ 维空间里；
- 当 $\omega>s$ 时 $\omega+s<2\omega$——这给出一个“挤压”，可能是 $\omega\le s$ 的来源；
- 需要把“挤压”与特征向量存在性严格连接（例如用 $Z|_V$ 的像空间维数与特征向量定理）。

## 状态

- 单式论证的失败：**[已证-纸面]**；
- $\omega\le s$：**[M2 猜想]**（634 穷举支持）；
- 证明缺口：**[未闭合]**。
