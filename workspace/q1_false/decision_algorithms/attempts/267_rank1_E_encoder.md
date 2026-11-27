# rank-1 $E$ 能编码什么：一个列条件 + 行空间包含

> 2026-11-09。路线 A 的 $E$ 设计第一步：取 rank-1 的 $E$，看 $(5a)$ 给出什么条件。
> 结论：rank-1 $E$ 只给**一个**行空间条件（$e_1\\in\\operatorname{row}H$，或对应列为零），
> 且当 $k=3$、$\\operatorname{rank}H=3$ 时自动成立；要非平凡必须 $k>3$。
> 状态：**M2（结构分析）**。

## 目标

把 $RE\\in\\operatorname{row}H$ 在 rank-1 $E$ 下写成显式条件，判断能否编码 ARM 的仿射方程。

## 设想与理由

266：$(5a)\\iff H_{A,0}\\in\\operatorname{row}H$ 且 $RE\\in\\operatorname{row}H$。
取 $E$ 只有一列非零，$RE$ 只有一列非零，于是条件变成一个列向量落在 $\\operatorname{row}H$。

## 做法

### 1. 显式

设 $K_0$ 的基 $N$，$k=\\dim K_0$，$E=(I-NN^+)AN$。
取 $E$ 的第 $j$ 列为 $e_a$（$a$ 在 $N$ 的补空间），其余列为 0。
则 $RE$ 只有第 $j$ 列非零，等于 $R e_a\\in\\mathbb C^r$（此处 $r=2$）。
$$RE\\in\\operatorname{row}H
\\iff
\\begin{cases}
R e_a=0,\\quad\\text{或}\\\\
e_j\\text{（作为 }\\mathbb C^k\\text{ 的标准基）}\\in\\operatorname{row}H.
\\end{cases}$$
（因为 $RE$ 的第 $j$ 列是 $R e_a$ 乘以 $e_j$。）

### 2. 何时非平凡

- 若 $\\operatorname{rank}H=k$：$\\operatorname{row}H=\\mathbb C^k$，条件自动；
- 若 $k=3$、$\\operatorname{rank}H=3$：同样自动；
- 非平凡需要 $\\operatorname{rank}H<k$，即 $\\omega<k$（$c>0$），且 $k>\\omega$。

对 ARM(3) 接口，$q=4$、$\\omega=3$；要非平凡必须有 $k>3$，即 $\\dim K_0\\ge4$。

### 3. 能编码什么

$e_j\\in\\operatorname{row}H$ 是一个**行空间包含**条件，等价于
$$\\operatorname{rank}\\begin{bmatrix}H\\\\e_j\\end{bmatrix}=\\operatorname{rank}H,$$
在 Plücker 坐标中是线性的（一个 3-平面经过固定点）。
所以 rank-1 $E$ 给的是**一个线性行空间条件**，不是任意仿射方程。

要编码 ARM 的多条仿射方程，需要：
- 多个 $E$ 列（每列给一个行空间条件），或
- 多个固定行 $L_0$（每行给一个 $H_{A,0}\\in\\operatorname{row}H$），或
- 让 $E$ 的列组合出更复杂的条件。

## 进展

* rank-1 $E$ 的显式条件；
* 非平凡性需要 $k>\\omega$；
* 每个 $E$ 列最多给一个线性行空间条件。

## 最终结论

* rank-1 $E$ 是“一行空间条件”的编码器；
* ARM 归约需要多个这样的条件，并且要证明它们能拼成任意仿射约束；
* 这不是不可能，但需要 $k>3$ 与多列/多固定行的组合设计。

## 放弃原因

* 未构造多条件组合；
* 未接 $(5b)$；
* 未证行空间条件能表示 ARM 的仿射方程。

## 残留价值

* 一个可操作的编码单元；
* 明确非平凡性条件 $k>\\omega$；
* 路线 A 的下一步设计约束。

## 相关文件

* [attempts/266](266_q4_r0_decomposition.md)
* [attempts/254](../../../q1_true/arm_reduction/attempts/254_arm3_embedding.md)

## 状态

* rank-1 $E$：**[M2 纸面]**。
* 多条件组合：**[未做]**。
