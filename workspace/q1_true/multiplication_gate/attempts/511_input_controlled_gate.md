# 511 第一个输入控制的 $(5a)$ 乘法门：$z=xy$ 精确成立，但 $(5b)$ 在 $y=3/2$ 处失败

> 2026-11-27。按 509/510 的入口，构造出一个**固定行、无自由行**的显式族，使
> $$(5a)\iff z=xy$$
> 精确成立（$x,y,z$ 都是 $A$ 或 $L_0$ 的条目，不再被 $R=0$ 置零）。但 $(5b)$ 在整个门上失败：
> 三个 $2\times2$ 子式共享因子 $q(\lambda)=\lambda^2-\lambda(y+1)+1$（ChatGPT 更正）。
> 状态：**[精确恒等式]**。

## 构造

$k=3$、$N=I_3$、$q=r_0=2$：
$$L_0=\begin{bmatrix}z&x&0\\1&0&1\end{bmatrix},\qquad
A=\begin{bmatrix}1&0&0\\1-y&0&1\\0&-1&1+y\end{bmatrix}.$$
（$A$ 的条目都是 $x,y,z$ 的一次式。）

## $(5a)\iff z=xy$

$H_0=L_0$、$H_{A,0}=L_0A$：
$$l_1A=(z-xy+x,\ 0,\ x),\qquad l_2A=(1,\ -1,\ 1+y).$$
两个 $3\times3$ 子式：
$$D_1=\det[l_1;l_2;l_1A]=x(z-xy),\qquad D_2=\det[l_1;l_2;l_2A]=z-xy .$$
$(5a)$ 要求 $D_1=D_2=0$；$D_2=0$ 即 $z=xy$，此时 $D_1$ 自动为零。反之 $z=xy$ 是 $(5a)$ 的必要条件。
所以
$$\boxed{(5a)\iff z=xy}\qquad(\text{精确恒等式}).$$

## $(5b)$：整个门上都失败（ChatGPT 更正）

在门上 $z=xy$：
$$H_0=\begin{bmatrix}xy&x&0\\1&0&1\end{bmatrix},\qquad
H_{A,0}=\begin{bmatrix}x&0&x\\1&-1&1+y\end{bmatrix},$$
$$P(\lambda)=\begin{bmatrix}\lambda xy-x&\lambda x&-x\\\lambda-1&1&\lambda-1-y\end{bmatrix}.$$
三个 $2\times2$ 子式（精确计算，ChatGPT 复核）：
$$M_{12}=-x\,q,\qquad M_{23}=x\,q,\qquad M_{13}=xy\,q,\qquad q(\lambda)=\lambda^2-\lambda(y+1)+1 .$$
三者有**共同因子 $q$**；$q$ 在 $\mathbb C$ 上必有根，所以 $x\ne0$ 的每个门上实例都使
$\operatorname{rank}P<2$，$(5b)$ **在整个门上失败**（不只是 $y=3/2$）。

（原稿把 $M_{23}$ 算成 $x(\lambda^2-\lambda y-1)$，是错的；正确为 $xq$。）

## 意义

- 这是**第一个** $(5a)$ 精确等于乘法关系的、输入控制的构造（$q=r_0$，无自由行）；
- 它把问题从“门变量可被置零”推进到“$(5b)$ 的**公共因子**”；
- 失败是结构性的：三个子式共享 $q$，必须打破这个 gcd，而不是移动某个公共根。

## 下一步

改动 $l_2$ 或 $A$ 的第 3 行，使代入 $z=xy$ 后三个 $2\times2$ 子式的 gcd 在 $\mathbb Q(x,y)[\lambda]$ 中为**非零常数**
（ChatGPT 的判据），同时保持 $D_2=z-xy$。

## 状态

- $(5a)\iff z=xy$：**[精确恒等式]**；
- $(5b)$：**[精确恒等式]**（共同因子 $q$，全门失败）；
- sound gadget：**[未完成]**。
