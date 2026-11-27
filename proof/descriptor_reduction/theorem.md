# 约化 descriptor 铅笔：左指标 = $R$ 的右指标

> **等级**：**[已证-纸面]**（本文）+ **[精确验证 66/66]**（[verify.py](verify.py)，$n=6,7,8$）。
> 来源：专家 2026-11-02 §4.1 给出的等价链；本文把它写成定理并核对。

## 构造

设 $A,C,L$ 满足 $(5a)$，$H=\begin{bmatrix}L\\CA\\C\end{bmatrix}$（$(q+2p)\times n$），$h=\operatorname{rank}H$。
由 $(5a)$ 取常值分解 $LA=XL+Y_1CA+Y_2C$，记
$$D(\lambda)=\operatorname{diag}(\lambda I_q-X,\ I_p,\ I_p),\qquad Q'(\lambda):=D(\lambda)H .$$
则 $Q_L=P(\lambda)H=U D(\lambda)H=U Q'$，其中 $U$ 常值可逆 ⟹ $Q_L$ 与 $Q'$ **严格等价**。

取 $J\in\mathbb C^{h\times(q+2p)}$ 满行秩且 $\ker J=\ker H^{\mathsf T}$（例如 $H^{\mathsf T}$ 的 $h$ 个独立行），
定义**约化 descriptor 铅笔**
$$R(\lambda):=J\,D(\lambda)^{\mathsf T}=[\lambda E-E X^{\mathsf T}\ \ B],\qquad
J=[J_1\ J_2\ J_3],\ E=J_1,\ B=[J_2\ J_3].$$

## 定理

1. $\operatorname{rank}E=\operatorname{rank}L$，且 $[E\ B]=J$ 满行秩 $h$。
2. **（主结论）** $R$ 的**右最小指标 = $Q_L$ 的左最小指标**。

## 证明

**1.** $J$ 的行空间 $=$ $H^{\mathsf T}$ 的行空间 ⟹ 存在 $M$（$h\times n$）使 $J=M H^{\mathsf T}$，且 $M$ 在
$\operatorname{im}H^{\mathsf T}=$ $\operatorname{row}(H)$ 上单射。于是 $J$ 的前 $q$ 列
$=M\cdot(L^{\mathsf T})$（因为 $H^{\mathsf T}$ 的前 $q$ 列是 $L^{\mathsf T}$）。
$\operatorname{im}L^{\mathsf T}=\operatorname{row}(L)\subseteq\operatorname{row}(H)$，$M$ 在其上单射 ⟹
$$\operatorname{rank}E=\operatorname{rank}(M L^{\mathsf T})=\operatorname{rank}L^{\mathsf T}=\operatorname{rank}L .$$
$[E\ B]=J$ 满行秩是构造 ✓。

**2.** 对任意多项式向量 $y(\lambda)$：
$$R(\lambda)y=0
\iff J D(\lambda)^{\mathsf T}y=0
\iff D(\lambda)^{\mathsf T}y\in\ker J=\ker H^{\mathsf T}
\iff H^{\mathsf T}D(\lambda)^{\mathsf T}y=0
\iff (D(\lambda)H)^{\mathsf T}y=0
\iff Q'(\lambda)^{\mathsf T}y=0 .$$
（第二个 $\iff$ 用 $\ker J=\ker H^{\mathsf T}$。）

所以 $R$ 的**右**零模 $=$ $Q'$ 的**左**零模。
$Q'=U^{-1}Q_L$ 只差常值可逆左乘 ⟹ 左零模只差常值可逆右乘（同一个模）⟹ 生成元的次数相同 ⟹
$R$ 的右最小指标 $=$ $Q'$ 的左最小指标 $=$ $Q_L$ 的左最小指标 ✓。$\square$

## 为什么这有用

把"$Q_L$ 的左最小指标"（$q+2p$ 行的左零模）换成"$R$ 的右最小指标"（$h$ 行、$q+2p$ 列的
descriptor 铅笔 $[\lambda E-F\ B]$、$[E\ B]$ 满行秩、$\operatorname{rank}E=\operatorname{rank}L$）。
右零模有标准工具（最小多项式基、可控性指标），可以接 descriptor 系统的**可控性指标**理论。

## 验证

[tools/verification/descriptor_pencil.py](../../tools/verification/descriptor_pencil.py)：
$n=6,7,8$ 的 **66 个**满足 $(5a)$ 的铅笔上，$\eta(R)=\varepsilon(Q_L)$ 逐个相等（0 个不一致），
并核对 $\operatorname{rank}E=\operatorname{rank}L$。

**注意**：$J$ 必须取 $H^{\mathsf T}$ 的行（即 $H$ 的**列**），不能取 $H$ 的行——
后者会破坏 $\operatorname{rank}E=\operatorname{rank}L$（本轮实测发现，记在验证脚本的注释里）。
