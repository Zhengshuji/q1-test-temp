# 580 有效的自由行：$k=4$、$q=3$ 的可行例子

> 2026-11-27。按 578/579 的设计，取 $H_{A0}$ 两行非零独立，得到自由行**真正改变 pencil** 的可行例子。
> 状态：**[已证-纸面]** + **[Lean]**。

## 构造

$k=4$、$q=3$、$r=(r_1,r_2,r_3,r_4)$：
$$H=\begin{bmatrix}1&0&0&0\\0&1&0&0\\r_1&r_2&r_3&r_4\end{bmatrix},\qquad
H_A=\begin{bmatrix}1&0&0&0\\0&2&0&0\\\alpha r_1&\beta r_2&0&0\end{bmatrix}$$
（$\alpha,\beta$ 为固定数据；$H_A$ 第三行来自 $rAN$，$AN=\operatorname{diag}(\alpha,\beta,0,0)$）。

## $(5a)$

$r_3=r_4=0$ 时 $\operatorname{rank}H=2$、$\ker H=\operatorname{span}\{e_3,e_4\}$；
$H_A$ 的三行都在前两个坐标里（第 3、4 分量为零）⇒ $(5a)$ 成立。

## $(5b)$

$\omega=2$。$P(\lambda)$ 的 $2\times2$ 子式（nonzero）：
$$m_{12}=(\lambda-2)(\lambda-1),\quad m_{13}=-r_2(\beta-\lambda)(\lambda-1),\quad m_{23}=r_1(\alpha-\lambda)(\lambda-2).$$
公共根分析：
- $\lambda=2$：$m_{13}=-r_2(\beta-2)$，需 $r_2(\beta-2)=0$；
- $\lambda=1$：$m_{23}=r_1(\alpha-1)(-1)$，需 $r_1(\alpha-1)=0$。

所以
$$\gcd=1\iff r_1(\alpha-1)\ne0\ \wedge\ r_2(\beta-2)\ne0 .$$

## 完整可行条件

$$\boxed{r_3=r_4=0,\quad r_1(\alpha-1)\ne0,\quad r_2(\beta-2)\ne0}$$
——自由行 $r_1,r_2$ **真正参与** $P(\lambda)$（第三行依赖它们），不是冗余行。

## Lean 核验

[580_lean_effective_row.lean](580_lean_effective_row.lean)（`namespace Q1Gadget580`，退出码 0）：
`no_common_root`：$r_1(\alpha-1)\ne0$、$r_2(\beta-2)\ne0$ 时三子式无公共根。

## 与 575 的关系

- 575 的冗余行引理讨论的是“给已有 gadget 追加一行”；580 是**从头设计**的 gadget，
  自由行 $r$ 一开始就在 $H,H_A$ 里，不是追加行；
- 这里 $rN=(r_1,r_2,0,0)\in\operatorname{row}H_0$、$rAN\in\operatorname{row}H_{A,0}$，
  但 $P$ 的第三行 $\lambda r-rAN$ 的**系数**含 $\alpha,\beta$，使子式 $m_{13},m_{23}$ 非零——
  这正是 562/580 类 gadget 能给出非平凡条件的来源。

## 下一步

检查这个例子能否作为“参数化门”的基础：$r_1,r_2$ 的角色类似于 520 的 $x,y$，
但这里 $\alpha,\beta$ 是数据、$r_1,r_2$ 自由——仍需把 $r_1,r_2$ 与目标变量联系起来。

## 状态

- 构造与条件：**[已证-纸面]**；
- Lean：**[Lean]**（1 条声明，退出码 0）；
- 与冗余性关系：**[已证-纸面]**。
