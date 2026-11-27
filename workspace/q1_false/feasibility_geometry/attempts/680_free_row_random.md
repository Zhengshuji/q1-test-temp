# 680 带自由行的可行性搜索：678 判据的可操作验证
> **审计注（729）**：$G=LW$ 的固定-$H$ 可达空间是 $T=\{lW:lN=0\}\subseteq S$；本文若把 $G\in S$ 当作可实现判据，需加 $T=S$ 或改用 $T$。


> 2026-11-27。用 [680_free_row_random.py](680_free_row_random.py) 在 638 数据上验证 678 的 $\exists H$ 判据。
> 状态：**[精确验证]**（有限随机搜索）。

## 设置

638 的数据：$Z'=\begin{bmatrix}0&0&0\\1&0&0\\0&0&0\end{bmatrix}$、$S=\operatorname{span}\{e_2\}$、$k=3$、$q=3$、$r_0=1$、$H_0=e_1^{\mathsf T}$。
自由行的行空间取 $\operatorname{span}\{e_1,e_2\}$（使 $\operatorname{rank}H=2$）；$G$ 的行在 $S$ 内（只有第 2 列非零）。

对每组 $(H,G)$ 构造 $P=\lambda H-(HZ'+G)$、2-子式族、$M\in\mathbb C^{4\times 2m}$，检查 $\operatorname{rank}M=4$。

## 结果

- 随机搜索 2000 组（整数系数 $\{-2,\dots,2\}$）：**找到**可行点
  $$H=\begin{bmatrix}1&0&0\\1&1&0\\-2&0&0\end{bmatrix},\qquad
  G=\begin{bmatrix}0&2&0\\0&1&0\\0&1&0\end{bmatrix},$$
  $\operatorname{rank}M=4$、$\operatorname{rank}[M\mid e_0]=4$ ⇒ $(5b)$ 成立；
- 638 的已知可行点 $H=\operatorname{diag}(1,1,0)$、$G=\begin{bmatrix}0&0&0\\0&0&0\\0&1&0\end{bmatrix}$ 同样 $\operatorname{rank}M=4$。

## 结论

- 678 的判据可操作：带自由行时，确实存在 $(H,G)$ 使 $D_2\ne0$；
- 随机搜索可作为**可行性 Monte Carlo 测试**：若可行，通常很快找到；若不可行（如 661），永远找不到；
- 但随机搜索不是多项式时间判定，也不能证明“不存在”（除非有 $D\equiv0$ 的符号证明）。

## 意义

- 与 679 对照：固定 $L$ 时判定是多项式时间；带自由行时“选择 $H,G$”是搜索问题；
- 与 672/673 对照：这里 $D_2\not\equiv0$ 是通过显式点验证的，符合“一般层可行”的图像。

## 下一步

1. 把随机搜索用于更多实例（含 $r_0\ge1$、$S$ 不同维数），估计“可行/不可行”的分布；
2. 对找不到可行点的实例，尝试符号证明 $D\equiv0$（661 型）；
3. 研究单自由行的 PIT/图表归约（见 679 的下一步）。

## 状态

- 随机验证：**[精确验证]**（有限）；
- 一般判定的多项式算法：**[未做]**。
