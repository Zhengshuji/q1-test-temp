# 665 秩 $d$ 模板的完整判据（$VZ'=0$ 情形）
> **更正（728）**：模板的 $G=BV$ 行必须在 $T$，故 $E$ 应为 $T\cap\ker(Z'^{\mathsf T})$（不是 $S\cap\ker Z'^{\mathsf T}$）。
> **审计注（729）**：661 因 $T=0$ 对 $d>0$ 不可行；本文若沿用“661 实例级不可行/满足 651 却不可行”的表述，以 726/729 为准。



> 2026-11-27。把 659 的秩 $d$ 模板（$H=UV$、$VZ'=0$、$\operatorname{row}(V)\subseteq S$）的可行性判据补完整。
> 状态：**[已证-纸面]**。

## 模板设定

$V\in\mathbb C^{d\times k}$ 行满秩、$VZ'=0$、$D=\operatorname{row}(V)\subseteq E:=S\cap\ker(Z'^{\mathsf T})$，$\dim D=d$。
$H=UV$（$U\in\mathbb C^{q\times d}$ 列满秩），$B=ZU$ 任意。则
$$G=ZH-HZ'=BV,\qquad \operatorname{row}(G)\subseteq D\subseteq S,$$
$$P(\lambda)=(\lambda U-B)V,\qquad \operatorname{rank}P(\lambda)=\operatorname{rank}(\lambda U-B).$$

## 定理（模板的充要条件）

模板可行 $\iff$
1. $\dim E\ge d$（存在 $D$）；
2. $q\ge d+1$；
3. $H_0$ 的行空间 $\subseteq D$，且 $H_{A,0}$ 的对应行可由 $B$ 匹配（$r_0\ge1$ 时）。

**$q=d$ 不可能**：$U,B$ 均 $d\times d$，$\det(\lambda U-B)$ 是首项为 $\det U\ne0$ 的 $d$ 次多项式，必有根 ⇒ 某 $\lambda$ 掉秩（与 518 一致）。

**$q\ge d+1$ 可构造**：取
$$U=\begin{bmatrix}I_d\\0\end{bmatrix},\qquad B=\begin{bmatrix}N\\e^{\mathsf T}\end{bmatrix},$$
则 $\operatorname{rank}(\lambda U-B)=d\ \forall\lambda\iff$ 不存在 $x\ne0$ 使 $Nx=\lambda x$ 且 $e^{\mathsf T}x=0$。
对 $N$ 的有限个特征向量 $x_i$，取 $e$ 使 $e^{\mathsf T}x_i\ne0$（一般位置）即可；故存在。

## 检验

| 实例 | $E$ | $d=1$ | $d=2$ |
|---|---|---|---|
| 629（$S=0$） | 0 | 无 | 无 ✓（只有 $\omega=0$） |
| 631（$S=\mathbb C^k$） | $\mathbb C^k$ | 可行 | 可行（$q\ge3$） ✓ |
| 657（$k=2$） | $\operatorname{span}\{e_1\}$ | 可行（657） | 模板无（$\dim E=1$） |
| 638 | 0 | 模板无 | 模板无，但**一般** $d=2$ 可行（$VZ'\ne0$） |
| 660 | $\operatorname{span}\{e_1\}$ | 模板无（$\dim E=1$） | 模板无；固定 $H$ 失败 |
| 661 | 0 | 无 | 模板无 + $d=q$ 障碍 ⇒ 不可行 ✓ |

## 意义

- 模板族（$VZ'=0$）的可行性**完全由 $(\dim E,\ q)$ 与固定行匹配决定**；
- 但 638 说明：$\dim E$ 小（甚至 0）时，**非模板**（$VZ'\ne0$）仍可能可行——模板不是一般可行性的必要条件；
- 因此 $d=2$ 的一般分类必须允许 $VZ'\ne0$，此时行约束变为 653 的
  $$\ker(V|_K)\subseteq\ker((VZ')|_K),$$
  且 $G=ZH-HZ'=BV-UVZ'$ 的行约束不再自动。

## 下一步

1. 对 $d=2$、$VZ'\ne0$ 写出行约束的仿射空间与铅笔 gcd 条件（653 的一般形式）；
2. 在 $k=3$、$q=3$、$\dim E\le1$ 的小族上做符号/数值搜索，找“必要条件全满足但无 $\gcd=1$”的反例；
3. 以 638（可行）与 661（不可行）为两端测试。

## 状态

- 模板判据：**[已证-纸面]**；
- 非模板 $d=2$：**[未做]**。
