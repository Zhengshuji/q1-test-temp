# $q=4$ rank-one 门的谱张力：$E$ 放固定方向保行列式但掉秩，放自由方向保秩但破行列式

> 2026-11-09。继续 Route A 的 $q=4,r_0=2,\\omega=3$ 落地。
> 显式计算揭示一个设计张力：
> - $E$ 的偏移放在固定方向 $e_1,e_2$：$(5a)$ 自动，$\\det P=(\\lambda-2)^2(\\lambda-1)(\\lambda+1)\\det Z$，
>   但在自由特征值 $\\lambda=2$ 处 $\\operatorname{rank}P=2<3$；
> - $E$ 的偏移放在自由方向 $e_3,e_4$：$\\det P$ 在 $\\det Z=0$ 上不恒为零，且 $\\lambda=0,2$ 处 rank 4。
> 两种放法都不能同时满足 $(5a)(5b)$。状态：**M2 + 精确计算**。

## 目标

为 275 的压缩门找 $E$ 的放置，使 $(5a)(5b)$ 同时成立。

## 设想与理由

$q=4$，$H_0=[e_1;e_2]$，$Y$ 支持在 $e_3,e_4$：
$$H=\\begin{bmatrix}1&0&0&0\\\\0&1&0&0\\\\0&0&r_{11}&r_{12}\\\\0&0&r_{21}&r_{22}\\end{bmatrix}.$$
固定块取 $H_{A,0}=M H_0$，$M=\\begin{bmatrix}0&1\\\\1&0\\end{bmatrix}$（交换），
避免 $M=I$ 的 $\\lambda=1$ 全掉秩。

$E$ 的偏移只影响自由行的 $H_A$；比较两种放置。

## 做法：两种 $E$

### 1. $E$ 在固定方向

自由行 $H_A$ 为
$$(s_1,s_2,2r_{11},2r_{12}),\\qquad(t_1,t_2,2r_{21},2r_{22}).$$
则 $(5a)$ 自动（$s e_1+t e_2$ 在 $\\operatorname{row}H$ 内），且
$$\\det P=(\\lambda-2)^2(\\lambda-1)(\\lambda+1)\\,(r_{11}r_{22}-r_{12}r_{21}).$$
在门 $r_{11}r_{22}=r_{12}r_{21}$ 上 $\\det P\\equiv0$；但
$$\\operatorname{rank}P(2)=2<3,$$
$(5b)$ 失败（自由特征值 2）。

### 2. $E$ 在自由方向

自由行 $H_A$ 为
$$(0,0,2r_{11}+s_1,2r_{12}+s_2),\\qquad(0,0,2r_{21}+t_1,2r_{22}+t_2).$$
则 $\\det P$ 在 $\\det Z=0$ 上**不**恒为零（含 $s_i,t_i$ 的项），且
$$\\operatorname{rank}P(0)=4,\\quad \\operatorname{rank}P(2)=4,$$
$(5b)$ 失败（秩过高，$\\det P\\ne0$）。

## 输出

`c280_tension.py`：
```
case 1 det P = (lam - 2)**2*(lam - 1)*(lam + 1)*(r11*r22 - r12*r21)
case 1 ranks at 0,1,2,3 = [3,3,2,3]
case 2 det P = (lam - 1)*(lam + 1)*(...)
case 2 ranks at 0,1,2,3 = [4,3,4,3]
PASS
```

## 进展

* 两种 $E$ 放置的精确谱行为；
* 明确张力：固定方向保行列式、自由方向保秩，但不能兼得；
* $M$ 交换后 $\\lambda=1$ 不再是问题，但自由特征值 2 成为新掉秩点。

## 最终结论

* $q=4,r_0=2,\\omega=3$ 的 rank-one 门在两种自然 $E$ 放置下都失败；
* 要成功，需要更细的 $E$（混合方向/多列）或不同 $q,\\omega$；
* 这不是不可能性定理，但把可行 $E$ 的搜索空间压到了“混合方向”。

## 放弃原因

* 未穷举 $E$ 的所有混合放置；
* 未证 $q=4$ 不可能；
* 未接完整 $A,C,L_0$。

## 残留价值

* 一个清晰的谱张力；
* 精确的两种反例；
* 下一步的搜索约束。

## 相关文件

* [attempts/275](../../../q1_false/decision_algorithms/attempts/275_rankone_section_gate.md)
* [attempts/279](../../../q1_false/decision_algorithms/attempts/279_fixed_row_invariance.md)（撤回的错误论证）
* `tools/verification/c280_tension.py`

## 状态

* 张力：**[M2 + 精确计算]**。
* 混合 $E$：**[未做]**。
