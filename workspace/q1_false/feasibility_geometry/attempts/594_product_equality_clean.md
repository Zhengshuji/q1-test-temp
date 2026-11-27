# 594 干净的乘积等式 gadget：可行 $\iff r_1r_2=z$（无附加条件）

> **更正（596）**：$H_A=ZH$ 在 q1 中不可实现（$H_A=LAN$ 由同一个 $A$ 决定）。
> 本构造对应的是**左铅笔** $P=(λI-Z)H$，不对应任何 q1 实例；保留作抽象铅笔的记录。

> 2026-11-27。593 的附加条件 $r_1^3\ne1$ 来自循环 $Z$；换**幂零 Jordan 块**后消失。
> 状态：**[已证-纸面]** + **[精确验证]** + **[Lean]**。

## 构造

$q=3$、$k=3$：
$$H=\begin{bmatrix}r_1&z&0\\1&r_2&0\\0&0&1\end{bmatrix},\qquad
Z=\begin{bmatrix}0&1&0\\0&0&1\\0&0&0\end{bmatrix}\ (\text{幂零 Jordan}),\qquad H_A=ZH .$$

## $(5a)$

$H_A=ZH$ ⇒ $Hv=0\Rightarrow H_Av=Z(Hv)=0$，**对所有 $R$ 自动成立**。

## 行列式

$$\det H=r_1r_2-z,\qquad \det P=\det(\lambda I-Z)\det H=\lambda^3(r_1r_2-z).$$

（$Z$ 幂零 ⇒ $\det(\lambda I-Z)=\lambda^3$。）

## $(5b)$

**门外**（$r_1r_2\ne z$）：$H$ 可逆、$\omega=3$，$\det P$ 在 $\lambda=0$ 为零 ⇒ 秩掉 ⇒ 失败。

**门上**（$r_1r_2=z$）：$\omega=2$，$\operatorname{im}H=\operatorname{span}\{(r_1,1,0),(0,0,1)\}$。
$Z$ 的唯一特征向量是 $e_1$（$\ker Z=\operatorname{span}\{e_1\}$），而 $e_1\notin\operatorname{im}H$：
$$a(r_1,1,0)+b(0,0,1)=(1,0,0)\ \Rightarrow\ a=0,\ b=0\ \text{矛盾}.$$
所以：
- $\lambda\ne0$：$\lambda I-Z$ 可逆（幂零）⇒ 秩 $=\operatorname{rank}H=2$；
- $\lambda=0$：$P(0)=-ZH$，$\ker Z\cap\operatorname{im}H=0$ ⇒ 秩 $=2$。

因此 $\operatorname{rank}P=2=\omega$ 对所有 $\lambda$ ✓。

## 结论

$$\boxed{\text{可行}\iff r_1r_2=z}$$
——**干净的乘积等式门**，没有附加开条件。

## 验证

- 精确验证（sympy）：
  - $(2,3,6)$：$\omega=2$、gcd=1、$3\times3$ 子式全零 ⇒ 可行；
  - $(1,2,2)$：同样可行（593 的循环 $Z$ 在这里失败，本构造修复）；
  - $(2,3,5)$：$\omega=3$、gcd $=\lambda^3$ ⇒ 不可行。
- Lean：[594_lean_product_equality_clean.lean](594_lean_product_equality_clean.lean)，
  `det_H`（$\det H=r_1r_2-z$）、`det_lambdaI_sub_Z`（$\det(\lambda I-Z)=\lambda^3$），退出码 0。

## 与 593 的关系

593 用循环 $Z$，其特征向量 $(1,\omega,\omega^2)$ 会在 $r_1=\omega^2$ 时落入 $\operatorname{im}H$，产生附加条件。
594 用幂零 $Z$（唯一特征向量 $e_1$），而 $e_1$ 永远不在 $\operatorname{im}H$ 里——附加条件消失。

## 意义

- 这是**第一个无附加条件的乘积等式 gadget**；
- 它表明 $(5a)$ 自动成立 + 门外 $\omega$ 升高 + 门内 pencil 无特征值碰撞 = 纯等式门；
- 可用于编码乘法链/算术电路，是 hardness 归约的关键原语。

## 下一步

1. 编码乘法链 $z_2=z_1r_2$（共享变量），检查变量共享是否保持可行性；
2. 加上常数/加法（线性约束可由 $H$ 的条目直接实现）；
3. 评估能否编码一个已知 NP-hard 问题（如二次方程组的可满足性）。

## 状态

- 构造与可行性：**[已证-纸面]**；
- 精确验证：**[精确验证]**；
- Lean：**[Lean]**（2 条声明）。
