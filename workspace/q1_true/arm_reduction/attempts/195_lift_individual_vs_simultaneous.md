# 188 的“个别提升”可以同时组装；全局条件是 $d'_C$ 不等式

> 2026-11-09。专家 62 号要求区分“个别行可提升”与“同时拼出满足秩与行独立约定的 $L$”。
> 本文件说明：188 的个别提升**逐行独立**，可以直接同时组装；真正独立的全局条件是
> 152 的 $d'_C\ge\dim\ker Z_{\rm pair}$。状态：**M2（纸面）**。

## 目标

回答 62 号 §2.2：188 是否只给个别行提升；同时组装还缺什么。

## 设想与理由

188 的构造：对每个 $h$，取一个提升 $l_0$，再用 $g_0$ 调成 $l=l_0-\frac{l_0\cdot Av}{g_0\cdot Av}g_0$。
这里 $g_0$ 只依赖 $v$（与 $h$ 无关），调整量逐行计算；**不同行之间没有耦合**。
所以给定任意有限个 $h_1,\dots,h_{q-r}$，可以逐行选提升，同时满足 $l_iN=h_i$ 与 $l_i\cdot Av=0$。

## 做法

### 1. 逐行独立性

对每行 $i$：
$$l_i=l_i^{(0)}-\frac{l_i^{(0)}\cdot Av}{g_0\cdot Av}g_0,$$
其中 $l_i^{(0)}$ 是 $h_i$ 的任一提升，$g_0$ 固定。则
$$l_iN=h_i,\qquad l_i\cdot Av=0.$$
各行独立，故同时成立。

### 2. 全局条件

同时组装后还需要：
- $\operatorname{rank}H=\omega$（由选 $h_i$ 保证）；
- $\operatorname{rank}[C;L]=p+q$（$\mathsf P_{\rm ind}$ 约定）。这是 **152** 的提升完成条件：
  $$\dim\ker Z_{\rm pair}\le d'_C,$$
  其中 $d'_C=\dim E'_C$、$Z_{\rm pair}$ 是压缩对映射。
- 该条件**不**由 188 推出；它取决于所选 $h_i$ 与 $g_i$ 的自由度。

### 3. 结论

- 188 是**逐行**的，但**可同时组装**（无耦合）；
- 缺的全局条件是 $d'_C\ge\dim\ker Z_{\rm pair}$（$\mathsf P_{\rm ind}$）；
- 在 $\mathsf P_{\rm full}$ 下，该不等式换成另一形式，但逐行提升仍可组装。

## 进展

* 明确了 188 的“个别 vs 同时”：逐行可同时组装；
* 全局条件定位到 152 的 $d'_C$ 不等式；
* 62 号 §2.2 的疑问解决。

## 最终结论

* 188 不会因“只个别”而失效；
* 真正需要单独检查的是提升完成不等式；
* 求解器已实现该检查（`lift_data`）。

## 放弃原因

* 未给出 $\mathsf P_{\rm full}$ 下 $d'_C$ 的替代形式；
* 未 Lean 化。

## 残留价值

* 澄清 188 与提升层的关系；
* 把“个别/同时”问题闭合。

## 相关文件

* [attempts/188](../../../q1_false/c_stratification/attempts/188_c1_outside_D.md)（个别提升）
* [attempts/152](../../../q1_false/c_stratification/attempts/152_lift_completion_fixed_l0.md)（$d'_C$）
* [attempts/194](../../multiplication_gate/attempts/194_62_verdict_implementation.md)（专家 62 号）

## 状态

* 澄清：**[已证-纸面，M2]**。
* $\mathsf P_{\rm full}$ 形式：**[未做]**。
