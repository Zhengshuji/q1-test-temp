# 两篇 Fernando 2026 与项目的逐项对照 —— 项目"想证明的"被覆盖了多少？

> 2026-10-30，接手者。对象：
> - **[P1]** arXiv:2609.33615，*A Minimum-Order Functional Observer Beyond the Darouach and Luenberger Constructions*（2026-09-27）
> - **[P2]** arXiv:2609.37992，*Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger*
> 本地全文：`literature/papers/2609.33615.txt`、`2609.37992.txt`。

## 1. 两篇论文到底证了什么

| 结论 | 出处 | 等级（论文自己） |
|---|---|---|
| $(A)/(S)$ 两条条件（与本项目 $(5a)/(5b)$ 逐项相同） | P1 §II、P2 §II | 定义 |
| $q_0=\sum_{j=1}^{r}\eta_j$ 是条件 $(A)$ 下的**最小维数**（$\eta_j$ = functional observability indices）| P1 §III、P2 §III–IV | 定理 |
| **条件 $(A)$ 在 $[q_0,\,n_0-p]$ 上无间隙**（每阶都可满足 $(A)$）| P2 Thm 2 | 定理（"no gaps"）|
| 最小 $(A)$-增广的**完整族** $\mathcal L=\binom{L}{X_J(\Theta)M_C+KC}$ | P1 Thm 3 + (22) | 定理 |
| **固定阶 $q$**：存在阶-$q$ 观测器 $\iff\exists Z$（$\operatorname{im}Z$ 是 $\ker[C;L]$ 的 $(n-p-q)$ 维子空间）满足 (8a)(8b)(8c) | P2 Thm 5 | 定理（充要）|
| 上述 $Z$ 用 Grassmann 图卡 $Z_I(\Theta)=K_LW_I(\Theta)$ 参数化，$\iff\exists$ 图卡与 $\Theta$ | P2 Thm 6 | 定理（充要）|
| 阶谱：$\Sigma_{FO}=\{q_0,\dots,n_0-p\}$ 中满足 $(S)$ 的那些阶；$\nu_{\min}=\min\Sigma_{FO}$ | P2 Thm 9 + (16) | 定理（**完备性声明**）|
| 端点的退化：$q_0=r$ 回收 Darouach；$n_0-p$ 回收 Luenberger | P1、P2 | 定理 |
| 具体例子：$n=8$，$q_0=4$、$\nu_{\min}=4$（P1）；$n=8$，$q_0=3$、$\nu_{\min}=5$（P2）| P1 §VII、P2 §VII | 精确求值 |

**关键：两篇都不给复杂度。** 全文检索 `complexity` / `polynomial time` / `NP` / `algorithm`（除 §Remark 的 "testing" 与 Algorithm 1 的自然语言流程）**没有复杂度类结论**；
$\exists\Theta$（图卡 × 连续参数）仍是**半代数可行性**，论文只在例子里（1 参数族、4 个图卡）做**精确求值**。

## 2. 和项目"s 的对应表

| 项目 | 论文 | 判断 |
|---|---|---|
| 层 $(\rho,c)$：$\rho=\dim\pi\mathcal V$、$c=\dim(\mathcal V\cap\mathcal J)$ | 阶 $q=\operatorname{rank}\mathcal L$（不分 $\rho,c$）| 两套坐标；他们的 $q$ 更粗 |
| $\exists(\mathcal U,\mathcal H)$（Grassmannian + 提升）| $\exists Z$（$\operatorname{im}Z$ 是 Grassmannian $\mathrm{Gr}(d,m_L)$ 的点）| **同一个量词**（P2 Thm 5/6）|
| 格判据 C.1–C.5（固定 $(\mathcal U,\mathcal H)$）| 固定 $(q,\text{图卡},\Theta)$ 时的 $(S)$ 检验 | 论文更一般（任意 $q$、任意格），项目的 C.1–C.5 只是 $(3,1)$ 的特例 |
| $\rho_{ci}=P(T,B,U_0)$（$O(n^4)$，"算术侧"）| $q_0=\sum\eta_j$（多项式）| **项目的更弱**：$q_0\ge\rho_{ci}+c$，且 $q_0$ 也是多项式 |
| "层程序"（逐层判可达）| 阶谱 $\Sigma_{FO}$ + 逐阶充要 + $\nu_{\min}=\min\Sigma_{FO}$ | **已被覆盖**（P2 Thm 9）|
| 秩屏障 $\rho\le\min_\lambda r(\lambda)$ | 未见 | **可能独有**（但要查是否已在别处）|
| $\exists\mathbb R$-hard / NP-hard 的框架 | 无 | **项目独有**（唯一还开放的）|
| T11（$\tau$ 量词消除）、Bézout 化 | 与 P2 Thm 6 的 gcd 检验同型 | 被覆盖（方法同） |

