# 命题：顶层（$\rho=d$）的可观测判据

> **对应 docs 条目**：B.2（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

## 陈述

设 $\rho=d$（即 $\pi(\mathcal V)=\mathbb C^n/\mathcal J$）。则

$$(5b)\iff \operatorname{rank}\big[(D_W)^{\mathsf T};\ (D_W)^{\mathsf T}T_W;\ \dots;\ (D_W)^{\mathsf T}T_W^{d-1}\big]=d,$$

即 $(D_W^{\mathsf T},T_W)$ **可观测**，其中 $T_W$ 是 $A$ 在 $\mathbb C^n/\mathcal J$ 上的作用、$D_W$ 是由 $\mathcal V\cap\mathcal J$ 决定的读映射。

## 证明

$Q_{\mathcal V}(\lambda)=[-D_W\ \mid\ \lambda I_d-T_W]$；$(5b)\iff\operatorname{rank}Q_{\mathcal V}(\lambda)=d\ \forall\lambda$（[docs/02](../../docs/02_theorems_proven.md) B.1）。
右边恒为 $d$ 加上 $[-D_W;\lambda I-T_W]$ 的行数条件 ⟹ PBH 型判据 ⟹ 可观测性。$\square$

**等级**：[已证] + [精确验证 65/65]（`tools/certificates/c191_pbh.py`）。

## 附带结论（$V=\mathbb C^n$ 的可行性）

$\mathcal V=\mathbb C^n$ 满足 $(5b)$ $\iff$ $A^{\mathsf T}$ 没有落在 $K=\ker[C;CA]$ 里的特征向量。
（否则取该特征向量 $v$，$\lambda v=vA$，$vC=vCA=0$，破坏 $\lambda I-A$ 的行满秩。）

**等级**：[已证]。**用途**：说明"$q=n$ 层总是非空"是**假**的。

## 复现

```bash
python tools/certificates/c191_pbh.py
```

## 文件

| 文件 | 内容 |
|---|---|
| [theorem.md](theorem.md) | B.2 的**完整证明**（铅笔恒等式 + PBH）|
| verify.py | 精确算术复核（验证，不是证明）|
