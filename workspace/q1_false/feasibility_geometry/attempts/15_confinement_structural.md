# 公开例子的 $q_0+1$ 失败：**结构解释**（不是抽样观察）

## 目标

把专家 §Q7/§B 的"$q=4$ 时所有可行增广都有 $h=q+r_1=8$"从抽样升级为**结构解释**：
指出为什么会这样，并说明它对 $q_{\min}$ 的含义。

## 设想与理由

$h=\\operatorname{rank}[L;CA;C]=q+r_1-\\delta$，其中 $\\delta=\\dim(\\operatorname{row}L\\cap W)$、$W=\\operatorname{row}[C;CA]$。
而 $\\operatorname{row}L\\subseteq Z^{\\perp}$（因 $[C;L]$ 的行空间就是 $Z^{\\perp}$），所以
$$\\delta\\le \\dim(Z^{\\perp}\\cap W)-\\dim(\\operatorname{row}C)=:\\delta_{\\max}.$$
若 $\\delta=0$（即 $\\operatorname{row}L$ 与 $W$ 只可能在 $\\operatorname{row}C$ 上相遇，而 $\\operatorname{row}L$ 是 $\\operatorname{row}C$ 在 $Z^{\\perp}$ 里的补），则
$$h=q+r_1 .$$
于是"禁闭"是一个**线性代数事实**，不需要 $(5a)$。

## 做法

[confinement_test.py](../../../../tools/verification/confinement_test.py) 与大样本核对：
对公开例子（$n=8$、$p=r=2$、$r_1=4$、$\\dim K=4$），在 $q=3,4,5$ 上各抽 $\\approx200$ 个 $Z$，
计算 $\\dim(Z^{\\perp}\\cap W)$、$h$ 与 $(5a)$。

## 进展

| $q$ | $d=n-p-q$ | $\\dim(Z^{\\perp}\\cap W)$（最小可能 $=\\dim\\operatorname{row}C=p=2$）| $h$ | $q+r_1$ |
|---|---|---|---|---|
| 3 | 3 | $2$（198/198）| — | 7 |
| 4 | 2 | $2$（**199/199**）| **8**（300/300）| 8 |
| 5 | 1 | $3$（199/199）| **8**（299/299）| 9 |

于是：

* $q=4$：$Z^{\\perp}\\cap W=\\operatorname{row}C$ ⟹ $\\delta=0$ ⟹ $h=q+r_1=8$ ⟹ **B.9 直接给出失败**。
  这条对**任意** $Z\\subseteq K$ 成立（不依赖 $(5a)$），199/199 与 300/300 一致；
* $q=5$：$\\dim(Z^{\\perp}\\cap W)=3>p$ ⟹ $\\delta=1$ ⟹ $h=q+r_1-1=8<9$ ⟹ B.9 不适用 ⟹ 可行。

即本例子满足
$$h=\\min(q+r_1,\\ n),$$
从而 B.9 在 **$q\\le n-r_1=4$** 的所有阶上都自动触发，而可行性只在 **$q>n-r_1$** 才可能：
$$q_{\\min}=n-r_1+1=5 .$$

## 最终结论

1. 公开例子的 $q_{\\min}=5$ 有一个**纯整数/维数**的解释：$h=\\min(q+r_1,n)$，故 $q\\le n-r_1$ 时
   $h\\ge q+r_1$（B.9）必然失败；到 $q=n-r_1+1$ 才可能 $h<q+r_1$；
2. 因此该例的"禁闭"是 $Z^{\\perp}\\cap W=\\operatorname{row}C$ 的后果——**与 $(5a)$ 无关**，
   也不需要谱分析；
3. **注意**：$h=\\min(q+r_1,n)$ 不是普遍公式（本项目已有反例：`jordan-n6 p=2 r=1` 的
   $q_0=1,r_1=4,n=6$ 给出 $\\min=5$ 但实际 $h=4$），所以这仍是**该例子**的结构解释。

## 放弃原因

不适用（结构解释完成）。**未做**：把"$Z^{\\perp}\\cap W=\\operatorname{row}C$"的条件一般化
（何时成立、何时不成立）。

## 残留价值

* 把 §B 的"40 个样本"升级为**结构解释 + 199/199、300/300 验证**；
* 得到公开例子的**完整机制链**：$Z^{\\perp}\\cap W=\\operatorname{row}C\\Rightarrow h=q+r_1\\Rightarrow$ B.9
  $\\Rightarrow q\\le n-r_1$ 全失败 $\\Rightarrow q_{\\min}=n-r_1+1$；
* 明确指出该公式**不普遍**（有反例），为后续一般化划清边界。

## 相关文件

- [tools/verification/confinement_test.py](../../../../tools/verification/confinement_test.py)
- [proof/fernando_2gap/README.md](../../../../proof/fernando_2gap/README.md)
- [proof/left_index_count/README.md](../../../../proof/left_index_count/README.md)（B.9）
- [workspace/q1_false/feasibility_geometry/attempts/14_confinement_large_sample.md](14_confinement_large_sample.md)
