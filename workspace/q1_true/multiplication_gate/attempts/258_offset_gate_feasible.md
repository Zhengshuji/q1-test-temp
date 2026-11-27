# 258 撤回：$2\times2$ 子式不是极大子式，$(5b)$ 实际失败

> 2026-11-09。258 声称找到 $(5a)(5b)$ 共存的偏移实例；**该结论错误**。
> 错误在于：$P$ 是 $q\times k=3\times5$，极大子式是 **$3\times3$**，不是 $2\times2$。
> 正确计算给出 $\\gcd=\\lambda(\\lambda-1)(\\lambda-2)$，$P(0),P(1),P(2)$ 的秩都是 2（$<3$），
> 所以 $(5b)$ 失败。状态：**撤回（M3 自查 + 精确复核）**。

## 目标

更正 258 的判定错误，恢复正确的验证标准。

## 设想与理由

$(5b)$ 要求 $\\operatorname{rank}P(\\lambda)=\\operatorname{rank}H$ 对所有 $\\lambda$。
$P$ 是 $q\\times k$；极大子式大小是 $\\min(q,k)=q=3$。
258 用 $2\\times2$ 子式的 gcd，只能说明“秩至少 2”，不能说明“秩等于 3”。

## 做法：正确计算

258 的实例
$$P(\\lambda)=\\begin{bmatrix}
0&0&0&0&\\lambda\\\\
0&0&2-\\lambda&2-\\lambda&\\lambda\\\\
\\lambda-1&1-\\lambda&2-\\lambda&2-\\lambda&\\lambda
\\end{bmatrix}.$$
全部 $\\binom{3}{3}\\binom{5}{3}=10$ 个 $3\\times3$ 子式的 gcd：
$$\\boxed{\\lambda(\\lambda-1)(\\lambda-2)}.$$
在 $\\lambda=0,1,2$ 处 $\\operatorname{rank}P=2<3=\\operatorname{rank}H$，$(5b)$ 失败。

`c258_offset_gate.py`（已改写为更正版）输出：
- 10 个 $3\\times3$ 子式；
- gcd $=\\lambda(\\lambda-2)(\\lambda-1)$；
- rank $P(0),P(1),P(2)=2,2,2$；
- `CORRECTED: attempt 258 is retracted`。

## 另一个问题：这个实例其实不是“偏移”

258 的 $A$ 中，$l_5$ 对 $lA$ 的 $Q$ 分量贡献来自 $A[5][1..4]$；这些入口全为 0，
所以 $lA$ 的 $Q$ 部分就是 $M x$，**没有偏移**。它是 256 的零偏移情形，$(5b)$ 必失败。
（$A e_5$ 有 $Q$ 分量是列 5 的入口 $A[1..4][5]$，它影响 $A e_5$，但不影响 $lA$ 的 $Q$ 分量。）

## 撤回与更正

- 258 的“偏移可行、门复活”结论**撤回**；
- 257 的“一般位置自动、非一般位置退化”仍成立；
- 偏移是否可行**仍未确定**；要构造真正的偏移，必须让 $A[5][1..4]$（或 $A[6][1..4]$、$A[7][1..4]$）非零，
  使 $s_5,s_6,s_7$ 进入 $lA$ 的 $Q$ 分量。

## 进展

* 修正了一个方法错误（极大子式大小）；
* 撤回 258；
* 明确真正偏移的矩阵入口。

## 最终结论

* 偏移门的可行性仍开放；
* 下一步：用真正的偏移（$A[5][1..4]\\ne0$）重做搜索，并用 $3\\times3$ 极大子式判定 $(5b)$。

## 放弃原因

* 258 的实例无效；
* 未重做真正偏移的搜索。

## 残留价值

* 一个明确的验证标准（极大子式大小）；
* 真正偏移的入口位置；
* 避免再次用错子式大小。

## 相关文件

* [attempts/257](257_offset_absorption.md)
* [attempts/256](256_invariant_gate_spectral_obstruction.md)
* `tools/verification/c258_offset_gate.py`（更正版）

## 状态

* 258：**[撤回]**。
* 真正偏移搜索：**[未做]**。
