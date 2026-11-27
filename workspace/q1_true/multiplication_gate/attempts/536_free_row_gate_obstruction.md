# 536 自由行门的结构障碍：$\lambda=0$ 的秩与 $u_3$ 的自由度

> 2026-11-27。535 的 ansatz 之后，追问“门能否放在自由行 $u=(u_1,u_2,u_3)$ 上”。
> 本文件给出两条先决约束，把下一步的搜索空间定死。状态：**[已证-纸面]**。

## 设定

$q=5$、$k=3$、$H=[H_0;u;v]$、$H_A=[0;0;0;uB;vB]$（$B$ 固定）。

## 引理 1：$\lambda=0$ 要求 $\operatorname{rank}H_A=\omega$

$(5b)$ 在 $\lambda=0$ 给 $\operatorname{rank}H_A=\omega$。若 $H_A$ 的前三行（固定行）为零，
则 $\operatorname{rank}H_A\le2$ ⇒ $\omega\le2$。

## 引理 2：$H_0=\operatorname{diag}(1,1,0)$ 时 $u_3=v_3=0$

$\omega=2$ 且 $\operatorname{rank}H_0=2$（$=\operatorname{span}\{e_1,e_2\}$）时，$u,v$ 必须落在
$\operatorname{span}\{e_1,e_2\}$ 里（否则 $\operatorname{rank}H\ge3$）。于是 $u_3=v_3=0$，
**门 $u_3=u_1u_2$ 不可能**。

## 推论

要在自由行上编码 $u_3=u_1u_2$，必须：

1. $H_0$ 的秩 $\le1$（否则 $u_3$ 被压成 0 或 $\omega\ge3$）；
2. $\omega=2$，且 $\operatorname{rank}H_A(0)=2$（$uB,vB$ 独立）；
3. $B$ 不能让 $P(1)$ 塌成秩 1（否则 $\lambda=1$ 处失败）。

## 唯一剩下的最小形状

$H_0=[e_1;0;0]$（秩 1），$u,v$ 张成含 $e_1$ 的平面之外的二维空间，$\omega=2$；
$B$ 待选，使 $\gcd_\lambda\{2\times2\ \text{子式 of}\ \lambda H-H_A\}=1\iff u_3=u_1u_2$。

## 下一步

在 $H_0=[e_1;0;0]$、$B$ 取小整数矩阵的族里做符号搜索：
$u=(u_1,u_2,u_3)$、$v=(v_1,v_2,v_3)$ 为符号，计算子式 gcd 作为 $u,v$ 的多项式，
找形如 $u_3-u_1u_2$ 的因子。

## 状态

- 引理 1、2：**[已证-纸面]**；
- $H_0$ 秩 1 的搜索：**[未做]**。
