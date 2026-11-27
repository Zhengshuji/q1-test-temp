# 590 反例：$q=3$、$\omega=2$ 可以可行（推翻 589）

> 2026-11-27。589 声称 $q=3$、$\omega=2$ 不可行；本文件给出反例。
> 状态：**[精确验证]**（sympy：$\det\equiv0$、$\gcd=1$、$\operatorname{rank}P=2$）。

## 实例

$$H=\begin{bmatrix}1&0&0\\0&1&0\\0&0&0\end{bmatrix},\qquad
H_A=\begin{bmatrix}0&1&0\\0&0&0\\1&0&0\end{bmatrix}.$$

$H$ 秩 2（$\omega=2$），$H_A=ZH$，其中
$$Z=\begin{bmatrix}0&1&0\\0&0&1\\1&0&0\end{bmatrix}$$
（三阶循环置换矩阵）。

## $(5a)$

$\operatorname{row}H=\operatorname{span}\{e_1,e_2\}$；$H_A$ 的三行是 $(0,1,0),(0,0,0),(1,0,0)$——都在 $\operatorname{row}H$ 内
⇒ $\ker H\subseteq\ker H_A$ ✓。

## $(5b)$

$$P(\lambda)=\lambda H-H_A=\begin{bmatrix}\lambda&-1&0\\0&\lambda&0\\-1&0&0\end{bmatrix}.$$
- $\det P\equiv0$；
- 非零 $2\times2$ 子式：$\lambda^2$、$\lambda$、$-1$ ⇒ $\gcd=1$；
- 采样 $\lambda=0,1,2$：$\operatorname{rank}P=2$。

所以 $\operatorname{rank}P(\lambda)=2=\omega$ 对所有 $\lambda$（gcd=1 保证 $\ge2$，det=0 保证 $\le2$）✓。

## 为什么 589 的论证错了

589 断言“$\lambda I-Z$ 的 2 维限制必有特征值”。但这里 $Z$ 的特征向量是 $(1,\omega,\omega^2)$
（$\omega^3=1$），**都不在** $\operatorname{im}H=\operatorname{span}\{e_1,e_2\}$ 里；
于是 $(\lambda I-Z)|_{\operatorname{im}H}$ 对所有 $\lambda$ 可逆——没有特征值掉秩。

## 意义

- $q=3$、$\omega=2$ 的可行实例**存在**；
- 3×3 路线没有关闭；关键是让 $Z$ 的特征向量全部落在 $\operatorname{im}H$ 之外；
- 这为“参数化 $H$ 让 $Z$ 依赖自由变量”的乘法编码提供了新的起点。

## 状态

- 反例：**[精确验证]**；
- 589 的分类：**被推翻**（已在 589 标注）。
