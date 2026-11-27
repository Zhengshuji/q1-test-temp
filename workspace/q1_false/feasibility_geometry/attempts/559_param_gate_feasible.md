# 559 参数化 520：第一个“可行且 $(5a)$ 非平凡”的例子

> 2026-11-27。按 558 的下一步，把 520 的形状参数化（第三行 = $rN$），得到
> **可行条件 $w=0\wedge v\ne0\wedge u\ne v$**——$(5a)$ 非平凡（$\ker H=\operatorname{span}\{e_3\}$），
> 且存在可行 $R$。状态：**[已证-纸面]** + **[Lean]**。

## 构造

$n=5$、$k=3$、$q=3$、$r=(u,v,w)$：
$$H=\begin{bmatrix}1&0&0\\0&1&0\\u&v&w\end{bmatrix},\qquad
H_A=\begin{bmatrix}1&0&0\\0&2&0\\v&0&w\end{bmatrix},$$
其中 $AN$ 的列取 $Ae_1=e_2$、$Ae_2=0$、$Ae_3=e_3$（故 $rAN=(v,0,w)$，第三行为 $(u,v,w)\cdot AN=(v,0,w)$）。

## $(5a)$

$w=0$ 时 $\operatorname{rank}H=2$、$\ker H=\operatorname{span}\{e_3\}$；而 $H_Ae_3=(0,0,0)$ ✓。
$w\ne0$ 时 $\ker H=0$，$(5a)$ 自动成立。

## $(5b)$

$w=0$ 时 $\omega=2$，$P$ 的行在 $\mathbb C^2$（第三列为零）：
$$P(\lambda)=\begin{bmatrix}\lambda-1&0&0\\0&\lambda-2&0\\\lambda u-v&\lambda v&0\end{bmatrix},$$
三个 $2\times2$ 子式：
$$m_{12}=(\lambda-1)(\lambda-2),\quad m_{13}=\lambda v(\lambda-1),\quad m_{23}=-(\lambda-2)(\lambda u-v).$$
公共根分析：
- $\lambda=1$：$m_{23}=u-v$ ⇒ 需 $u=v$ 才为零；
- $\lambda=2$：$m_{13}=2v$ ⇒ 需 $v=0$ 才为零。

所以 $\gcd=1\iff v\ne0\wedge u\ne v$。

$w\ne0$ 时 $\omega=3$，$\det P=(\lambda-1)^2(\lambda-2)w$ 有根 ⇒ $(5b)$ 失败。

于是
$$\boxed{\text{可行}\iff w=0\ \wedge\ v\ne0\ \wedge\ u\ne v}$$
——$(5a)$ 非平凡、可行集是超平面 $w=0$ 上的开集（去两条线）。

## Lean 核验

[559_lean_param_gate.lean](559_lean_param_gate.lean)（`namespace Q1Gadget559`，退出码 0）：
`no_common_root`：$v\ne0$、$u\ne v$、三个子式同时为零 ⇒ False。

## 与 555 判据

$(5a)$ 的解集（$w=0$ 的超平面）**不**被 gcd 跳变簇（$\{u=v\}\cup\{v=0\}$）包含，
所以判据正确预测“可行”；且一般点 $R$（$w=0$、$u\ne v$、$v\ne0$）可行。

## 状态

- 例子：**[已证-纸面]**；
- Lean：**[Lean]**（1 条声明）；
- 判据一致性：**[已证-纸面]**。
