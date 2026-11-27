# 路线 A 的结构困难：$E$ 只能编码“行空间包含”，不能编码任意仿射方程

> 2026-11-09。继续路线 A（固定行 + $E$ 编码 ARM(3)）。
> 一般 $E$ 下，$(5a)$ 的自由行条件是
> $$RE\\in\\operatorname{row}H.$$
> 记 $W_R=\\operatorname{row}(RE)\\subseteq\\operatorname{row}E$（维数 $\\le r$）。则
> $$RE\\in\\operatorname{row}H\\iff W_R\\subseteq\\operatorname{row}H.$$
> 这是 Grassmannian 上的**关联条件**（一个 $\\le r$ 维子空间包含在 $\\operatorname{row}H$ 中），
> 不是 $H$ 的条目上的任意仿射方程。路线 A 在这里遇到结构困难。
> 状态：**M2（结构分析，路线 A 的障碍）**。

## 目标

判断 $E$ 能否把 ARM(3) 的仿射约束编码进 $(5a)$。

## 设想与理由

266 把 $(5a)$ 写成 $H_{A,0}\\in\\operatorname{row}H$ 与 $RE\\in\\operatorname{row}H$。
267 处理 rank-1 $E$，给一个列条件。一般 $E$ 应给更多条件；本文件写出其确切形状。

## 做法

### 1. 一般 $E$ 的条件

$RE$ 是 $r\\times k$ 矩阵；它的每一行是 $R$ 的行线性组合 $E$，所以
$$\\operatorname{row}(RE)\\subseteq\\operatorname{row}E.$$
$RE\\in\\operatorname{row}H$ 意味着 $RE$ 的每一行都属于 $\\operatorname{row}H$，即
$$\\boxed{W_R:=\\operatorname{row}(RE)\\subseteq\\operatorname{row}H.}$$
$\\dim W_R\\le r$（这里 $r=2$）。

### 2. 这是关联条件，不是仿射方程

固定 $R$ 时，$W_R$ 是 $\\mathbb C^k$ 的一个 $\\le2$ 维子空间；
条件 $W_R\\subseteq\\operatorname{row}H$ 是
$$\\operatorname{Gr}(3,k)\\ \\text{中的 incidence}\\quad \\{\\Lambda:\\ W_R\\subseteq\\Lambda\\}.$$
在 Plücker 坐标中，它是**线性**方程（$\\Lambda$ 经过固定子空间）；
不是 $H$ 的条目的任意线性方程，更不是任意仿射方程。

固定行条件 $H_{A,0}\\in\\operatorname{row}H$ 同理：每个固定点是“$\\operatorname{row}H$ 经过该点”的 incidence。

### 3. 与 ARM 的差距

ARM(3) 的约束是 $X=H$ 的条目上的仿射方程
$$\\langle A_\\ell,H\\rangle=b_\\ell.$$
这是**线性泛函等于常数**；incidence $W_R\\subseteq\\operatorname{row}H$ 是**行列式/秩**条件。
两者一般不能互相编码：
- incidence 的零点集是 determinantal variety（次数 $\\omega$）；
- 仿射方程是超平面。
除非 $\\omega=1$（线性），否则 incidence 不是超平面。

### 4. 结论

路线 A 的 $E$ 编码只能产生 incidence/rank 条件；
要把 ARM 的仿射方程编进去，需要额外的机制（例如把每个方程变成一个固定点 incidence，
但这要求 $\\operatorname{row}H$ 经过大量固定点，最终变成“这些点张成 $\\le3$ 维”的秩条件，
仍然不是任意仿射系统）。

## 进展

* 一般 $E$ 的精确条件 $W_R\\subseteq\\operatorname{row}H$；
* 识别为 Grassmannian incidence；
* 与 ARM 仿射方程的型不匹配。

## 最终结论

* **路线 A 在“编码任意仿射约束”这一步遇到结构困难**；
* 可以继续的变体：
  1. 找约束本身就是 incidence/rank 的 ARM 变体；
  2. 用 incidence 编码乘法门（回到门路线）；
  3. 转路线 B（谱分支）或 C（变 $\\kappa_{\\rm obs}$ 算法）。

## 放弃原因

* incidence ≠ 仿射方程；
* 未找到把 ARM 仿射约束转成 incidence 的编码；
* 未接 $(5b)$。

## 残留价值

* 一个清晰的“型不匹配”障碍；
* 解释了为什么固定行/ $E$ 不能直接做 ARM；
* 明确下一步只能换机制。

## 相关文件

* [attempts/266](266_q4_r0_decomposition.md)
* [attempts/267](267_rank1_E_encoder.md)
* [attempts/254](../../../q1_true/arm_reduction/attempts/254_arm3_embedding.md)

## 状态

* 路线 A：**[遇到结构困难]**。
* 变体/其他路线：**[未做]**。
