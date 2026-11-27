# 命题：$S=\mathcal J$ 闭包族

> **对应 docs 条目**：C.1（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

$$\operatorname{row}(L_0)=\mathcal J,\ \ \langle\mathcal J\rangle_A=\mathbb C^n\ \Longrightarrow\ q_{\min}=n\ \text{（或不可行）}$$

## 状态

| 项 | 值 |
|---|---|
| 等级 | [已证]（[theorem.md](theorem.md) 完整证明）|
| 复核 | `python tools/certificates/c190_invariant_family.py` → $8/8$ 实例 $q_{\min}=n$ |
| 用途 | 严格推翻 $\dim V+1$（R1）与 $\max(r,\rho^*+1)$（R3）；**不**推翻 $F_3$（R4）|

## 文件

| 文件 | 内容 |
|---|---|
| [theorem.md](theorem.md) | 完整证明（引理 2.1/2.3、推论 2.2、用途表）|

## 一句话

$(5a)$ 在这个族里强制 $\mathcal V$ 是 $A$-不变且 $\supseteq\mathcal J$，于是被闭包吃掉全部维数——这是"行数可以很大但问题依旧多项式可判"的典型（`c190` 只用来算 $\langle\mathcal J\rangle_A$）。