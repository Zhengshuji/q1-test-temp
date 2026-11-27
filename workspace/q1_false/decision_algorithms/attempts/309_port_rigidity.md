> **311 更正（81 号）**：本引理只是**条件性**结果：当 $E_1\cap E_2$ 已是一条固定线、且 $\dim W$ 最小时成立。
> 固定子空间一般**可以**有移动端口：$E_1=\operatorname{span}(e1,e2)$、$E_2=\operatorname{span}(e4,e5)$、$W_t=\operatorname{span}(e1,e2,e3,e4+t e5)$ 给 $W_t\cap E_2=\operatorname{span}(e4+t e5)$。

# port rigidity：固定局部子空间会冻结 $W$，与乘法所需的变量行冲突

> 2026-11-10。308 说 sound 与乘法表达力冲突。本文件给出一个具体的局部 incidence 引理，
> 说明“固定子空间 + 端口线”可以排除额外行，但也把 $W$ 冻结。
> 状态：**M2（纸面引理）**。

## 目标

判断局部子空间交能否既排除额外自由行、又保留乘法所需的变量方向。

## 设想与理由

设
$$E_1=\operatorname{span}(e_1,e_2),\qquad E_2=\operatorname{span}(e_1,e_3),$$
$$E_1\cap E_2=\operatorname{span}(e_1).$$
若 $W\supseteq E_1$ 且要求端口
$$W\cap E_2=\operatorname{span}(e_1),$$
则 $W$ 中不能有 $e_3$ 方向。

## 做法：port rigidity 引理

**引理**：设 $W\supseteq E_1$，$\dim W=3$（比 $E_1$ 多一维），且
$$W\cap E_2=\operatorname{span}(e_1).$$
则不存在这样的 $W$。

*证明*：写 $W=\operatorname{span}(e_1,e_2,v)$，$v=a e_1+b e_2+c e_3$。
若 $c\ne0$，则
$$e_3=\frac{1}{c}(v-a e_1-b e_2)\in W,$$
于是 $e_3\in W\cap E_2$，与 $W\cap E_2=\operatorname{span}(e_1)$ 矛盾。
所以 $c=0$，$v\in E_1$，$W=E_1$，与 $\dim W=3$ 矛盾。$\square$

**推论**：在 $E_1$ 固定、端口 $E_2$ 固定的情形下，任何额外的自由行都会立刻把 $e_3$ 带入 $W$，
使端口从一条线扩大为整个 $E_2$。因此“端口恰好是一条线”与“$W$ 比 $E_1$ 多一维”不能同时成立。

## 对 soundness 的意义

- 固定局部子空间可以**排除额外行**（好：soundness）；
- 但代价是 $W$ 被冻结在 $E_1$（坏：没有变量方向，不能编码乘法）。

乘法需要 $W$ 含 $v_x=(0,1,x)$ 这样的变量行；若 $E_1,E_2$ 固定，$v_x$ 要么在 $E_1$ 内（无变量），
要么带 $E_2$ 分量（端口扩大）。

## 进展

* 一个精确的 port rigidity 引理；
* 说明固定子空间交能排除额外行，但冻结 $W$；
* 把 308 的二分具体化为一个局部几何障碍。

## 最终结论

* sound 的局部 incidence 需要**端口随变量移动**，不能是固定子空间；
* 或者乘法变量必须进入 $E_1/E_2$ 的定义，而不是作为额外行；
* 这正是 global incidence realization 的难点。

## 放弃原因

* 未构造“移动端口”的实例；
* 未证明不可能；
* 未接硬度。

## 残留价值

* 一个干净的线性代数引理；
* 对 soundness/表达力冲突的几何解释；
* 下一步“移动端口”的方向。

## 相关文件

* [attempts/308](../../../q1_true/multiplication_gate/attempts/308_soundness_expressiveness.md)
* [attempts/307](307_soundness_obligations.md)
* [attempts/80](../../../for_expert/archive/80_wiring_copy_gadget-answer.md)

## 状态

* 引理：**[M2 纸面]**。
* 移动端口：**[未做]**。
