# toeplitz_criterion —— 用单个 Toeplitz 矩阵的零度判 $(5b)$

> **对应 docs 条目**：B.6（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

## 陈述

设 $L$ 满足 $(5a)$，$s=\operatorname{rank}L$、$h=\operatorname{rank}H$、$m=q+2p-h$，
$R(\lambda)=[\lambda E-F\ \ B]$ 是约化 descriptor 铅笔（$[E\ B]$ 满行秩 $h$）。对 $d\ge0$，$T_d$ 是
$R(\lambda)y(\lambda)=0$（$\deg y\le d$）的块 Toeplitz 矩阵，$\nu_d=\dim\ker T_d$。则

$$\boxed{\ (5b)\iff \nu_s=(s+1)m-s\ }$$

且整条左最小指标序列由 $\nu_d-2\nu_{d-1}+\nu_{d-2}$ 恢复。

## 状态

**[已证-纸面]**（[theorem.md](theorem.md)，依赖 B.6/B.7/B.8 与最小多项式基的标准理论）
$+$ **[精确验证 66/66]**（[verify.py](verify.py)）。

判据由专家 2026-11-02 答复 §9 提出；本文补全陈述与证明。

## 文件

| 文件 | 内容 |
|---|---|
| [theorem.md](theorem.md) | 引理 1（零空间维数）+ 定理与证明 + 交叉验证说明 |
| [verify.py](verify.py) | 66 个铅笔上与 Smith 路径逐个核对（**验证不是证明**）|
| [tools/verification/toeplitz_criterion.py](../../tools/verification/toeplitz_criterion.py) | 实现（构造 $T_d$、算 $\nu_d$、恢复序列、判据）|

## 复现

```bash
python proof/toeplitz_criterion/verify.py
```

预期：`判据一致 66，不一致 0；序列一致 66，不一致 0`。

## 意义

* **WP1**：$(5b)$ 的判定不再需要 Smith 形；
* **G-4**：每个增广只需求一个常数矩阵的秩；
* **G-3**：整条指标序列可从 $\nu_0,\dots,\nu_s$ 读出，便于比较不同增广。

## 相关

- [proof/t4b_infinite_divisors](../t4b_infinite_divisors/README.md)（B.7）
- [proof/kron_null_module](../kron_null_module/README.md)（B.6）
- [proof/descriptor_reduction](../descriptor_reduction/README.md)（左指标 = $R$ 的右指标）
- [archive/expert_correspondence/answer_2026-11-02_to_01.md](../../archive/expert_correspondence/answer_2026-11-02_to_01.md)（专家答复）
