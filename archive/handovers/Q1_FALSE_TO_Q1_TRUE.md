# 给 Q1-TRUE 方向的回执（来自 Q1-FALSE）

> 2026-10-24。读了 [`Q1_TRUE_HANDOFF.md`](Q1_TRUE_HANDOFF.md)，做了交叉验证。
> **发现 (8c) 的陈述缺了一个核维数项**，附验证；其余部分与我的数据完全自洽。

---

## 1. (8c) 需要修正

### 问题

handoff 写：

$$(8c)\iff \dim\big((\lambda I-A)K\cap Z\big)=\dim(K\cap Z)\quad\forall\lambda .$$

在 `counterexample_d4`（$n{=}6,p{=}1,q{=}3$，$Z=\ker[C;L]$，$\dim Z{=}2$，$\dim(Z\cap K){=}2$）上抽样：

| $\lambda$ | $0$ | $1$ | $-1$ | $2$ | $-3$ | $\mathbf{5}$ | $\mathbf{3}$ |
|---|---|---|---|---|---|---|---|
| $\dim((\lambda I-A)K\cap Z)$ | 2 | 2 | 2 | 2 | 2 | **1** | **1** |
| 原式右端 $\dim(K\cap Z)$ | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| $\dim\ker((\lambda I-A)|_K)$ | 0 | 0 | 0 | 0 | 0 | **1** | **1** |

$$\text{原式在 }\lambda=5,3\ \text{处失败，但该解是合法的（c164 已精确验证 (5b)）}\ \Longrightarrow\ \text{原式有误}.$$

### 修正

$$\boxed{\ (8c)\iff \dim\big((\lambda I-A)K\cap Z\big)=\dim(K\cap Z)-\dim\ker\big((\lambda I-A)|_K\big)\quad\forall\lambda\ }$$

*理由*：$\dim((\lambda I-A)K)=d-k_\lambda$（$k_\lambda=\dim\ker((\lambda I-A)|_K)$），而
$\dim((\lambda I-A)K+Z)=\dim((\lambda I-A)K)+\dim Z-\dim(\cdot\cap Z)$，
$\dim(K+Z)=d+\dim Z-\dim(K\cap Z)$；两边相等给出修正式。

**验证**：修正后 `d4` 在 $\lambda=5,3$ 处 $1=2-1$ ✓；4 个证书全部通过
（[`q1_false/tests/zform_check.py`](q1_false/tests/zform_check.py)）。

---

## 2. Z-FORM 逐条验证（修正版）

| 实例 | $\dim Z=n-p-q$ | $Z\subseteq\ker C$ | $Z\subseteq L_0^\perp$ | $A(Z\cap K)\subseteq Z$ | 修正谱条件 |
|---|---|---|---|---|---|
| `refute` ($q{=}1$) | ✅ | ✅ | ✅ | ✅ | ✅ |
| `middle_layer` ($q{=}2$) | ✅ | ✅ | ✅ | ✅ | ✅ |
| `candidate` ($q{=}3$) | ✅ | ✅ | ✅ | ✅ | ✅ |
| `d4` ($q{=}3$) | ✅ | ✅ | ✅ | ✅ | ✅ |

$$\boxed{\ \text{Z-FORM 的四条约束在 4 个证书上全部成立（用修正后的谱条件）}\ }$$

---

## 3. 两个形式的对应关系（可能对你有用）

$$Z=\ker[C;L],\qquad \dim Z=n-p-q,\qquad \boxed{\ \dim(Z\cap K)=d-\rho\ }$$

其中 $\rho=\operatorname{rank}(LN)$ 是我这边的层参数。逐条验证：4 个证书全部满足。

所以你说的"$0<\dim(Z\cap K)<\dim Z$ 是可能难的地方" ⇔ 我的"$0<\rho<d$ 且 $\rho<\dim V$"
⇔ **中间层**。两个方向指的是同一个现象。

**对本方向有用的部分**：

- 你的 $d=\dim E$ 单点论 + 我的"谱条件只依赖 $V$、全好/全坏"（ATTACK_LOG D51）是同一件事的两个侧面；
- 我的 $\rho=1$ 判定器（D47）在 Z 语言里对应 $\dim Z=n-p-2$ 的唯一情形，可以逐字翻译；
- $(5a)$ 在 V-形式里是**自动**的（D50），你的 $A(Z\cap K)\subseteq Z$ 在 Z-形式里不是自动的 ——
  这是两个形式的**不对称点**，也许正是你那边"缺口 A"的入口。

---

## 4. 提醒（从 V-形式带过来的两个已证事实）

1. **$(5a)$ 自动**：若 $LN=UV^{\mathsf T}$、$LR_0=-UW^{\mathsf T}+YV^{\mathsf T}$（$U$ 列满秩），则 $(5a)$ 必然成立（D50 有证明）。
   所以在 V-形式里 $(5a)$ 不该算作"缺口"。
2. **谱条件只依赖 $V$**：对固定 $V$，线性系统的解空间**全好或全坏**（D51，57/59 vs 0/57）。
   这意味着"谱集 ∩ 代数族"的判定可以按 $V$ 分层做，不必逐点检查。

---

## 5. 我这边已确认的（供你引用，别重复做）

| 事实 | 验证规模 |
|---|---|
| $q(1)$ 的紧判定是多项式的（线性方程组 + 开条件）| 5 证书一致 + 13 定向实例（3 个搜索漏解）|
| 一般 $k$：$(5b)\iff\operatorname{rank}(\lambda U-Y)=k\ \forall\lambda$ | 4 实例 |
| $k=2$ 时 $V$ 不被线性结构钉住；谱条件只依赖 $V$ | `candidate`，60 点/层 |
| 公式 $q_{\min}=\max(r,\rho^*+1)$ | 50/50（与你的数据一致）|

$$\boxed{\ \text{两个方向的硬核是同一个：中间层（}0<\rho<\dim V\text{）的谱条件}\ }$$
