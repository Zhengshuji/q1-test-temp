# 593 乘积等式 gadget：可行 $\iff r_1r_2=z\ \wedge\ r_1^3\ne1$

> 2026-11-27。把 591 的第三列参数化，得到**乘积等式门**（附一个开条件）。
> 状态：**[已证-纸面]** + **[精确验证]** + **[Lean]**。

## 构造

$q=3$、$k=3$：
$$H=\begin{bmatrix}r_1&z&0\\1&r_2&0\\0&0&1\end{bmatrix},\qquad
Z=\begin{bmatrix}0&1&0\\0&0&1\\1&0&0\end{bmatrix}\ (\text{三阶循环}),\qquad H_A=ZH .$$

## $(5a)$

$H_A=ZH$ ⇒ 对任意 $v$，$Hv=0\Rightarrow H_Av=Z(Hv)=0$，故 $\ker H\subseteq\ker H_A$ **自动成立**。

## 行列式

$$\det H=r_1r_2-z,\qquad \det P=\det(\lambda I-Z)\det H=(\lambda^3-1)(r_1r_2-z).$$

## $(5b)$ 分析

**门上**（$r_1r_2=z$）：$\operatorname{rank}H=2=\omega$，$\operatorname{im}H=\operatorname{span}\{(r_1,1,0),(0,0,1)\}$。
$P=(λI-Z)H$，$\operatorname{rank}P=2\ \forall\lambda$ $\iff$ $\operatorname{im}H$ 不含 $Z$ 的特征向量。
$Z$ 的特征向量是 $(1,\omega,\omega^2)$（$\omega^3=1$）。设
$$v=a(r_1,1,0)+b(0,0,1)=(ar_1,a,b)=(1,\omega,\omega^2)
\ \Rightarrow\ a=\omega,\ b=\omega^2,\ ar_1=1\ \Rightarrow\ r_1=\omega^2 .$$
所以掉秩 $\iff r_1\in\{1,\omega,\omega^2\}$（三次单位根）。

**门外**（$r_1r_2\ne z$）：$H$ 可逆、$\omega=3$，$\det P=(\lambda^3-1)(r_1r_2-z)$ 有根 ⇒ $(5b)$ 失败。

## 结论

$$\boxed{\text{可行}\iff r_1r_2=z\ \wedge\ r_1^3\ne1}$$
——第一个**乘积等式门**，代价是一个开条件 $r_1^3\ne1$。

## 验证

- 纸面：上述推导；
- 精确验证（sympy）：
  - $(r_1,r_2,z)=(2,3,6)$：$\omega=2$、gcd$(2\times2$ 子式$)=1$ ⇒ 可行；
  - $(1,2,2)$：gcd $=\lambda-1$ ⇒ 不可行（$r_1=1$）；
  - $(2,3,5)$：gcd $=\lambda^3-1$ ⇒ 不可行（门外）。
- Lean：[593_lean_product_equality.lean](593_lean_product_equality.lean)，`det_H`（$\det H=r_1r_2-z$），退出码 0。

## 意义

- 等式门**可以**出现——前提是 $(5a)$ 在秩层上自动成立、$(5b)$ 在秩层上恰好可行；
  这与 555 的“开集”不矛盾：可行性是各秩层的并，秩层本身可以是超曲面；
- 额外的开条件 $r_1^3\ne1$ 来自 $Z$ 的特征向量与 $\operatorname{im}H$ 的碰撞；
- 归约时可用变量替换（如 $r_1\mapsto r_1+c$）把 $r_1^3\ne1$ 变成“$r_1$ 避开三个固定点”，
  在 $\mathbb C$ 上这是可满足的（选一般点），不构成实质限制。

## 下一步

1. 把 $r_1^3\ne1$ 也消掉（换 $Z$ 使特征向量与 $\operatorname{im}H$ 对所有 $r$ 都不碰撞？不可能——但可让碰撞条件依赖于额外变量并被其他门排除）；
2. 用 593 的门编码乘法链（$z_2=z_1r_2$ 等），尝试组合成硬度归约；
3. 检查 $q\ge4$ 时能否让 $\omega$ 更低、消掉开条件。

## 状态

- 构造与可行性：**[已证-纸面]**；
- 精确验证：**[精确验证]**；
- Lean：**[Lean]**（1 条声明）。
