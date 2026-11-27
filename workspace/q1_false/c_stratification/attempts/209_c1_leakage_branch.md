# $c=1$ 泄漏分支：可容许真空后的铅笔障碍

> 2026-11-09。专家 64 号的第 3 项：刻画 $c=1$ 非不变分支（$A(V)\not\subseteq K_0$）的铅笔障碍。
> 结论：泄漏使可容许条件真空（188），可行性只剩铅笔条件；给出精确判据与结构性坏例。状态：**M2**。

## 目标

对 $c=1$、$V=\mathbb Cv$、$A(V)\not\subseteq K_0$，刻画何时可行、何时铅笔恒坏。

## 设想与理由

由 207 的局部刚性，可行（$\omega>0$）必须 $A(V)\not\subseteq K_0$。写
$$l=(h,g)\in K_0^*\oplus G^*,\qquad Av=A_Kv+A_Gv,$$
$J_V:V\to G$、$J_V(v)=\pi_G(Av)$。$A(V)\not\subseteq K_0$ ⇔ $J_V\ne0$。

$(5a)$：$h|_v=0$ 且 $h(A_Kv)+g(A_Gv)=0$。$J_V\ne0$ ⇒ 对任意 $h$ 都有 $g$ 解（188），可容许真空。

## 做法

### 1. 可容许真空

$A_Gv\ne0$ ⇒ 对每个 $h\in\operatorname{Ann}(v)$，取 $g$ 使 $g(A_Gv)=-h(A_Kv)$；则 $l=(h,g)$ 可容许。
故 $H$ 的行可在 $\operatorname{Ann}(v)$（$\omega=k-1$ 维）中任选（秩条件外无约束）。

### 2. 铅笔条件

$H$ 的 $\omega$ 行张满 $\operatorname{Ann}(v)$；$H_A$ 的行由 $h$ 与 $g$ 决定。令
$$P(\lambda)=\lambda H-H_A.$$
$$\text{好}\iff\operatorname{rank}P(\lambda)=\omega\ \forall\lambda
\iff\ker(A_*-\lambda I)\cap\ker B_*=\{0\}\ \forall\lambda.$$

### 3. 结构性坏例

- 若所有可容许提升给 $H_A=HT$（某个固定的 $T$），则 $P=H(\lambda I-T)$，$\det(\lambda I-T)$ 有根 ⇒ 坏；
- 若 $H_A$ 的行都落在 $\operatorname{row}H$ 的同一个低维子空间，且该子空间含 $A_*$ 的特征向量，也会坏；
- 两个合成例（189/202）都是这种结构。

### 4. 判据

对固定候选 $(H,H_A)$，**精确判据**是 $\gcd$ 的 $\omega$ 阶子式是否为常数（191/192）。
对自由参数（$h$ 与 $g$），好 locus 是开条件；**空/非空**仍无闭式判据（Task C 的残留）。

## 进展

* 泄漏分支的精确描述：可容许真空、铅笔是唯一约束；
* 结构性坏例的分类；
* 精确判据（固定候选）与开放点（自由参数）分开。

## 最终结论

* $c=1$、$A(V)\not\subseteq K_0$：可容许真空，铅笔是唯一约束；
* 固定候选可精确判定（gcd/特征空间单射）；
* 自由参数的空/非空仍开放，需要结构判据或消元。

## 放弃原因

* 未给出自由参数的好 locus 非空判据；
* 未把泄漏量 $J_V$ 与铅笔好性定量联系；
* 未 Lean 化。

## 残留价值

* 泄漏分支的清晰刻画；
* 与 207 的 $J_V$ 公式衔接；
* 为 $c\ge2$ 泄漏 gadget 提供 $c=1$ 的对照。

## 相关文件

* [attempts/207](../../../q1_true/multiplication_gate/attempts/207_64_verdict_implementation.md)（局部刚性、$J_V$）
* [attempts/188](188_c1_outside_D.md)（可容许真空）
* [attempts/191](191_c1_pencil_criterion.md)（铅笔判据）

## 状态

* 刻画：**[M2]**。
* 自由参数判据：**[开放]**。
