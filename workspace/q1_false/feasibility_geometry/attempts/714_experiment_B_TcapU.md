# 714 实验 B：$T\cap U$ 的方向交互（$Z'=0$ 情形）

> 2026-11-27。在小例上验证：决定可行性的不只是 $t=\dim T$，还有 $T\cap U$。
> 状态：**[已证-纸面]** + **[精确验证]**。

## 定理（$Z'=0$）

设 $Z'=0$、$d'>0$。若 $T\cap U=\{0\}$（$U=\operatorname{row}H$），则不可行。

**证明**：$Z'=0$ 时 $HZ'=0$，$G=ZH$；$G$ 的行在 $T$，而 $Z_iH\in U$，故 $G_i\in T\cap U=0$ ⇒ $G=0$。于是
$$P(0)=-H_A=-ZH-G=0,$$
秩 $0<d'$ ⇒ $(5b)$ 失败。$\square$

## 构造（$Z'=0$、$T\cap U=U$ 时可行，$d'=1$）

$k=2$、$q=3$、$T=\operatorname{span}\{e_1\}$、$Z'=0$、$H=u e_1^{\mathsf T}$（$u=(1,0,1)$，故 $U=\operatorname{span}\{e_1\}=T$，$T\cap U=U$）。
取 $Z$ 满足 $Zu=e_2$：
$$Z=\begin{bmatrix}0&0&0\\1&0&0\\0&0&0\end{bmatrix}.$$
则 $G=ZH=e_2e_1^{\mathsf T}$（行在 $T$），
$$P(\lambda)=(\lambda u-e_2)e_1^{\mathsf T},$$
$\lambda u=e_2$ 无解 ⇒ 秩 1 对所有 $\lambda$。sympy：$\operatorname{rank}M=2=2d'$ ⇒ 可行 ✓。

## 对照

| $v$（$U=\operatorname{span}v$） | $T\cap U$ | 结果 |
|---|---|---|
| $e_1$ | $U$（1 维） | 可行（构造如上） |
| $e_2$ | $0$ | 不可行（定理） |

## 意义

- 决定方向可行性的不是 $t$ 单独，而是 $T\cap U$（以及 $T$ 在 $U$ 外的部分）；
- 这与 ChatGPT 的“$\mathfrak I(H)$ 含 $\dim(T\cap U)$”一致；
- $Z'=0$ 时给出干净的必要条件：$T\cap U\ne0$（对 $d'>0$）。

## 状态

- 定理：**[已证-纸面]**；
- 构造与对照：**[精确验证]**；
- 一般 $Z'$ 的 $T\cap U$ 理论：**[未做]**。
