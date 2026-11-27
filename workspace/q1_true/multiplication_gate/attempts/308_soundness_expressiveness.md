# soundness 与表达力的张力：$k=\\operatorname{rank}H_0$ 时 sound 但线性；乘法需要变量行

> 2026-11-10。307 说 rank forcing 不够。本文件给出一个更结构性的观察：
> - 若 $H_0$ 满行秩 $k$，则 $\\operatorname{rank}H=k$、$\\operatorname{im}H$ 固定，$(5a)$ 对 $H_A$ 是**线性**的，
>   不能产生 $xy$；
> - 若 $H_0$ 不满秩，自由行可以增加 $\\operatorname{rank}H$，在通用提升模型里秩层不被强制，
>   303 与 80 号的反例正是这样产生的。
> 因此“sound + 乘法”需要 rank/pencil 之外的机制（局部子空间交），这正是 global incidence。
> 状态：**M2（结构分析）**。

## 目标

判断 soundness 与乘法表达力是否在 $H$ 层直接冲突。

## 设想与理由

$(5a)$ 只给 $H_A$ 的行在 $\\operatorname{row}H$ 中。若 $\\operatorname{row}H$ 固定为常数平面，
这个条件是线性的；若 $\\operatorname{row}H$ 含自由变量，条件可以非线性，但自由的额外行也能改变秩层。

## 做法：两种极端

### 1. $H_0$ 满行秩 $k$

$H_0$ 是 $r_0\\times k$ 且秩 $k$。则对任意自由行，$\\operatorname{rank}H\\ge k$，但 $H$ 只有 $k$ 列，
故
$$\\operatorname{rank}H=k,\\qquad \\operatorname{im}H=\\operatorname{im}H_0\\ (\\text{固定}).$$
于是 $(5a)$ 等价于
$$H_A\\text{ 的每一行} \\in \\operatorname{im}H_0,$$
这是对 $H_A$ 条目的**线性**条件；$H$ 的行是常数，$(5a)$ 不含 $x\\cdot y$。
所以这个 regime 是 sound 的（秩固定），但不能编码乘法。

### 2. $H_0$ 不满秩

自由行可以增加 $\\operatorname{rank}H$。在通用提升模型中，每个自由行对 $(H_i,H_{A,i})$ 可任意选，
所以：
- 可以把“应为零”的行选成非零，扩大 $\\operatorname{row}H$；
- 可以把 $H_A$ 的行选成新行空间中的元素，使 $(5a)$ 自动；
- $(5b)$ 只要求“铅笔的秩 = 当前 $\\operatorname{rank}H$”，不要求预期层。

303 的 $R=0$ 与 80 号的假赋值都是这个机制的具体实例。

### 3. 结论

- $k=\\operatorname{rank}H_0$：sound，但 $(5a)$ 线性，无乘法；
- $k>\\operatorname{rank}H_0$：有乘法所需的变量行，但秩层不被强制，soundness 失败；
- 要两者兼得，必须用**局部子空间交**限制额外行，而不是只靠秩/pencil。

## 进展

* 一个 soundness–表达力的二分；
* 解释了为什么 296/303C（$k=1$）sound 但不能乘法；
* 解释了 303B/297/299/300 的 bypass 来源。

## 最终结论

* 在 $H$ 层，sound 与乘法表达力直接冲突；
* 乘法的 sound 实现必须引入 $H$ 之外的约束（局部坐标子空间、射影线、全局 incidence）；
* 这支持 80 号的 global incidence 方向。

## 放弃原因

* 未构造“局部子空间交”的具体实例；
* 未证明二分是严格的（“必须”仍是分析）；
* 未接硬度。

## 残留价值

* 一个清晰的二分；
* 对多个 bypass 的统一解释；
* 下一步 global incidence 的动机。

## 相关文件

* [attempts/307](../../../q1_false/decision_algorithms/attempts/307_soundness_obligations.md)
* [attempts/306](306_80_soundness_correction.md)
* [attempts/303](../../../q1_false/decision_algorithms/attempts/303_79_verdict_lifts.md)

## 状态

* 二分：**[M2 纸面]**。
* 局部子空间实现：**[未做]**。
