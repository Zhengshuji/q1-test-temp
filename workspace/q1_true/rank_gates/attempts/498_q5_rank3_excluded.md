# 498 $q=5$ 完整移位 $A$：rank-3 分支被排除（$(5a)$ 迫使 $\operatorname{rank}H_A\le2$）

> 2026-11-27。497 的 172 个失败点有统一解释：在这个 $A$、$L_0=[e_1;e_1]$ 下，
> 任何 rank-3 且满足 $(5a)$ 的 $H$ 都有 $\operatorname{rank}H_A\le2$，故 $\lambda=0$ 处 $(5b)$ 必失败。
> 状态：**[已证-纸面]**（该族）。

## 设定

$n=6$、$C=e_6^{\mathsf T}$、$A$ 为完整移位（$e_1\mapsto\cdots\mapsto e_6\mapsto0$）、$N=I_4$、
$P$ 取 $L$ 的 1–4 列、$Q$ 取 2–5 列：
$$H=LN=LP,\qquad H_A=LAN=LQ .$$
$L_0=[e_1;e_1]$，故 $H_A$ 的前两行是 $e_1Q=0$。

## 定理

若 $\operatorname{rank}H=3$ 且 $\ker H\subseteq\ker H_A$，则 $\operatorname{rank}H_A\le2$。

**证明.** 取 $0\ne v\in\ker H$，写 $u=Pv$、$w=Qv$。则 $Lu=0$、$Lw=0$。
对 $L$ 的任一自由行 $r$（6 维行向量），有 $r\cdot u=r\cdot w=0$，即（$u=(0,a,b,c,0,0)$、$w=(0,0,a,b,c,0)$，
记 $v=(0,a,b,c)$）
$$a r_2+b r_3+c r_4=0,\qquad a r_3+b r_4+c r_5=0 .$$
而 $rQ=(r_2,r_3,r_4,r_5)$，故**每一行 $rQ$ 都落在同一个 2 维子空间**
$$\{x\in\mathbb C^4:\ a x_1+b x_2+c x_3=0,\ a x_2+b x_3+c x_4=0\}$$
里（$(a,b,c)\ne0$ 时两条方程独立）。$H_A$ 的行正是 $rQ$（自由行）与 $0$（固定行），故 $\operatorname{rank}H_A\le2$。$\square$

**推论**：$\lambda=0$ 时 $P(0)=-H_A$，$\operatorname{rank}P(0)\le2<3=\omega$，$(5b)$ 失败。
结合 493 引理 A（$\omega=4$ 不可行），该族（$q=5$、完整移位、$L_0=[e_1;e_1]$）的可行实例只能有 $\omega\le2$。

## 与 285 的门的关系

285 的门在 $z=xy$ 时 $\operatorname{rank}H=2$（第三行是第二行的 $y$ 倍）——**正好是 $\omega=2$ 的可行侧**。
所以 rank-3 分支被排除并不否定这个门；下一步应直接在 $\omega=2$ 的层里检验 285 的门能否在这个 $A$ 下实现。

## 状态

- 定理：**[已证-纸面]**（该族）；
- $\omega=2$ 的门：**[未检验]**。
