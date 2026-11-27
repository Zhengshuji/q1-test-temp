# 518 $q=r_0=2$ 的乘积门必败：$\omega=q$ 的特征值障碍

> 2026-11-27。511 的 $(5a)$ 门可以用 $E\ne0$ 真正落地（$n=5$、$C=e_5^{\mathsf T}$、$k=3$）。
> 但本文件证明：**只要门上 $\operatorname{rank}H_0=q=2$，$(5b)$ 必失败**——
> 这正是 493 引理 A，固定行 $q=2$ 的乘积门因此整体不可行。状态：**[已证-纸面]** + **[精确验证]**。

## 落地（$E\ne0$）

$n=5$、$C=e_5^{\mathsf T}$、$K_0=\operatorname{span}(e_1,e_2,e_3)$：
$$A=\begin{bmatrix}1&0&0&0&0\\1-y&0&1&0&0\\-2&-1&y-1&0&0\\z&x&0&0&0\\0&0&0&1&0\end{bmatrix},
\qquad
L_0=\begin{bmatrix}z&x&0&1&0\\1&0&1&0&0\end{bmatrix}.$$
（$Ae_5=e_4$ ⇒ $CA=e_4^{\mathsf T}$；$A(K_0)\not\subseteq K_0$ 因 $Ae_1$ 有 $e_4$ 分量 $z$。）

压缩数据：$H_0=L_0N$、$H_{A,0}=L_0AN$，精确计算
$$D_1=\det[h_1;h_2;a_1]=x(z-xy),\qquad D_2=\det[h_1;h_2;a_2]=z-xy .$$
所以 $(5a)\iff z=xy$——与 511 相同，但这次是**真实观测器数据**（$E\ne0$）。

## 定理：$(5b)$ 必失败

门上 $z=xy$、$x\ne0$ 时 $\operatorname{rank}H_0=2=q$。$(5a)$ 给 $H_{A,0}=ZH_0$（$Z$ 为 $2\times2$），故
$$P(\lambda)=(\lambda I_2-Z)H_0,\qquad \operatorname{rank}P(\lambda)=\operatorname{rank}(\lambda I_2-Z).$$
$\det(\lambda I_2-Z)$ 在 $\mathbb C$ 上必有根，所以某个 $\lambda$ 处 $\operatorname{rank}P<2$，$(5b)$ 失败。$\square$

精确核验：[518_verify.py](518_verify.py)（三子式 $\gcd=x(\lambda^2-\lambda y+y)$，非常数）。

## 解释 511–517 的全部失败

- 511–517 的门全部落在 $\omega=q=2$ 的 regime；
- 每次“改 $l_2$/第三行”只是换 $Z$，特征值总存在，所以 gcd 永远非常数；
- 512 的 $Q$、514 的 $D_2=a^2x$、516 的杂项，都是这个特征值障碍的不同表现。

## 含义

- 固定行 $q=r_0$ 的乘积门要可行，必须 $\omega<q$（即 $\operatorname{rank}H_0\le q-1$）；
- 对 $q=2$ 这要求 $\omega=1$，而 $z=xy$ 的门需要 $\operatorname{rank}H_0=2$——矛盾；
- 所以 $q=2$ 的固定行乘积门**整体不可行**；下一步只能 $q\ge3$ 且 $\omega\le q-1$，或回到自由行 gadget（296 的 $\omega=1<q=2$ 正是可行的那一类）。

## 状态

- 落地 + $(5a)\iff z=xy$：**[精确验证]**；
- $\omega=q$ 障碍：**[已证-纸面]**；
- $q\ge3$、$\omega<q$ 的门：**[未做]**。
