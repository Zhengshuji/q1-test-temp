# 562 第二个参数族（$AN=I$）：可行 = $w=0$ + 非零条件

> 2026-11-27。取 $AN=I_3$（即 $rAN=r$），重复 560 的计算，验证“等式 + 非零条件”的结构是否稳定。
> 状态：**[已证-纸面]**。

## 族

$$H=\begin{bmatrix}1&0&0\\0&1&0\\u&v&w\end{bmatrix},\qquad
H_A=\begin{bmatrix}a&0&0\\0&b&0\\u&v&w\end{bmatrix}.$$

$(5a)$：$w=0$ 时 $\ker H=\operatorname{span}\{e_3\}$，$H_Ae_3=(0,0,w)=0$ ✓。

$(5b)$：$w=0$ 时
$$P(\lambda)=\begin{bmatrix}\lambda-a&0&0\\0&\lambda-b&0\\(\lambda-1)u&(\lambda-1)v&0\end{bmatrix},$$
$$m_{12}=(\lambda-a)(\lambda-b),\quad m_{13}=(\lambda-a)(\lambda-1)v,\quad m_{23}=-(\lambda-b)(\lambda-1)u .$$

公共根：

| $\lambda$ | 需要 |
|---|---|
| $a$ | $(a-1)u=0$ |
| $b$ | $(b-1)v=0$ |
| $1$ | $(1-a)(1-b)=0$ |

所以（$a\ne b$ 的一般情形）
$$\gcd=1\iff a\ne1\ \wedge\ b\ne1\ \wedge\ u\ne0\ \wedge\ v\ne0 .$$

$w\ne0$ 时 $\omega=3$，$\det P=(\lambda-a)(\lambda-b)(\lambda-1)w$ 有根 ⇒ 失败。

## 结论

$$\boxed{\text{可行}\iff w=0\ \wedge\ a\ne1\ \wedge\ b\ne1\ \wedge\ u\ne0\ \wedge\ v\ne0}$$
——仍是“一个线性等式 + 若干非零（开）条件”，与 560 的结构一致。

（sympy 在 $w=0$ 上算得 $\gcd=1$（作为 $\mathbb Q(a,b,u,v)[\lambda]$ 的元素），
说明一般点可行；特殊点（$a=1$ 等）才是跳变簇。）

## 与 555/560

- 560：$rAN=(v,0,w)$，条件 $w=0\wedge au\ne v\wedge v\ne0$；
- 562：$rAN=r$，条件 $w=0\wedge u\ne0\wedge v\ne0\wedge a,b\ne1$；
- 两族的可行集都是“超平面 $w=0$ 上的开集”——**$(5a)$ 的等式 + $(5b)$ 的开条件**。

## 状态

- 第二族：**[已证-纸面]**；
- 一般结构猜想（等式+开条件）：**[猜想]**。
