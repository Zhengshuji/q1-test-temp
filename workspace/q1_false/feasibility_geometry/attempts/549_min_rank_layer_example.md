# 549 最小秩层例子：$q=3$、$k=2$ 的可行集是开条件

> 2026-11-27。按 548 的第一步，取最小非平凡例子算清楚秩层上的可行集结构。
> **结果：本例中 $(5a)$ 自动成立，$(5b)\iff r_3\ne0$——可行集是锥减去一个超平面（开条件）。**
> 状态：**[已证-纸面]** + **[Lean]**。

## 设定

$n=4$、$C=e_4^{\mathsf T}$、$A$ 为移位（$e_1\mapsto e_2\mapsto e_3\mapsto e_4\mapsto0$）。
则 $CA=e_3^{\mathsf T}$、$K_0=\operatorname{span}(e_1,e_2)$、$k=2$、$N=I_2$。

$L_0=[e_1;e_2]$（2 行）、$R=r=(r_1,r_2,r_3,r_4)$（1 行，$\operatorname{rank}R=1$）。

## 压缩数据

$$H=\begin{bmatrix}1&0\\0&1\\r_1&r_2\end{bmatrix},\qquad
H_{A,0}=\begin{bmatrix}0&0\\1&0\\r_2&r_3\end{bmatrix}.$$
（$A N=[e_2,e_3]$；$e_3\notin K_0$ 只影响 $rN$ 的第三坐标。）

- $\operatorname{rank}H=2=k$（只要 $(r_1,r_2)\ne0$）⇒ $\ker H=0$ ⇒ **$(5a)$ 自动成立**；
- $P(\lambda)$ 的三行：$(\lambda,0)$、$(-1,\lambda)$、$(\lambda r_1-r_2,\ \lambda r_2-r_3)$。

三个 $2\times2$ 子式：
$$m_{12}=\lambda^2,\qquad m_{23}=r_3-\lambda^2 r_1,\qquad m_{13}=\lambda(\lambda r_2-r_3).$$
$\gcd=1\iff r_3\ne0$（$\lambda^2=0\Rightarrow\lambda=0$，而 $m_{23}(0)=r_3$）。

所以
$$\boxed{\text{可行}\iff r_3\ne0}$$
（一个开条件；可行集是锥减超平面 $\{r_3=0\}$）。

## Lean 核验

[549_lean_min_example.lean](549_lean_min_example.lean)（`namespace Q1Gadget549`，退出码 0）：

| 声明 | 内容 |
|---|---|
| `no_common_root` | $r_3\ne0\wedge\lambda^2=0\wedge r_3-r_1\lambda^2=0\Rightarrow$ False |
| `gcd_one` | 等价形式 |

## 对 548 的意义

- 本例中可行集是**构造性**（线性等式 + 开条件），可在多项式时间内判定；
- 支持“固定秩层上可行性可能是简单构造性条件”的猜想；
- 但一般情形下 $(5b)$ 的 gcd 条件是**高次**的（resultant），本例只是最简化的秩层。

## 下一步

在 $q=3$、$k=2$ 的其它 $L_0/A$（以及 $m=2$）上重复这个计算，收集“可行集 = 线性条件 + 开条件”的实例；
若普遍成立，则给出多项式算法的结构定理；若出现高次不可约条件，则记为硬度候选。

## 状态

- 例子计算：**[已证-纸面]**；
- Lean：**[Lean]**（2 条声明）；
- 一般结构：**[未定]**。
