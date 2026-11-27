# observability_chain —— 可观性链：$(5b)$ 恒成立，$(5a)$ 需"链闭合"

> **对应 docs 条目**：B.13（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

## 陈述

设 $L_k=\begin{bmatrix}C\\ CA\\ \vdots\\ CA^{k-1}\end{bmatrix}$（$k\ge1$），$H_k=\begin{bmatrix}C\\ \vdots\\ CA^{k}\end{bmatrix}$。

1. **$(5b)$ 恒成立**：对一切 $\lambda$，$\operatorname{rank}Q_{L_k}(\lambda)=\operatorname{rank}H_k$。
2. **$(5a)$**：$k=1$ 时**恒成立**；$k\ge2$ 时 $(5a)\iff$ **链在 $k-1$ 步闭合**，即
   $\operatorname{rank}H_k=\operatorname{rank}H_{k-1}$（等价地 $CA^k\in\operatorname{row}[C;\dots;CA^{k-1}]$）。

## 证明

**(1)** $Q_{L_k}(\lambda)$ 的行是 $\lambda CA^i-CA^{i+1}$（$0\le i<k$）以及 $CA$、$C$。

* $\le h$：这些行都在 $\operatorname{row}(L_k;CA;C)$ 里（$\lambda L_k$ 与 $L_kA$ 的行都是 $C A^j$，$j\le k$）✓。
* $\ge h$（$\lambda\ne0$）：由 $\lambda CA^i-CA^{i+1}$ 可反解 $CA^i=\lambda^{-1}\bigl(CA^{i+1}+(\lambda CA^i-CA^{i+1})\bigr)$，
  逐次（$i=0$ 起）得到 $C,CA,\dots,CA^{k-1}$，再由 $i=k-1$ 那行得到 $CA^k$ ⟹ span 含 $\operatorname{row}H_k$ ✓。
* $\ge h$（$\lambda=0$）：行是 $-CA^{i+1}$（$i<k$）加 $CA,C$ ⟹ span 也是 $\operatorname{row}H_k$ ✓。

故秩恒为 $\operatorname{rank}H_k$ ✓。

**(2)** $(5a)$ 是 $\operatorname{rank}[L_kA;L_k;CA;C]=\operatorname{rank}[L_k;CA;C]$。
左边：$L_kA$ 的行是 $CA,\dots,CA^k$，故左边 $=\operatorname{rank}H_k$。
右边：$[L_k;CA;C]$ 在 $k\ge2$ 时 $=\operatorname{row}H_{k-1}$；在 $k=1$ 时 $=[C;CA]=H_1$。
故 $k\ge2$ 时 $(5a)\iff\operatorname{rank}H_k=\operatorname{rank}H_{k-1}$，而 $k=1$ 时 $(5a)$ 恒真 ✓。
$H_k$ 与 $H_{k-1}$ 的秩相同 $\iff CA^k\in\operatorname{row}H_{k-1}$ ✓。

**反例（$(5a)$ 会失败）**：$n=3$、$A e_0=e_1,\ A e_1=e_2,\ A e_2=0$、$C=e_0^{\mathsf T}$、$k=2$：
$CA=e_1$、$CA^2=e_2\notin\operatorname{row}[e_0;e_1]$ ⟹ $(5a)$ 左边秩 $3$、右边秩 $2$ ⟹ 失败 ✗。

## 等级与验证

- **(1) [已证-纸面]**（上文）+ **[精确验证]**：`tools/verification/kron_sweep.py` 的链族候选
  在 $n=6,7,8$ 上全部通过 $(5b)$；
- **(2) [已证-纸面]**（上文）+ 反例（$n=3$ 的手算，已写入上文）。

## 与专家复核的关系

专家 2026-11-02 §6 同意 (1) 的证明，并说"$(5a)$ 是显然的，因为 $L_kA$ 的行是 $CA,\dots,CA^k$，
已经在 $[L_k;CA;C]$ 的行空间里"。**这一步需要 (2) 的闭合假设**：$CA^k$ 一般**不在**
$\operatorname{row}[C;\dots;CA^{k-1}]$ 里（见上面的 $n=3$ 反例）。所以：
- 作为**谱条件 $(5b)$ 的可行族**，链族无条件可用 ✓；
- 作为**观测器候选**（还要 $(5a)$），必须加闭合假设。

## 意义

- 给出一个**构造性**的 $(5b)$-可行族，用于压力测试 T4-b（$d_\infty=h-\operatorname{rank}L$）；
- 也解释了"为什么大 $q$ 的可行铅笔很常见"：链在闭合后 $(5a)$ 与 $(5b)$ 同时成立。

## 复现

```bash
python tools/verification/kron_sweep.py 8 6   # 链族候选参与扫描
python tools/verification/kron_t4b_prime.py    # 链族上核对 sum(eps)=rank L
```
