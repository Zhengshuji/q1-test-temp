# 不变特征空间障碍：$\dim(K\cap\ker A)>k-\omega\Rightarrow$ 全坏

> 2026-11-08。按专家 54 号：把“$\operatorname{row}Z_1\cap\operatorname{row}Z_2=0$”升级为更不变、
> 更强的**特征空间障碍**。状态：**M2（纸面）**；对任意 $k,\omega$ 成立。

## 目标

证明：

> **定理**：若 $\dim(K\cap\ker A)>k-\omega$，则每个可容许压缩点都在 $\lambda=0$ 处坏。
> 即
> $$\boxed{\dim(K\cap\ker A)\ge k-\omega+1\ \Longrightarrow\ \text{all bad at }0.}$$
> 对 $k=\omega+1$：$\dim(K\cap\ker A)\ge2$。

## 设想与理由

* 若 $v\in K\cap\ker A$，则 $Av=0$。$H_A=LAN$ 的每一行都是 $K$ 上的线性泛函，且湮灭 $v$。
* 所以 $\operatorname{rank}H_A\le k-\dim(K\cap\ker A)$。
* 若这个维数 $<\omega$，则 $P(0)=-H_A$ 秩 $<\omega$，在 $\lambda=0$ 处坏。
* 这比 $Z_1=0$ 更一般：$Z_1=0$ 只是让 $\ker T\subseteq\{0\}\times\ker A$，从而
  $\dim(K\cap\ker A)\ge\delta$；而定理允许 $Z_1\ne0$。

## 做法

**证明**：设 $v_1,\dots,v_s$ 是 $K\cap\ker A$ 的基，$s=\dim(K\cap\ker A)$。
对任意行 $h$ of $H_A$，$h=LAN$ 的某行，$h\,v_i=L A v_i=0$。故 $H_A$ 的每一行都湮灭
$V_0:=\operatorname{span}\{v_1,\dots,v_s\}$，于是 $H_A$ 在商 $K/V_0$ 上因子化：
$$\operatorname{rank}H_A\le\dim(K/V_0)=k-s.$$
若 $s>k-\omega$，则 $k-s<\omega$，故 $\operatorname{rank}H_A<\omega$，$\lambda=0$ 处坏。$\square$

**特殊情形**：
* $Z_1=0$：$\ker T\subseteq\{0\}\times\ker A$，故 $s\ge\delta$；若 $\delta>k-\omega$（超平面 $k=\omega+1$ 时 $\delta\ge2$），定理适用。
* $U_0=0$、$d=2$、$k=3$（138）：$k-\omega=1$；若 $s\ge2$ 则全坏；但 138 的全坏是用 $\lambda=-1$ 证的，
  说明零障碍不是唯一的。

**必要条件（对好候选）**：对任意 $\lambda$，
$$H_A-\lambda H=L(A-\lambda I)N,$$
故 $H_A-\lambda H$ 的每一行湮灭 $K\cap\ker(A-\lambda I)$，于是
$$\operatorname{rank}(H_A-\lambda H)\le k-\dim\big(K\cap\ker(A-\lambda I)\big).$$
若存在 $\lambda$ 使右端 $<\omega$，则好候选不可能。因此**好候选的必要条件**是
$$\boxed{\dim\big(K\cap\ker(A-\lambda I)\big)\le k-\omega\qquad\forall\lambda.}$$

## 进展

* 定理已证（一行商空间论证）。
* 它统一了 110/117/118 的“零障碍”，并给出一个对任意 $k,\omega$ 的充分条件。
* 它不是充要的：138 的坏根在 $\lambda=-1$，零障碍未必成立；好候选的必要条件 (4.7) 也只是必要。
* 与专家 54 号的 3.4 节一致：$\operatorname{rank}Q=\delta-1$ on $D_A$，$\delta$ off；零障碍对应 $v\in K\cap\ker A$。

## 最终结论

* **充分**：$\dim(K\cap\ker A)>k-\omega\Rightarrow$ 全坏（$\lambda=0$）。
* **必要**（对好）：$\dim(K\cap\ker(A-\lambda I))\le k-\omega$ 对所有 $\lambda$。
* 两者都不是充要；精确判据仍是分量上的 generic gcd。
* 这把“全坏”的条件从 $Z_1=0$ 这种坐标相关形式，升级为**不变的特征空间维数**。

## 放弃原因

* 没有给出充要条件；138 说明坏根可以在 $\lambda\ne0$。
* 只证了 $\lambda=0$ 的充分方向与一般 $\lambda$ 的必要方向。

## 残留价值

* 一条干净、坐标无关的充分条件与必要条件。
* 与 121 的超平面向量丛定理互补：121 给分量数，本文件给“某个分量必坏”的判据。
* 对论文的“all-bad obstructions”一节直接可用。

## 相关文件

* [attempts/121](121_hyperplane_vector_bundle.md)（超平面向量丛定理）
* [attempts/110](110_d2_all_bad_example.md)（$U_0=0$ 全坏）
* [attempts/117](../../decision_algorithms/attempts/117_d2_e1_v0z2_criterion.md)（$Y$ 与原像）
* [attempts/118](118_k_omega_plus_1_d2_attempt.md)（旧的充分条件）

## 状态

* 充分方向：**[已证-纸面，M2]**。
* 必要条件：**[已证-纸面]**。
* 充要：**[开放]**；精确判据是 generic gcd。
* **[Lean 内核-独立编译]**：抽象秩不等式 `rank_lt_of_large_kernel`
  （`workspace/augmentation_family/lean/RankKernel.lean`）；WSL 独立编译 exit 0；
  `#print axioms` = `[propext, Classical.choice, Quot.sound]`。未加入 `lake build MyProof`
  聚合图，故记 `[Lean 内核]` 而非 `[Lean]`。
