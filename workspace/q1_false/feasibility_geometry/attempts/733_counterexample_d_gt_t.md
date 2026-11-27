# 733 反例：$d'=2>t=1=s$ 可行（推翻 $d'\le t$ 猜想，恢复 $\omega>s$）

> 2026-11-27。构造出 $t=s=1$、$d'=\omega=2$ 的**可行**实例，推翻 732 的 $d'\le t$ 猜想，并恢复 $\omega>s$ 的有效例子。
> 状态：**[已证-纸面]** + **[精确验证]**。

## 数据

$n=4$、$k=2$、$q=3$、$N$ 前 2 坐标嵌入，
$$A e_1=e_1+e_2+e_3,\quad A e_2=2e_1+e_2,\quad A e_3=e_4,\quad A e_4=0,\qquad C=e_4^{\mathsf T}.$$
sympy 验证 $K_0=\operatorname{span}\{e_1,e_2\}$。
$$Z'=\begin{bmatrix}1&2\\1&1\end{bmatrix},\qquad W=AN-NZ'=e_3e_1^{\mathsf T},$$
$$S=\operatorname{row}W=\operatorname{span}\{e_1\}=T\ (s=t=1).$$

## 可行解

$$H=\begin{bmatrix}2&2\\-1&-1\\2&1\end{bmatrix}\ (\text{秩 }2),\qquad
Z=\begin{bmatrix}4&-3&-5\\-2&-3&-2\\7/2&-3&-5\end{bmatrix},$$
$$G=ZH-HZ'=\begin{bmatrix}-3&0\\-3&0\\-3&0\end{bmatrix}\quad(\text{行在 }T).$$

- $(5a)$：$H_A=ZH$；
- $P(\lambda)=\lambda H-ZH$ 的 2-子式（$3$ 个中非零）：
$$-9(\lambda-3),\qquad -2\lambda^2+\lambda+5,\qquad \lambda^2+4\lambda-25,$$
$\gcd=1$ ⇒ $\operatorname{rank}M=4=2d'$ ⇒ $(5b)$ 成立。

## 显式 $L$ 与 725 的检验

取
$$L=[\,H \mid (-3,-3,-3)^{\mathsf T} \mid 0\,]\in\mathbb C^{3\times4}.$$
验证：$LN=H$ ✓；$LW=(-3,-3,-3)^{\mathsf T}e_1^{\mathsf T}=G$ ✓；$LAN=HZ'+G=ZH$ ✓。

$A=RZH$（$R=(H^{\mathsf T}H)^{-1}H^{\mathsf T}$）：
$$A=\begin{bmatrix}-7/5&2\\14/5&1\end{bmatrix},\qquad
\sigma(A)=\Big\{\tfrac{-1\pm4\sqrt{11}}{5}\Big\},$$
两个特征值均为单重（几何重数 $1$），故 $g_\mu=1\le a=1$ ✓（725 成立）。

## 结论

$$\boxed{d'=2>t=1,\qquad \omega=2>s=1\ \text{且可行}.}$$

- **732 的 $d'\le t$ 猜想被推翻**；
- **$\omega>s$ 重新成立**（638/661 失效后，这是第一个有效例子）；
- 726 的 $a\ge1$ 仍成立（此处 $a=\dim(U\cap T)=1$）；
- 725 的 $g_\mu\le a$ 仍成立（$A=RZX$ 的谱可检查）。

## 意义

- 方向性预筛选不能简化为 $d'\le t$；
- “$\omega\le s$” 再次被否定（本实例 $\omega=2>s=1$）；
- 说明小 $t$ 下仍可借助 $Z'$ 的非平凡作用（此处 $Z'$ 有无理特征值）实现可行。

## 预筛选链的检验

- 704：$\operatorname{rank}H_A=2=d'$ ✓；
- 690：$Z'$ 的特征值 $1\pm\sqrt2$ 处 $\operatorname{rank}(\mu I-Z')=1\ge d'-t=1$ ✓；
- 695：$\dim(\operatorname{row}(H(\mu I-Z'))+T)=2\ge d'=2$ ✓（**恰好取等**）；
- 726：$a=\dim(U\cap T)=1\ge1$ ✓；
- 725：$g_\mu=1\le a=1$ ✓。

即该实例**通过全部已知必要条件**，且真实可行——说明现有预筛选链在边界上是紧的。

## 待办

1. ~~复核 $L$ 的显式实现~~（已完成）；
2. ~~检查 725 的 $g_\mu\le a$~~（已完成，$g_\mu=1$）；
3. ~~测试 690/695/704 预筛选链~~（已完成，全部通过，695 取等）。

## 状态

- 反例：**[已证-纸面]** + **[精确验证]**；
- 732 猜想：**推翻**；
- $\omega>s$：**[成立]**。
