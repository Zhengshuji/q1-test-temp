# 488 行包含接口 $X=[L;L_{\rm fix}]$ 的 no-go：q1 不约束 $\operatorname{rank}L$

> 2026-11-27。按 [PLAN](../PLAN.md) 的第 1–2 步，检验唯一候选接口
> $X=[L;L_{\rm fix}]$ 能否承载 ARM(3) 的 $\operatorname{rank}X\le3$。
> **结论：不能。** 在可容许性 $\operatorname{row}L_0\subseteq\operatorname{row}L$ 下，
> $\operatorname{rank}X=\operatorname{rank}L$，而 q1 对 $\operatorname{rank}L$ **没有任何上界**；
> 存在 q1 可行且 $\operatorname{rank}L=n>3$ 的实例。状态：**[已证-纸面]** + **[精确验证]**。

## 目标

判断 $X=[L;L_{\rm fix}]$ 的行包含接口能否把 ARM(3) 的秩约束 $\operatorname{rank}X\le3$
变成 q1 条件的一个推论。若不能，按 PLAN 写该接口的 no-go，并停止这条接口。

## 设想与理由

ARM(3) 需要一个 $m\ge4$ 行的载体 $X$ 与 $\operatorname{rank}X\le3$（$m\le3$ 时秩约束自动，问题退化）。
q1 的可变量是 $L$（$q\times n$，$\operatorname{row}L_0\subseteq\operatorname{row}L$）。
最自然的接口是把 ARM 的载体行放进 $X$ 的行，即 $X=[L;L_{\rm fix}]$，希望 q1 的条件逼出
“多出来的行落在前几行张成里”，也就是 $\operatorname{rank}X\le3$。

## 做法

### 1. 行数账

设 $L$ 有 $q$ 行，$L_{\rm fix}=L_0$（$r_0$ 行），$X=[L;L_0]$。

**引理 1.** 若 $\operatorname{row}L_0\subseteq\operatorname{row}L$，则
$$\operatorname{rank}X=\operatorname{rank}[L;L_0]=\operatorname{rank}L.$$

*证明.* $L_0$ 的行都在 $\operatorname{row}L$ 里，堆叠不增加秩。$\square$

**推论.** $\operatorname{rank}X\le3\iff\operatorname{rank}L\le3$。

于是接口要求的是“$\operatorname{rank}L\le3$”。而 $L$ 有 $q$ 行：

- 若 $L$ 行满秩（$q=\operatorname{rank}L$），则 $\operatorname{rank}L\le3\Rightarrow q\le3$；
  ARM 需要 $m\ge4$，**装不下**；
- 若允许 $L$ 行不满秩（$q>3$、$\operatorname{rank}L\le3$），则“$\operatorname{rank}L\le3$”
  对任何行空间不超过 3 维的 $L$ **自动成立**——它不是门，不携带任何约束。

### 2. q1 对 $\operatorname{rank}L$ 没有上界（反例）

取 $n=5$、$p=1$、$C=e_5^{\mathsf T}$、$A$ 为移位（$e_iA=e_{i-1}$，$e_1A=0$）、
$L=I_5$、$L_0=e_1^{\mathsf T}$。

- $(C,A)$ 可观测（可观测性矩阵满秩 5）；
- $(5a)$：$\operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C]=5$（$L=I$）；
- $(5b)$：$\lambda L-LA=\lambda I-A$，由 PBH 可观测性，$\operatorname{rank}[\lambda I-A;CA;C]=5$ 对一切 $\lambda$；
- 但 $\operatorname{rank}L=5>3$，$\operatorname{rank}[L;L_0]=5$。

所以“q1 可行”**不推出** $\operatorname{rank}X\le3$；不是“可能找不到反例”，而是反例族存在
（任何可观测 $(C,A)$ 配 $L=I_n$、$n\ge4$）。

精确核验：[488_verify.py](488_verify.py)（`rank[L;CA;C]=5`、`rank[LA;L;CA;C]=5`、
可观测性 5、$\operatorname{rank}L=5$；$(5b)$ 抽查 $\lambda=0,1,2,3,5$，$\forall\lambda$ 由 PBH）。

### 3. 另一条路也堵死：$q=3$

若硬取 $q=3$ 让 $\operatorname{rank}L\le3$ 自动成立，则 ARM 的 $m\ge4$ 个载体行没有位置；
而 $q>3$ 又必须额外假设 $\operatorname{rank}L\le3$（254 已指出这不是 q1 的条件）。

## 进展

1. 引理 1（$\operatorname{rank}[L;L_0]=\operatorname{rank}L$）与推论写成；
2. 反例族（$L=I_n$）给出并精确核验；
3. 接口在“$q\le3$ 装不下 / $q>3$ 约束自动或需额外假设”两种情形下都失败。

## 最终结论

**$X=[L;L_{\rm fix}]$ 的行包含接口不能承载 ARM(3) 的秩约束。** 按 PLAN 的失败判据 1–2，
这是该接口的 no-go；结合 390 的“仿射控制不足”，ARM 路线回到同一个关口：
**q1 没有可用的秩上界机制，除非引入新的秩约束 gadget**（而乘法 gadget 已 unsound）。

最省的陈述：

> 在候选编码 $X=[L;L_{\rm fix}]$（$L_{\rm fix}=L_0$、$\operatorname{row}L_0\subseteq\operatorname{row}L$）下，
> $\operatorname{rank}X=\operatorname{rank}L$，而 q1 的满秩等式、行空间包含与谱条件都不给
> $\operatorname{rank}L$ 的任何非平凡上界（$L=I_n$ 是可行反例）；因此该接口不能承载
> ARM(3) 的 $\operatorname{rank}X\le3$，除非引入新的秩约束机制。

这只是**该接口**的 no-go，不是对所有 ARM(3)→q1 归约的否定。

## 放弃原因

- 接口的行数账与 q1 的秩自由度不匹配（$q$ 是输入，q1 不约束 $\operatorname{rank}L$）；
- 没有找到不把载体放在 $L$ 的行上的替代编码（列编码同样被 $\operatorname{rank}L\le q$ 卡住）；
- 未尝试“把秩约束编码进 $(5b)$ 的谱条件”的新机制（这是唯一还没排除的方向）。

## 残留价值

- 一条干净的**接口 no-go**（引理 + 反例族 + 精确核验），可直接引用；
- 把 ARM 路线的剩余可能压缩成一句：**是否存在一种秩约束机制，使 q1 条件推出某个载体的秩上界**；
- 与 390 合并后，ARM 的自然接口全部有明确死因（逐行忠实、仿射控制、行包含、$X=L$）。

## 相关文件

- [PLAN](../PLAN.md)、[390](390_arm_translation_analysis.md)、[254](254_arm3_embedding.md)、[197](197_ARM3_expressiveness_limit.md)
- [488_verify.py](488_verify.py)

## 状态

- 引理 1 与推论：**[已证-纸面]**；
- 反例族：**[精确验证]**（[488_verify.py](488_verify.py)）；
- 接口 no-go：**[已证-纸面]**（该接口，不是全部归约）；
- 新秩约束机制：**[未尝试]**。
