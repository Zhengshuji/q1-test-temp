# $c=2$、$q=3$ 的一般可行性算法：$W_L$ 枚举 + $b$-强制判据 + 空空间搜索

> 2026-11-08。把 165 的“被迫平面”判据推广到一般 $W_L$：在 $\operatorname{Gr}(2,W_L)$ 上枚举 $V$，
> 对每个 $V$ 判 $b$ 是否被可容许方程强制为 0；未被强制的行给出秩 2 的 $H$，再在自由参数上搜索
> 满足 $\operatorname{rank}[C;L]=p+q$ 与 $(5b)$ 的 $L$。状态：**M2 + 工具**。

## 目标

实现并验证 $c=2$、$q=3$ 的完整可行性判定（任意 $\dim W_L\ge2$），
输出 $\mathrm{Feasible}$（带见证）或 $\mathrm{Infeasible}$（$b$-强制为 0 的证明）。

## 设想与理由

* $V\in\operatorname{Gr}(2,W_L)$；$H$ 的顶部行 $h_0=L_0N$，底部行 $h_i=a_ih_0+b_iu_1$（$\operatorname{Ann}(V)=\langle h_0,u_1\rangle$）；
* $b_i=0\Rightarrow h_i\propto h_0$；若两行都强制 0，$H$ 秩 $1<\omega=2$，不可行；
* 若某行 $b_i$ 不被强制 0，则存在秩 2 的 $H$；其自由参数（可容许方程的解空间）用于满足
  $\operatorname{rank}[C;L]=p+q$ 与 $(5b)$。

## 做法

工具：[tools/verification/c2_q3_algorithm.py](../../../../tools/verification/c2_q3_algorithm.py)

1. 算 $K_0,N$、$W_L=\ker[L_0N;L_0AN]$；若 $\dim W_L<2$ 不可行；
2. 枚举 $V\in\operatorname{Gr}(2,W_L)$：
   * $\dim W_L=2$：$V=W_L$；
   * $\dim W_L>2$：用 $\mathbb P(W_L^*)$ 的参数（小整数网格）枚举 2-平面，RREF 去重；
3. 对每个 $V$：$\operatorname{Ann}(V)=\ker V$；取 $h_0=L_0N$（必须 $\in\operatorname{Ann}(V)$）与 $u_1$；
   对每个底部行构造 $\mathrm{Des}_i$（$2\times(2+\dim\operatorname{row}[C;CA])$），判
   $$e_b\in\operatorname{rowspace}(\mathrm{Des}_i);$$
4. 两行都强制 0 ⇒ 该 $V$ 不可行；否则解 $b_i=1$ 得特解 + 空空间；
5. 在两行的空空间上随机搜索（精确有理），构造 $L$ 并跑 `check_candidate` 的七条检查；
6. 返回见证（可行）或所有 $V$ 都失败（在枚举范围内不可行）。

## 结果（精确有理算术，seeds）

| seed | $\dim W_L$ | $V$ 数 | 强制 0 的行数 | 结果 |
|---|---|---|---|---|
| 10 | 2 | 1 | 0 | **可行**（见证，七条检查）|
| 16 | 2 | 1 | 2 | **不可行**（$H$ 秩 $1<\omega$）|
| 21 | 2 | 1 | 2 | **不可行**（同上）|

这复现了 165 的结论，并把它实现为工具。

**一般 $\dim W_L>2$**：枚举与判据已实现，但当前 seeds 都是 $\dim W_L=2$；需要构造一个
$\dim W_L>2$ 的实例来测试（待做）。

## 进展

* $q=3$ 的完整算法（枚举 + 判据 + 搜索）已实现为工具，seeds 全部判定；
* 16/21 不可行的证明是结构性的（$b$ 强制 0 ⇒ 秩 1）；
* seed10 可行，见证可复现。

## 最终结论

* $c=2$、$q=3$ 的可行性 = 对每个 $V\in\operatorname{Gr}(2,W_L)$，检查是否有底部行的 $b$ 不被强制 0，
  并在自由参数上找到满足秩与谱条件的 $L$；
* seeds 10/16/21 全部判定；
* 一般 $\dim W_L>2$ 的情形需要进一步测试（构造实例或从更大 seeds 中找）。

## 放弃原因

* 未测试 $\dim W_L>2$ 的实例；
* 随机搜索不是完备的（对每个 $V$，若好 locus 非空但稀有，可能错过；不过 16/21 是不可行，不涉及此）。
* 未处理 $q>3$（$\omega>2$）。

## 残留价值

* 一个可复现、精确的 $c=2$、$q=3$ 可行性工具；
* 结构性不可行判据（$b$ 强制 0）；
* 与 165 的纸面证明互补。

## 相关文件

* [attempts/165](../../c_stratification/attempts/165_c2_forced_plane_criterion.md)（被迫平面判据）
* [attempts/156](../../c_stratification/attempts/156_c2_algorithm_spec.md)（算法规格）
* [tools/verification/c2_q3_algorithm.py](../../../../tools/verification/c2_q3_algorithm.py)
* [tools/verification/c2_seed10_witness.py](../../../../tools/verification/c2_seed10_witness.py)

## 状态

* 算法与 seeds 判定：**[已证-纸面 + 精确计算]**。
* $\dim W_L>2$ / $q>3$：**[未做]**（$\dim W_L>c$ 只是搜索，见 [179](179_c2_scope.md)）。
