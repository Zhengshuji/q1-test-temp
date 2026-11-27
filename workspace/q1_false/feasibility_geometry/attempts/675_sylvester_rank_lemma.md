# 675 一般 $d$ 的 Sylvester 秩引理（猜想）与证据

> 2026-11-27。把 674 的一般 $d$ 猜想归结为一条关于“多多项式 Sylvester 映射”的秩公式，并收集证据。
> 状态：**[猜想]**（核心引理）+ **[已证-纸面]**（$d=2$）+ **[精确验证]**（抽样）。

## 引理 S（Sylvester 秩公式，猜想）

设 $f_1,\dots,f_m\in\mathbb C[\lambda]$，$\deg f_i\le d$，且 $\max_i\deg f_i=d$。令 $g=\gcd(f_1,\dots,f_m)$。定义
$$\Phi:\bigoplus_{i=1}^m\mathbb C[\lambda]_{<d}\longrightarrow\mathbb C[\lambda]_{<2d},\qquad
(g_i)\longmapsto\sum_i g_if_i .$$
则
$$\boxed{\operatorname{rank}\Phi=2d-\deg g .}$$

对 $m=2$ 这是经典 Sylvester 矩阵的秩公式（$\operatorname{rank}=2d-\deg\gcd$，当 $\deg f=\deg g=d$）。对 $m>2$ 是否仍成立，是本文件的核心问题。

## 由引理 S 推出 674 的猜想

若 $\operatorname{rank}H=d$，则某个 $d$-子式 $f_j$ 的次数恰为 $d$（其首项系数是 $H$ 的一个非零 $d$-子式），故 $\max\deg f_i=d$。
由引理 S：
$$\operatorname{rank}M=2d-\deg\gcd(f_i).$$
于是
$$(5b)\iff\gcd=1\iff\operatorname{rank}M=2d .$$
（$M$ 就是 $\Phi$ 在单项式基下的矩阵。）

## 证据

| 证据 | 内容 |
|---|---|
| $d=1$ | 674：秩 $<2$ ⇒ 所有条目常数 ⇒ $H=0$，矛盾 |
| $d=2$ | 674 的完整证明 |
| $d=3$ 的铅笔样本 | 4 个随机秩 3 的 $H$、随机 $Z$：全部 $\operatorname{rank}M=6$，无“秩 $<6$ 且可解” |
| 抽象多项式抽样 | 3000 组随机三次三元组（$\gcd=1$）：**全部** $\operatorname{rank}M=6$，无“秩 $<6$ 且可解” |
| 非平凡 gcd 抽样 | 5 组 $f_i=(\lambda+a)h_i$（$\deg h_i\le2$）：$\deg\gcd=1$，$\operatorname{rank}M=5=2d-\deg g$ ✓ |

## 证明引理 S 的可能路线

1. **Smith 形**：把 $1\times m$ 行 $[f_1\ \cdots\ f_m]$ 化为 $[g\ 0\ \cdots\ 0]$（$g=\gcd$）；映射 $\Phi$ 与“乘以 $g$”在相差可逆变换下等价；
2. 于是只需证 $\gcd=1$ 时 $\Phi$ 满射（秩 $2d$）：即对任意 $p\in\mathbb C[\lambda]_{<2d}$，存在 $g_i$（$\deg<d$）使 $\sum g_if_i=p$；
3. 这一步可能需要用“$\max\deg f_i=d$”来保证 $\lambda^{2d-1}$ 可达，再向下归纳；
4. $m=2$ 的经典情形由 Sylvester 矩阵的行列式（结式）给出；$m>2$ 可用“两两约化 + 归纳”或“Macaulay 矩阵”的标准结论。

## 风险

- 若引理 S 对 $m>2$ 不成立（例如 $m\ge3$ 时秩公式有修正项），674 的猜想就需要修改；
- 抽样只覆盖小范围（三次、整数系数），不能排除反例。

## 下一步

1. 先证 $m=3$、$d=3$ 的引理 S（最小非经典情形）；
2. 用 Smith 形/结式实现一个精确算法，在随机样本上验证秩公式（含 $\deg g\ge1$ 的情形）；
3. 若引理 S 成立，则 674 的一般 $d$ 猜想随之成立，统一判据的“满秩 ⇔ 可解”即完成。

## 状态

- 引理 S：**[猜想]**；
- $d=1,2$：**[已证-纸面]**；
- 抽样：**[精确验证]**（有限）。
