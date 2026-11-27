# t4b_infinite_divisors —— 观测器铅笔的无穷初等因子全是 1 次

> **对应 docs 条目**：B.6（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

## 陈述

设 $L$ 满足 $(5a)$，$H=[L;CA;C]$，$h=\operatorname{rank}H$。则观测器铅笔
$$Q_L(\lambda)=\begin{bmatrix}\lambda L-LA\\ CA\\ C\end{bmatrix}$$
的**无穷初等因子全是 1 次**，个数为 $h-\operatorname{rank}L$。于是
$$d_\infty=h-\operatorname{rank}L .$$
**左指标的和**（更正版）：只用 $(5a)$ 时
$$\sum_j\varepsilon_j=\operatorname{rank}L-d_{\rm fin},$$
再要求 $(5b)$（即 $d_{\rm fin}=0$）才有 $\sum_j\varepsilon_j=\operatorname{rank}L$。

**只用 $(5a)$，不需要 $(5b)$。**

## 状态

**[已证-纸面]**（[theorem.md](theorem.md)）+ **[Lean 内核]**（`KronFactor.kron_block_factor`，见 [tools/lean/MyProof/KronFactor.lean](../../trash/lean_removed_2026-11-19/tools/lean/MyProof/KronFactor.lean)）+ **[精确验证 151/151]**（[verify.py](verify.py)，
$n=6,7,8,9,10$，其中 108 个可行）。验证现在核对四条：$d_\infty=h-\operatorname{rank}L$、
$\sum\varepsilon=\operatorname{rank}L-d_{\rm fin}$、恒等式、以及 $(5b)$ 时的 $\sum\varepsilon=\operatorname{rank}L$。

## 证明思路（六步）

1. $(5a)$ ⟹ $LA=XL+Y_1CA+Y_2C$（常值）⟹ $Q_L=P(\lambda)H$；
2. $P=U\operatorname{diag}(\lambda I-X,I_{2p})$，$U$ 常值可逆 ⟹ $Q_L$ **严格等价**于
   $M=[(\lambda I-X)L;CA;C]$；
3. 无穷因子 = 反转铅笔 $\widehat M(\mu)=[(I-\mu X)L;\mu CA;\mu C]$ 在 $\mu=0$ 的初等因子；
4. $\mu=0$ 处的局部等价（乘 $(I-\mu X)^{-1}$，局部环里的单位）⟹ 化为 $\widetilde M=[L;\mu CA;\mu C]$；
5. $\widetilde M$ 的行列式因子：$\Delta_k=\mu^{k-r_1}$（$r_1=\operatorname{rank}L$，$r_1<k\le h$），
   其余为常数；
6. 不变因子因此是 "$r_1$ 个单位 + $(h-r_1)$ 个 $\mu$" ⟹ 每个无穷因子次数 1 ⟹ $d_\infty=h-r_1$。∎

## 文件

| 文件 | 内容 |
|---|---|
| [theorem.md](theorem.md) | 完整证明（含行列式因子的上下界与达到性）|
| [verify.py](verify.py) | 151 个满足 $(5a)$ 的铅笔上的精确核对（**验证不是证明**）|

## 复现

```bash
python proof/t4b_infinite_divisors/verify.py
```

## 意义

* 这是 Workstream B 的**第二条定理**（第一条是 [B.6](../kron_null_module/README.md)）：
  B.6 管右侧（右最小指标为 $0$），本定理管无穷侧（全是 1 次）；
* 合起来：观测器铅笔的"奇异自由度"只剩**左最小指标**，且由恒等式
  $\sum\varepsilon_j=\operatorname{rank}L$ 完全钉死；
* 与专家的目标形式 T 对齐：T4-a（右指标）与 T4-b（无穷因子）现在都是**定理**，
  剩下的是"左指标"的描述（但已被 $\sum\varepsilon=\operatorname{rank}L$ 定死和）。

## 相关

- [proof/kron_null_module](../kron_null_module/README.md)（B.6）
- [proof/refuted R19](../refuted/README.md)（$\ker L=N$ 的错误等价）、R20（$d_\infty$ 用总次数的错误）
- [tools/verification/kronecker_pencil.py](../../tools/verification/kronecker_pencil.py)（`d_infinity` 字段）
- [workspace/kronecker/TARGET_FORM_T.md](../../workspace/kronecker/TARGET_FORM_T.md)
