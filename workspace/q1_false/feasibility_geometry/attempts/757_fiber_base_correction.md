# 757 基础更正：$G$ 的纤维是 $H W_{\mathrm{top}}+T^q$，不是 $T^q$

> 2026-11-27。复核 692 的推导时发现一处基础错误：$LW$ 的**基项**被丢掉了。本文给出正确结构，并给出受影响的结论。
> 状态：**[更正]**（影响 692/693/697/726/749/753 的表述；638/733/747 不受影响）。

## 错误所在

692 写 $L=L_N+L_0$、$L_0N=0$，于是 $G=LW=L_NW+L_0W$，然后声称“$G$ 的行空间是 $T$”。
但 $L_NW$ 是**非零基项**，不能丢掉；$L_0W$ 才是 $T$ 方向。

## 正确的纤维结构

取标准坐标 $N=\begin{bmatrix}I_k\\0\end{bmatrix}$（$n\times k$）。$LN=H$ 只约束 $L$ 的前 $k$ 列，后 $n-k$ 列自由。写
$$W=\begin{bmatrix}W_{\mathrm{top}}\\ W_{\mathrm{bot}}\end{bmatrix},\qquad W_{\mathrm{top}}\in\mathbb C^{k\times k},\ W_{\mathrm{bot}}\in\mathbb C^{(n-k)\times k}.$$
则
$$T=\operatorname{row}(W_{\mathrm{bot}}),$$
且（取后 $n-k$ 列为 0 的特解）
$$\boxed{G=LW=H\,W_{\mathrm{top}}+M\,W_{\mathrm{bot}},\qquad M\in\mathbb C^{q\times(n-k)}\ \text{自由}.}$$
即 $G$ 的纤维是**仿射空间** $H W_{\mathrm{top}}+T^q$，不是 $T^q$。

## 正确的约化

令
$$Z''=Z'+W_{\mathrm{top}},\qquad G'=G-H W_{\mathrm{top}}\in T^q .$$
则
$$P(\lambda)=\lambda H-HZ'-G=\lambda H-HZ''-G' .$$
$(5a)$ 变成 $ZH=HZ''+G'$。于是 692–755 的全部 $T$-理论对 $(Z'',G')$ 成立：
- 相容性 $H_iZ''\in U+T$；
- $G'_i\in T\cap(U-H_iZ'')$；
- 690/695/725/726/734/739/749/753 中的 $Z'$ 都应读作 $Z''=Z'+W_{\mathrm{top}}$。

## 影响清单

| 对象 | $W_{\mathrm{top}}$ | 影响 |
|---|---|---|
| 638 | 0（$W=e_3e_1^{\mathsf T}$） | 不受影响（709/710 有效） |
| 733 | 0 | 不受影响（733 的 $L$ 给出 $G=(-3,-3,-3)^{\mathsf T}e_1^{\mathsf T}$，确在 $T$） |
| 747 族 | 0 | 不受影响 |
| 661 | $W$（$N=I$） | 旧推理“$G=0$”错误；但 $Z''=Z'+W=A$，$P=H(\lambda I-A)$ 在 $\sigma(A)$ 降秩 ⇒ 结论（不可行）仍成立 |
| **693** | $\begin{bmatrix}0&1\\0&0\end{bmatrix}\ne0$ | **原构造无效**：其 $G$ 与真实纤维 $H W_{\mathrm{top}}+T^q$ 不符（差 $(0,-1)$ 等不在 $T$ 的行）；见下 |
| 726（$a\ge1$） | — | 证明用 $G$ 行在 $T$；需改用 $Z'',G'$ 重述，结论待重证 |
| 749/753 | — | 假设“$G$ 行在 $T$”应改为“$G'$ 行在 $T$，$Z''=Z'+W_{\mathrm{top}}$” |

## 693 的反例核对

693 数据：$N$ 前 2 坐标、$W=\begin{bmatrix}0&1\\0&0\\1&0\\0&0\end{bmatrix}$、$H=u e_1^{\mathsf T}$（$u=(1,0,1)$）。
取 $L$ 后两列为 0，则 $LW=\begin{bmatrix}0&1\\0&0\\0&1\end{bmatrix}$；$T=\operatorname{span}\{e_1\}$。
693 的 $G=\begin{bmatrix}0&0\\1&0\\0&0\end{bmatrix}$ 与 $LW$ 之差为 $\begin{bmatrix}0&-1\\1&0\\0&-1\end{bmatrix}$，其第 3 行 $(0,-1)\notin T$ ⇒ **该 $G$ 不可实现**。

用正确的 $Z''=Z'+W_{\mathrm{top}}=\begin{bmatrix}0&1\\1&0\end{bmatrix}$ 重算：$P(0)=-HZ''-G'$ 的前两行含 $(0,-1)$ 方向，秩 $2>d'=1$ ⇒ **693 不可行**。

## 结论

- **693 撤回**（其“$t<s$ 可行例”地位失效；690 的 $t$-版本失去该紧性例证）；
- 638/733/747 因 $W_{\mathrm{top}}=0$ 全部有效；
- 661 结论有效、推理更新；
- 692/697/726/749/753 需要用 $Z''=Z'+W_{\mathrm{top}}$ 重述；**下一步优先级最高**。

## 状态

- 更正：**[已确认]**（数值核对）；
- 693：**撤回**；
- 其余影响的逐条重述：**[待做]**。
