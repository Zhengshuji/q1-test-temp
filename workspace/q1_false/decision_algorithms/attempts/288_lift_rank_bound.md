> **303 更正**：秩界 $\operatorname{rank}[N\ AN]\le n-p$ 正确；但“永不满射”是**错误靶空间**。
> 映射 $R\mapsto(RN,RAN)$ 的靶空间是 $2k$ 维，不是 $n$；79 号的 $3k$ 构造中秩 $2k$，满射。

# 287 撤回：$[N\ E]$ 不可能满秩，提升永远受 $\\ker C$ 限制

> 2026-11-09。287 的“$[N\ E]$ 可逆 ⇒ 任意压缩行对可提升”在观测器数据下**不可实现**：
> $$N\\subseteq\\ker C,\\qquad AN\\subseteq\\ker C,$$
> 所以 $[N\\ AN]$ 的秩 $\\le n-p$，映射 $R\\mapsto(RN,RAN)$ 永远不是满射。
> 287 的充分条件因此是空条件；281 的不可提升不是“秩不足”的偶然，而是 $\\ker C$ 的结构限制。
> 状态：**撤回（M3 自查）**。

## 目标

更正 287 的提升引理，给出正确的秩上界。

## 设想与理由

287 的 $[N\ E]$ 满秩要求与 $N,AN\subseteq\ker C$ 冲突；先检查这一点。

## 做法：为什么 $[N\ E]$ 不可能满秩

- $N$ 张成 $K_0=\\ker[C;CA]\\subseteq\\ker C$，故 $C N=0$。
- $AN$ 的列：$C(AN)=(CA)N$；而 $N\\subseteq\\ker(CA)$（因为 $K_0=\\ker[C;CA]$），故 $CA N=0$。
  所以 $C(AN)=0$，即 $AN\\subseteq\\ker C$。
- $E$ 是 $AN$ 在 $N$ 补空间的分量，故 $E\\subseteq\\ker C$ 亦然。

因此
$$\\operatorname{rank}[N\\ E]\\le\\operatorname{rank}[N\\ AN]\\le n-p.$$
当 $p>0$ 时 $n-p<n$，$[N\\ E]$ **不可能**满行秩；287 的“双射”前提不成立。

## 正确的提升图像

对 $r$ 行自由行，
$$R\\longmapsto(RN,RAN)$$
的像秩 $\\le r(n-p)$，而目标空间维数 $2rk$；每行至少有 $p$ 个线性约束。
所以压缩对 $(H,H_A)$ 必须满足这些约束才能提升；281 的失败正是其中之一。

## 对 285 门的影响

285 的 $q=5$ 门要落地，必须检查：
$$(H_i,H_{A,i})\\in\\operatorname{row}[N\\ AN]\\quad(i=1,\\dots,r).$$
这给出每行 $p$ 个约束；不是自动的。
下一步应先用这些约束筛 285 的 $H,H_A$，再构造 $A$。

## 进展

* 更正 287 的空条件；
* 得到提升的秩上界 $\\operatorname{rank}[N\\ AN]\\le n-p$；
* 明确 281 的结构性原因。

## 最终结论

* $[N\\ E]$ 满秩在观测器中不可能；
* 提升永远受 $\\ker C$ 限制；
* 285 门必须先过 $\\operatorname{row}[N\\ AN]$ 测试。

## 放弃原因

* 未对 285 的具体 $H,H_A$ 做 $\\operatorname{row}[N\\ AN]$ 测试；
* 未构造满足约束的 $A$。

## 残留价值

* 一个正确的秩上界；
* 撤回一个空引理；
* 明确下一步的测试。

## 相关文件

* [attempts/287](287_lift_surjectivity.md)（撤回）
* [attempts/281](../../../q1_true/rank_gates/attempts/281_q4_gate_not_liftable.md)
* [attempts/285](../../../q1_true/rank_gates/attempts/285_q5_gate_target.md)

## 状态

* 287：**[撤回]**。
* 285 提升测试：**[未做]**。
