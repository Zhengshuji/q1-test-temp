# 被反驳：S1 判据的"充要"形式（$\dim K\ge\rho$）

> 反驳日期：2026-10-28 深夜。证书：[counterexample_s1.json](../rho1_layer/counterexample_s1.json)（可直接复核）。

## 被反驳的陈述

> **命题（曾被写成定理 24.3 / 25.3 / 26.2）** 设 $c\ge\rho-1$、$\rho\ge2$、$\dim B\ge\rho-1$，记
> $K=\{b\in B:T(b)\in B\}$、$U_0=\pi(\operatorname{row}L_0)$。则第 $(\rho,c)$ 层可行
> $\iff\dim K\ge\rho$ 且 $U_0\subseteq K$。

## 反例（精确、可复核）

$n=4$、$\rho=2$、$c=1$、$j=\dim\mathcal J=2$，$A,C,L_0$ 与解 $L$ 见证书。

| 量 | 值 |
|---|---|
| $(5a)$ | **True** ✓ |
| $(5b)$ | **True** ✓ |
| $c=\dim(\operatorname{row}L\cap\mathcal J)$ | $1=\rho-1$ ✓（层号对得上）|
| $\dim K$ | **0** ✗（判据说必须 $\ge2$）|

$$\Longrightarrow\ \text{判据为假而层可行}\ \Rightarrow\ \textbf{充分性之外的方向是错的}$$

复核命令：见 [verify_s1_real.py](../rho1_layer/verify_s1_real.py)（运行即写出证书），
或独立复核：读证书 → `AI.cond_5a_orig` / `AI.cond_5b_orig` / 交集维数 ✓（已跑过：True, True, 1 ✓）。

## 错在哪（诊断）

1. **定理 22.1 只给充分方向**：$\mu=\dim(B\cap\mathcal U)> \nu=\dim(B\cap W_0)$ 且 $\rho\ge2$ $\Rightarrow$ $\dim\mathrm{Bad}<\dim\mathcal A$ $\Rightarrow$ 可行 ✓。这一步没问题。
2. **反方向（$\mu=\nu\Rightarrow$ 不可行）是错的**：它假设"每个非空的 $\mathrm{Bad}_\lambda$ 都等于 $\mathcal A$"。但 $\mathrm{Bad}_\lambda=\mathcal A$ 需要"条件完全真空"，
   即 $\{\beta(\tau_i)\in\lambda u_i-\widetilde T(u_i)+W_0\}$ 对整个 $\mathcal A$ 都成立；一般只在 $\lambda$ 的一个值上成立 ✗。
   于是 $\mathrm{Bad}$ 是**一参数族的仿射子集的并**，它可能既不空也不满 ⟹ 存在可行的 $\tau$ ✓（反例正是这种情形）。
3. **引理 25.1（单调性）本身没错**，但它只说明"取大 $\beta(\mathcal H)$ 不劣"，不排除"$\nu<\rho-1$ 时可行" ⟹ 不能用它推出充要 ✗。

## 幸存的部分（仍然成立、可引用）

| 结论 | 状态 |
|---|---|
| $\dim(B\cap\mathcal U)\ge\rho\ \Rightarrow$ 该 $(\mathcal U,\mathcal H)$ 可行（$\rho\ge2$）| [已证] 定理 22.1 |
| 单调性：$\beta(\mathcal H_1)\subseteq\beta(\mathcal H_2)$ 时 $\mathcal H_2$ 可行 $\Leftarrow$ $\mathcal H_1$ 可行 | [已证] 引理 25.1 |
| $W_0=B\cap\mathcal U\Rightarrow V=B$；$\Lambda(\mathcal U)$ 与基无关 | [已证] 推论 23.6/23.7 |
| $(5a)$ 的商形式 $T(\mathcal U)\subseteq\mathcal U$ | [已证] [docs/02 A.0](../../docs/02_theorems_proven.md) |
| "$\dim K\ge\rho$ 且 $U_0\subseteq K$"是**充分**条件 | [已证] 由上两条 |

## 教训

- 维数计数只能给**单向**结论；把"$\dim\mathrm{Bad}<\dim\mathcal A$"的**逆否**当成充要，是这次错误的根源 ✗；
- 反例只用**精确算术 + 项目自己的可信判据**就抓到了 ⟹ 说明"先用真实实例跑一遍"比继续写推导更有效 ✓
  （这条应写进 CLAUDE §10.2）。