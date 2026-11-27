# 偏移线不可能性：$o\\notin U$ 时 $U$ 被钉死，$o\\in U$ 时 $(5b)$ 掉秩

> 2026-11-09。把 259 的负搜索升级为结构定理（线偏移）：
> 设偏移子空间是一条线 $O=\\langle o\\rangle$，$o\\ne0$，$M$ 可逆，$U=\\operatorname{span}\\{x_1,x_2\\}$ 是二平面，
> $$v_i=Mx_i+s_i o\\in U\\quad(i=1,2).$$
> 则：
> 1. $o\\in U$ ⇒ $U$ 是 $M$ 的不变二平面 ⇒ $(5b)$ 在 $M|_U$ 的特征值处掉秩；
> 2. $o\\notin U$ ⇒ 在一般位置（$U+\\langle o\\rangle\\ne M^{-1}(U+\\langle o\\rangle)$）$U$ 被**唯一确定**，
>    没有连续族，不能编码乘法。
> 状态：**M2（纸面）**。

## 目标

把 259 的“搜索为负”升级为线偏移的结构障碍。

## 设想与理由

256 处理 $o=0$（$U$ 不变 ⇒ $(5b)$ 失败）。257 指出偏移可吸收 $(5a)$。
本文件处理 $O$ 为一维线的一般情形，证明它不能给出连续的门族。

## 做法

### 1. $o\\in U$

$s_i o\\in U$，故 $v_i\\in U\\iff Mx_i\\in U$。$x_1,x_2$ 张成 $U$，所以 $MU\\subseteq U$。
$M|_U$ 在 $\\mathbb C$ 上有特征值 $\\lambda_0$；在 $\\lambda_0$ 处 $P$ 在 $U$ 上掉秩，
与 $(5b)$ 矛盾（同 256）。

### 2. $o\\notin U$

令 $H=U+\\langle o\\rangle$（3 维）。$v_i\\in U\\subset H$，且 $s_i o\\in H$，故
$$Mx_i=v_i-s_i o\\in H.$$
于是 $x_i\\in M^{-1}H$。又 $x_i\\in U\\subset H$，所以
$$U\\subseteq H\\cap M^{-1}H.$$
若 $H\\ne M^{-1}H$，则 $\\dim(H\\cap M^{-1}H)=2$，故
$$U=H\\cap M^{-1}H.$$
但 $H=U+\\langle o\\rangle$ 由 $U$ 决定，所以这是 $U$ 的一个**固定点方程**；
解是低维的（至多有限或曲线；至少不是 4 维族），不能支撑 $2\times2$ Plücker 门。

若 $H=M^{-1}H$（即 $MH=H$），则 $U$ 可在 $H$ 内变化（$\\operatorname{Gr}(2,H)=\\mathbb P^2$，最多 2 维族），
仍不是 Plücker 门所需的 4 维族；且 $M|_H$ 有特征线，$U$ 需避开它，进一步限制。

### 3. 结论

线偏移 $O=\\langle o\\rangle$ 下：
- $o\\in U$：$(5b)$ 失败；
- $o\\notin U$：$U$ 被钉死（或最多 2 维族），没有连续 4 维 Plücker 族。

所以线偏移不能实现 $2+2$ 特征空间的乘法门。

## 进展

* 259 的负搜索有了结构解释；
* 线偏移的两种情形都封住；
* 与 256/257 一致。

## 最终结论

* **线偏移不可能**给出不变平面乘法门（在 $M$ 可逆、$H\\ne M^{-1}H$ 的一般情形）；
* $MH=H$ 的例外最多给 2 维族，不足以做 $2\\times2$ Plücker 门；
* 高维偏移（$\\dim O\\ge2$）在 257 中已是一般位置自动/受限，仍不乐观；
* 不变平面门目前**没有可行构造**。

## 放弃原因

* 未处理 $M$ 不可逆；
* 未完全排除 $MH=H$ 的例外；
* 未处理 $\\dim O\\ge2$ 的所有非一般位置。

## 残留价值

* 一个清晰的结构定理（线偏移）；
* 把 259 的负搜索升级为解释；
* 明确剩余例外。

## 相关文件

* [attempts/259](../../../q1_true/multiplication_gate/attempts/259_true_offset_search.md)
* [attempts/257](../../../q1_true/multiplication_gate/attempts/257_offset_absorption.md)
* [attempts/256](../../../q1_true/multiplication_gate/attempts/256_invariant_gate_spectral_obstruction.md)

## 状态

* 线偏移：**[M2 纸面]**。
* 例外/高维偏移：**[未完成]**。
