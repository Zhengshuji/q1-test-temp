# $c=3$ 分量界：不变部分 + $B_{u,v}$ Bézout 界的显式形式

> 2026-11-08。专家 60 号指出：159 的“每层不可约”对非不变层**不成立**（(2a)/(1b) 的底是秩层）；
> 正确的 $c=3$ 分量界应是不变部分（169）+ 非不变部分的 $B_{u,v}$ 分量数（171 的 Bézout 界）。
> 本文件给出显式公式。状态：**M2（纸面，Bézout 引用）**。

## 目标

用 169 + 171 给出 $c=3$ 的**严格（粗糙）分量上界**，取代 159 的“每层不可约”计数。

## 设想与理由

$c=3$ 的非不变层是 $t=0,1,2$；每层通过 incidence 归约到 $B_{u,v}$（161/171）。
由专家 60 号 §5：每个 $B_{u,v}$ 的不可约分量对相应的 exact $(t,u,v)$ incidence 层贡献**至多一个**
不可约分量。所以
$$N_3\le N_{\rm inv}(3)+\sum_{t=0}^{2}\sum_{u=t}^{\min(2t,3)}\sum_{v=t}^{u}b_{u,v}.$$

## 做法

### 不变部分

$c=3$ 的特征值标号 Jordan 型：分拆 $3$（$s$ 种）、$2+1$（$s^2$ 种）、$1+1+1$（$s^3$ 种）：
$$N_{\rm inv}(3)\le s+s^2+s^3.$$

### 非不变部分（$k=\dim K_0$）

Bézout 界（171）：$b_{u,v}\le\binom{k}{u}(2(u-v+1))^{u(k-u)}$（$0\le u-v<\min(u,n-u)$；
满秩情形 $u-v=\min(u,n-u)$ 时 $B_{u,v}$ 开、不可约；超过则空）。

$c=3$ 的 $(t,u,v)$ 与 $b_{u,v}$：

| $t$ | $u$ | $v=t$ | $r=u-v$ | $b_{u,v}$ 上界 |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1（单点）|
| 1 | 1 | 1 | 0 | $\binom{k}{1}2^{k-1}$ |
| 1 | 2 | 1 | 1 | $\binom{k}{2}4^{2(k-2)}$ |
| 2 | 2 | 2 | 0 | $\binom{k}{2}2^{2(k-2)}$ |
| 2 | 3 | 2 | 1 | $\binom{k}{3}4^{3(k-3)}$ |

**exact 层只需 $v=t$**（176 §5：$W\subseteq U\cap A^{-1}U\subseteq V\cap A^{-1}V=W$，故 $v=t$），
所以 $v>t$ 的项不必计入。

### 汇总

$$\boxed{N_3\le s+s^2+s^3+\binom{k}{1}2^{k-1}
+\binom{k}{2}\big(4^{2(k-2)}+2^{2(k-2)}\big)
+\binom{k}{3}4^{3(k-3)}.}$$

**$k=4$**：
$$N_3\le s+s^2+s^3+32+1536+96+256
=s+s^2+s^3+1921.$$

## 进展

* $c=3$ 的严格分量上界已写出（不变 + Bézout 界）；
* 159 的 $\binom{s}{3}+\binom{s}{2}+2s^2+4s+3$ 是“期望计数”，在非不变层不可约性未证前**不是定理**；
  本文件的界是**严格但粗糙**的。

## 最终结论

* $c=3$ 的严格界：$N_3\le s+s^2+s^3+1921$（$k=4$）；
* 一般 $k$ 的显式式如上；
* 159 的紧计数保留为“期望/特殊 $A$ 下可证”的目标，不作一般定理。

## 放弃原因

* Bézout 界很粗糙（$k=4$ 时 1921）；
* 未证每个 $B_{u,v}$ 的实际分量数（一般不可约性为假，见 171 反例）；
* incidence 纤维论证见 [176](../../c_stratification/attempts/176_incidence_fibre_argument.md)（已写全；$v=t$ 的收紧也见 176 §5）。

## 残留价值

* $c=3$ 的第一个**严格**分量上界（不依赖不可约性猜想）；
* 与 159 的期望计数形成对照。

## 相关文件

* [attempts/159](../../c_stratification/attempts/159_c3_component_bound_corrected.md)（期望计数，降级）
* [attempts/169](../../c_stratification/attempts/169_invariant_strata_irreducibility.md)（不变部分）
* [attempts/171](../../c_stratification/attempts/171_Buv_rank_strata.md)（Bézout 界）
* [attempts/176](../../c_stratification/attempts/176_incidence_fibre_argument.md)（incidence 纤维论证）
* [attempts/170](../../c_stratification/attempts/170_c3_strata_table.md)（十一层）

## 状态

* 严格界：**[已证-纸面，M2]**（Bézout 引用；incidence 纤维论证引用专家 60 号 §5）。
* 159 的紧计数：**[降级为期望]**。
