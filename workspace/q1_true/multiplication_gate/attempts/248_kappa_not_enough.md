> **已修正（255/专家 75 号）**：$N$ 满列秩 ⇒ $\operatorname{rank}[N,AN]\ge k$ ⇒ $\kappa_{\rm obs}\ge rk$，
> 所以固定 $\kappa_{\rm obs}$ **确实**控制 $k$。本文“$k$ 无界、κ_obs 不控制 k”的结论错误；
> 正确版本见 [255](255_kappa_correction.md)。

# $\\kappa_{\\rm obs}$ 单独是否足够？—— 行数有界但列数无界的障碍

> 2026-11-09。对 247 的补充与修正：固定 $\\kappa_{\\rm obs}$ 确实把**自由参数**压到常数维，
> 但它**不**自动给出 XP，因为 $H$ 的**列数 $k$** 仍可随 $n$ 增长，
> 秩条件需要全部 $(\\omega+1)$-子式，个数随 $k$ 增长。安全的多项式定理是固定 $(q,c)$（247）。
> 状态：**M2（纸面）**。

## 目标

判定“固定 $\\kappa_{\\rm obs}$ ⇒ 多项式”是否成立，或需要什么额外参数。

## 设想与理由

74 号建议 $\\kappa_{\\rm obs}=r\\operatorname{rank}[N,AN]$ 作为有效维数。247 用它给出固定 $(q,c)$ 的定理；
但 74 号也警告 $\\kappa_{\\rm obs}$ 是“压缩数据的维数，不一定是最终最优参数”。
本文件检查：固定 $\\kappa_{\\rm obs}$ 是否足以控制整个问题的规模。

## 做法

### 1. $\\kappa_{\\rm obs}$ 控制什么

- $r=q-r_0\\le\\kappa_{\\rm obs}$（若 $\\operatorname{rank}[N,AN]\\ge1$），所以 $q$ 有界；
- 由 247 的 $\\omega\\le q-1$，$\\omega$ 也有界；
- 但 $k=\\omega+c$，$c$ 可随 $n$ 增长，所以 **$k$ 无界**。

### 2. 障碍：子式个数

$H,H_A$ 是 $q\\times k$，$q$ 有界、$k$ 无界。
- $(5a)$：$\\operatorname{rank}[H_A;H]=\\operatorname{rank}H$，需要所有 $(\\omega+1)$-子式为零；
  个数 $\\binom{2q}{\\omega+1}\\binom{k}{\\omega+1}$ 随 $k$ 增长（$\\omega$ 固定时是 $k^{\\omega+1}$）。
- $(5b)$：$P(\\lambda)$ 的极大子式 gcd $=1$，子式个数同样随 $k$ 增长。

固定 $\\kappa_{\\rm obs}$ 只给“参数 $t$ 的维数固定”，但公式规模（子式个数）仍随 $k$ 增长；
实量词消去的复杂度对公式规模是多项式的，但这里公式规模本身不是 $\\operatorname{poly}(n)$。

### 3. 结论

$$\\boxed{\\text{固定 }\\kappa_{\\rm obs}\\ \\not\\Rightarrow\\ \\text{自动 XP（至少不能由 247 的论证直接得到）}.}$$

安全的多项式定理是：
$$\\boxed{\\text{固定 }(q,c)\\ \\Rightarrow\\ k\\le q-1+c\\ \\text{有界}\\ \\Rightarrow\\ \\text{常数维、常数子式}\\ \\Rightarrow\\ \\text{多项式}.}$$

若要用 $\\kappa_{\\rm obs}$ 单独作参数，需要额外的**紧凑证书**：
- 用行空间基（$q$ 行、$\\omega$ 维）表示秩条件，避免枚举列子式；
- 或用 Bezout/subresultant 的紧凑表示处理 $(5b)$；
- 或把 $k$ 也纳入参数：$\\kappa_{\\rm obs}^{+}=\\kappa_{\\rm obs}+k$（等价于固定 $(q,c)$ 的实用版本）。

### 4. 修正 247 的表述

247 的“固定 $(q,c)$”是安全的；但**不能**写成“固定 $\\kappa_{\\rm obs}$ ⇒ 多项式”。
docs/05 Q10 已把这一点列为开放问题。

## 进展

* 明确 $\\kappa_{\\rm obs}$ 控制 $q,\\omega,r$，但不控制 $k$；
* 指出子式个数障碍；
* 安全定理仍是固定 $(q,c)$。

## 最终结论

* $\\kappa_{\\rm obs}$ 是**冗余维数**的正确概念，但不是完整的可解性参数；
* 固定 $(q,c)$ 是第一个严格的多项式 regime；
* 固定 $\\kappa_{\\rm obs}$ 的 XP 需要紧凑行列式证书，开放。

## 放弃原因

* 未构造紧凑证书；
* 未证 fixed $\\kappa_{\\rm obs}$ 的 XP 或不可能；
* 未实现算法。

## 残留价值

* 修正了一个可能的过度声称；
* 明确下一步：紧凑行列式/Bezout 证书，或把 $k$ 纳入参数。

## 相关文件

* [attempts/247](247_fixed_qc_tractable.md)
* [attempts/246](../../rank_gates/attempts/246_74_verdict.md)
* [docs/05 Q10](../../../../docs/05_open_questions.md)
* `tools/verification/c248_kappa_check.py`（90 个随机实例 PASS）


**Lean 内核**：`tools/lean/MyProof/KappaObs.lean`（`finrank_ker_pairMap` 等，pairMap 的秩-零化度；`lake env lean` EXIT 0，axioms 仅 propext/choice/quot）。矩阵实例与“$r$ 行相乘”由纸面 + `c248_kappa_check.py`（90 例）覆盖。

## 状态

* 修正：**[M2 纸面]**。
* 紧凑证书：**[开放]**。
