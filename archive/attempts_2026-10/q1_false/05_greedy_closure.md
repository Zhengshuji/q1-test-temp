# 路线 5：贪心 / 闭包算法

## 目标
用 Kleiman–Krener 式的**闭包迭代**直接算出最小 ci 子空间（从而 $\rho_{ci}$），或算出 $q_{\min}$。

## 设想与理由
$B=0$ 时 $P=\dim\langle S\rangle_A$ 是闭包；有 $B$ 时直觉上"先闭包、不够再加 $B$"应该能逼近最优。

## 做法
`archive/old_scripts/core/` 的 `c131_phi_closure.py`、`c137_cyclic_candidate.py`、`c138_S_extension.py`、`c139_liftability_scan.py`；以及 `q1_false/tests/verify/descent_algorithm.py`。

## 进展
| 算法 | 与精确值一致 |
|---|---|
| 纯闭包（$\varphi=0$）| 11/120 |
| "链式" $S, S+AS, S+AS+A^2S,\dots$ 上第一个满足的 | 66/80 |
| 贪心加 $B$ 方向 | 20/24 |
| 下降算法（保持 $\rho$）| 只能解出**起始层**，遇到中间层就停 |

## 最终结论
**死**。贪心给的是"按包含"的极小（或某个局部极小），不是"按维数"的极小。

## 放弃原因
具体卡在：$(A,B)$-不变族对和封闭、对交不封闭 ⟹ 没有拟阵/格结构支撑贪心；且最优解可能不在任何"自然链"上。

## 残留价值
- 这些脚本是**反例发生器**（它们的失败案例就是最好的测试集）。
- 精确算法现在是 $P$ 的递归（$O(n^4)$）——贪心被完全取代。

## 相关文件
- [proof/p_is_polynomial/algorithm.md](../../../proof/p_is_polynomial/algorithm.md)
- `q1_false/tests/verify/descent_algorithm.py`