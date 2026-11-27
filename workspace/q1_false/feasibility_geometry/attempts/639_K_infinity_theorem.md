# 639 定理：$\omega\le k-\dim K_\infty$（$K_\infty$ 为 $Z'$ 在 $S^\perp$ 内的最大不变子空间）

> 2026-11-27。ChatGPT 提出 $K_\infty$ 不变量；本文件把它写成定理并证明，解释 629/631/638 与穷举现象。
> 状态：**[已证-纸面]**。

## 设定

$k=\dim K_0$、$q$ 行；$H_A=HZ'+G$，$G$ 的每一行在 $S=\operatorname{row}(W)$ 内，$s=\dim S$。
$K=S^\perp\subseteq\mathbb C^k$（$\dim k-s$），
$$K_\infty=\bigcap_{j\ge0}(Z')^{-j}K=\{x\in K:\ (Z')^jx\in K\ \forall j\ge0\},$$
即 $Z'$ 在 $K$ 内的**最大不变子空间**。

## 定理

若 $(5a)$、$(5b)$ 成立，则
$$\boxed{H|_{K_\infty}=0,\qquad \omega=\operatorname{rank}H\ \le\ k-\dim K_\infty.}$$

## 证明

1. 对 $x\in K=S^\perp$：$Gx=0$（$G$ 的每行在 $S$ 内），故 $ZHx=HZ'x$。
2. 对 $x\in K_\infty$，由不变性 $(Z')^jx\in K_\infty\subseteq K$，归纳得
   $$Z^jHx=H(Z')^jx\qquad(j\ge0).$$
3. 反设存在 $x_0\in K_\infty$ 使 $Hx_0\ne0$。$K_\infty$ 是 $Z'$-不变子空间，按 $Z'|_{K_\infty}$ 的广义特征分解
   $K_\infty=\bigoplus_\lambda E_\lambda$；$H$ 在某个 $E_\lambda$ 上非零。
   在该 $E_\lambda$ 中取 $u$ 使 $Hu\ne0$ 且 $(Z'-\lambda)u\in\ker H$（按广义特征向量的层级取最小者）。
   则
   $$ZHu=HZ'u=\lambda Hu+H\big((Z'-\lambda)u\big)=\lambda Hu,$$
   即 $Hu\in\operatorname{im}H$ 是 $Z$ 的特征向量（特征值 $\lambda$）。
4. 但 $(5b)$ 要求 $\operatorname{rank}(\lambda H-ZH)=\omega$ 对所有 $\lambda$；若 $Hu\ne0$ 且 $ZHu=\lambda Hu$，
   则 $(\lambda H-ZH)u=0$，秩掉——矛盾。故 $H|_{K_\infty}=0$。
5. 于是 $\ker H\supseteq K_\infty$，$\omega=\operatorname{rank}H=k-\dim\ker H\le k-\dim K_\infty$。$\square$

## 检验（与已知结果对照）

| 情形 | $S$ | $K_\infty$ | 上界 | 已知 |
|---|---|---|---|---|
| 629（$W=0$） | $S=0$ | $K_\infty=\mathbb C^k$ | $\omega\le0$ | ✓ 只有 $\omega=0$ |
| 631（$W$ 满行秩） | $S=\mathbb C^k$ | $K_\infty=0$ | $\omega\le k$ | ✓ 无限制 |
| 638（反例） | $S=\operatorname{span}\{e_2\}$，$Z'=\begin{bmatrix}0&0&0\\1&0&0\\0&0&0\end{bmatrix}$ | $\dim K_\infty=1$ | $\omega\le2$ | ✓ $\omega=2$ 可行 |
| 634/637（$S=e_1$，三种 $Z'$） | $S=\operatorname{span}\{e_1\}$ | $\dim\ge2$ | $\omega\le1$ | ✓ $\omega=2$ 全部不可行 |

## 意义

- 这是一个**数据层面**的上界：$Z'$ 与 $S$ 固定，$K_\infty$ 可计算；
- 若 $k-\dim K_\infty<\operatorname{rank}H_0$（或小于所需 $\omega$），实例**不可行**——data-dependent 的不可行判据；
- 它统一了 629、631、638 与穷举结果，是比 $\omega\le s$ 更正确的结构定理。

## 下一步

1. 检查“$\omega\le k-\dim K_\infty$ 且 $H_0$ 可扩展”是否**充分**（638 达到上界，629/631 也吻合）；
2. 若充分，则 q1 的可行性判定可归约为计算 $K_\infty$ + 线性代数——q1 ∈ P 的一步；
3. 把证明与 ChatGPT 交叉核对。

## 状态

- 定理：**[已证-纸面]**；
- 充分性：**[M2 猜想]**。
