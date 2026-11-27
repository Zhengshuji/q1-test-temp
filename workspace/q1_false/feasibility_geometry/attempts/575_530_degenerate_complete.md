# 575 530 gadget 的退化情形：可扩展行必冗余（完整证明）

> 2026-11-27。补上 574 的退化情形（$h_1=xh_2$、$a_3=0$）——直接对 530 的门做计算。
> 状态：**[已证-纸面]**。

## 数据（530，门上 $z=xy$）

$h_1=(xy,x,0)$、$h_2=(y,1,0)$、$h_3=(0,0,1)$；$a_1=(-2y,-2,2)$、$a_2=(0,0,-2)$、$a_3=0$。
$P_0$ 的三行：
$$p_1=(\lambda xy+2y,\ \lambda x+2,\ -2),\quad p_2=(\lambda y,\lambda,2),\quad p_3=(0,0,\lambda).$$
$\det[p_1;p_2;p_3]\equiv0$，且对 $\lambda\ne0$，$\operatorname{row}P_0=\operatorname{span}\{p_2,p_3\}$。

## 依赖关系

$$p_1=\Big(x+\frac{2}{\lambda}\Big)p_2+\Big(-\frac{2+2x}{\lambda}-\frac{4}{\lambda^2}\Big)p_3,$$
系数在 $\lambda=0$ 有极点——这正是退化的来源。（乘以 $\lambda^2$ 可得多项式恒等式。）

## 扩展行

设 $v(\lambda)=\lambda rN-rAN=( \lambda\alpha-a,\ \lambda\beta-b,\ \lambda\gamma-c)$，且 $v\in\operatorname{row}P_0(\lambda)$（$\lambda\ne0$）。

对 $\lambda\ne0$ 写 $v=A p_2+B p_3$。比较 $y$ 分量：$A=\beta-b/\lambda$；比较 $x$ 分量：
$$\lambda\alpha-a=\lambda y(\beta-b/\lambda)=\lambda\beta y-by
\ \Longrightarrow\ \alpha=\beta y,\quad a=by .$$
比较 $z$ 分量：$\lambda\gamma-c=2A+B\lambda=2\beta-\frac{2b}{\lambda}+B\lambda$。
左边是多项式，右边含 $1/\lambda$ 项 ⇒ 必须 $b=0$，于是 $a=0$。

所以
$$rN=(\beta y,\ \beta,\ \gamma)=\beta h_2+\gamma h_3\in\operatorname{row}H_0,\qquad
rAN=(0,0,c)\in\operatorname{span}\{a_2\}\subseteq\operatorname{row}H_{A,0}.$$
即扩展行是已有行的组合——**冗余**。$\square$

## 结论

530 gadget 的**任何**可行扩展行都冗余：
- 若 $v\in\operatorname{row}P_0(\lambda)\ \forall\lambda$，则 $rN\in\operatorname{row}H_0$、$rAN\in\operatorname{row}H_{A,0}$；
- 于是 $\operatorname{rank}H$、$\operatorname{rank}P$ 不变，扩展不产生新自由度。

结合 574（非退化情形），这给出冗余行定理的一个完整版本。

## 状态

- 530 退化情形：**[已证-纸面]**；
- 冗余行定理（两种情形）：**[已证-纸面]**；
- 后续：530 不可扩展，转新构造。
