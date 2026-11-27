# kron_null_module —— $(5a)$ ⟹ 右最小指标全为 $0$

> **对应 docs 条目**：B.6（见 [docs/02](../../../../docs/02_theorems_proven.md) §0.1 归并表）

## 陈述

设 $(A,C,L_0)$ 给定、$L$ 满足 $(5a)$。则观测器铅笔
$$Q_L(\lambda)=\begin{bmatrix}\lambda L-LA\\ CA\\ C\end{bmatrix}$$
的**右最小指标全为 $0$**（其右零模有常值基）。

只用 $(5a)$，**不需要** $(5b)$。

## 状态

**[已证-纸面]** + **[Lean 内核]**（[tools/lean/MyProof/KronCoeff.lean](../../../../trash/lean_removed_2026-11-19/tools/lean/MyProof/KronCoeff.lean)：`kron_coeff_chain_strong` / `kron_coeff_mem_N`，登记在 STATEMENT_MAP；**差异**：多项式翻译与 Kronecker 结论在纸面） + **[精确验证 150/150]**（$n=6,7,8$，每维 50 个满足 $(5a)$ 的铅笔）。

## 文件

| 文件 | 内容 |
|---|---|
| [theorem.md](theorem.md) | 陈述 + 证明（按 $\lambda$ 的幂展开 + $(5a')$ + 归纳）|
| [verify.py](verify.py) | 在 $n=6,7,8$ 的 150 个满足 $(5a)$ 的铅笔上精确核对（**验证不是证明**）|

## 复现

```bash
python proof/kron_null_module/verify.py
```

预期：`满足 (5a) 的铅笔：150 个`、`右最小指标全为 0：150 / 150`。

## 意义与边界

* 这是专家 2026-11-02 §7 第 5 步要的"一条观测器特有的限制"——但它是 $(5a)$ 的**直接推论**，
  所以**不是**新的观测器理论，只是"铅笔分块结构 + $(5a)$"的后果；
* 它与一般铅笔的"常数秩 ⇏ 右指标 0"（反例 $[\lambda\ 1]$，见
  [proof/refuted R18](../../../../proof/refuted/README.md)）不矛盾：那条讲一般铅笔，这里用了 $Q_L$ 的分块与 $(5a)$；
* 剩下的结构问题（$d_\infty$、左侧）见 [workspace/kronecker/TARGET_FORM_T.md](../../../../workspace/kronecker/TARGET_FORM_T.md)。

## 相关

- [proof/refuted R18](../../../../proof/refuted/README.md)（被推翻的"$(5b)$ ⟹ 右指标 0"）
- [workspace/kronecker/](../../../../workspace/kronecker/README.md)（Kronecker 工具与实验）
