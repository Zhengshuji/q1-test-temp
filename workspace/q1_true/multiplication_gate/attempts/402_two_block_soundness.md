# 364 两块、$m=2$ 的直和 **soundness 成立**（手算证明）

> 承接 363（匹配攻击未排除）。本文件在两块、每个块一条自由行的情形下**证明**匹配攻击不可能。
> 这与 c363 的 50 组取样一致，但现在有证明。

## 目标

对"两块直和、块 1 的 $x_1=0$"这一情形，证明**直和不可行**。
若成立，则两块 AND 组合是 sound 的（至少对 303C 门、$m=2$）。

## 设想与理由

$x_1=0$ 时 $A_1N_1=0$，故块 1 的 $H_A$ 列恒为零。唯一的逃生是"匹配"：
让块 4 的 $H_A$ 列空间覆盖块 1 的 $H$ 列，使 $\lambda=0$ 的秩条件仍满足。
那就把矩阵写出来，看铅笔条件能不能同时满足。

## 做法：显式矩阵

两块、$m=2$ 时 $L=[L_0;R]$ 有 3 行，$N=\operatorname{diag}(N_1,N_2)$ 有 2 列（每块 1 列）。
$N_1=e_1$、$N_2=e_4$，故

$$H=L N=\begin{pmatrix}1&1\\ a&b\\ c&d\end{pmatrix},\qquad
H_A=L A N=\begin{pmatrix}0&0\\ 0&e\\ 0&f\end{pmatrix},$$

其中 $a=R_{11},b=R_{14},c=R_{21},d=R_{24},e=R_{15},f=R_{25}$（块 1 的 $H_A$ 列全零，因为 $A_1N_1=0$）。

**第一步：$\omega$ 只能是 1.** $\operatorname{rank}H_A\le1$（只有一个非零列），而 $(5b)$ 在 $\lambda=0$ 给
$\operatorname{rank}H=\operatorname{rank}H_A\le1$。又 $H$ 的第一列 $=(1,a,c)\ne0$（锚定），故 $\omega=1$。

**第二步：$\operatorname{rank}H=1$ 迫使两列成比例**：
$$(1,a,c)\ \parallel\ (1,b,d)\quad\Longrightarrow\quad a=b,\ c=d .$$

**第三步：$(5b)$ 在 $\lambda\ne0$ 迫使 $e=f=0$.** 
$$P(\lambda)=\Bigl(\lambda(1,a,c)\ \Bigm|\ \bigl(\lambda,\ \lambda b-e,\ \lambda d-f\bigr)\Bigr).$$
两列的第一分量都是 $\lambda\ne0$，故比例系数必须是 $1$，于是
$$\lambda b-e=\lambda a,\qquad \lambda d-f=\lambda c\quad(\forall\lambda\ne0).$$
由第一步 $a=b$、$c=d$，得 $e=f=0$。

**第四步：矛盾.** $e=f=0$ 时 $P(0)$ 的两列都是零，$\operatorname{rank}P(0)=0<1=\omega$，违反 $(5b)$。$\square$

## 进展

- **两块、$m=2$ 的直和 sound**（对 303C 门），已证；
- **穷举复核**：在 $(a,b,c,d,e,f)\in\{-2,\dots,2\}^6$ 上，满足 $\operatorname{rank}H=1$、$\operatorname{rank}H_A=1$ 的
  **600 个情形全部不可行** ✓（与证明一致）；
- 这与 363 的取样实验一致（50 组无违反），但现在是**证明 + 穷举**；
- 证明的支点与 363 相同：**锚定**（第一列 $=(1,a,c)\ne0$）+ **$\lambda=0$ 的秩条件**。

### 顺带修掉一个判据 bug（重要）

穷举的第一版给出"600/600 可行"——那是**判据错了**，不是证明错了。$(5b)$ 是
$$\operatorname{rank}P(\lambda)=\omega\ \ \forall\lambda,$$
它包含**两个**条件：

1. $\operatorname{rank}P(\lambda)\le\omega$ **恒成立** $\iff$ 所有 $(\omega+1)$-子式**恒零**；
2. $\operatorname{rank}P(\lambda)\ge\omega$ 对每个 $\lambda$ $\iff$ $\omega$-子式**无公共根**。

我原来的脚本只查了 2（$\gcd=1$），漏了 1。在 $3\times2$ 铅笔、$\omega=1$ 时这一个漏检会让**秩 2** 的点被误判为可行。

**对既有结果的影响**：362/363 的两块/三块实验里，铅笔是 $3\times2$ 或 $4\times3$ 且 $\omega$ 恰等于列数，
故 $\operatorname{rank}\le\omega$ **由形状自动成立**，结论不受影响 ✓。
但工具已修正（[c362](../../../../tools/verification/c362_and_composition.m)、
[c363](../../../../tools/verification/c363_direct_sum_soundness.m) 的 `symbolic_good` 现在先验 $(\omega+1)$-子式恒零），
修正后重跑两脚本，结果不变。

## 最终结论

1. 两块 AND 组合在这个情形下**是 sound 的**；
2. 关键结构：$\lambda=0$ 把 $\omega$ 压到 $H_A$ 的秩以下，而锚定保证 $H$ 的列非零 ⟹ 不匹配；
3. 顺带修正了两条工具的可行性判据（漏了秩上界那一半）；
4. 一般 $k$ 块、$m>2$ 的情形**未证**（下一步）。

## 放弃原因

- 只证了 $k=2$、$m=2$；
- $k\ge3$ 时 $H_A$ 有 $k-1$ 个非零列、$\omega$ 可以更大，匹配的自由度更大，上面的"比例系数必须为 1"不再直接适用；
- 没有考虑 $m>2$（多一条自由行可能带来额外的匹配自由度）。

## 残留价值

- **一条短的 soundness 证明**（两块），可作为一般情形的模板；
- 明确了证明的两个支点（锚定 + $\lambda=0$），下一步只需把它们推广到 $k$ 块。

## 下一步

对 $k$ 块尝试同样的写法：把 $H$、$H_A$ 写成块列，用 $\lambda=0$ 定 $\omega$，
再用 $\lambda\ne0$ 的比例条件逼出"被关块的 $H_A$ 列必须为零"的矛盾。

## 相关文件

- [363](401_and_soundness.md)（问题的提出与关块攻击）
- [362](400_and_composition.md)（AND 组合的实验）
- [361](../../../q1_false/c_stratification/attempts/399_relation_gadgets_impossible.md)（架构诊断）
- [c363](../../../../tools/verification/c363_direct_sum_soundness.m)

## 状态

- 两块 soundness：**[已证-纸面]**（四步）。
- $k\ge3$ 或 $m>2$：**[未证]**。
