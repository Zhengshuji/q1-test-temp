> **已撤回（467）**：Galois 分组本身没问题，但它只解决「分支如何 $\mathbb Q$-定义」，
> **不解决有理点存在性**。见 [467](467_two_more_retractions.md)。

# 465 命题 A 的最后一块：用 $\mathbb Q$-不可约分支（而不是 $\mathbb C$-分支）

> 承接 464（命题 A 在 $\mathbb Q$-仿射情形成立）。专家提到的细节——"不可约分支是否 $\mathbb Q$-定义"——本轮解决。

## 目标

把命题 A 里的"不可约"落实成**可枚举、$\mathbb Q$-定义**的对象。

## 设想与理由

$X$ 由 $\mathbb Q$-系数多项式定义。它在 $\bar{\mathbb Q}$ 上分解成有限个不可约分支，
Galois 群 $\operatorname{Gal}(\bar{\mathbb Q}/\mathbb Q)$ 置换这些分支。

于是**按轨道分组**得到 $X$ 的 **$\mathbb Q$-不可约分支**：每个是若干 $\mathbb C$-分支的并，且**$\mathbb Q$-定义** ✓。

**关键观察**：命题 A 的论证只需要"**两个非零多项式之积非零**"——
而这对**$\mathbb Q$-不可约**的分支就够（不需要它在 $\mathbb C$ 上不可约）✓。

**另一个关键观察（对复杂度有利）**：$\mathbb Q$-分支是 $\mathbb C$-分支的**并** ⟹
$$\#\{\mathbb Q\text{-分支}\}\ \le\ \#\{\mathbb C\text{-分支}\}$$
——所以 463 的 XP 估计**不会因为这一步变大** ✓。

## 做法

按 Galois 轨道把 C-分支分组得 Q-分支，再套 464 的论证。

## 进展

> **命题 A（$\mathbb Q$-分支版）.** 设 $X\subseteq\mathbb A^d$ 非空、$\mathbb Q$-局部闭，
> $X=\bigcup_j X_j$ 为其 $\mathbb Q$-不可约分支。则
> $$\exists x\in X(\mathbb Q):\ \operatorname{rank}F_1(x)\ge r_1\wedge\operatorname{rank}F_2(x)\ge r_2
> \iff\exists j:\ \operatorname{rank}_{\mathbb Q(X_j)}F_1\ge r_1\wedge\operatorname{rank}_{\mathbb Q(X_j)}F_2\ge r_2 .$$

*证明.* 与 464 相同，只是把"不可约"换成"$\mathbb Q$-不可约"：开集 $O_i=\{g_i\ne0\}\cap X_j$ 非空 ⟹
$g_1g_2$ 在 $X_j$ 上不恒零 ⟹ 存在 $\mathbb Q$-点使 $g_1g_2\ne0$ ✓。$\square$

## 最终结论

1. **不需要 $\mathbb C$-不可约分支**：$\mathbb Q$-不可约分支就够（论证只用到"非零多项式之积非零"）；
2. **$\mathbb Q$-分支是 $\mathbb Q$-定义的**（Galois 轨道）⟹ 可枚举 ✓；
3. **分支数不超过 $\mathbb C$-分支数** ⟹ 复杂度估计不变（仍是 XP，$n^{O(\ell)}$）✓；
4. 于是命题 A **完整**：判定 = 枚举（卡 × 秩层 × $\mathbb Q$-分支），每处一次函数域秩计算。

## 放弃原因

- 没有给"如何枚举 $\mathbb Q$-分支"的算法（需要 $\mathbb Q$ 上的分解/子式 $\gcd$ 工具，未实现）；
- 没有估"分支数的实际大小"（只给了与 $\mathbb C$-分支的对比）；
- 没有验证端到端（从分层到判定）的实例。

## 残留价值

- **命题 A 收尾**：所需对象（$\mathbb Q$-不可约分支）与所需性质（$\mathbb Q$-定义、可枚举、数目有界）都落实了；
- 复杂度估计**不受影响**（$\mathbb Q$-分支不多于 $\mathbb C$-分支）；
- 明确了实现层面还缺**分支枚举**这个工具步骤。

## 下一步

实现 $\mathbb Q$-分支枚举（对 $k=3$、$\omega=2$ 的小实例先做），把命题 A 端到端跑通一次；
再估分支数对 $\ell$ 的增长。

## 相关文件

- [464](464_proposition_A.md)（命题 A）
- [463](../../decision_algorithms/attempts/463_expert108_audit.md)（专家建议）

## 状态

- 命题 A（$\mathbb Q$-分支版）：**[已证-纸面]**。
- 分支枚举算法：**[未做]**。
- 端到端验证：**[未做]**。
