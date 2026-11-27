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

## 结论

$$\boxed{d'=2>t=1,\qquad \omega=2>s=1\ \text{且可行}.}$$

- **732 的 $d'\le t$ 猜想被推翻**；
- **$\omega>s$ 重新成立**（638/661 失效后，这是第一个有效例子）；
- 726 的 $a\ge1$ 仍成立（此处 $a=\dim(U\cap T)=1$）；
- 725 的 $g_\mu\le a$ 仍成立（$A=RZX$ 的谱可检查）。

## 意义

- 方向性预筛选不能简化为 $d'\le t$；
- “$\omega\le s$” 再次被否定（本实例 $\omega=2>s=1$）；
- 说明小 $t$ 下仍可借助 $Z'$ 的非平凡作用（此处 $Z'$ 有复特征值）实现可行。

## 待办

1. 复核 $L$ 的显式实现（$LN=H$、$LW=G$），给出具体 $L$；
2. 检查 725 的 $g_\mu\le a$ 在本例的取值；
3. 用本例测试 690/695/704 预筛选链是否全部通过。

## 状态

- 反例：**[已证-纸面]** + **[精确验证]**；
- 732 猜想：**推翻**；
- $\omega>s$：**[成立]**。
