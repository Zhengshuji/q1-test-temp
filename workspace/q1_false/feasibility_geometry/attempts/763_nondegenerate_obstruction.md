# 763 非退化 $(5a)$ 例：$n=4,k=2$ 不可能，需更大规模

> 2026-11-27。按 ChatGPT 的优先级（先构造非退化 $(5a)$ 例子），先证明 $n=4,k=2,q=3$ 时秩亏不可能，再派子 agent 搜索更大规模。
> 状态：**[已证-纸面]**（不可能性）+ **[搜索中]**。

## ChatGPT 的优先级

1. 非退化 $(5a)$ 例子（$W_{\mathrm{top}}\ne0$、$\operatorname{rank}[L;CA;C]<n$、完整 $(5a)(5b)$）；
2. Lean 化 $(\star)$（低风险，独立通用引理）；
3. B：先形式化 Bézout 恒等式（$\exists x,\exists u$ 使 $\sum u_jf_j=1$），再谈 PIT；
4. 不要跳过非退化例子直接做 PIT。

## 不可能性命题（$n=4,k=2,q=3$）

设 $K_0=\ker[C;CA]=\operatorname{im}N$（$\dim K_0=2$，故 $\operatorname{rank}[C;CA]=2$）、$H$ 为 $3\times2$ 行满秩、$L=[H|M]$（$3\times4$，$\operatorname{rank}L=3$）。
若 $\operatorname{rank}[L;CA;C]<4$，则 $C,CA\in\operatorname{row}L$。

但 $K_0=\operatorname{im}N$ 给 $C e_1=C e_2=0$、$CA e_1=CA e_2=0$，即 $C,CA$ 的前两个坐标为零，故
$$C,CA\in \operatorname{row}L\cap(\{0\}\times\mathbb C^2).$$
而 $\operatorname{row}L$ 投影到前两坐标满秩 2，$\dim\operatorname{row}L=3$，故该交的维数为 $3-2=1$。
于是 $CA=\lambda C$，$\operatorname{rank}[C;CA]=1<2$，与 $\dim K_0=2$ 矛盾。$\square$

**结论**：$n=4,k=2,q=3$ 时不存在非退化的 $(5a)$ 例子；需要 $n\ge5$ 或更大的 $k/q$。

## 下一步

已派子 agent `nondeg-5a` 在 $n\in\{5,6\}$、$k\in\{2,3\}$、$q\in\{k,k+1\}$ 上反向搜索：
先选 $A,C$ 使 $\operatorname{rank}[C;CA]=n-k$、$K_0=\operatorname{im}N$，再取 $W_{\mathrm{top}}\ne0$、$Z'$，按 761 构造 $L,Z$ 并验证原始 $(5a)(5b)$ 与 $\operatorname{rank}[L;CA;C]<n$。

## 状态

- 不可能性：**[已证-纸面]**（$n=4,k=2,q=3$）；
- 更大规模搜索：**[进行中]**；
- Lean $(\star)$：**[待做]**。
