# 519 $q=3$、$\omega=2$ 的压缩门存在；落地受 $E$ 的秩 1 限制

> 2026-11-27。518 说明 $q=r_0=2$ 的乘积门必败（$\omega=q$）。按 518 的下一步，试 $q=3$、$\omega=2$。
> **结果：压缩层找到真正的门**（$(5a)\iff z=xy$、$(5b)$ 成立），但 $n=5$ 的落地只有秩 1 的 $E$ 调整，
> 落地问题留下一个明确的小族。状态：**[精确验证]**（压缩层）+ **[未落地]**。

## 压缩门

$k=3$、$N=I_3$、$q=3$：
$$H_0=\begin{bmatrix}z&x&0\\y&1&0\\0&0&1\end{bmatrix},\qquad \det H_0=z-xy,$$
$$H_{A,0}=\begin{bmatrix}-2h_2-2h_3\\-2h_2-2h_3\\-2h_2-h_3\end{bmatrix},\qquad h_2=(y,1,0),\ h_3=(0,0,1).$$

**$(5a)$**：$z=xy$ 时 $h_1=(xy,x,0)=x h_2$，所以 $\operatorname{row}H_0=\operatorname{span}\{h_2,h_3\}$，
而 $H_{A,0}$ 的行都是 $h_2,h_3$ 的组合 ⇒ 行包含成立。反之 $z\ne xy$ 时 $\operatorname{rank}H_0=3$，行包含也成立
（$H_0$ 满秩）。所以 $(5a)$ 对所有参数成立——门来自 $(5b)$，不是 $(5a)$。

**$(5b)$**：门上 $\omega=2$，精确计算
$$\gcd\{2\times2\ \text{子式 of}\ \lambda H_0-H_{A,0}\}=1 .$$
所以门上 $(5b)$ 成立；而 $z\ne xy$ 时 $\omega=3=q$，由 518 的特征值障碍 $(5b)$ 必失败。
因此
$$\boxed{\text{q1 可行}\iff z=xy}$$
（压缩层）。核验：[519b_check.py](519b_check.py)（$\operatorname{rank}H_{A,0}=2$、$\gcd=1$）。

## 落地的限制

$n=5$、$C=e_5^{\mathsf T}$ ⇒ $CA=e_4^{\mathsf T}$ ⇒ $A$ 的第 5 行被固定为 $e_4$。
于是 $E$ 只有第 4 行自由（$1\times3$），
$$H_{A,0}=H_0A_{00}+u\,a,\qquad u=L_0[:,4]\in\mathbb C^3,\ a=E_{4,:}\in\mathbb C^{1\times3},$$
即调整项**秩 $\le1$**。而压缩门需要 $\operatorname{rank}H_{A,0}=2$，所以不能直接照搬。

## 下一步

在 $n=5$ 的族里解：$H_{A,0}=H_0A_{00}+u a$ 且门上行包含、$(5b)$ 成立。
已推导：若 $a\in\operatorname{span}\{h_2,h_3\}$ 且
$$A_{00}=\begin{bmatrix}\beta&0&0\\0&\beta&\gamma\\0&0&\gamma'\end{bmatrix},$$
则门上 $H_{A,0}$ 的行落在 $\operatorname{span}\{h_2,h_3\}$；剩下的是在这个 4 参数族里让 $(5b)$ 成立（gcd 为常数）。

## 状态

- 压缩门：**[精确验证]**（$(5a)$ 恒成立、门上 $\gcd=1$）；
- 落地：**[未完成]**（$E$ 秩 1 限制 + 4 参数族待算）。
