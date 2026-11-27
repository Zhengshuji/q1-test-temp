# 591 乘积不等式 gadget：可行 $\iff r_1r_2\ne z$

> 2026-11-27。从 590 的反例出发，把 $H$ 参数化，得到**第一个编码自由变量乘法**的 gadget——
> 形式是不等式 $r_1r_2\ne z$。
> 状态：**[已证-纸面]** + **[精确验证]** + **[Lean]**。

## 构造

$q=3$、$k=3$：
$$H=\begin{bmatrix}0&0&0\\r_1&1&0\\z&r_2&0\end{bmatrix},\qquad
Z=\begin{bmatrix}0&1&0\\0&0&1\\0&0&0\end{bmatrix}\ (\text{幂零 Jordan 块}),\qquad H_A=ZH.$$
展开：$H_A=\begin{bmatrix}r_1&1&0\\z&r_2&0\\0&0&0\end{bmatrix}$。

## $(5a)$

$H e_3=0$ ⇒ $H_Ae_3=Z\cdot0=0$ ✓（$\ker H$ 含 $e_3$；当 $r_1r_2\ne z$ 时 $\ker H=\operatorname{span}\{e_3\}$）。

## $(5b)$

$P(\lambda)=(\lambda I-Z)H$。$Z$ 幂零、$\det(\lambda I-Z)=\lambda^3$：
- $\lambda\ne0$：$\lambda I-Z$ 可逆 ⇒ $\operatorname{rank}P=\operatorname{rank}H=2$；
- $\lambda=0$：$P(0)=-ZH$，其 $2\times2$ 子式（行 1,2 列 1,2）为
  $$(-r_1)(-r_2)-(-1)(-z)=r_1r_2-z .$$
  而 $\ker Z=\operatorname{span}\{e_1\}$，$\operatorname{im}H=\operatorname{span}\{(0,r_1,z),(0,1,r_2)\}$；
  $\operatorname{im}H\cap\ker Z=0\iff r_1r_2-z\ne0$。

所以
$$\boxed{\text{可行}\iff r_1r_2\ne z}$$
（$r_1r_2=z$ 时：$H$ 降秩为 1，$P(0)$ 秩 1 $<\omega=2$ ⇒ $(5b)$ 失败；同时 $(5a)$ 也失效）。

## 意义

- 这是第一个**在自由变量上编码乘法**的 gadget（此前 520/530 只对固定数据判断乘法）；
- 形式是**不等式**：$(5b)$ 的成立集是开集（gcd=1 是开条件，见 555），所以等式 $r_1r_2=z$ **不可能**作为可行集；
- 因此这条路线自然给出“$\ne$”门。若归约只需要否定/不等式约束，这就够用；
  若需要等式门，必须在归约层面用“$\ne$ 的并”或补变量处理。

## 验证

- 纸面：上述推导；
- 精确验证：sympy 对 $(r_1,r_2,z)=(2,3,7)$ 得 $\det\equiv0$、$\gcd=1$、$\operatorname{rank}P(0)=2$；
  $(2,3,6)$ 得 $\operatorname{rank}P(0)=1$；
- Lean：[591_lean_product_inequality.lean](591_lean_product_inequality.lean)，`det_P_zero`、`minor_zero`，退出码 0。

## 下一步

1. 把 $H$ 的第三列也参数化（现在为零），使 $\omega$ 可变、可能得到等式形式的门；
2. 检查这个 $\ne$ 门能否组合成更有用的约束（例如“至少一个变量非零”）；
3. 在归约层面评估：$\ne$ 门是否足以编码某个已知难问题（如多项式恒等式的否定）。

## 状态

- 构造与可行性：**[已证-纸面]**；
- 精确验证：**[精确验证]**；
- Lean：**[Lean]**（2 条声明）。
