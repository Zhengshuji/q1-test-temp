# 族定理：$E=0,Z_1=0,Z_2=e_1$ 的 $\mathbb P^1$ 混合层

> 2026-11-08。把 attempts/104 的单例提升为**族定理**：对
> $E=0$、$Z_1=0$、$Z_2=e_1$、$V_0=(0,a,b)$（$ab\ne0$）、$d=1$、$k=3,q=3,\omega=2$，
> $q=3,\omega=2$ 层是**混合**的：开层全坏、例外点好。三个实例由
> `tools/verification/p2_stratification_check.py` 程序化核对。

## 目标

证明族定理：

> 设 $k=3$、$q=3$、$\omega=2$、$d=1$、$E=0$、$Z_1=0$、$Z_2=e_1$、$V_0=(0,a,b)\ne(0,0)$。
> 则
> (i) 可容许轨迹 $=\{\sigma:\sigma\cdot V_0=0\}\cong\mathbb P^1$；
> (ii) 对 $\sigma\ne(1,0,0)$，纤维中每个可容许点都在 $\lambda_0=0$ 处坏；
> (iii) 对 $\sigma=(1,0,0)$，纤维含好点：
> * 若 $ab\ne0$：取 $x_1=e_2,\ x_2=e_2+e_3,\ y_1=y_2=e_2$，
>   $2$-子式为 $b(\lambda-1)$、$(b-a)\lambda-b$、$\lambda(\lambda-1)$，gcd $=1$；
> * 若 $a=0$ 或 $b=0$：取 $x_1=e_2,\ x_2=e_3,\ y_1=e_3,\ y_2=e_2$，
>   $2$-子式为 $a+b\lambda$、$-a\lambda-b$、$\lambda^2-1$，gcd $=1$；
> (iv) 故 $q=3,\omega=2$ 层**混合**（对所有 $V_0\ne0$）。

## 设想与理由

* 104 的单例结构是：$E=0$ 使 $F_0\subseteq S$ 成为唯一线性条件；$Z_1=0,Z_2=e_1$ 使兼容条件退化为 $y_1=0$；
  $V_0$ 的第一坐标为 $0$ 使 $V_0$ 落在 $S\cap\{y_1=0\}$ 里。
* 这三件事只用到 $V_0=(0,a,b)$、$ab\ne0$，所以整个族都应该成立。
* 例外点的好点可以用**统一构造**：$x_1=e_2$、$x_2=e_2+e_3$、$y_1=y_2=e_2$；
  三个 $2$-子式一次算出，gcd $=1$。

## 做法

**(i) 可容许轨迹。** $E=0$，故只需 $F_0=\langle V_0\rangle\subseteq S$，即 $\sigma\cdot V_0=0$。
反之若 $\sigma\cdot V_0=0$，则 $V_0\in S$。兼容条件 $y_1=0$；对任意 $x\in S$，存在 $y\in S$ 使 $y_1=0$
（$S\cap\{y_1=0\}$ 非零：若 $S\ne\{y_1=0\}$ 是一条线，若 $S=\{y_1=0\}$ 是整个 $S$），故 $X_S=S$，
$E+X_S=S$。所以可容许 $\iff\sigma\cdot V_0=0$。

**(ii) 开层全坏。** 设 $\sigma\ne(1,0,0)$，即 $S\ne\{y_1=0\}$。则 $S\cap\{y_1=0\}$ 是 $S$ 中的线；
$V_0\in S$ 且 $(V_0)_1=0$，故 $V_0$ 在这条线里；于是 $S\cap\{y_1=0\}=\langle V_0\rangle$。
每个兼容的 $y_i$ 满足 $y_i\in S$、$(y_i)_1=0$，故 $y_i\in\langle V_0\rangle$。在 $\lambda=0$ 处
$$P(0)=-H_A=\begin{pmatrix}-V_0\\-y_1\\-y_2\end{pmatrix}$$
三行全在 $\langle V_0\rangle$ 里，秩 $\le1<2$。✓

**(iii) 例外点的好点。** $\sigma=(1,0,0)$ 时 $S=\{y_1=0\}=\langle e_2,e_3\rangle$，$V_0=(a,b)$（$S$-坐标）。

*情形 A（$ab\ne0$）*：取 $x_1=e_2,\ x_2=e_2+e_3,\ y_1=y_2=e_2$。$H$ 的行是 $0,e_2,e_2+e_3$（秩 2）；
$H_A$ 的行都在 $S$ 里，故可容许。$P(\lambda)$ 的行（$S$-坐标）为 $(-a,-b)$、$(\lambda-1,0)$、$(\lambda-1,\lambda)$，$2$-子式
$$b(\lambda-1),\qquad (b-a)\lambda-b,\qquad \lambda(\lambda-1).$$
$b\ne0$ 时第一个有根 $1$；第二个在 $\lambda=1$ 处为 $-a\ne0$、在 $\lambda=0$ 处为 $-b\ne0$；故 gcd $=1$。

