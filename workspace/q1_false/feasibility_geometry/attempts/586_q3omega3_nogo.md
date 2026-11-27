# 586 $q=\omega=3$ 的 no-go：$\det P$ 必须恒为常数，至少两个条件

> 2026-11-27。585 之后，检查 $q=3$、$\omega=3$ 的一般情形。
> **结论：$\det P$ 必须是非零常数，要求 $\lambda^3,\lambda^2,\lambda$ 三个系数同时为零——
> 至少两个独立条件，无法编码单一乘积关系。**
> 状态：**[已证-纸面]**。

## 设定

$q=3$、$k\ge3$、$\omega=\operatorname{rank}H=3$（$H$ 行满秩）。
$(5b)$ 要求 $\operatorname{rank}P(\lambda)=3$ 对所有 $\lambda$，即
$$\det P(\lambda)\ne0\quad\forall\lambda .$$
$\det P$ 是 $\lambda$ 的至多三次多项式；要在 $\mathbb C$ 上处处非零，必须**恒为非零常数**。

## 系数

$$\det P=\lambda^3\det H-\lambda^2C_2+\lambda C_1-C_0,$$
$C_2$（二次齐次）、$C_1$（一次齐次）、$C_0=\det(a_1,a_2,a_3)$（常数）。

$\det P$ 恒为非零常数 $\iff$
$$\det H=0,\qquad C_2=0,\qquad C_1=0,\qquad C_0\ne0 .$$
（$\det H=0$ 与 $H$ 行满秩矛盾！）

## 更强的问题

$\omega=3$ 需要 $H$ 行满秩 ⇒ $\det H\ne0$ ⇒ $\lambda^3$ 项非零 ⇒ $\det P$ 是非常数三次多项式
⇒ 在 $\mathbb C$ 上有根 ⇒ $(5b)$ 失败。

**所以 $q=3$、$\omega=3$ 根本不可行**——这与 518 的“$\omega=q$ 不可行”一致。

## 推论

$q=3$ 的可行实例必须 $\omega\le2$；此时 $(5b)$ 用 $2\times2$ 子式的 gcd，
$\det P$ 不是判据，3×3 行列式路线在这里不适用。

## 状态

- $q=\omega=3$ no-go：**[已证-纸面]**（即 518 的特例）；
- $q=3,\omega=2$ 的 3×3 det 路线：**[已由 584/585 分析]**。
