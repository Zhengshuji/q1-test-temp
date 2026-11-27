# 最小阶的失败分类：**全是 Type I（B.9）**，以及一个可检验的猜想 T

> **2026-11-03 更正**：猜想 T **已被推翻**——结构化 $A$（Jordan 块）下立刻找到 Type III 反例
> （$q_0$ 阶、$h<q_0+r_1$、$d_{\rm fin}=2>0$），见
> [proof/refuted/C4_type3_counterexample.md](../../../../proof/refuted/C4_type3_counterexample.md)。
> 本文档记录的"228 个样本无 Type III"是**实例族太窄**（无重复特征值/Jordan 块、$p\le2$）的结果。

## 目标

> **2026-11-04 补充（已证）**：**Type II 是空类**。由 $h\ge r_1$（行堆叠）与 $s=\operatorname{rank}\mathcal L=q$
> （行满秩）得 $k=q+r_1-h\le q=s$，故 $k>s$ 永不可能。见 [docs/02](../../../../docs/02_theorems_proven.md) B.9b。
> 因此三类实际只有两类：**Type I（计数）** 与 **Type III（谱/几何）**。


把 $q_0$ 阶的失败按专家 §Q1 的三类（Type I/II/III）分类，看哪一类真正需要几何分析。

## 设想与理由

分类判据（**已更正 Type II**；专家原文的"$0<k<s$ ⟹ 失败"不成立，反例是论文的
$\mathcal L_5$：$k=1<s=5$ 却满足 $(5b)$）：

* **Type I**：$h\ge q+r_1$（B.9，无非零左指标）；
* **Type II**：$k:=q+r_1-h>s$（由 $\sum\varepsilon\ge k$ 与 $\sum\varepsilon=s$ 矛盾）；
* **Type III**：$k\le s$ 且 $h<q+r_1$ 却仍 $d_{\rm fin}>0$——只有这一类需要谱/几何分析。

## 做法

[failure_types.py](../../../../tools/verification/failure_types.py)：56 个功能可观测实例，$q_0$ 阶 40 个
Z-参数化样本，逐点算 $h,s,r_1,k,d_{\rm fin}$ 并分类。

## 进展

| 类别 | 样本数 |
|---|---|
| $(5b)$ 成立 | **78** |
| Type I（$h\ge q+r_1$）| **150** |
| Type II（$k>s$）| **0** |
| Type III（几何型）| **0** |

**更正**：上一轮我把三个实例称为"几何型障碍"，那是**错的**——它们的候选全部是
$h=q+r_1$（恰好在边界），即 **Type I**（例：$n=5,p=1,r=1$，seed 3006，$q_0=3$：$h=5=q+r_1$、
$m=0$、$\varepsilon=[]$、$d_{\rm fin}=3$）。

## 最终结论

1. 在 228 个 $q_0$ 阶样本里，**失败全部由 B.9 解释**（Type I），没有一例 Type II/III。
2. 由此提出**猜想 T**（未证，有数据）：
   $$\text{在 }q=q_0\text{ 处：}\ (5b)\iff h<q_0+r_1 .$$
   等价说法：**最小阶上的失败总是 Type I**。
3. 猜想 T 能统一解释已知现象：
   * $q_{\min}=q_0$ 的 39 个实例：存在 $h<q_0+r_1$ 的候选；
   * $q_{\min}>q_0$ 的 16 个实例：**所有** $q_0$ 候选都 $h\ge q_0+r_1$；
   * 公开两阶差例子：$r_1=4$、$q_0=3$ ⟹ $h\ge7$；而 $h\le q_0+2p=7$ ⟹ 必有 $h=7$ ⟹ $m=0$ ⟹
     $\sum\varepsilon=0$ ⟹ $d_{\rm fin}=s=3$ ⟹ 失败 ✓（与本项目的样本一致）。
4. 于是"$q_{\min}>q_0$ 吗"被化成一个**纯组合/几何问题**：
   > 是否存在 $q_0$ 阶的 $(5a)$-可行 $\mathcal L$ 使 $h<q_0+r_1$？

## T 的定向检验（[type3_search.py](../../../../tools/verification/type3_search.py)）

只统计 $h<q_0+r_1$ 的样本（T 说这些都应满足 $(5b)$）：

| 项 | 数 |
|---|---|
| 检查的铅笔 | 655（其中 8 个与 Smith 路径交叉核对 $d_{\rm fin}$ 一致）|
| $h<q_0+r_1$ 的样本 | **175** |
| 其中 $d_{\rm fin}>0$（Type III，即 T 的反例）| **0** |

$d_{\rm fin}$ 用 Toeplitz 零度快速算：$d_{\rm fin}=s-(s+1)m+\nu_s$（不算 Smith），
抽样 8 个与 Smith 路径比对一致。

**结论**：T 在 175 个 $h<q_0+r_1$ 的样本上无反例。**这不是证明**；而且很多实例每阶只找到
1–2 个代数可行样本（$(A)$ 常是薄集），所以"候选多样性"有限。

## 放弃原因

不适用。**未做**：猜想 T 的证明；更大规模的 Type III 搜索（若 T 假，必有一例 $h<q_0+r_1$ 但失败）。

## 残留价值

* 一个**干净的可反驳猜想 T**，且它的反例形态明确（$h<q_0+r_1$ 但 $d_{\rm fin}>0$）；
* 修正了对专家 Type II 判据的表述（有反例）；
* 把"$q_{\min}$ 与 $q_0$ 的间隔"问题化归为 $h$ 在最小阶可达集上的取值问题。

## 相关文件

- [tools/verification/failure_types.py](../../../../tools/verification/failure_types.py)
- [tools/verification/q0_scan.py](../../../../tools/verification/q0_scan.py)
- [workspace/q1_false/feasibility_geometry/attempts/07_q0_scan.md](07_q0_scan.md)（上一轮，含被更正的那条）
- [proof/left_index_count/](../../../../proof/left_index_count/README.md)（B.9）
