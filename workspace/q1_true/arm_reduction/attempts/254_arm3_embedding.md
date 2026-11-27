# ARM(3) 嵌入的可行性分析：$q=3$ 的秩约束是自动的

> 2026-11-09。检查能否把 ARM(3)（仿射约束 + $\\operatorname{rank}X\\le3$）嵌入观测器问题。
> 关键障碍：若令 $X=L$、$q=3$，则 $\\operatorname{rank}L\\le3$ **自动**成立，ARM 的秩约束消失；
> 若 $q>3$，观测器又没有 $\\operatorname{rank}L\\le3$ 的约束。
> 状态：**M1/M2（可行性分析，未构造嵌入）**。

## 目标

把 ARM(3) 的 $\\exists X$（$\\langle A_\\ell,X\\rangle=b_\\ell$，$\\operatorname{rank}X\\le3$）归约到 $q1$。

## 设想与理由

ARM(3) 的硬度需要 $m\\ge4$：$m=3$ 时 $\\operatorname{rank}X\\le3$ 自动，问题退化为线性可行性（P）。
观测器的 witness 是 $L$（$q\\times n$）。最自然的映射是 $X=L$，但这要求 $q=m$ 且 $\\operatorname{rank}L\\le3$。

## 做法：逐条检查

### 1. $q=3$：秩约束自动，不能用

$L$ 有 3 行 ⇒ $\\operatorname{rank}L\\le3$ 恒成立。ARM 的全局秩约束消失；
$(5a)$ 只能给线性条件（$u\\ne0$ 情形）或二次条件（$u=0$），无法表达“$\\operatorname{rank}X\\le3$ 且 $m\\ge4$”。

### 2. $q>3$：观测器没有 $\\operatorname{rank}L\\le3$

$(5a)$ 约束的是 $\\operatorname{row}(LA)\\subseteq\\operatorname{row}[L;CA;C]$，不是 $\\operatorname{rank}L$。
把 $\\operatorname{rank}L\\le3$ 作为额外条件加入，就不是原问题了；
需要证明它可由 $(5a)(5b)$ 推出，目前没有。

### 3. 仿射常数

ARM 的 $\\langle A_\\ell,X\\rangle=b_\\ell$ 有常数 $b_\\ell$；观测器的 $(5a)$ 是齐次行包含。
常数只能通过固定行 $L_0$ 引入；$L_0$ 只有 $r$ 行，能携带的常数有限。
需要把每个 $b_\\ell$ 编码进 $L_0$ 或 $C$ 的结构，尚未构造。

### 4. Gauge block 的类比

ARM 的 gauge 是固定一个满秩 $3\\times3$ 子块，消除 rank-3 分解的歧义。
观测器的“gauge”应是固定 $L_0$ 与 $CA,C$ 的行空间，消除 $L$ 的行空间冗余。
但观测器的冗余是**行空间**冗余（$q$ 行可替换），而 ARM 的冗余是**因子分解**冗余（$X=UV$ 的基变换）；
两者不是同一种歧义，gauge 不能直接搬。

### 5. 一个可能的接口

若把 $X$ 写成 $X=[L;L_{\\rm fix}]$（$L$ 3 行 + 固定行），则 $\\operatorname{rank}X\\le3\\iff$
$\\operatorname{row}L_{\\rm fix}\\subseteq\\operatorname{row}L$，是一个**行包含**条件——与 $(5a)$ 同型。
这可能是唯一可行的接口：用 $(5a)$ 同时编码 ARM 的仿射约束和这个行包含。
但 $L_{\\rm fix}$ 是输入的一部分，$\\operatorname{rank}X\\le3$ 还要求 $L$ 的 3 行独立；
需要把 ARM 的仿射约束塞进 $L$ 的条目，同时保持 $(5b)$ 可行。尚未构造。

## 进展

* 明确 $q=3$ 的秩自动性障碍；
* 明确仿射常数与 gauge 的差异；
* 提出“$X=[L;L_{\\rm fix}]$ + 行包含”的候选接口。

## 最终结论

* 没有构造出 ARM(3) → 观测器的嵌入；
* 直接令 $X=L$ 不可行（$q=3$ 秩自动、$q>3$ 无秩约束）；
* 唯一有希望的接口是“$L$ + 固定行”的行包含，但需要新的编码想法。

## 放弃原因

* 未处理 $q>3$ 的 $\\operatorname{rank}L\\le3$；
* 未编码仿射常数；
* 未接 $(5b)$。

## 残留价值

* 明确的障碍清单；
* 候选接口（$X=[L;L_{\\rm fix}]$，行包含）；
* 避免直接重复“$X=L$”的无效尝试。

## 相关文件

* [attempts/253](../../multiplication_gate/attempts/253_coefficient_encoding_obstruction.md)
* [docs/07 §10.1](../../../../docs/07_literature_review.md)
* [ARM 笔记](../../../../literature/notes/MAJUMDAR_2026_ARM_ER.md)

## 状态

* 可行性分析：**[M1/M2]**。
* 嵌入：**[未构造]**。
