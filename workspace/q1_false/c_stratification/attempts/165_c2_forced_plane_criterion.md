# $c=2$、$q=3$、被迫平面情形：可行性判据与 16/21 的不可行证明

> 2026-11-08。对专家 59 号的 Deliverable 1（$q=3,\omega=2$ 的精确判据），在 $V=W_L$ 被迫的情形
> 得到一个**线性代数判据**：每个底部压缩行的系数 $b$ 是否被可容许方程强制为 0。
> 结果：seed10 可行（已有见证）；**seeds 16/21 的 $q=3$ 不可行**（不是“好 locus 稀有”，是结构性的）。
> 状态：**M2（纸面 + 精确计算）**。

## 目标

在 $c=2$、$q=\omega+1=3$、$\dim W_L=c$（$V=W_L$ 被迫）的情形，给出 $q=3$ 可行性的**充要判据**，
并判定 seeds 16/21。

## 设想与理由

$V=W_L$、$\operatorname{Ann}(V)=\operatorname{span}\{h_0,u_1\}$（$h_0=L_0N$）。$H$ 的每一行必须属于
$\operatorname{Ann}(V)$，故底部行形如
$$h_i=a_ih_0+b_iu_1,\qquad i=1,2.$$
**若 $b_i=0$，则 $h_i\propto h_0$**；若两行都 $b_i=0$，则 $H$ 秩 1 $<\omega=2$，矛盾。
因此
$$\boxed{q=3\ \text{可行}\ \Longrightarrow\ \text{至少一个底部行有}\ b_i\ne0.}$$

$H_{A,i}=l_iAN$，$l_i=a_ip_0+b_ip_1+g_i$（$p_0,p_1$ 为 $h_0,u_1$ 的特解），
$g_i\in\operatorname{row}[C;CA]$，$g_iAN=\sum_j c_{ij}G_j$（$G_j=RD_jAN$）。
可容许条件 $H_{A,i}|_V=0$ 是 $(a_i,b_i,c_i)$ 的**两个线性方程**（RHS 0）。

**判据**（专家 60 号确认：仅对**齐次**方程成立；本处 RHS 为 0，故适用）：$b_i$ 被强制为 0 $\iff$ 向量 $e_b=(0,1,0,\dots)$ 在方程矩阵的行空间中
$\iff \operatorname{rank}[\mathrm{Des}_i;e_b]=\operatorname{rank}\mathrm{Des}_i$。
（因为方程 RHS 为 0，$b_i$ 是方程组的线性函数。）

## 做法

对每个 seed：
1. 算 $V=W_L$、$u_1$、$p_0,p_1$、$G$；
2. 对每个底部行 $i$，构造 $\mathrm{Des}_i$（$2\times(2+m)$）；
3. 判 $e_b$ 是否在行空间中；
4. 若两行都强制 $b_i=0$ ⇒ $q=3$ 不可行；否则构造 $b\ne0$ 的解，回代检验。

## 结果（精确有理算术）

| seed | $\operatorname{rank}\mathrm{Des}_1$ | $\operatorname{rank}[\mathrm{Des}_1;e_b]$ | $b$ 强制 0？ | 结论 |
|---|---|---|---|---|
| 10 | 0 | 1 | 否 | 可行（已有见证）|
| 16 | 1 | 1 | **是** | **$q=3$ 不可行** |
| 21 | 1 | 1 | **是** | **$q=3$ 不可行** |

**证明（16/21）**：两行的 $b_i$ 都被强制为 0，故任何可容许 $H$ 的底部行都 $\propto h_0$，
$H$ 秩 1 $<\omega=2$，矛盾；而 $V=W_L$ 是唯一候选（$\dim W_L=c$）。$\square$

**seed10**：$\mathrm{Des}_1$ 秩 0，$b$ 自由；构造的解已给出完整 $L$，七条检查通过
（[c2_seed10_witness.py](../../../../tools/verification/c2_seed10_witness.py)）。

## 进展

* 得到 $q=3$、被迫平面情形的**充要判据**：$\exists i:\ b_i$ 不被强制为 0（且构造解可回代）。
* seeds 16/21 判定为 $q=3$ **不可行**（结构性，不是好 locus 稀有）；seed10 可行。
* 这把专家 59 号的“符号行列式”问题在被迫平面情形化成了一个**秩判定**，无需符号多项式。

## 最终结论

* 被迫平面情形：$q=3$ 可行 $\iff$ 某个底部行的 $b$ 不被可容许方程强制为 0；
* 16/21 不可行；10 可行；
* 一般 $\dim W_L>c$ 的情形仍需在 $\operatorname{Gr}(c,W_L)$ 上枚举 $V$，再对每个 $V$ 用同一判据。

## 放弃原因

* 未处理 $\dim W_L>c$（需枚举 $V$）；
* 未处理 $q>3$（$\omega>2$）的类似判据；
* 未把判据写成符号算法（当前是每个实例的精确秩判定）。

## 残留价值

* $c=2$、被迫平面情形的完整可行性判据与 16/21 的不可行证明；
* 判据是线性代数的，可直接算法化。

## 相关文件

* [attempts/156](156_c2_algorithm_spec.md)（算法规格）
* [attempts/164](164_59_verdict_implementation.md)（专家 59 号判据）
* [tools/verification/c2_seed10_witness.py](../../../../tools/verification/c2_seed10_witness.py)（seed10 见证）

## 状态

* 判据与 16/21 不可行：**[已证-纸面 + 精确秩计算]**。
* 一般 $\dim W_L>c$ / $q>3$：**[未做]**。
