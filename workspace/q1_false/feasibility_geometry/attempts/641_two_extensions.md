# 641 实验：同一 $K_\infty$、两个扩展一可行一不可行
> **审计注（729）**：$G=LW$ 的固定-$H$ 可达空间是 $T=\{lW:lN=0\}\subseteq S$；本文若把 $G\in S$ 当作可实现判据，需加 $T=S$ 或改用 $T$。


> 2026-11-27。按 ChatGPT 的建议做“同一 $K_\infty$、同一 $H_0$、两个扩展”的实验。
> 状态：**[精确验证]**。

## 数据

$q=k=3$、$Z'=\begin{bmatrix}0&0&0\\1&0&0\\0&0&0\end{bmatrix}$、$S=\operatorname{span}\{e_2\}$（$s=1$）；
$K=S^\perp=\operatorname{span}\{e_1,e_3\}$，
$$K_\infty=\bigcap_j(Z')^{-j}K=\operatorname{span}\{e_3\}\quad(\dim1),$$
得上界 $\omega\le k-1=2$。$H_0=0$（无固定行）。

## 两个扩展（都满足 $\omega=2$ 与上界）

| | $H$ | $Z$ | $G=ZH-HZ'$ | $\gcd$ of 2×2 minors | 可行 |
|---|---|---|---|---|---|
| A | $\begin{bmatrix}-1&-1&0\\-1&0&0\\0&-1&0\end{bmatrix}$ | $\begin{bmatrix}1&0&0\\1&-1&0\\1&0&0\end{bmatrix}$ | $\begin{bmatrix}0&-1&0\\0&-1&0\\0&-1&0\end{bmatrix}$ | $1$ | **是** |
| B | $\begin{bmatrix}-1&-1&0\\-1&-1&-1\\-1&-1&-1\end{bmatrix}$ | $\begin{bmatrix}1&0&0\\1&0&0\\1&0&0\end{bmatrix}$ | $\begin{bmatrix}0&-1&0\\0&-1&0\\0&-1&0\end{bmatrix}$ | $\lambda(\lambda-1)$ | **否** |

- 两者 $\operatorname{rank}H=2=\omega$，$G$ 的行都在 $S$ 内，$(5a)$ 自动成立（$H_A=ZH$）；
- A：$\operatorname{rank}P(\lambda)=2$ 对所有 $\lambda$（采样 $0,1,2$）；
- B：$\lambda=0,1$ 时秩 1 $<2$（$Z$ 的特征向量落在 $\operatorname{im}H$ 内）。

## 结论

- **$K_\infty$ 上界是逐 $H$ 的必要条件，不是完整不变量**：同一数据、同一 $H_0$、同一 $G$，可行性却不同；
- 决定因素是 $Z$（由 $R$ 导出）在 $\operatorname{im}H$ 上的特征向量；
- 实例层面：A 存在 ⇒ 该实例**可行**（$q=3$）。

## 下一步

- 存在性 = “能否选到 $H$ 使 $H|_{K_\infty}=0$ 且 $\operatorname{im}H$ 避开 $Z$ 的特征向量”；
- 若 $K_\infty$ 上界不满（$\omega<k-\dim K_\infty$）时总可构造 A 型扩展，则实例可行；否则需检查第二层；
- 需要把第二层化为有限个可计算的秩条件（ChatGPT 的建议）。

## 状态

- 实验：**[精确验证]**；
- 存在性判定：**[开放]**。
