# O1 的小算法：块量 $A_*,B_*$ + 子式 gcd（验证 191）

> 2026-11-08。191 给出块判据；本文件把它实现为可执行的小算法，并在 189 的合成例上验证：
> $B_*=0$、gcd 次数 3（非常数）⇒ 恒坏。状态：**精确验证 1/1**。

## 目标

对固定的 $V=L$ 与候选 $(H,H_A)$，计算：
- $Q$：$\operatorname{im}H$ 的基（$q\times\omega$）；
- $ZQ=H_AX$（$HX=Q$）；
- $A_*=Q^+(ZQ)$、$B_*=R^+(ZQ)$（$R$ 为 $Q$ 的补）；
- $\omega$ 阶子式的 gcd。

判据：$B_*=0$ ⇒ 恒坏；$B_*\ne0$ ⇒ gcd 常数则好。

## 设想与理由

191 的判据是“$B_*=0$ 或特征线被吞”；对固定候选，最直接的判定是 $\omega$ 阶子式的 gcd。
把块量与 gcd 一起算出来，既能验证 191，也能给出不可行证书（gcd 非零次）。

## 做法

工具：[tools/verification/c1_pencil_block.py](../../../../tools/verification/c1_pencil_block.py)

输入 $(A,C,L_0,q,\omega,V,\{(h_i,h_{A,i})\})$，输出 `Astar`、`Bstar`、`Bzero`、`gcd_degree`。

合成例（189 的 $L_0=[e_4;e_5;e_6]$、$Ae_3=e_1$、$Ae_i=e_i$）：
```
{'rankH': 3,
 'Astar': diag(1, 1, 1/2),
 'Bstar': [[0,0,0]],
 'Bzero': True,
 'gcd_degree': 3,
 'gcd': [-1, 3, -3, 1] = -(λ-1)^3}
```
- $B_*=0$ ⇒ 由 191 恒坏；
- gcd 为 $-(λ-1)^3$，非常数，与 $B_*=0$ 一致。

## 合成族的 $B_*=0$ 结构证明

该族：$L_0=[e_4;e_5;e_6]$、$Ae_3=e_1$、$Ae_i=e_i$（$i=4,5,6$）。
底部行 $h\in\operatorname{Ann}(e_3)$，即 $h=lN$ 的 $e_3$ 系数 $l_3=0$ 或 $h$ 不含 $e_3$。
提升的 $h_A=lAN$ 在 $K_0$ 上等于 $l_4e_4^*+l_5e_5^*+l_6e_6^*$（$e_1$ 分量为 0）。
而 $h=l_3e_3^*+l_4e_4^*+l_5e_5^*+l_6e_6^*$。于是
$$h_A=h-l_3e_3^*\in\operatorname{row}H$$
（$e_3^*$ 若由某个底部行带入，则 $e_3^*\in\operatorname{row}H$；否则 $l_3=0$，$h_A=h$）。
故所有 $H_A$ 行都在 $\operatorname{row}H$ 中，$B_*=0$，恒坏。$\square$

## 进展

* O1 的小算法实现（块量 + gcd）；
* 合成例验证 $B_*=0$ 与 gcd 非常数；
* 合成族的 $B_*=0$ 结构证明。

## 最终结论

* O1 对固定候选有可执行算法；
* 对合成族，$B_*=0$ 是结构性的，故整族不可行；
* 一般情形：先算 $B_*$，再 gcd；两者都是有限线性代数/多项式运算。

## 放弃原因

* 未把“对自由参数的所有候选”做成符号判定（当前逐候选）；
* 未处理不可对角化特例的完整分类；
* 未 Lean 化。

## 残留价值

* O1 的可执行算法；
* 合成族的完整 $B_*=0$ 证明。

## 相关文件

* [attempts/191](../../c_stratification/attempts/191_c1_pencil_criterion.md)（块判据）
* [attempts/189](../../c_stratification/attempts/189_c1_outside_D_feasible.md)（合成反例）

## 状态

* 算法 + 验证：**[精确验证 1/1]**。
* 自由参数的符号判定：**[未做]**。
