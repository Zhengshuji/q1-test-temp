# 撤回：固定行不变性论证不成立

> 2026-11-09。曾尝试证明“$H_{A,0}=M H_0$ ⇒ $F$ 保持 $\\operatorname{row}H_0$ ⇒ $(5b)$ 掉秩”，
> 并推出 $q=4,r_0=2,\\omega=3$ 不可能。**该论证错误，结论撤回。**
> 状态：**撤回（M3 自查）**。

## 目标

判断固定行 $H_0$ 是否给出 $(5b)$ 的谱障碍。

## 设想与理由（错误版本）

由 $L_0A\\in S$ 得 $H_{A,0}=M H_0$，于是 $F H_0=H_{A,0}=M H_0$，
似乎 $\\operatorname{row}H_0$ 是 $F$ 的不变子空间；在 $M$ 的特征值处 $P$ 掉秩。

## 做法：错误所在

$H_A=FH$ 是**行组合**：$H_A$ 的每一行是 $H$ 的行的线性组合。
它**不**意味着 $F(\\operatorname{im}H)\\subseteq\\operatorname{im}H$。
列空间上只有
$$F(\\operatorname{im}H)=\\operatorname{im}H_A,$$
而 $\\operatorname{im}H_A$ 一般**不**包含于 $\\operatorname{im}H$。

因此不能从 $F H_0=M H_0$ 推出 $F$ 在 $\\operatorname{im}H$ 上有特征向量；
谱判据是
$$\\operatorname{im}H\\cap\\ker(\\lambda I-F)=\\{0\\},$$
在 $q=3,\\omega=2$ 时这个交可以是 0（244 就是例子）。

**244 反例**：$H$ 秩 2、$q=3$，$H_0$ 行与 $F$ 的关系并不导致 $P$ 掉秩；
$\\gcd$ 的 $2\\times2$ 子式为 1。

## 进展

* 发现并撤回一个错误的“不可能性”论证；
* 明确行包含 $H_A=FH$ 与列空间不变性的区别；
* 避免把 275 误判为不可落地。

## 最终结论

* $q=4,r_0=2,\\omega=3$ 的可行性**仍开放**；
* 275 的压缩门仍可能落地；
* 固定行的作用必须通过 $\\operatorname{im}H\\cap\\ker(\\lambda I-F)$ 分析，不能用行空间不变性。

## 放弃原因

* 论证不成立；
* 未给出替代的可行性/不可能性结果。

## 残留价值

* 一个明确的错误记录，避免重复；
* 强调行包含与列空间不变性的区别。

## 相关文件

* [attempts/275](275_rankone_section_gate.md)
* [attempts/277](277_gram_fpt.md)

## 状态

* 论证：**[撤回]**。
* $q=4,r_0=2,\\omega=3$：**[仍开放]**。
