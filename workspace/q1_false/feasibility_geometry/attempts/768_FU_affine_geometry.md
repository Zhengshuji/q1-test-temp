# 768 $\mathcal F_U$ 的仿射几何与坏集 $\mathcal B_U$

> 2026-11-28。按 ChatGPT 的 P1 建议，把 761 的 $\mathcal F_U$ 写成显式仿射空间，并把 B 改写为“坏集是否为真子集”。
> 状态：**[已证-纸面]**（仿射结构）+ **[整理]**（坏集框架）。

## 仿射结构

设 $U=\operatorname{row}H$、$T=\{lW:lN=0\}$、$a=\dim(U\cap T)$，
$$F_i=T\cap(U-H_iZ''),\qquad \mathcal F_U=\prod_{i=1}^q F_i .$$

### 引理

若 $F_i\ne\varnothing$，取 $g_i\in F_i$，则
$$\boxed{F_i=g_i+(U\cap T),\qquad \dim F_i=a .}$$

**证明**：$F_i$ 是仿射子空间，方向为 $T\cap U$（两个仿射空间 $T$ 与 $U-H_iZ''$ 的交，方向空间取交）。$g_i\in F_i$ 给 $F_i=g_i+(T\cap U)$。$\square$

（与 737 的 $F_i=t_i+(U\cap T)$ 同一事实；737 用于 $E_H$ 的维数，这里用于参数化。）

### 推论

若所有 $F_i\ne\varnothing$，则
$$\boxed{\mathcal F_U\ \text{是仿射空间，}\ \dim\mathcal F_U=q\,a .}$$

取 $U\cap T$ 的基 $v_1,\dots,v_a$，则
$$G'_i(\theta)=g_i+\sum_{\ell=1}^{a}\theta_{i,\ell}\,v_\ell,\qquad \theta\in K^{qa}.$$
每个 $d'$-子式成为 $(\lambda,\theta)$ 的多项式
$$f_j(\lambda;\theta)=f_j\big(\lambda;G'(\theta)\big).$$

## B 的坏集表述

$$\boxed{\mathcal B_U=\{\theta\in K^{qa}:\ \gcd(f_1(\lambda;\theta),\dots,f_m(\lambda;\theta))\ne1\}.}$$
则
$$U\ \text{可行}\iff \mathcal F_U\ne\varnothing\ \text{且}\ \mathcal B_U\ne K^{qa}.$$

## 关键观察（与 765 呼应）

- $\mathcal B_U$ 是**代数集**（$\gcd\ne1$ 等价于所有 $d'$-子式有公共根，可用结式/判别式表达）；
- “存在 $\theta\notin\mathcal B_U$”**不能**由“泛型 $\theta$ 不在 $\mathcal B_U$”推出——765 的 $f_1=(x\lambda+1)(\lambda+1)$、$f_2=(x\lambda+1)(\lambda+2)$ 正是反例；
- 因此需要研究 $\mathcal B_U$ 的**具体方程**，而不是只在函数域上算 gcd。

## 待办（P1/P2）

1. 用 764 的实例验证 $\dim\mathcal F_U=q\,a$ 与参数化（$d'=1$、$a=\dim(U\cap T)$ 待算）；
2. 对 $m=1$（$q=k=d'$）与 $m=2$ 写 $\mathcal B_U$ 的显式方程；
3. 研究 $\mathcal B_U\subsetneq\mathcal F_U$ 的结构性充分条件。

## 状态

- 仿射结构：**[已证-纸面]**；
- 参数化：**[已证-纸面]**；
- 坏集：**[定义完成，结构待研究]**。