## 3. 结论：项目"想证明的"被覆盖到什么程度

$$\boxed{\ \text{“刻画 $q_{\min}$、给出逐阶充要条件、构造”}\ \textbf{已由 P1+P2 完成}\ ;\qquad \text{“复杂度”}\ \textbf{没人做}\ }$$

具体说：

1. **"证明 $q_{\min}$ 可以刻画/计算"** —— 已被 P2 Thm 5/6/9 完成（在每个阶上给充要条件 + 构造；最小阶 = 最小谱可行阶）。
   如果项目的目标只是"把 $q_{\min}$ 化成可检验的代数条件"，那**目标已达成**（而且比项目做得更全：任意阶、任意格）。
2. **"证明 $q_{\min}$ 有多项式算法（即 $q1$ = 假）"** —— **没有**被完成：$\exists\Theta$ 仍是半代数可行性，
   论文只在例子里做精确求值；没有多项式算法，也没有说它不可判。
3. **"证明 $q1$ = 真（NP-hard / $\exists\mathbb R$-hard）"** —— 也没人做。

所以项目**唯一还站得住的靶子**是：**$(S)$-over-charts 的判定复杂度**（= 项目的 $\exists(\mathcal U,\mathcal H)$）。
其余部分（层程序、格判据、$\rho_{ci}$、$\tau$ 消除）都应当**降级为"重新发现"**，并改为引用 P1/P2。

## 4. 项目还剩什么

| 项 | 状态 |
|---|---|
| 秩屏障 $\rho\le\min_\lambda r(\lambda)$（层的过滤器；$q_0$ 的补充）| **可能独有**，值得查文献后写成一页 |
| $q_0$ 下界接进项目（新 A.4）| 已做 ✓（但 $q_0$ 本身是 P1 的结果）|
| $(3,1)$ 格判据 C.1–C.5 | 被 P2 Thm 5 覆盖（作为特例）；可作为**教材式推导**保留，但不能当新结果 |
| $d=4$ 谱步（可行 $\varphi$ 至多 2 个）| 未见同样陈述；类似"图卡上 1 参数族"的精确求值在 P2 例子里做过 ⟹ **可能只是特例**，需查 |
| $\exists\mathbb R$-hard 框架、$\mathbb F_p$ 筛、撤回纪律 | 工程性/方法论，不算学术贡献 |

## 5. 建议（对项目）

1. **把 STATUS/README 的"贡献"改成两句**：
   (i) 复现/对接 P1–P2 的刻画（引用）；
   (ii) **唯一新问题**：$\exists\Theta$（图卡 × 半代数）的**判定复杂度** —— 多项式 or $\exists\mathbb R$-hard。
2. 停止在"层程序/格判据"上继续投入（已被覆盖）；把精力放到 (ii)。
3. 若走 (ii)：一个自然的切入点是把 P2 的 Thm 6 的 $\exists\Theta$ 当作**半代数可行性**问题，
   证明它 $\exists\mathbb R$-hard（归约源：ETR / 二次方程组可行性），或给出**多项式**判定（若 $\Theta$ 只以低次出现，可能有）。

## 6. 复现

```bash
python proof/layer_program/c206_paper_example.py   # P1 的 n=8 例子：全部断言复现 ✓
python proof/layer_program/c207_q0_eta.py          # P1 的 (η1,η2)=(3,1)、q0=4 ✓
python tools/ledger/c208_q0_lower_bound.py         # q0 作为下界：6/20 实例比 A.3 紧
```
