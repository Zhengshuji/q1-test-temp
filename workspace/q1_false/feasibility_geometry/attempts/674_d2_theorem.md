# 674 $d=2$ 的定理：可解 $\iff$ $M$ 满秩；一般 $d$ 的猜想

> 2026-11-27。把 673 的抽样观察在 $d=2$ 上升级为证明，并陈述一般 $d$ 的猜想。
> 状态：**[已证-纸面]**（$d=2$）+ **[猜想]**（一般 $d$）。

## 定理（$d=2$）

设 $\operatorname{rank}H=2$，$f_1,\dots,f_m$ 为全部非零 2-子式，
$$f_i=a_i\lambda^2+b_i\lambda+c_i\qquad(\text{某 }a_i\ne0,\ \text{因 }H\text{ 有非零 }2\text{-子式}).$$
则
$$(5b)\iff \operatorname{rank}M(H)=4 .$$

**证明**：设 $(5b)$ 成立，即 $1=\sum g_if_i$（$\deg g_i<2$），故 $e_0\in\operatorname{col}M$。
若 $\operatorname{rank}M<4$，取非零左零向量 $y=(y_0,y_1,y_2,y_3)$。由 $e_0\in\operatorname{col}M$ 得 $y_0=0$。
$M$ 的列是 $v_i=(c_i,b_i,a_i,0)$ 与 $w_i=(0,c_i,b_i,a_i)$，故
$$y_1b_i+y_2a_i=0,\qquad y_1c_i+y_2b_i+y_3a_i=0\quad\forall i .$$

- 若 $y_1=0$：第一式给 $y_2a_i=0$；取 $a_i\ne0$ 得 $y_2=0$；第二式给 $y_3a_i=0$ ⇒ $y_3=0$，故 $y=0$，矛盾。
- 若 $y_1\ne0$：由第一式 $b_i=-(y_2/y_1)a_i$；代入第二式得
  $$c_i=\Big(\frac{y_2^2}{y_1^2}-\frac{y_3}{y_1}\Big)a_i .$$
  于是每个 $f_i=a_i\,q(\lambda)$，$q(\lambda)=\lambda^2+\frac{y_2}{y_1}\lambda+\big(\frac{y_2^2}{y_1^2}-\frac{y_3}{y_1}\big)$。
  因某 $a_i\ne0$，$q$ 整除所有 $f_i$，$\gcd(f_i)$ 非平凡，与 $1=\sum g_if_i$ 矛盾。$\square$

于是 $d=2$ 时“可解 $\iff$ 满秩”，672 的充分条件在 $d=2$ 且 $H$ 秩 2 时是**充要**的。

## 一般 $d$ 的猜想

> 设 $\operatorname{rank}H=d$（故某个 $d$-子式 $f_i$ 的次数恰为 $d$）。则
> $$(5b)\iff \operatorname{rank}M(H)=2d .$$

**支持**：
- $d=1$：$e_0\in\operatorname{col}M$ 且秩 $<2$ ⇒ 所有条目为常数 ⇒ $H=0$，与秩 1 矛盾；
- $d=2$：674 的定理；
- $d=3$：随机抽 4 个秩 3 的 $H$（配随机 $Z$），全部 $\operatorname{rank}M=6$，无“秩 $<6$ 且可解”。

**风险**：$d=2$ 的证明用了“$a_i\ne0$ 对所有 $i$”这一强性质（由 $y_1\ne0$ 推出 $f_i$ 共享二次因子），
一般 $d$ 的类似推理会遇到“$y$ 的多个自由度”和“$d$-子式次数不齐”的复杂情形；不能直接推广。

## 若猜想成立的意义

$$\text{可行}\iff\exists H:\ \operatorname{rank}H=d\ \wedge\ D_d(H)\ne0,$$
即可行性化为一族**开条件**的并（每个 $d$ 一个），不需要再处理“退化层的列空间条件”。
这将把 672 的“一般层/退化层分裂”消去一半：退化层只在 $\operatorname{rank}H<d$ 时出现（递归到更低秩）。

## 下一步

1. 尝试 $d=3$ 的证明（先假设所有 $d$-子式的次数结构最一般，或对 $y$ 的自由度做归纳）；
2. 若一般证明受阻，先证 $d=3$ 的定理（与 $d=2$ 平行的分类），检验是否有新的障碍；
3. 用 $D_d$ 的符号计算在 $d=3$ 小族上找“$\operatorname{rank}M<6$ 且可解”的反例。

## 状态

- $d=2$ 定理：**[已证-纸面]**；
- 一般 $d$ 猜想：**[猜想]**（$d=3$ 有有限抽样支持）。
