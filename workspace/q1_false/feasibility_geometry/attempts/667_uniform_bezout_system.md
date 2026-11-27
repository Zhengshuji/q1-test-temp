# 667 Theorem U 的完整证明与统一 Bézout 系统

> 2026-11-27。把 666 的 Theorem U 写成完整纸面证明，并给出“设计变量 $U$ + Bézout 辅助变量”的统一代数系统与规模/次数界。
> 状态：**[已证-纸面]**。

## Theorem U（重述）

$P(\lambda)=\lambda H-H_A\in\mathbb C[\lambda]^{m\times n}$，$1\le d\le\min(m,n)$。以下等价：

1. $\operatorname{rank}P(\lambda)=d\ \forall\lambda\in\mathbb C$；
2. 所有 $(d+1)$ 阶子式恒为零，且所有 $d$ 阶子式的 gcd 为 1；
3. 所有 $(d+1)$ 阶子式恒零，且存在 $g_I$ 使 $\sum_I g_I\Delta_I=1$；
4. normal rank 为 $d$，且非零 Smith 不变因子全为 1。

## 证明

**(1)⇒(2)**：秩 $\le d$ ⇒ 所有 $(d+1)$-子式为零（恒等，因对每个 $\lambda$ 成立）。
秩 $\ge d$ 处处 ⇒ 不存在 $\lambda_0$ 使所有 $d$-子式同时为零 ⇒ 这些多项式无公共复根 ⇒ gcd=1（$\mathbb C[\lambda]$ 是 PID；公共根 ⇔ 非常数公因子）。

**(2)⇒(1)**：$(d+1)$-子式恒零 ⇒ 秩 $\le d$；gcd=1 ⇒ 无公共复根 ⇒ 每个 $\lambda$ 至少一个 $d$-子式非零 ⇒ 秩 $\ge d$。

**(2)⇔(3)**：$\mathbb C[\lambda]$ 是 PID，gcd=1 ⇔ 理想为 $(1)$ ⇔ 存在 Bézout 组合。

**(2)⇔(4)**：Smith 形 $S=\operatorname{diag}(s_1,\dots,s_d,0,\dots)$；$d$-阶最大子式的 gcd 等于 $s_1\cdots s_d$（差单位）；其为 1 ⇔ 所有 $s_i$ 为单位。normal rank 为 $d$ ⇔ 秩 $d$ 在一般 $\lambda$ 成立（等价于 $(d+1)$-子式恒零且某个 $d$-子式非零）。$\square$

## 统一 Bézout 系统

设 $f_1,\dots,f_m$ 为全部 $d$ 阶子式，$\deg f_i\le d$（$P$ 是一次铅笔 ⇒ $d$-子式的 $\lambda$ 次数 $\le d$）。
取 $g_i=\sum_{k=0}^{d-1}g_{i,k}\lambda^k$（若 gcd=1，Bézout 系数可取 $\deg<d$）。比较
$$\sum_i g_i(\lambda) f_i(\lambda)=1$$
的 $\lambda^0,\dots,\lambda^{2d-1}$ 系数，得线性系统
$$M(H)\,\mathbf g=e_0,\qquad M(H)\in\mathbb C^{2d\times md},\quad e_0=(1,0,\dots,0)^{\mathsf T}.$$
于是
$$\boxed{(5b)\iff \operatorname{rank}\big[M(H)\mid e_0\big]=\operatorname{rank}M(H).}$$

**次数**：$f_i$ 的 $\lambda^k$ 系数是 $H$ 的 $d$ 阶子式在“$k$ 行取 $\lambda H$、其余取 $-H_A$”下的和，关于自由变量 $R$ 的次数 $\le k$（$H$ 线性于 $R$）。故 $M$ 的条目关于 $R$ 的次数 $\le d$。

## 统一的可行性系统

$$\exists H:\quad
\underbrace{\big[(d+1)\text{-子式}\equiv0\big]}_{\text{多项式方程，次数}\le d+1}
\ \wedge\
\underbrace{\operatorname{rank}[M(H)\mid e_0]=\operatorname{rank}M(H)}_{\text{行列式条件}} .$$
再加上 $(5a)$ 的行空间约束与固定行 $H_0$。这是**与 $d$ 无关的统一形式**：没有逐 $d$ 的分类，只有 $H$ 的多项式/行列式条件。

## 验证

- 638（可行）：$H=\operatorname{diag}(1,1,0)$、$Z$ 循环；$P$ 的非零 2-子式 $\lambda^2,-\lambda,1$，gcd=1 ✓；
- 641B（不可行）：gcd $=\lambda(\lambda-1)$ ✓；
- 661：$d=2=q$，唯一 2-子式为 $\det P=\det(\lambda I_2-Z)\det H$，非常数 ⇒ 不可行 ✓。

## 关键认识

- 统一判据把“秩 $d$”消成了**最大子式理想**；$d$ 只影响矩阵尺寸 $md\times 2d$ 与次数界，不需要新的引理；
- 真正的困难完全转移到“$\exists H$ 使 $M(H)$ 的秩条件成立”——$M$ 的条目与辅助变量 $\mathbf g$ 相乘（$M\mathbf g=e_0$），对 $\mathbf g$ 线性、对 $R$ 多项式；
- 下一步应研究这个统一的“行列式 + 多项式”系统的消元结构（而不是再分 $d$）。

## 状态

- Theorem U：**[已证-纸面]**；
- Bézout 系统与次数界：**[已证-纸面]**；
- 638/641B/661 验证：**[精确验证]**；
- 统一系统的消元/复杂度：**[未做]**。
