# 命题：$q_{\min}$ 的下界

> **对应 docs 条目**：A.1（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

$$\boxed{\ q_{\min}\ \ge\ \max\big(r+\varepsilon,\ \rho+\max(c_0,1)\big)\ }$$

其中 $\rho=\dim\pi(\mathcal V)$ 对任意可行解取最小，$c_0=\dim(\operatorname{row}L_0\cap\mathcal J)$，$\varepsilon=1-[L_0\ \text{本身是解}]$。

## 证明

1. $q\ge r$（$\mathcal L$ 含 $L_0$ 的 $r$ 行）；$L_0$ 非解时 $q\ge r+1$。
2. $q=\rho+c$，$c=\dim(\mathcal V\cap\mathcal J)$。
3. $c\ge c_0$（$S=\operatorname{row}L_0\subseteq\mathcal V$）。
4. $c\ge 1$：若 $c=0$，$A$ 在 $\mathcal V$ 上诱导 $\varphi$；其特征向量 $v$ 给 $(\lambda I-A)v\in\mathcal J$，于是 $\dim((\lambda I-A)\mathcal V+\mathcal J)\le q-1+j<q+j$，与 $(5b)$ 矛盾。

**等级**：[已证]。**位置**：[docs/02](../../docs/02_theorems_proven.md) A.2/A.3。

## 已知的紧性

- 不紧的例子：$n{=}4$ 反例（下界 3、真值 4）——见 [proof/refuted/](../refuted/README.md) R4。
- 因此**需要更强的 $c$-项**，见 [docs/05](../../docs/05_open_questions.md) Q4。

## 文件

| 文件 | 内容 |
|---|---|
| [theorem.md](theorem.md) | A.1–A.3 的**完整证明**（展开版）|
| verify.py | 精确算术复核（验证，不是证明）|
