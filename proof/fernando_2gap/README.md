# fernando_2gap —— 复现"两阶差"的公开例子

> **对应 docs 条目**：B.9（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

**目的**：把 Fernando 2026（arXiv:2609.37992）§VII 的例子放回本项目的框架里，算它的全部不变量，
作为**回归测试**，并检验 B.9 与更强不等式。

## 例子（论文原文数据）

$n=8$、$p=r=2$、$(A,C)$ 完全可观测（$n_0=8$）、$\eta=(2,1)$、$q_0=3$、$\nu_{\min}=5=q_0+2$、$n_0-p=6$。
论文给出显式的 order-5 增广 $\mathcal L_5$（前两行即 $L$，后三行补到 5 阶），此处逐元素录入。

## 结果

| 项 | 值 |
|---|---|
| $\operatorname{rank}C,\operatorname{rank}L,\operatorname{rank}[C;L]$ | $2,2,4$ |
| $(A,C)$ 可观测 / $L$ 可估 | 是 / 是 |
| $q_0$（功能指标算法）| **3** |
| 本项目的"闭包"维数 | **4** |
| 论文 $\mathcal L_5$：$h,s,r_1,\varepsilon,d_{\rm fin}$ | $8,5,4,[5],0$ |
| $\mathcal L_5$ 满足 $(5a),(5b)$ | 是，是 |
| B.9 区间 $q+r_1-s\le h<q+r_1$ | $4\le 8<9$ ✓ |
| $d_{\rm fin}\le s-(q+r_1-h)$ | $0\le 4$ ✓ |
| $q=3$（论文：代数可行、谱不可行）| 本项目的闭包只有 **4** 行，故不能在 3 阶上检验 |
| $q=4$ 抽样 20 个 | $(5b)$ 成立 **0** 个 |
| $q=5$ 抽样 40 个 | $(5b)$ 成立 **40** 个（含论文的 $\mathcal L_5$，$\varepsilon=[5]$）|

## 两个结论

1. **复现成功**：$\nu_{\min}=q_0+2=5$。在 $q=4$ 处（代数可行阶）我们抽样 20 个增广全部谱不可行，
   在 $q=5$ 处 40/40 可行——与论文的"order 3,4 infeasible；order 5 feasible"一致
   （order 3 我们无法检验，原因见下）。
2. **本项目的"闭包"不是精确最小维数**：它给出 4，而 $q_0=3$。
   这与专家 2026-11-02 答复 §8.1 的提醒一致——贪心地加入 $xA$（而不是其模 $W$ 的剩余类）
   可能**加多了行**。$\mathrm{cl}_{\rm closure}\ge q_0$ 只在部分实例取等号。
   **权威的最小维数是功能指标算法的 $q_0$**（本项目实现见 `tools/ledger/c208_q0_lower_bound.py`）。

## 谱退化簇在 $q_0+1$ 阶的"负责关系"：$h=q+r_1$

用 Z-参数化在 $q=4$ 与 $q=5$ 各抽 40 个代数可行增广，看 $h$：

| 阶 $q$ | $h$ 的取值 | $q+r_1$ | $(5b)$ 成立 |
|---|---|---|---|
| 4 | $\{8\}$ | $8$ | **0** |
| 5 | $\{8\}$ | $9$ | **40** |

即 $q=4$ 的代数可行族**被限制在 $h=q+r_1$ 上**，于是 B.9 解释该阶全部失败；
到 $q=5$ 族离开该超曲面（$h=8<9$），$(5b)$ 成立。这与猜想 T 一致。

## 大样本检验（2000 次抽样）

| 阶 $q$ | 抽样 | 代数可行 | $h$ 分布 |
|---|---|---|---|
| 4（$=q_0+1$）| 2000 | **1999** | $\{8:\,1999\}$（$=q+r_1$）|
| 3（$=q_0$）| 2000 | **0** | — |

即：$(5a)$ 在 $q_0+1$ 是**开条件**（几乎处处成立）且该阶的可行族**禁闭**在 $h=q+r_1$ 上；
在 $q_0$ 处 $(5a)$ 是**薄集**（2000 次 0 命中）。脚本：
[confinement_test.py](../../tools/verification/confinement_test.py)。

## 结构解释：为什么 $q=4$ 的可行族全在 $h=q+r_1$ 上

$h=q+r_1-\delta$，$\delta=\dim(\operatorname{row}\mathcal L\cap\operatorname{row}[C;CA])$，
而 $\operatorname{row}\mathcal L\subseteq\mathcal Z^{\perp}$。本例子在 $q=4$ 处
$$\mathcal Z^{\perp}\cap\operatorname{row}[C;CA]=\operatorname{row}C\quad(\dim=2,\ 199/199\ \text{抽样}),$$
故 $\delta=0$、$h=q+r_1=8$（$300/300$ 抽样），**B.9 直接给出失败**——与 $(5a)$ 无关。
在 $q=5$ 该交为 3 维，$\delta=1$、$h=8<9$，于是可行。

即本例子满足 $h=\min(q+r_1,n)$，从而 $q\le n-r_1=4$ 全被 B.9 排除、$q_{\min}=n-r_1+1=5$。
（该公式**不普遍**：`jordan-n6 p=2 r=1` 有 $\min(=5)\ne h(=4)$。）

## 失败类型：$q_0$ 与 $q_0+1$ 都是 **Type I**（整数障碍）

$q=3$：$(5a)$ 迫使 $\operatorname{class}(v)\propto c\ne0$（$c$ 是 $\operatorname{row}L_0$ 的像在 $\mathbb C^8/S$ 中的类，
$S=\operatorname{row}[C;L_0]+\operatorname{row}[C;CA]$），故 $v\notin S$、$h=7=q+r_1$ ⟹ **Type I**（已证）。
并且可**显式**解出 3 行可行增广（此前抽样 0/2000 未获得）：

$$\mathcal L=\begin{pmatrix}L_{0,1}\\ L_{0,2}\\ v\end{pmatrix},\quad
v=(-42919/32067,\ -55096/10689,\ 1,0,0,0,0,0),$$
$(5a)$ ✓、$h=7=q+r_1$、$\varepsilon=[]$、$d_{\rm fin}=3$、$(5b)$ 失败。

$q=4$：$h=8=q+r_1$（1999/1999 抽样）⟹ 也是 Type I（该阶无符号证明）。

⟹ 公开例子的两阶失败**都是整数障碍**；本项目的 C4 反例（$h=6<7$、$d_{\rm fin}=2$）是**不同机制**。
脚本：[fernando_type.py](fernando_type.py)。

## 复现

```bash
python proof/fernando_2gap/verify.py
```

## 相关

- [proof/left_index_count](../left_index_count/README.md)（B.9 与 $q+r_1-s\le h<q+r_1$）
- [proof/toeplitz_criterion](../toeplitz_criterion/README.md)（判 $(5b)$）
- [proof/refuted/C3](../refuted/C3_gap_can_be_two.md)（"$q_{\min}\in\{\mathrm{cl},\mathrm{cl}+1\}$"被此例推翻）
