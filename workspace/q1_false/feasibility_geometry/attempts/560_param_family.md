# 560 参数族：$H_A=\operatorname{diag}(a,b)$ 时的完整可行条件

> 2026-11-27。按 ChatGPT 的建议把 559 推广成参数族，推导完整可行集。
> 状态：**[已证-纸面]**。

## 族

$$H=\begin{bmatrix}1&0&0\\0&1&0\\u&v&w\end{bmatrix},\qquad
H_A=\begin{bmatrix}a&0&0\\0&b&0\\v&0&w\end{bmatrix},\qquad r=(u,v,w).$$
（$rAN=(v,0,w)$，与 559 同一 $AN$；$a,b$ 为 $A$ 的固定数据。）

$(5a)$：$w=0$ 时 $\ker H=\operatorname{span}\{e_3\}$，$H_Ae_3=(0,0,w)=0$ ✓；$w\ne0$ 时 $\ker H=0$。

$(5b)$：$w\ne0$ 时 $\omega=3$，$\det P=(\lambda-a)(\lambda-b)(\lambda-1)w$ 有根 ⇒ 失败。
$w=0$ 时 $\omega=2$，三个子式：
$$m_{12}=(\lambda-a)(\lambda-b),\quad m_{13}=\lambda v(\lambda-a),\quad m_{23}=-(\lambda-b)(\lambda u-v).$$

## 公共根分析（$w=0$）

| 情形 | 条件 | 结论 |
|---|---|---|
| $a\ne b$，$a,b\ne0$ | $\lambda=a$ 需 $au=v$；$\lambda=b$ 需 $v=0$ | $\gcd=1\iff au\ne v\wedge v\ne0$ |
| $a=b\ne0$ | $\lambda=a$ 时三式全零 | 恒失败（不可行） |
| $b=0$，$a\ne0$ | $\lambda=0$ 需 $au=v$；$\lambda=a$ 需 $au\ne v$ | $\gcd=1\iff au\ne v$ |
| $a=0$，$b\ne0$ | $\lambda=0$ 需 $v=0$ | $\gcd=1\iff v\ne0$ |

所以完整可行集：
$$\boxed{\text{可行}\iff w=0\ \wedge\ \big(\text{上表对应条件}\big)}$$
——始终是“一个代数等式（$w=0$）+ 若干非零条件”的结构。

559 是 $a=1,b=2$ 的特例：$au\ne v\wedge v\ne0$ 即 $u\ne v\wedge v\ne0$。

## 与 555 判据

$(5a)$ 的解集（$w=0$ 超平面）不被跳变簇（$au=v$ 或 $v=0$ 的并）包含，
所以判据一致地预测“可行”，且一般点可行。

## 状态

- 参数族与条件：**[已证-纸面]**；
- 559 矩阵笔误（$H_A$ 第三行应为 $(v,0,w)$）已更正。
