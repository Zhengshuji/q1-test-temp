# pair-lift 纤维定理：固定 $V$ 的行对纤维与同时完成

> 2026-11-09。专家 64 号的第 2 项：给出固定 $V$ 时行对提升的精确纤维描述。
> 本文件把 201/195 的结果整理成一条纤维定理，并给出可解性/同时完成的公式。状态：**M2（纸面）**。

## 目标

固定 $V\subseteq K_0$，描述：
1. 可容许行空间 $\mathcal L_V$；
2. 对给定压缩行 $h$，所有提升 $l$ 的纤维；
3. 对给定行对 $(h,g)$，可实现性与纤维维数；
4. 同时选择多行时的完成条件。

## 设想与理由

$\mathcal L_V=(V+AV)^\perp$（201）。行对映射 $\Theta(l)=(lN,lAN)$；核为 $(K_0+AK_0)^\perp$。
对固定 $h$，提升的差在 $\ker(l\mapsto lN)=\operatorname{ann}(K_0)=\operatorname{row}[C;CA]$ 中。

## 做法

### 1. 可容许行空间

$$\mathcal L_V=(V+AV)^\perp,\qquad \dim\mathcal L_V=n-\dim(V+AV).$$

### 2. 固定 $h$ 的提升纤维

设 $h\in\operatorname{Ann}(V)$，$l_0$ 是任一提升（$l_0N=h$）。则
$$\{l:\ lN=h\}=l_0+\operatorname{row}[C;CA].$$
可容许子集
$$\{l\in\mathcal L_V:\ lN=h\}=l_0+\{g\in\operatorname{row}[C;CA]:\ g|_{AV}=-l_0|_{AV}\}.$$
这是仿射空间；非空条件
$$l_0|_{AV}\in\operatorname{im}\big(g\mapsto g|_{AV}\big).$$
由 201，每个 $h$ 都有可容许提升（取 $l\in(V+AV)^\perp$），故非空总成立。

### 3. 行对的纤维

$\Theta:\mathcal L_V\to K_0^*\oplus K_0^*$。对给定 $(h,g)\in\Theta(\mathcal L_V)$，纤维
$$\Theta^{-1}(h,g)=l_0+\big(\operatorname{row}[C;CA]\cap\mathcal L_V\cap\ker\Theta\big),$$
维数为
$$\dim\ker\Theta|_{\mathcal L_V}=n-\dim(K_0+AK_0+V+AV).$$
可实现性：$(h,g)\in\operatorname{im}\Theta$，即 $hN^{-1}$ 与 $g$ 来自同一 $l$。

### 4. 同时完成

选 $q-r$ 个底部行对 $(h_i,g_i)$。需要：
- $\operatorname{rank}H=\omega$（$h_i$ 在 $\operatorname{Ann}(V)/\operatorname{row}(L_0N)$ 的投影秩 $\omega-\rho_0$）；
- $\mathsf P_{\rm ind}$ 下 $\dim\ker Z_{\rm pair}\le d'_C$（152）；
- 铅笔好（$B_*$ 在特征空间单射）。

**注意**：第 3 条的纤维维数公式给出“每个行对有多少提升”；第 4 条的 $d'_C$ 给出“能否同时选到足够独立的行”。
两者不同，不能混淆（195）。

## 进展

* 纤维定理整理完成：$\mathcal L_V$、单行纤维、行对纤维、同时完成；
* 与 201/195/152 一致；
* 明确“个别纤维”与“同时完成”的分界。

## 最终结论

* 固定 $V$ 的行对纤维是仿射空间，维数由 $\ker\Theta|_{\mathcal L_V}$ 给出；
* 同时完成由 $d'_C$ 不等式控制；
* 这为求解器的“提升层”提供精确公式。

## 放弃原因

* 未把纤维定理写成算法（求解器已隐式实现）；
* 未 Lean 化纤维维数；
* 未处理 $\mathsf P_{\rm full}$ 的完成条件。

## 残留价值

* 一条完整的 pair-lift 纤维定理；
* 明确了“个别/同时”的公式分界。

## 相关文件

* [attempts/201](201_pair_lift_theorem.md)
* [attempts/195](../../arm_reduction/attempts/195_lift_individual_vs_simultaneous.md)
* [attempts/152](../../../q1_false/c_stratification/attempts/152_lift_completion_fixed_l0.md)
* [attempts/207](207_64_verdict_implementation.md)

## 状态

* 纤维定理：**[已证-纸面，M2]**。
* Lean/算法化：**[未做]**。
