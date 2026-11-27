# 秩屏障（rank barrier）：层 $(\rho,c)$ 可行为什么要求 $\rho$ 不太大

> **对应 docs 条目**：F.1（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

> 2026-10-30 新增。作者：接手者（第二个会话）。
> 起因：给 §82 反例找"最短证明"时发现，它其实是一个**一般机制**的特例
> （该实例 $r(0)=1<3=\rho$）。本目录把这个机制写成命题 + 复核脚本。

## 陈述

记 $\mathcal J=\operatorname{row}[C;CA]$、$j=\dim\mathcal J$、$X=\mathbb C^n/\mathcal J$、$\pi:\mathbb C^n\to X$。
对 $\lambda_0\in\mathbb C$ 定义

$$r(\lambda_0)\;:=\;\dim\pi\big(\mathbb C^n(\lambda_0 I-A)\big)\;=\;\operatorname{rank}[\lambda_0 I-A;\ C;\ CA]-j .$$

> **命题 1（秩屏障）**：设 $\mathcal L$ 是层 $(\rho,c)$ 的任一候选（$\rho=\dim\pi(\mathcal V)$、$c=\dim(\mathcal V\cap\mathcal J)$）。
> 若 $(5b)$ 在 $\lambda_0$ 处成立，则
> $$\rho\;\le\;r(\lambda_0).$$
> 等价地：**若 $\rho>r(\lambda_0)$，则层在 $\lambda_0$ 处必失败；若对某个 $\lambda_0$ 有 $\rho>r(\lambda_0)$，则该层不可行。**

## 证明（三行）

$\lambda_0\mathcal L-\mathcal LA$ 的行是 $\ell_i(\lambda_0I-A)$，故其行空间含于 $\mathbb C^n(\lambda_0I-A)$，于是

$$\operatorname{rank}[\lambda_0\mathcal L-\mathcal LA;\ CA;\ C]
=\dim\big(\operatorname{row}(\mathcal L)(\lambda_0I-A)+\mathcal J\big)
\le j+\dim\pi\big(\mathbb C^n(\lambda_0I-A)\big)=j+r(\lambda_0).$$

而 $(5b)$ 在 $\lambda_0$ 处成立要求左端 $=\operatorname{rank}[\mathcal L;CA;C]=j+\rho$。故 $\rho\le r(\lambda_0)$。$\square$

## 推论

1. **层的过滤器**：$\rho>\min_\lambda r(\lambda)$ 的层**全部**可以不看。
   由于 $\lambda\notin\operatorname{spec}(A)$ 时 $\lambda I-A$ 可逆、$r(\lambda)=d$，这个 min 只在**特征值**上取到。
2. **无解判据**：若 $\min_\lambda r(\lambda)<\rho_{ci}$，则**没有任何解**（因为任何解的 $\rho\ge\rho_{ci}$，又要 $\le\min r$）。
   这是本项目第一个"全局不可行"的多项式判据（$\rho_{ci}=P$ 已是多项式）。

   **实例（可证无解）**：[no_solution_certificate.py](no_solution_certificate.py) 里三个写死的 $n=6$、$p=2$、
   $\operatorname{rank}(A)=1$ 的实例：

   ```bash
   python proof/rank_barrier/no_solution_certificate.py
   # rank1_n6_p2_A: rank(A)=1、j=2、d=4、r(0)=1、ρ_ci=2  ⟹ 可证无解 ✓
   # rank1_n6_p2_B: rank(A)=1、j=3、d=3、r(0)=0、ρ_ci=1  ⟹ 可证无解 ✓
   # rank1_n6_p2_C: rank(A)=1、j=3、d=3、r(0)=0、ρ_ci=1  ⟹ 可证无解 ✓
   ```

   对 $\operatorname{rank}(A)=1$ 的随机族扫了 58 个实例，**58/58** 都满足 $\rho_{ci}>r(0)$ ⟹ 无解
   （这是**抽样得到的族**，不是定理；每个实例单独可证）。
   ⟹ **MIN-ROWS 不总有解**：论文里必须先声明"对可解实例求 $q_{\min}$"，否则 $q_{\min}=\infty$。
3. **对 hardness gadget 的约束**：任何想造出 $(\rho,c)$ 层不可行/可行的归约，必须让实例满足
   $r(\lambda)\ge\rho$ 对**所有**特征值 $\lambda$；换言之 $\ker(\lambda I-A)$ 不能太大、也不能藏在 $\mathcal J$ 里。
   §82 的反例正是 $r(0)=1<3$，所以它**做不了** $(3,1)$ 的"结构上允许"的实例 —— 这是 gadget 设计的硬约束。
4. **与顶层判据 B.2 相容**：若 $\rho=d$ 且层可行，则 $r(\lambda)\ge d$ 对所有 $\lambda$，即 $r\equiv d$；
   于是 B.2 的可观测性判据在它允许的情形里可以正常成立。
5. **账本审计**（[tools/ledger/c201_barrier_audit.py](../../tools/ledger/c201_barrier_audit.py)）：
   对账本里 30 个实例算 $(\rho_{ci},\min_\lambda r)$，**没有**一个被屏障否定；
   且每个有见证的实例都满足 $\rho_{ci}\le\rho_{\text{wit}}\le\min_\lambda r$（对 $P$ 实现的一条独立交叉检查）。
   在 c190 族上屏障**紧**：$\rho^*=3=\min_\lambda r$。

## 等级

| 项 | 值 |
|---|---|
| 命题 1 | **【已证-纸面】**（上面三行）|
| 推论 1–5 | 由命题 1 直接得到 |
| 验证 | `python proof/rank_barrier/verify.py` → 1484 次秩不等式检查 + 113 个定向实例 ✓ |
| 无解证书 | `python proof/rank_barrier/no_solution_certificate.py` → 3/3 实例 $\rho_{ci}>r(0)$ ✓ |

**验证不是证明**：脚本只检查"秩不等式"与"$\rho>r(\lambda_0)$ 时该 $\lambda_0$ 必失败"这两条在
随机实例上成立，不替代证明。

## 覆盖范围与限制（诚实）

- 命题**只**给出必要条件；$\rho\le r(\lambda_0)$ 时它什么也不说（层仍可能不可行，例如 C.4 的 $\mu=0$ 格子）。
- $r(\lambda_0)$ 的计算需要 $\lambda_0$ 的具体值；$\min_\lambda r$ 需要特征值（代数数），
  实际用的时候通常取 $\lambda_0=0$（或已知的特征值）做**快速筛**。
- 它**不**解决 $q1$：$\rho\le r(\lambda)$ 的层仍需判 $\exists(\mathcal U,\mathcal H,\tau)$。
- 无解实例的"58/58"是**抽样**，不是定理；**每个**实例的无解性单独可证（$\rho_{ci}>r(0)$ 是有限计算）。

## 文件

| 文件 | 内容 |
|---|---|
| `README.md` | 本文件：陈述、证明、推论、限制 |
| `verify.py` | 精确算术复核（随机实例上的秩不等式 + "必失败"方向）|
| `no_solution_certificate.py` | 三个写死的**无解**实例（$\operatorname{rank}(A)=1$），逐个验 $\rho_{ci}>r(0)$ |
| `../../tools/ledger/c201_barrier_audit.py` | 对账本 30 个实例做屏障审计（无一被否定；$\rho_{ci}\le\rho_{\rm wit}\le\min r$ 全过）|
