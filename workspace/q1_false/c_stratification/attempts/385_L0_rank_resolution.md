# 385 $L_0$ 秩问题的解决：它是问题定义隐含的必要条件；并补满秩引理

> 承接 384（105 号审计：$L_0$ 的秩是硬错误、缺满秩首项系数引理）。本轮两件都落实。

## 目标

1. 决定 Route A 还是 Route B（$L_0$ 的秩）。
2. 把"满秩首项系数引理"写成正式陈述（含证明）。

## 设想与理由

105 号说：$\dim V\le t_0+(q-r_0)$，$t_0=\operatorname{rank}L_0$，所以除非 $t_0=r_0$，行空间达不到 $q$ 维。

**但原问题的定义就要求 $\mathcal L=\binom{L_0}{R}$ 是 $q$ 行、行满秩**（见 `docs/00_problem.md` §0.1）。
于是

$$q=\operatorname{rank}\mathcal L\le t_0+(q-r_0)\ \Longrightarrow\ t_0\ge r_0\ \Longrightarrow\ t_0=r_0 .$$

即：**$\operatorname{rank}L_0=r_0$ 是可行性的必要条件**；若违反，任何 $q$ 都不可行（连一个合法设计都不存在）。
所以这是**前置检查**，不是需要额外假设的定理前提——**Route A 由问题定义自动成立**。

## 做法

### 前置检查（新增，零成本）

> **命题 0.** 若 $\operatorname{rank}L_0<r_0$，则对**任意** $q$ 都不存在行满秩的 $\mathcal L=[L_0;R]$，
> 故该实例不可行。

这就是问题的平凡前筛，与层无关。

### 引理 7′（全行秩归一化，专家的展开证明）

> **引理 7′.** 设 $L_0$ 行满秩、$V_0\subseteq V\subseteq U_v^\perp$、$\dim V=t<q$ 且 $q\le\dim U_v^\perp$。
> 则存在 $q$ 维的 $V'\supseteq V$（在 $U_v^\perp$ 内）使 $(5a)$ 与 $(5b)$ 保持。
>
> *证明.* 取 $V\subseteq V'\subseteq U_v^\perp$、$\dim V'=q$。$V'\supseteq D_v$ 且 $V'\subseteq U_v^\perp$
> ⟹ $V'\cap K_0=D_v$（$\dim=k-1$）⟹ $\operatorname{rank}H'=\omega$ ✓；
> 每行 $x\in V'$ 消去 $v,Av$ ⟹ $xN,xAN\in a^\circ$（$v=Na$）⟹ $\operatorname{row}H'\subseteq a^\circ$ 且
> $\operatorname{row}H'_A\subseteq a^\circ$ ⟹ $(5a)$ ✓。
> 铅笔是"加行"，秩不会下降；而结构包含给出上界 $\omega$ ⟹ 秩恒为 $\omega$ ⟹ $(5b)$ 保持。$\square$

### 满秩首项系数引理（专家的证明）

> **引理 8.** 设参数图表上 $\operatorname{rank}H\equiv\omega$。则每个参数点处至少有一个极大子式的 $\lambda$-次数**恰为 $\omega$**。
> 于是：若 $K(X)[\lambda]$ 上的 gcd 次数**为正**，则每个特化点都含非平凡公因子 ⟹ 整图卡全坏。
>
> *证明.* 去掉内容后的非常数公因子 $g\in K[X,\lambda]$ 整除每个 $m_I$。若在某点 $g(X_0,\cdot)$ 为**非零常数**，
> 则每个 $m_I(X_0,\cdot)$ 的次数 $<\omega$，与"某子式次数恰为 $\omega$"矛盾；
> 若 $g(X_0,\cdot)\equiv0$，则所有子式恒零，同样矛盾。$\square$

**为什么必须有它**：对一般族，"generic gcd 正次数 ⟹ 处处有公因子"是**假**的
（$X\lambda+1$ 的 gcd 是 $X\lambda+1$，在 $X=0$ 退化为常数 1）。真正起作用的是 $\operatorname{rank}H=\omega$ 这个不变量。

## 进展

1. **$L_0$ 秩问题解决**：由问题定义的前置检查（Proposition 0）自动满足 Route A，不需要改 $q$ 或 $s$。
2. **引理 7′** 按专家要求展开（加行不降秩 + 结构上界）。
3. **引理 8**（满秩首项系数）写成正式陈述，并说明它是"generic gcd 正次数 ⟹ 整图卡坏"的**唯一**理由。

## 最终结论

1. Route A 成立（**由问题定义**，非额外假设）；Route B 不需要。
2. 新增前置检查：$\operatorname{rank}L_0<r_0$ ⟹ 不可行（平凡）。
3. 满秩引理补上后，"逐图卡判坏"的论证闭合。

## 放弃原因

- 没有把 Proposition 0 接进实现（当前脚本假设 $L_0$ 行满秩）；
- 没有处理"$\mathcal L$ 不要求行满秩"的变体（专家 Route B 的情形）——本项目问题定义要求行满秩，故不需要。

## 残留价值

- **$L_0$ 秩问题的定论**（由问题定义而非假设）；
- 两条引理的正式陈述与证明，可直接进论文；
- 一句可写进论文的前置检查。

## 相关文件

- [attempts/384](../../decision_algorithms/attempts/384_expert105_audit.md)（105 号裁决）
- [attempts/378](378_parameterization_with_L0.md)（定理 1′，需按本轮更新更正块）
- `docs/00_problem.md` §0.1（问题定义要求行满秩）

## 状态

- $L_0$ 秩：**已解决**（前置检查 + Route A）。
- 引理 7′、8：**[已证-纸面]**。