*情形 B（$a=0$ 或 $b=0$）*：取 $x_1=e_2,\ x_2=e_3,\ y_1=e_3,\ y_2=e_2$。$P(\lambda)$ 的行（$S$-坐标）为
$$(-a,-b),\qquad (\lambda,-1),\qquad (-1,\lambda),$$
$2$-子式
$$a+b\lambda,\qquad -a\lambda-b,\qquad \lambda^2-1.$$
若 $a=0,b\ne0$：为 $b\lambda$、$-b$、$\lambda^2-1$，gcd $=1$（$b$ 是非零常数）。
若 $b=0,a\ne0$：为 $a$、$-a\lambda$、$\lambda^2-1$，gcd $=1$（$a$ 是非零常数）。
$(a,b)=(0,0)$ 被 $V_0\ne0$ 排除。✓

**(iv)** 由 (ii)(iii)：开层全坏、例外点好，故混合。✓

**满行秩 lifting（专家 52 号的限定）。** 以上是**压缩层面**（兼容对 $(x_i,y_i)$）的证明；要得到原问题，
需验证这些对能提升为 $R$ 且 $L=[L_0;R]$ 满行秩。兼容性只保证 $K$ 与 $AK$ 上的限制一致，**不**保证 $L$ 满行秩。
需要一条 lifting 引理：给定 $(RN_K,RAN_K)$ 的兼容规定，刻画实现它的仿射空间里是否存在 full-row-rank 的 $R$。
对本族：104 的例外点已回代出显式 $R$ 并过七条检查；开层的 lifting 仍待补。

## 进展

* 族定理 (i)–(iv) 已证（纸面，$V_0\ne0$；含 $ab=0$ 边界，用情形 B）。
* 三个实例（$V_0=(0,-1,c)$，$c=-4,1,3$）用
  `tools/verification/p2_stratification_check.py` 枚举 $\sigma$ 核对：
  * 分层 $(r_Q,r_{PQ},\dim X_S,E+X_S{=}S)$：开层 $(1,1,2,\text{True})$，例外点 $(0,0,2,\text{True})$；
  * 开层 7/7 采样全坏；例外点 1/1 好；$\dim X_S$ 公式 **0 不匹配**（三实例）。
* 三个实例满足 $ab\ne0$（情形 A）；边界 $ab=0$ 由情形 B 覆盖，实例中未出现。

## 最终结论

* **族定理成立**：$E=0,Z_1=0,Z_2=e_1,V_0=(0,a,b)\ne(0,0)$ 时，$q=3,\omega=2$ 层混合；
  开层全坏（$\lambda_0=0$），例外点好（$ab\ne0$ 用情形 A，$a=0$ 或 $b=0$ 用情形 B；gcd 均为 $1$）。
* 这把 104 的单例从"一个例子"提升为"一族例子"，并给 107/108 的投影定理一个**可证明的特例**。
* 仍未做：$d\ge2$、$k>\omega+1$、Lean、实点。

## 放弃原因

* 只处理 $d=1$；$d\ge2$ 的对应族未做。
* 没有把族定理写成 Lean（矩阵 3×3、参数 $a,b$；可行但本轮未做）。
* 程序化验证只覆盖三个实例，不是族定理的机器证明。

## 残留价值

* 一个完整的族定理 + 统一的例外点构造 + 三个实例的程序化核对。
* 给 107 的投影定理提供了"开层全坏、例外点好"的可证明模型。
* 边界情形（$ab=0$）与 $d\ge2$ 是明确的下一步。

## 相关文件

* [attempts/104](104_p2_constrained_locus.md)（单例；本文件把它提升为族）
* [attempts/107](107_projective_constrained_theorem_v2.md) / [108](108_layer_constancy.md)（投影定理与常值性）
* [tools/verification/p2_stratification_check.py](../../../../tools/verification/p2_stratification_check.py)（三实例枚举）
* [workspace/ROADMAP.md](../../../ROADMAP.md) §5

## 状态

* 族定理：**[已证-纸面，M2]**（$V_0\ne0$；含 $ab=0$ 边界；**压缩层面**）。
* 满行秩 lifting：**待补引理**（专家 52 号）；104 的例外点已回代显式 $R$ 过七条。
* 程序化核对：**[精确验证 3 实例]**（分层 + $\dim X_S$ 公式 0 不匹配 + 开层 7/7 坏 + 例外点 1/1 好）。
* 未做：lifting 引理、$d\ge2$、一般 $k$、Lean、实点。
