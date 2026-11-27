# P1 §V 最小增广族的实现与 $(5a)$ 密度

## 目标

实现 P1（Fernando, arXiv:2609.33615）§V 的最小增广参数化，用于：
1. 把"增广族"变成显式可计算的对象（WP2 的模块 A）；
2. 测量 $(5a)$ 在族内是否自动成立、成立的密度。

## 设想与理由

专家 §12 第 5 步要求研究完备族的几何；而完备族的显式参数化在 P1 §V：
所有最小增广（$\operatorname{rank}(LN_C)=q_0$、含 $L_0$）在 $T$-坐标下都形如
$W_J(\Theta)=\operatorname{diag}(I_r, Y_J(\Theta))$，$Y_J(\Theta)=[I_k\ \Theta]\Pi_J^{\mathsf T}$。
把 $k$ 换成 $q-r$ 就得到**任意阶** $q$ 的同一参数化。

## 做法

[tools/verification/p1_family.py](../../../../tools/verification/p1_family.py)：

1. $N_C$ = $\ker C$ 的基（列）；$B=L_0N_C$；$T=[T_1\ T_2]$，$BT_1=I_r$、$T_2$ 张成 $\ker B$；
   $s=d_C-r$、$k=q-r$；
2. 图卡 $J\subseteq\{1..s\}$（$|J|=k$）；$Y_J(\Theta)$ 的 $J$ 列为单位列、其余为 $\Theta$；
3. 原坐标 $L(\Theta)=W_J(\Theta)(N_CT)^{+}$（$(N_CT)^{+}$ 为左逆）；
4. 断言：行满秩、$\operatorname{row}L_0\subseteq\operatorname{row}L$（这两条是族的定义）；
   测 $(5a)$ 与 $(5b)$（它们是对 $\Theta$ 的条件，**不**自动成立）；
5. 抽样：每图卡 6 点（$\Theta=0$ 与 5 个小整数点）。

## 进展

$n=5,6,7$ 各 3 seed：

| 实例 | $q_0$ | $r$ | $s$ | $k$ | 图卡 | 采样 | $(5a)$ 成立 |
|---|---|---|---|---|---|---|---|
| 5/1000 | 2 | 1 | 3 | 1 | 3 | 18 | 3 |
| 5/1001 | 1 | 1 | 3 | 0 | 1 | 6 | 6 |
| 5/1002 | 1 | 1 | 3 | 0 | 1 | 6 | 6 |
| 6/1000 | 3 | 1 | 4 | 2 | 6 | 36 | 0 |
| 6/1001 | 4 | 1 | 4 | 3 | 4 | 24 | 18 |
| 6/1002 | 3 | 1 | 4 | 2 | 6 | 36 | 1 |
| 7/1000 | 3 | 1 | 5 | 2 | 10 | 60 | 0 |
| 7/1001 | 3 | 1 | 5 | 2 | 10 | 60 | 0 |
| 7/1002 | 4 | 1 | 5 | 3 | 10 | 60 | 1 |

合计 **51 图卡、306 采样、$(5a)$ 成立 35（11.44%）**；采样中**没有** $(5b)$ 成立的成员。

## 最终结论

* P1 §V 的参数化可以逐点实现并**机器核验**：所有构造出的 $L(\Theta)$ 都行满秩、含 $L_0$；
* **$(5a)$ 不是本路线的目标**：它早在 2026-10-21 就解决（构造见 P1 Thm 1、完备族见 Thm 3）。
  P1 §V 的参数化只覆盖"最小维候选"，$(5a)$ 是之后附加的秩条件（Lemma 2 / 式 (20)），
  所以盲抽 $\Theta$ 只有 35/306 命中——这是**抽样效率**，不是 $(5a)$ 的困难性；
* 对 $(5b)$ 的意义：扫描必须在可行集 $\Omega^{\star}_{A,J}$ 内做。**已尝试**用"固定 $\Gamma$ 解 $\Theta$"
  直接生成 $\Omega$ 内的点（[archive/old_scripts/omega_family_attempt.py](../../../../archive/old_scripts/omega_family_attempt.py)），
  但 114 个图卡只解出 2 个点，**无效**，已归档；
* 在 $q=q_0$ 上抽样未找到 $(5b)$ 成立的成员——与"$q_{\min}>q_0$"的经验一致，但抽样不能证明不存在。

## 放弃原因

不适用（实现完成）。**未做**：不可约性（需要 $\Theta$ 的多项式方程组与消元，当前环境无 CAS）。

## 残留价值

* 一个任意阶的、显式的增广族生成器（`sample_q`），后续可直接接：
  - 不可约性/维数研究（把 $(A)$ 写成 $\Theta$ 的方程）；
  - $\mathrm{DEC}(q)$ 的构造性求解（找到 $(5b)$ 成立的 $\Theta$ 就给出解）；
* "$(5a)$ 密度 ≈ 11%"这一读数，可用于判断"生成 + 筛选"路线的可行性。

## 相关文件

- [tools/verification/p1_family.py](../../../../tools/verification/p1_family.py)
- [workspace/augmentation_family/README.md](../../README.md)
- [workspace/kronecker/attempts/02_family_sequences.md](../../../kronecker/attempts/02_family_sequences.md)
- [archive/expert_correspondence/answer_2026-11-02_notes.md](../../../../archive/expert_correspondence/answer_2026-11-02_notes.md)
