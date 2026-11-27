# 路线 B：$(5a)$ 编等式、$(5b)$ 编不等式——极性对了

> 2026-11-09。重新审视路线 B：不要用 $(5b)$ 编等式，而是用它编**非零/不等式**；
> 等式由 $(5a)$ 的秩条件提供。这个极性与 $\exists\mathbb R$ 的结构匹配：
> 等式 + 非零条件足以编码半代数可行性。
> 状态：**M2（路线分析 + 精确核对）**。

## 目标

判断 $(5b)$ 的谱条件能否作为 $\exists\mathbb R$-hardness 的“非零/不等式”部分。

## 设想与理由

- $(5a)$：秩等式，天然产生多项式**等式**（子式为零）。
- $(5b)$：$\operatorname{rank}P(\lambda)=\omega\ \forall\lambda$，等价于极大子式的 gcd 为常数，是**非零/开条件**。
- 在 $\mathbb R$ 上，等式 + 非零条件足以编码一般半代数集：
  $$f>0\iff \exists y:\ y^2=f\ \text{且}\ f\ne0.$$
  所以“等式（$(5a)$）+ 非零（$(5b)$）”是正确极性；之前把 $(5b)$ 当等式用，方向反了。

## 做法：两个极性事实

### 1. $q=2,\omega=1$：$(5b)$ 自动

$H$ 秩 1 ⇒ $P=(\lambda I-F)H$ 的秩恒 $\le1$，$(5b)$ 自动成立（对任意 $F$）。
`c269` 数值核对：随机 $F,H$，$P$ 在所有测试 $\lambda$ 处秩 $\le1$。

所以 $q=2,\omega=1$ 没有谱信息；要非平凡必须 $\omega\ge2$。

### 2. $q=3,\omega=2$：失败 $\iff$ 特征向量落入 $\operatorname{im}H$

$P=(\lambda I-F)H$；在特征值 $\lambda_0$ 处，
$$\operatorname{rank}P(\lambda_0)<2\iff \operatorname{im}H\cap E_{\lambda_0}(F)\ne0.$$
`c269`：$\operatorname{im}H=\operatorname{span}\{e_1,e_2\}$ 时在 $\lambda=0,1$ 掉秩；
避开三条特征线的平面 $\operatorname{span}\{e_1+e_3,e_2+e_3\}$ 在所有测试点保持秩 2。

于是 $(5b)$ 成功 = “平面避开所有特征线”，是一个**非零条件**
（Plücker 坐标全非零）；$(5b)$ 失败 = “包含特征线”，是等式。

## 对 $q1$ 的含义

- 要证 $\exists\mathbb R$-hardness，应把 $(5b)$ 用作**非零守卫**，等式由 $(5a)$ 提供；
- 具体子问题：
  1. **等式 gadget**：$(5a)$ 的秩条件编码 $f(x)=0$；
  2. **非零 gadget**：$(5b)$ 的极大子式 gcd 编码 $f(x)\ne0$；
  3. **组合**：共享 witness，保持两边；
- 这比“用 $(5b)$ 编等式”自然得多，也解释了为什么之前的系数编码方向反了。

## 进展

* 明确 $(5a)$=等式、$(5b)$=非零的正确极性；
* $q=2,\omega=1$ 自动、$q=3,\omega=2$ 特征向量判据的精确核对；
* 给出 $\exists\mathbb R$-hardness 的两个子 gadget 目标。

## 最终结论

* 路线 B 的正确形式是“等式 + 非零”，不是“把方程写进谱条件”；
* 需要构造：
  - $(5a)$ 的等式 gadget（秩条件）；
  - $(5b)$ 的非零 gadget（gcd=1 当且仅当目标多项式非零）；
* 若两者可组合，$q1$ 可望 $\exists\mathbb R$-hard。

## 放弃原因

* 未构造非零 gadget；
* 未构造等式 gadget（门路线已显示 $(5a)$ 的等式 encoding 很难）；
* 未组合。

## 残留价值

* 极性判断（决定性）；
* 两个明确的 gadget 目标；
* 与专家 74 号“nonvanishing guard”一致。

## 相关文件

* [attempts/253](../../../q1_true/multiplication_gate/attempts/253_coefficient_encoding_obstruction.md)
* [attempts/251](../../../q1_true/multiplication_gate/attempts/251_coupled_plane_obstruction.md)
* `tools/verification/c269_spectral_polarity.py`

## 状态

* 路线 B 形式：**[M2 纸面 + 数值核对]**。
* Gadget：**[未构造]**。
