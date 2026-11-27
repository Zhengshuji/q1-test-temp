# 一般情形：定理是 $k$-无关的，枚举只是例子

> 2026-11-08。回应“不能一个 $k$ 一个 $k$ 枚举”：一般定理已经写了（attempts/113），它对**任意** $k,\omega,q$
> 成立；$k=3,4$ 的枚举只是发现机制与验证，不是理论路线。

## 目标

1. 明确：一般定理不依赖 $k$，不需要逐 $k$ 枚举；
2. 说清哪些是 $k$-无关的、哪些是 $k$-特定的；
3. 指出真正的开放问题（分量分解的复杂度），它不是“再算一个 $k$”。

## 设想与理由

* 113 的定理（lifted incidence + determinantal 分层 + 闭坏集 + 二分 + generic gcd）对 $k$ 没有任何限制；
  $k$ 只改变矩阵尺寸、$\operatorname{Gr}(\omega,k)$ 的维数和分层数。
* 逐 $k$ 的枚举只能给例子/反例/机制，不能替代一般定理；而一般定理已经在那里。
* 真正 $k$-特定的是**分量分解**：把 rank 层拆成不可约分量，这是 determinantal variety 的标准问题
  （Bruns–Vetter；Fulton），方法是统一的，不是逐 $k$ 枚举。

## 做法

**一般定理（113，任意 $k,\omega,q$）**：令
$$\mathcal I=\{(\sigma,R):\ \operatorname{row}(L_0N)\subseteq S,\ \operatorname{row}(L_0AN)\subseteq S,\ 
\operatorname{row}(RN)\subseteq S,\ \operatorname{row}(RAN)\subseteq S,\ 
\operatorname{row}(L_0N;RN)=S,\ \operatorname{rank}[L_0;R]=q\}.$$
它是局部闭代数集；按
$$\big(\operatorname{rank}Q,\ \operatorname{rank}[P;Q],\ \operatorname{rank}(\varphi_S|_{\widetilde E_S}),\ \operatorname{rank}H\big)$$
分成有限个局部闭的 determinantal 层。每个不可约分量上，坏集
$\{(\sigma,R):\exists\lambda,\operatorname{rank}(\lambda H-H_A)<\omega\}$ 闭；
要么全坏、要么好点 Zariski 开稠密；由 $\mathbb C(X)$ 上的 generic gcd 判定。

**$k$-特定的部分**：分量分解（determinantal variety）与具体例子（$k=3$ 的纤维跳变、$k=3,e=1$ 的
$V_0Z_2$ 现象、$k>3$ 的 $Y$ 原像）。这些是发现机制的例子，不是一般定理本身。

**一般“全坏”判据**：精确判据是分量上的 generic gcd；手算的充分条件是找 $\lambda_0$ 与子空间 $Y$，
$\dim Y<\omega$，使 $\lambda_0H-H_A$ 的所有行都在 $Y$ 里。例如 $\lambda_0=0$ 时
$Y=\{y:yZ_2\in\operatorname{row}Z_1\}$（118 的定理：交集 $0\Rightarrow\dim Y=\omega-1$）。
没有闭式的一般全坏判据；精确判据就是 generic gcd。

## 进展

* 一般定理已写（113），对任意 $k,\omega,q$ 成立。
* $k=3$ 的例子（112/116/117）与 $k>3$ 的充分定理（118）都落在这个框架里。
* **开放**：分量分解与每分量 gcd 的**复杂度**（这正是 $q1$）；没有多项式算法。

## 最终结论

* 一般理论不需要逐 $k$ 枚举；113 就是一般定理。
* 逐 $k$ 的工作只用于：发现机制、构造例子/反例、验证一般定理。
* 真正的开放问题是分量分解与 gcd 的复杂度，不是“再多算一个 $k$”。

## 放弃原因

* 没有给出分量分解的一般算法（只有存在性与 determinantal 结构）。
* 没有把 113 的定理写成可执行的算法；复杂度仍是 $q1$。

## 残留价值

* 把“一般定理 / 例子 / 开放问题”的分工写清，避免继续把枚举当理论。
* 指出后续应攻分量分解的复杂度，而不是扩大 $k$。
* 为论文的“一般定理 + 例子”结构提供依据。

## 相关文件

* [attempts/113](../../decision_algorithms/attempts/113_projective_theorem_corrected.md)（一般定理）
* [attempts/118](118_k_omega_plus_1_d2_attempt.md)（$k>3$ 的充分全坏定理）
* [attempts/112](112_incidence_table.md)（$k=3$ 例子）
* [attempts/115](115_k3_component_decomposition.md)（determinantal 框架、线性性撤回）

## 状态

* 一般定理：**[草稿，M2]**（113；结构部分依赖 B.24）。
* $k$-特定例子：**[精确验证]**（112/116）。
* 开放：分量分解与 gcd 的复杂度（$q1$）。
