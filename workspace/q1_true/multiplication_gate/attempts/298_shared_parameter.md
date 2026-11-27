# 共享参数的直和：复制不增加表达力

> 2026-11-10。297 的直和用独立参数 $f_1,f_2$。本文件检查“共享同一个 $f$”的版本：
> 两个 296 块都取 $f_1=f_2=f$。
> 结论：$(5b)\iff f\ne0$，与单个 gadget 相同；直和共享参数只是**复制**，不增加约束。
> 状态：**M2 + 精确验证（负结果）**。

## 目标

判断共享参数能否把两个非零 gadget 组合出新的条件。

## 设想与理由

若两个块共享 $f$，直和给出
$$(5b)\iff f\ne0\ \wedge\ f\ne0\iff f\ne0,$$
没有新信息。这看起来显然，但需要确认块分解在 $f_1=f_2=f$ 时仍然成立，且没有隐藏的交叉项。

## 做法

取 297 的数据，令 $f_1=f_2=f$：
$$A=\operatorname{diag}(A_1,A_1),\quad
C=\operatorname{diag}(C_1,C_1),\quad
L_0=\operatorname{diag}(L_{0,1},L_{0,1}),\quad
R=\operatorname{diag}(R_1(f),R_2(f)).$$
则
$$P=\operatorname{diag}(P_1(f),P_2(f)),$$
$$\operatorname{rank}P=\operatorname{rank}P_1+\operatorname{rank}P_2.$$
$f\ne0$ 时两项各为 1，总 2；$f=0$ 时两项各为 0，总 0。

## 验证（c298）

- $H$ 的秩恒为 2；
- $(5a)$ 对所有 $f$ 成立；
- $f=0$：$\operatorname{rank}P(0)=0<2$；
- $f\ne0$：$\operatorname{rank}P=2$ 对所有 $\lambda$；
- 所以
  $$(5b)\iff f\ne0,$$
  与单块相同。

## 进展

* 共享参数的直和是“复制”，不增加表达力；
* 确认块分解在共享参数下没有交叉项；
* 明确下一步必须是**非线性共享**（一个块的输出进入另一个块的等式），而不是简单复制。

## 最终结论

* 直和 + 共享参数 = 单个非零 gadget；
* 要得到乘法，必须让同一个变量同时出现在**等式**（$(5a)$）和**非零**（$(5b)$）中；
* 复制型的组合不够。

## 放弃原因

* 未构造非线性共享；
* 未得到等式；
* 未接硬度。

## 残留价值

* 一个明确的负结果；
* 排除“多复制几份就能编码算术”的幻想；
* 下一步聚焦“非零 + 等式”的混合。

## 相关文件

* [attempts/296](296_nonzero_gadget_observer.md)
* [attempts/297](297_direct_sum_gadgets.md)
* `tools/verification/c298_shared_parameter.py`

## 状态

* 复制：**[M2 + 精确验证]**。
* 非线性共享：**[未做]**。
