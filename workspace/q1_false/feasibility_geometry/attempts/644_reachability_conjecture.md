# 644 猜想：可行 $\iff \operatorname{rank}H_0\le k-\dim K_\infty$

> 2026-11-27。由 639 的上界与 638/641 的构造，提出“上界可达”的猜想；并记录一个未决的实验。
> 状态：**[M2 猜想]** + **[精确验证]**（部分）。

## 猜想

记 $\omega^*=k-\dim K_\infty$。若 $q\ge\omega^*$、$q-r_0$ 足够、且 $\operatorname{rank}H_0\le\omega^*$，则实例**可行**；
反之（$\operatorname{rank}H_0>\omega^*$）不可行。

## 支持

| 情形 | $\omega^*$ | $\operatorname{rank}H_0$ | 可行性 | 与猜想一致 |
|---|---|---|---|---|
| 629（$W=0$） | 0 | $>0$ 或 $0$ | 仅 $H_0=0$ 可行 | ✓ |
| 631（$W$ 满行秩） | $k$ | $\le k$ | 可行 | ✓ |
| 638 | 2 | 0 | 可行（$\omega=2$） | ✓ |
| 634/637（$S=e_1$，三种 $Z'$） | 1 | 0 | $\omega=2$ 全不可行；$\omega=1$ 未定 | 部分 |

## 精确验证（638 数据的“典范 $H$”）

取 $H=\operatorname{diag}(1,1,0)$（核 $=\operatorname{span}\{e_3\}=K_\infty$），解 $ZH=HZ'+G$（$G$ 行在 $S$ 内）：
$$Z=\begin{bmatrix}0&1&0\\1&0&0\\0&1&0\end{bmatrix}\ (\text{令自由参数为 }0),\qquad G=\begin{bmatrix}0&1&0\\0&0&0\\0&1&0\end{bmatrix},$$
$2\times2$ 子式 gcd $=1$ ⇒ **可行**。所以 638 的上界可达。

## 未决实验

对 $S=e_1$、$Z'=C_3$（$K_\infty=\operatorname{span}\{e_2,e_3\}$，$\omega^*=1$）：
- 取 $H=\operatorname{diag}(1,0,0)$（核 $\supseteq K_\infty$）时约束 $ZH=HZ'+G$ **无解**；
- 其它 rank-1 $H$ 是否可行未完成（扫描过慢被终止）。

这说明“上界可达”不是对任意 $H$ 成立，需要存在合适的 $H$；猜想的完整形式应包含“存在性”。

## 下一步

1. 对 $\omega^*=1$ 的小族做**定向**构造（不要盲目扫描）：从 $K_\infty$ 的补空间出发选 $H$；
2. 若 $\omega^*$ 层总可构造，则猜想成立，q1 判定 = 计算 $K_\infty$ + 检查 $\operatorname{rank}H_0$；
3. 否则寻找“上界不可达”的反例。

## 状态

- 638 的典范构造：**[精确验证]**；
- 一般猜想：**[M2]**。
