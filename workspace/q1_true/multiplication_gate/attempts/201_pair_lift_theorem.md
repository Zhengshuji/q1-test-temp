# pair-lift 定理：$\mathcal L_V=(V+AV)^\perp$

> 2026-11-09。专家 63 号的 Task A：写出 $\mathcal L_V=\{l:lN|_V=0,\ lAN|_V=0\}$ 的纤维描述。
> 结论：$\mathcal L_V=(V+AV)^\perp$；$\dim=n-\dim(V+AV)$；且每个 $h\in\operatorname{Ann}(V)$ 都可提升。
> 这把 188 的“个别提升”升级为精确的线性代数定理。状态：**M2（纸面，短证明）**。

## 目标

给出固定 $V\subseteq K_0$ 时可行行 $l$ 的空间、其维数、行对映射的像，以及观测器条件。

## 设想与理由

$lN|_V=0$ 意味着 $l$ 在 $V$ 上为零；$lAN|_V=0$ 意味着对 $v\in V$，$lANv=l(Av)=0$，即 $l$ 在 $AV$ 上为零。
所以 $\mathcal L_V$ 就是 $V+AV$ 的零化子。

## 做法

### 定理（pair-lift）

对任意 $V\subseteq K_0$，
$$\boxed{\mathcal L_V=(V+AV)^\perp\subseteq\mathcal X^*},\qquad
\dim\mathcal L_V=n-\dim(V+AV).$$

*证明*：$lN|_V=0\iff l|_V=0$（因 $N$ 的列张成 $K_0$，$V\subseteq K_0$）；$lAN|_V=0\iff l|_{AV}=0$。
两者合起来即 $l|_{V+AV}=0$。$\square$

### 行对映射

$\Theta:\mathcal X^*\to K_0^*\oplus K_0^*$，$\Theta(l)=(lN,lAN)$。限制到 $\mathcal L_V$：
$$\dim\Theta(\mathcal L_V)=|K_0+AK_0+V+AV|-|K_0+AK_0|,$$
因为 $\ker\Theta=(K_0+AK_0)^\perp$，故
$$\ker\Theta|_{\mathcal L_V}=(K_0+AK_0+V+AV)^\perp.$$

### 每个 $h\in\operatorname{Ann}(V)$ 都可提升

$l\mapsto lN$ 在 $\mathcal L_V$ 上的像是
$$\{h\in K_0^*:\ h|_{K_0\cap(V+AV)}=0\}=(K_0\cap(V+AV))^\perp.$$
因 $V\subseteq K_0\cap(V+AV)$，有 $\operatorname{Ann}(V)=(K_0/V)^*\subseteq(K_0\cap(V+AV))^\perp$。
所以**每个** $h\in\operatorname{Ann}(V)$ 都有 $l\in\mathcal L_V$ 使 $lN=h$。
（这解释了 188：个别提升总是存在；182 的超平面限制来自“$Av\in K_0$ 时所有提升给出同一个 $h_A$”。）

### 观测器条件（固定 $V$）

1. 顶行：$L_0\subseteq\mathcal L_V$（等价 $V\subseteq W_L$）；
2. 秩：$q-r$ 个底部行的 $h_i=l_iN$ 在 $\operatorname{Ann}(V)/\operatorname{row}(L_0N)$ 中的投影秩 $\omega-\rho_0$；
3. 铅笔：由选出的对 $(h_i,h_{A,i})$ 诱导的 $Z$ 满足
   $\ker(A_*-\lambda I)\cap\ker B_*=\{0\}\ \forall\lambda$；
4. 提升完成：$\mathsf P_{\rm ind}$ 下 $\dim\ker Z_{\rm pair}\le d'_C$。

## 进展

* Task A 的 pair-lift 定理完成：$\mathcal L_V=(V+AV)^\perp$；
* 维数与行对像的维数公式；
* “每个 $h$ 可提升”的一般证明（不依赖 $Av\in K_0$）；
* 观测器四条件整理。

## 最终结论

* 行提升空间是 $V+AV$ 的零化子；
* 可容许性对 $h$ 没有限制；
* 真正的约束是秩、铅笔、提升完成——与 182 的机制一致：$Av\in K_0$ 时 $h_A$ 被 $h$ 决定。

## 放弃原因

* 未把“秩+铅笔+完成”的联合可行性写成算法；
* 未处理 $\mathsf P_{\rm full}$ 的完成条件；
* 未 Lean 化。

## 残留价值

* 一个干净的 pair-lift 定理；
* 把 188 升级为精确公式；
* 为 Task B（gadget 实现）提供接口。

## 相关文件

* [attempts/188](../../../q1_false/c_stratification/attempts/188_c1_outside_D.md)（个别提升）
* [attempts/195](../../arm_reduction/attempts/195_lift_individual_vs_simultaneous.md)（同时组装）
* [attempts/152](../../../q1_false/c_stratification/attempts/152_lift_completion_fixed_l0.md)（$d'_C$）
* [attempts/200](200_multiplication_gadget.md)（gadget）

## 状态

* 定理：**[已证-纸面，M2]**。
* 联合可行性算法：**[未做]**。
