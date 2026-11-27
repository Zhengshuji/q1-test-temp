# 命题：$c_0=1$、$\rho=d$ 的循环向量判据

> **对应 docs 条目**：B.2（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

> 来源：`archive/expert_correspondence/Q1_FOR_EXPERT_9.md` §4（那里有完整纸面证明）。
> 这是 $(5b)$ 侧**第二条**层判据（第一条是顶层可观测性，见 [../top_layer_observability/](../top_layer_observability/README.md)）。

## 陈述

设 $c_0=1$，即 $S=\operatorname{span}\{j_0\}\subseteq\mathcal J$（$j_0$ 是 $L_0$ 的唯一行）。取 $W$ 为 $\mathcal J$ 的补（$\dim W=d$、$W\cap\mathcal J=0$），令
$$\mathcal V=\operatorname{span}\{j_0\}\oplus W\quad(\Rightarrow\ \mathcal V+\mathcal J=\mathbb C^n,\ (5a)\ \text{自动}).$$
记 $T_W:W\to W$ 为 $A$ 沿 $\mathcal J$ 的压缩（$T_W w=\pi_W(wA)$）、$v_W=\pi_W(j_0A)$。则

$$\boxed{\ \mathcal V\ \text{不满足}\ (5b)\iff v_W\ \text{落在某个}\ T_W\text{-不变真子空间里}\iff v_W\ \text{不是}\ T_W\ \text{的循环向量}\ }$$

即：**可行 $\iff v_W$ 循环**（$\operatorname{rank}[v_W;v_WT_W;\dots;v_WT_W^{d-1}]=d$）。

## 证明要点

$(5b)$ 失败 $\iff\exists\lambda$ 与 $0\ne\psi\in\mathcal J^\perp$ 使 $\psi(\lambda\ell-\ell A)=0$ 对 $\mathcal L$ 的所有行 $\ell$。
由 $j_0\in\mathcal J$ 得 $\psi(j_0)=0$，故 $\psi(j_0A)=\lambda\psi(j_0)=0$；对 $w\in W$ 得 $\psi(wA)=\lambda\psi(w)$，
即 $\varphi:=\psi|_W\ne0$ 是 $T_W$ 的**左特征向量**且 $\varphi(v_W)=0$。
反之这样的 $\varphi$ 延拓成 $\psi$ 即得失败。$\square$

## 等级与验证

| 项 | 值 |
|---|---|
| 等级 | [已证]（纸面，来源见上）|
| 复核 | `python proof/cyclic_vector_criterion/verify.py` → **35/35** |
| 覆盖 | $n=4,5,6$、$d=2,3,4$，每例多组补空间 $W$（不同 $W$ 给不同的 $v_W,T_W$）|
| **诚实说明** | 随机采样**没有命中不可行实例**（$\varphi(v_W)=0$ 是余维条件，$\mathbb Q$ 上概率为 0）；负侧需要**构造**实例，尚未做。这与原始文档"30/30 全可行"的记录一致。|

## 意义

- 这是"每层一个判据"计划的第二条：$\rho=d$ 层 + $c_0=1$ 时可**精确判定**（一次循环性检验）；
- 它把 $(5b)$ 归结为一个**算子几何**条件（$v_W$ 的循环性），而不是行列式；
- 与可观测性判据（[top_layer_observability](../top_layer_observability/README.md)）互为补充：后者用 $(D_W^{\mathsf T},T_W)$，前者用 $v_W$ 的单向量循环性。

## 文件

- `verify.py` — 精确算术复核（正侧 35/35，负侧待构造）
- 原始证明：`archive/expert_correspondence/Q1_FOR_EXPERT_9.md` §4
