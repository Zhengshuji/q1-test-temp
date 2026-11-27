# 613 不可约 \(Z'\) 的乘积门：可行 $\iff r_1r_2=z\ \wedge\ r_2\notin\{1,\omega,\omega^2\}$

> 2026-11-27。612 停止判断后，尝试在**单个不可约块**内直接编码乘积，成功得到一个带开条件的门；
> 且因 $Z'$ 不可约，秩 1 逃逸被阻断。
> 状态：**[已证-纸面]** + **[精确验证]**。

## 构造

$Q=k=3$、$Z'=C$（三阶循环置换）、
$$H=\begin{bmatrix}r_1&z&0\\1&r_2&0\\0&0&1\end{bmatrix},\qquad H_A=HZ'\ \ (\text{由 }AN=NZ'\text{ 实现}).$$

$\det H=r_1r_2-z$。

## 秩条件

$C$ 的特征值 $\lambda\in\{1,\omega,\omega^2\}$（$\omega=e^{2\pi i/3}$）；其它 $\lambda$ 处 $M(\lambda)$ 可逆。

- **门外**（$r_1r_2\ne z$）：$\omega=3$；在任一特征值处 $M$ 奇异、秩 2 ⇒ $\operatorname{rank}(HM)\le2<3$ ⇒ 失败；
- **门上**（$r_1r_2=z$）：$\omega=2$；$\ker H=\operatorname{span}\{(-r_2,1,0)\}$（代入 $z=r_1r_2$ 验证）；
  $P=H(\lambda I-C)$ 在特征值 $\lambda$ 处的秩为 $2-\dim(\ker H\cap\operatorname{im}M(\lambda))$；
  $\operatorname{im}M(\lambda)=\{x:x\cdot u_\lambda=0\}$（$u_\lambda=(1,\lambda,\lambda^2)$），
  $$\ker H\subseteq\operatorname{im}M(\lambda)\iff -r_2+\lambda=0\iff r_2=\lambda .$$
  所以门上的秩 2 条件 ⇔ $r_2\notin\{1,\omega,\omega^2\}$。

## 结论

$$\boxed{\text{可行}\iff r_1r_2=z\ \wedge\ r_2\notin\{1,\omega,\omega^2\}}$$

## 精确验证（sympy）

| $(r_1,r_2,z)$ | $\omega$ | 秩（$\lambda=1,\omega,\omega^2$） | 可行 |
|---|---|---|---|
| $(2,3,6)$ | 2 | $2,2,2$ | 是 |
| $(1,2,2)$ | 2 | $2,2,2$ | 是 |
| $(2,2,4)$ | 2 | $2,2,2$ | 是 |
| $(2,1,2)$ | 2 | $2,2,1$ | 否（$r_2=1$） |

## 与 598 的区别

- 598：$Z'=\operatorname{diag}(0,1,0)$，门干净但**块对角**，多块时秩 1 逃逸（605/611）；
- 613：$Z'$ 不可约（循环），秩 1 逃逸被阻断（612 的左特征向量第一坐标非零），代价是开条件 $r_2\notin$ 三次单位根。

## 下一步

1. 多门：$Q=3s$，$Z'$ 取 $3s$ 阶循环移位（仍不可约），设计 $H$ 使门关系可分离；
2. 若不可分离，考虑 $Z'$ 为“循环 + 块”的折中（部分不可约）。

## 状态

- 构造与可行性：**[已证-纸面]**；
- 精确验证：**[精确验证]**；
- 多门：**[未做]**。
