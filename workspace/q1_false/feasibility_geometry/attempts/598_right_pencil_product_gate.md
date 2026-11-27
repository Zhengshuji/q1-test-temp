# 598 右铅笔乘积等式门：可行 $\iff r_1r_2=z$（q1 可实现）

> 2026-11-27。596 更正后，在右铅笔 $P=H(\lambda I-Z')$ 下重做，取 $Z'=\operatorname{diag}(0,1,0)$（带特征值 0 与 1）。
> **结果：可行 $\iff r_1r_2=z$，且可由具体 q1 数据实现。**
> 状态：**[已证-纸面]** + **[精确验证]** + **[Lean]**。

## 构造

$k=3$、$q=3$：
$$H=\begin{bmatrix}r_1&z&0\\1&r_2&0\\0&0&0\end{bmatrix},\qquad
Z'=\begin{bmatrix}0&0&0\\0&1&0\\0&0&0\end{bmatrix},\qquad
H_A=H Z'.$$

**可实现性**：取 $n=5$、$C=e_5^{\mathsf T}$、$A$ 在 $e_1,e_2,e_3$ 上为 $\operatorname{diag}(0,1,0)$、
$Ae_4=e_5$、其余为 0；$N$ 为前 3 个坐标的嵌入。则 $AN=NZ'$，故 $H_A=LAN=HZ'$ ✓。

## $(5a)$

$H_A=HZ'$ ⇒ $Hv=0\Rightarrow H_Av=HZ'v=0$，自动成立。

## $(5b)$

$$P=H(\lambda I-Z')=\begin{bmatrix}\lambda r_1&(\lambda-1)z&0\\\lambda&(\lambda-1)r_2&0\\0&0&0\end{bmatrix},$$
其左上 $2\times2$ 行列式：
$$\lambda r_1(\lambda-1)r_2-\lambda(\lambda-1)z=\lambda(\lambda-1)(r_1r_2-z).$$

- **门外**（$r_1r_2\ne z$）：$\omega=\operatorname{rank}H=2$；$\lambda=0$ 时左上块为
  $\begin{bmatrix}0&-z\\0&-r_2\end{bmatrix}$，秩 1（只要 $(z,r_2)\ne(0,0)$）⇒ 秩 $<\omega$ ⇒ 失败；
- **门上**（$r_1r_2=z$）：$\omega=1$；两列分别为 $\lambda(r_1,1)^{\mathsf T}$ 与 $(\lambda-1)(z,r_2)^{\mathsf T}$，
  $\lambda=0$ 时第一列为零、第二列非零（若 $(z,r_2)\ne0$）；$\lambda=1$ 时第二列为零、第一列非零（若 $(r_1,1)\ne0$）；
  $\lambda\ne0,1$ 时两列成比例（因 $z=r_1r_2$）⇒ 秩 1 对所有 $\lambda$ ✓。

## 结论

$$\boxed{\text{可行}\iff r_1r_2=z}$$
（除去 $(r_1,r_2,z)=(0,0,0)$ 的退化点：此时 $\omega=1$ 但 $\lambda=0$ 秩 0；可加非零条件或用非退化变量避免。）

## 精确验证（sympy）

| $(r_1,r_2,z)$ | $\omega$ | 秩 $\lambda=0,1,2$ | 结论 |
|---|---|---|---|
| $(2,3,6)$ | 1 | $1,1,1$ | 可行 |
| $(2,3,5)$ | 2 | $1,1,2$ | 不可行（$\lambda=0$ 掉秩） |
| $(1,1,1)$ | 1 | $1,1,1$ | 可行 |
| $(0,0,0)$ | 1 | $0,1,1$ | 不可行（退化） |

## Lean

[598_lean_right_pencil.lean](598_lean_right_pencil.lean)：`det2_P`（左上 $2\times2$ 行列式 $=\lambda(\lambda-1)(r_1r_2-z)$），退出码 0。

## 与 594 的区别

- 594 的 $H_A=ZH$（左铅笔）不可实现（596）；
- 598 的 $H_A=HZ'$（右铅笔）可由 $AN=NZ'$ 实现，且门成立。

## 下一步

1. 块对角合取在右铅笔下重做（595 的结论需按 $H_A=HZ'$ 重写）；
2. 线性门 $\ell=0$ 的右铅笔版本；
3. 算术电路编码与硬度归约。

## 状态

- 构造与可行性：**[已证-纸面]**；
- 精确验证：**[精确验证]**；
- Lean：**[Lean]**（1 条声明）；
- q1 可实现性：**[已证-纸面]**（给出具体 $n,C,A,N$）。
