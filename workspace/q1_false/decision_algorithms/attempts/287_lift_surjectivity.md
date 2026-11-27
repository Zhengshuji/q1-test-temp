> **303 更正**：本文件的“$[N\ E]$ 可逆”前提仍不可能；但“任意压缩对可提升”的**结论成立**，
> 机制是 79 号的 $[N\ AN]$ 行满秩 $2k$（$n=3k$），不是 $[N\ E]$ 可逆。

> **已撤回（288）**：$N\subseteq\ker C$、$AN\subseteq\ker C$ ⇒ $[N\ E]$ 的秩 $\le n-p<n$，
> 不可能满秩。287 的“双射”前提在观测器数据下为空；281 的不可提升是结构性限制。

# 提升的充分条件：$[N\\ E]$ 可逆时任意压缩行对都可提升

> 2026-11-09。检查 281/286 的“不可提升”是否是普遍现象。
> 结论：**不是**。若 $E=(I-NN^+)AN$ 的列与 $N$ 的列一起张满 $\\mathbb C^n$
> （等价于 $[N\\ E]$ 可逆，$n=2k$ 时可能），则对任意压缩行对 $(H_i,H_{A,i})$，
> 都存在 $r_i$ 使
> $$r_iN=H_i,\\qquad r_iAN=H_{A,i}.$$
> 因此 285 的 $q=5$ 门**可以**被提升；281 的失败只是 $E$ 的秩不够。
> 状态：**M2（纸面）+ 构造计划**。

## 目标

判断 281 的“不可提升”是否普遍；给出提升的充分条件。

## 设想与理由

$AN=NM+E$。对一行 $r_i$：
$$r_iAN=r_iNM+r_iE=H_iM+r_iE.$$
给定 $H_i,H_{A,i}$，需要
$$r_iE=H_{A,i}-H_iM.$$
若 $[N\\ E]$ 可逆（$n=k+\\operatorname{rank}E$，$E$ 补足 $N$），则映射
$$r_i\\longmapsto(r_iN,r_iE)$$
是双射到 $\\mathbb C^k\\times\\mathbb C^k$；
于是对任意 $(H_i,H_{A,i})$ 都能解出 $r_i$。

## 做法：引理与推论

**引理**：设 $N\\in\\mathbb C^{n\\times k}$ 满列秩，$E\\in\\mathbb C^{n\\times k}$，
$[N\\ E]$ 是 $n\\times2k$ 且秩 $n$（特别 $n=2k$ 且可逆）。则对任意
$H_i\\in\\mathbb C^k$、$H_{A,i}\\in\\mathbb C^k$，存在 $r_i\\in\\mathbb C^n$ 使
$$r_iN=H_i,\\qquad r_i(E+N M)=H_{A,i}.$$

*证明*：$r_i(E+NM)=r_iE+H_iM$；取 $r_i$ 使 $(r_iN,r_iE)=(H_i,H_{A,i}-H_iM)$，
由 $[N\\ E]$ 可逆性存在。$\\square$

**推论**：若 $n=2k$、$E$ 的列补足 $N$，则**任意**压缩对 $(H,H_A)$ 都可逐行提升；
281 的失败只是因为该实例的 $E$ 秩不足（$n-k<k$）。

## 对 285 门的意义

285 的 $q=5$ 门：
$$H_0=[e_1;e_1],\\quad Y=[e_1;(0,0,1,x);(0,0,y,z)],\\quad \\text{门 }z=xy.$$
取 $k=4$、$n=8$、$N=e_1,\\dots,e_4$、$E$ 的列为 $e_5,\\dots,e_8$（秩4），
则 $[N\\ E]=I_8$ 可逆。于是每一行都能提升；剩下的只是：
1. 选 $A$ 使 $AN=NM+E$ 且 $C A=CA$、$L_0A\\in S$；
2. 选 $M$ 使 $(5b)$ 成立（$\\operatorname{im}H$ 避开 $M$ 的特征空间）；
3. 处理 $H_0$ 的固定行与 $L_0$ 的兼容。

## 进展

* 提升的充分条件 $[N\\ E]$ 可逆；
* 281 的失败解释为 $E$ 秩不足；
* 285 门有了明确的落地路线。

## 最终结论

* “压缩门不可提升”不是普遍障碍；$n=2k$ 且 $E$ 满秩时可提升；
* 下一步是构造满足 $AN=NM+E$、$CA$、$L_0A\\in S$ 的 $A$，并验证 $(5b)$。

## 放弃原因

* 未构造完整 $A,C,L_0$；
* 未处理 $L_0A\\in S$ 与 $AN$ 的兼容；
* 未验证 $(5b)$。

## 残留价值

* 一个关键的提升引理；
* 解释了 281 的失败；
* 为 285 门提供了落地路径。

## 相关文件

* [attempts/281](../../../q1_true/rank_gates/attempts/281_q4_gate_not_liftable.md)
* [attempts/285](../../../q1_true/rank_gates/attempts/285_q5_gate_target.md)
* [attempts/286](../../../q1_true/rank_gates/attempts/286_q5_spectral_compatibility.md)

## 状态

* 提升引理：**[M2 纸面]**。
* 完整 $A$：**[未构造]**。
