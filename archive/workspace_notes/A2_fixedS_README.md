# A2_fixedS/ —— 固定 $S$ 的判据（任务）

> **主线的哪一半**：A2。给定可容许 $S\subseteq D$，判定是否存在 $U$ 使
> $$T_S\subseteq U\subseteq H/S,\quad \dim U=r,\quad U\cap B_S=0,\quad U\cap I_\lambda=0\ \ \forall\lambda .$$

## 1. 现在有什么（已沉到 `proof/`）

| 结果 | 位置 | 等级 |
|---|---|---|
| 系数空间判据：可行 $\iff\operatorname{Gr}\cap\mathbb P(K)\not\subseteq\mathbb P(\ker a_0)$ | [A2 §25](../../proof/incidence_strata/README.md) | 已证（纸面）+ 三例机器核对（`c285`）|
| 负例的结构刻画：$X\subseteq\mathbb P(\ker a_0)\iff a_0\in D(K)^\perp$ | [A2 §29.2](../../proof/incidence_strata/README.md) | 已证（纸面）|
| $(2,4)$ 上 $\operatorname{rank}(Q\|_K)\ge2$ ⟹ 判据坍缩为 $a_0\notin\operatorname{span}\{a_1,a_2\}$ | [A2 §29.2c](../../proof/incidence_strata/README.md) | 已证（纸面）|
| $(2,m)$ 的坍缩证书（$m\le6$，$D\le m-1$）| [A2 §30](../../proof/incidence_strata/README.md) | 精确证书（`c290`）|
| $n=5$ 的 pencil-span（11 例）与 $(2,6)$ 结构化铅笔（6 例）| [A2 §31](../../proof/incidence_strata/README.md) | 精确证书（`c291`、`c292`）|
| 定理 A（$\mathbb P^1/\mathbb A^1$ 有理曲线）| [A2 §27](../../proof/incidence_strata/README.md) | 已证（纸面）+ 两曲线核对 |

## 2. 当前进展（2026-10-31）

**核心判断**：$r=2$ 时判据**基本是线性代数**——$G3$ 不构成障碍。唯一退化是**非一般**的
（$(2,4),D=3$ 的 $\operatorname{rank}(Q\|_K)=1$ 实例）。

⟹ **固定 $S$ 的可判定性在 $r=2$ 上不再是 $q1$ 的瓶颈。**

## 3. 剩余工作

| 编号 | 任务 | 状态 |
|---|---|---|
| A2-1 | 把"$r=2$ 判据 = 线性代数"升级为**定理**（Zariski 开集的精确表述 + 退化参数化）| 待做 |
| A2-2 | 解除恒秩假设（秩跳变 ⟹ "一般位置 + 例外值"）| 半完成 |
| A2-3 | $r\ge3$（$G(3,m)$ 的第一个实例）| 空白 |

## 4. 相关文件

- 证明主体：[proof/incidence_strata/README.md](../../proof/incidence_strata/README.md)（§1–31）
- 实验：`proof/layer_program/c265`–`c292`
- Lean：`tools/lean/MyProof/`（A2、A2dim、A2root、A2prop3、G4）

## 5. 注意

$\operatorname{span}(X)=L$ 的"证书"是：**精确有理点集达到 $\dim L$**（下界 = 上界）。这不是采样证据。
但**退化**情形只能靠构造（如 $(2,4),D=3$ 的显式实例），采样永远只能给下界。
