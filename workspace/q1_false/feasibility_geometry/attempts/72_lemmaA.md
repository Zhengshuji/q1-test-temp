# Lemma A 的第一轮证明尝试：两副本的阶差可加**已证**（走单-λ 证书），且阶差无界

## 目标

专家 2026-11-04 §Q4 把阶差可加性拆成 Lemma A（下界）与 Lemma B（上界），并指出 Lemma A 难在
"混合增广"。本轮尝试证明 Lemma A（先两副本）。

## 设想与理由

先看混合增广到底长什么样：在直和上，$V=V_1\oplus V_1$、$K=K_1\oplus K_1$，而 $\mathcal Z$（$d=1$）
按"落在哪一块"分类：**块内**（$\mathcal Z\subseteq K_1\oplus 0$ 或 $0\oplus K_1$）与**横截**
（$\mathcal Z=\langle(z_1,z_2)\rangle$，$z_1,z_2\ne0$）。在 $q=7$ 的 20 个样本里横截占 16、块内只有 4——
**横截才是主要情形**，所以"逐块用单副本定理"不够。

关键观察：单副本满足**单-$\lambda$ 证书** $(\lambda_0I-A_1)V_1=K_1$（本实例 $\lambda_0=-2$）。于是直和上
$$(\lambda_0I-A)(V_1\oplus V_1)=K_1\oplus K_1=K$$
（同一个 $\lambda_0$！因为副本相同）。故 B.13e 直接适用于**整个直和**，横截 $\mathcal Z$ 也不例外
（取 $x=((\lambda_0I-A_1)^{-1}z_1,(\lambda_0I-A_1)^{-1}z_2)$，则 $(\lambda_0I-A)x=(z_1,z_2)\in\mathcal Z$，
且 $x\notin\mathcal Z$ 因 $V_1\cap K_1=0$）。

## 做法

1. 数值核验直和（$k=1,2,3$）的证书 $\exists\lambda:(\lambda I-A)V=K$ 与 $V\cap K=0$；
2. 核验块对角见证（$k=1,2,3$）满足 $(5a)$ 与 $(5b)$（后者用 B.12 可观性检验，等价于 $(5b)$）；
3. 写成命题 B.15。

## 进展

| 副本数 $k$ | $\exists\lambda:(\lambda I-A)V=K$ | $\operatorname{rank}[C;CA;L_0]$ | $q_{\min}$ 见证（$q=k\cdot4$）| 见证核验 |
|---|---|---|---|---|
| 1 | $\lambda=-2$ | 6 $=n$（$V\cap K=0$）| $q=4$ | $(5a)$ ✓、B.12 ✓ |
| 2 | $\lambda=-2$ | 12 $=n$ | $q=8$ | $(5a)$ ✓、B.12 ✓、$\operatorname{rank}Q(\lambda)=h$ 取样全等 |
| 3 | $\lambda=-2$ | 18 $=n$ | $q=12$ | $\operatorname{rank}[C;\mathcal L]=18$、$(5a)$ ✓、B.12 ✓ |

并已在两副本上核验：$q=4,5,6,7$ 的 **1820 个候选无可行点**（上一轮 attempts/71）。

## 最终结论

**B.15（已证）**：若单副本满足 $V_1\cap K_1=0$ 且 $\exists\lambda_0:(\lambda_0I-A_1)V_1=K_1$，则 $k$ 重直和满足
同样的证书（**同一个** $\lambda_0$）⟹ 所有 $d\ge1$ 的阶整族不可行；而 $q=kq_1$（$d=0$）处块对角增广可行。于是
$$q_{\min}\big(\text{copy}^{\oplus k}\big)=k\,q_{\min}(\text{copy}),\qquad \text{阶差}=k\cdot(\text{单副本阶差}).$$
*证明*：分块对角 ⟹ $V,K$ 直和、证书按块相加、$(5a)/(5b)$ 的秩按块相加；例外集由 $V\cap K=0$ 消失（B.13e）。

$$\boxed{\text{阶差可以任意大（}k\text{ 个 gap-2 副本给阶差 }2k\text{）}}$$

## 放弃原因

不适用（Lemma A 在两副本、且更一般地在"同型副本直和"这一族上**已证**；一般非同型块的下界仍未处理，
但本命题已足以给出"阶差无界"）。

## 残留价值

* **Lemma A 在一大类上成立且是定理**（同型副本直和），不需要"排除混合增广"——混合增广被单-$\lambda$ 证书
  **直接覆盖**（这正是上一轮"横截 $\mathcal Z$ 占多数"的那个担心被绕开的方式）；
* **阶差无界**（B.15）：$q_{\min}$ 与代数最小阶之差可随规模线性增长；
* 与专家预判对照：他担心"混合增广可能越过障碍"；在同型副本的直和上，混合增广**不能**越过，
  原因是各块共享同一个 $\lambda_0$。

## 相关文件

- `docs/02` B.15（陈述与证明）、B.13e（单-$\lambda$ 证书）、B.14（可解类）
- `tools/verification/two_copy_gap.py`（两副本实验）
- `attempts/71_two_copy.md`（前一轮的采样证据）
