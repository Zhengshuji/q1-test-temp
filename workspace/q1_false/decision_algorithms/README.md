# decision_algorithms —— 判定算法（算法侧，已冻结）

> 状态：**已冻结**（并入 Paper I）。上级：[q1_false](../README.md)。

本子方向保存 Paper I 的本地支撑材料（固定 $q$ 的 XP、固定 $\ell$ 的 FPT、$\exists\mathbb R$、
$r=0$ 的多项式判定），以及当时的验证脚本索引。

## 现在怎么用

- 结论一律引 **Paper I**（Theorem 1/2/5、Proposition 4）；
- 本地 attempts（`312`/`313`/`314`/`318` 等）只作历史推导与脚本索引，不再作为依据；
- 需要复跑：`tools/verification/` 下的 c3xx 脚本。

## 不再推进

固定参数的判定已闭合；剩余是 **Paper I 的审计性工作**（系数常数、位复杂度细则），在 artifact 仓库做。
