> **311 更正（81 号）**：本文件的“固定子空间给不出移动交线”只对最小秩情形成立；一般固定子空间可有移动端口（$E_1\cap E_2=0$、$\dim W$ 足够）。
> 本文件降为条件性观察。

# 移动端口的尝试：固定局部子空间给不出随变量移动的交线

> 2026-11-10。309 说固定端口冻结 $W$。本文件试“移动端口”，发现一个更细的障碍：
> 一旦 $W$ 含变量向量 $v=e_2+x e_3$，它就含 $e_3$；任何固定二维 $E_2\\subseteq\\operatorname{span}(e_1,e_3)$
> 都被 $W$ 包含，交线扩大；若 $E_2$ 带 $W$ 外方向，交线又被固定住。
> 状态：**M2（结构分析，负结果）**。

## 目标

在 $k=3$ 或 $4$ 中构造 $E_1,E_2$ 固定、$W$ 随 $x$ 变化，但
$$W\\cap E_2=\\text{一条随 }x\\text{ 移动的线}.$$

## 设想与理由

乘法需要 $W$ 含
$$v_x=(0,1,x).$$
若 $E_1=\\operatorname{span}(e_1,e_2)\\subseteq W$，则 $v_x-e_2=x e_3\\in W$，所以 $e_3\\in W$（$x\\ne0$）。
于是 $W$ 实际上包含整个 $\\operatorname{span}(e_1,e_2,e_3)$。

## 做法：两种 $E_2$

### 1. $E_2\\subseteq\\operatorname{span}(e_1,e_3)$

若 $E_2=\\operatorname{span}(e_1,e_3)$，则 $E_2\\subseteq W$，
$$W\\cap E_2=E_2$$
是二维，不是线。

若 $E_2=\\operatorname{span}(e_1+x e_3,e_4)$（$e_4\\notin W$），则
$$W\\cap E_2=\\operatorname{span}(e_1+x e_3)$$
是一条**移动的线**。但 $E_2$ 依赖 $x$，不是固定数据。

### 2. $E_2$ 固定且带 $W$ 外方向

若 $E_2=\\operatorname{span}(e_1,e_4)$，$e_4\\notin W$，则
$$W\\cap E_2=\\operatorname{span}(e_1)$$
是固定的线，不随 $x$ 移动。

## 结论（负结果）

- $E_2$ 固定且 $\\subseteq W$：交线扩大为二维；
- $E_2$ 固定且带 $W$ 外方向：交线固定；
- 要移动端口，$E_2$ 必须依赖 $x$，而固定数据给不出。

## 进展

* 两个具体例子；
* 说明固定局部子空间无法产生移动端口；
* 把 309 的“冻结”加强为“端口要么固定、要么扩大”。

## 最终结论

* 在“固定 $E_j$ + 变量 $W$”的框架里，移动端口不可得；
* 若 global incidence 需要移动端口，则 $E_j$ 必须也是变量（由见证行定义），这又回到 soundness 问题；
* 这是 80 号 global incidence 计划的一个具体障碍。

## 放弃原因

* 未穷举所有 $E_2$ 依赖方式；
* 未证明一般不可能；
* 未接硬度。

## 待问专家

1. 固定坐标子空间是否**必然**给不出移动端口？
2. 若 $E_j$ 也由见证行定义，如何保证它们不被额外行改变？
3. 是否存在完全不同的 wiring 编码（例如射影空间中的线丛）？

## 残留价值

* 两个固定/移动端口的反例；
* 对 global incidence 的具体障碍；
* 下一步可问专家的三个问题。

## 相关文件

* [attempts/309](309_port_rigidity.md)
* [attempts/308](../../../q1_true/multiplication_gate/attempts/308_soundness_expressiveness.md)
* [80 答复](../../../for_expert/archive/80_wiring_copy_gadget-answer.md)

## 状态

* 分析：**[M2 纸面]**。
* 移动端口：**[未构造]**。
