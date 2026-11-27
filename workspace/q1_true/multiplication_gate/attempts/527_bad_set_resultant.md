# 527 坏超平面的来源与“无坏集”条件

> 2026-11-27。526 发现 520 在 $x=-1/2$ 上失败。本文件把坏集写成 resultant 的零点，
> 并给出 gadget **完全 sound**（无坏集）的充要形式条件——下一个设计目标。
> 状态：**[M2 分析]** + **[已证-纸面]**（小命题）。

## 坏集 = resultant 的零点

门上两个子式 $M_1,M_2\in\mathbb Q[x,y][\lambda]$。$(5b)$ 成立 $\iff\gcd_\lambda(M_1,M_2)=1$
$\iff\operatorname{Res}_\lambda(M_1,M_2)\ne0$。因此
$$\text{坏集}=\{(x,y):\operatorname{Res}_\lambda(M_1,M_2)(x,y)=0\}.$$

520 的 $\operatorname{Res}=64(2x+1)^2$，坏集是超平面 $x=-1/2$。

## 无坏集的充分条件

若 $M_2=a(x,y)\,M_1+k$，其中 $k\ne0$ 是常数、$a$ 是任意多项式，则
$$\gcd(M_1,M_2)=\gcd(M_1,k)=1\quad(\text{只要 }M_1\ne0),$$
**对所有参数成立**，坏集为空。

对二次 $M_1=\lambda^2+c$：设 $M_2=a\lambda^2+b\lambda+d$，则
$$\operatorname{Res}=(d-ca)^2+c\,b^2 .$$
无坏集 $\iff (d-ca)^2+c\,b^2$ 是非零常数 $\iff b$ 为常数且 $d-ca$ 为常数、不同时为零。
特别地 $b=0$、$d=ca+k$ 即上面的形式。

## 对 520 的诊断

520 的 $M_2=xM_1+2(2x+1)(\lambda-2)$：$b=2(2x+1)$ 非常数，$d-ca=2(2x+1)(-2)$ 也非常数，
所以 $\operatorname{Res}=64(2x+1)^2$ 非常数——坏集非空。

## 下一步

在 519/520 的结构里改 $H_{A,0}$（或 $A_{00}$、$u,a$），使某个子式满足
$$M_2=a(x,y)M_1+k,\qquad k\ne0\ \text{常数}.$$
这是纯代数条件，可直接用 sympy 的 `resultant` 检验；若找到，gadget 就没有坏超平面，
520 的“可行 $\iff z=xy$”就能恢复为双向。

## 状态

- 坏集 = resultant 零点：**[已证-纸面]**；
- 无坏集条件 $M_2=aM_1+k$：**[已证-纸面]**；
- 满足条件的 gadget：**[未找到]**。
