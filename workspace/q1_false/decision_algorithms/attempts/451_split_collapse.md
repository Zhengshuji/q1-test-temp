# 451 迁移落实：split 设计下 (R)(E) 只通过 $\Phi(W)$ 依赖 $W$

> 承接 450（从算法线借 W-消去定理）。本轮把迁移**做出来**：在算法线的 split 设计里，
> 我这条线的两个条件 (R)(E) 确实**只通过 $\Phi(W)$ 依赖 $W$**——与他们的结论一致 ✓。

## 目标

在 split 设计下写出 (R)(E) 的显式形式，验证"只通过 $\Phi$ 依赖 $W$"。

## 设想与理由

回忆 split 设计：$V=D^{\perp_{K_0}}\oplus W$（$D\le K_0$、$W\subseteq K_0^\perp$、$\dim W=t$），
行空间 $V$ 分解成两块。按 [406](../../c_stratification/attempts/406_eliminate_W.md)：

| 行 $v$ | $h^v=v^{\mathsf T}N$ | $g^v=v^{\mathsf T}AN$ |
|---|---|---|
| $v\in W$ | $0$ | $\varphi_v\in D^\circ$ |
| $v\in D^{\perp_{K_0}}$ | K-块 $h^v$ | K-块 $g^v$ |

所以可用对分成两类：**W-行给 $(0,\varphi_v)$**（第一分量为零）、**K-行给 K-块对**。

## 做法：写出两个条件

**$(E)$：** $E_\lambda(0,\varphi_v)=-\varphi_v$（**与 $\lambda$ 无关**），$E_\lambda$ 在 K-块对上是
$\lambda x-y$（与 $\lambda$ 有关）。于是
$$E_\lambda(\mathcal T_W)=\underbrace{\operatorname{span}\{\lambda x-y:\text{K-块对}\}}_{=:K_\lambda}+\Phi(W),$$
其中 $K_\lambda$ 由 K-块决定、**与 $W$ 无关**（K-块只依赖 $D$ 与 $(A,C)$）✓。故
$$\boxed{(E)\iff K_\lambda+\Phi(W)=W\quad\forall\lambda}$$
——$W$ 只通过 $\Phi(W)$ 进入 ✓。

**$(R)$：** $\pi_1(\mathcal T_W)$ 的第一分量只来自 K-块（W-行的第一分量为零），加上固定行：
$$(R)\iff\operatorname{span}\bigl(V_0\cup\pi_1(K\text{-块})\bigr)=W.$$
右边与 $W$ 无关（记为 $K_1$），所以
$$\boxed{(R)\iff K_1=W}$$
——要求 $W$ 恰好等于一个**由数据决定的固定子空间** $K_1$ ✓，这比 (E) 强得多。

## 进展（结论）

1. **$(E)$ 塌缩到 $\Phi$** ✓：$K_\lambda+\Phi(W)=W\ \forall\lambda$，$W$ 只通过 $\Phi(W)\subseteq D^\circ$（$\dim\le c$）进入；
2. **$(R)$ 更强**：它要求 $W=K_1$（数据决定的固定空间）⟹ 在 split 设计里 $W$ **完全被钉死**，
   搜索只剩"$K_1$ 是否满足"一个检验 ✓；
3. 于是 split 设计下 **$\exists W$ 的搜索消失** ⟹ 可行性判定 = 一个 $\gcd$ + 一个等式检验 ⟹ **多项式** ✓；
4. 与算法线的结论**一致**（他们的 $c=2$ 也是 $\mathbb P^1$ 穷尽）✓。

## 最终结论

1. 我这条线的 (R)(E) 在 **split 设计**下确实塌缩，而且比预期更强：$(R)$ 直接把 $W$ 钉死；
2. 所以"$\exists W$ 的障碍"在 split 设计里**不存在** ⟹ 该设计下 $q1$ 可判（多项式）；
3. 一般 $\mathcal S$ 下是否也有类似塌缩，**未定**——这正是剩下的问题；
4. 两条线的判据现在可以在 split 设计下**合并**：算法线的 $\Phi$-穷尽 + 我的 (R)(E) 都是多项式可查。

## 放弃原因

- 一般 $\mathcal S$ 的对应结论未做（只做了 split 设计）；
- 没有验证 $(R)$ 把 $W$ 钉死这个结论的实例（纯推导）；
- 固定行补一位的边界未处理。

## 残留价值

- **一次成功的迁移**：把算法线的 W-消去搬到我的 (R)(E) 框架，并且在 split 设计下更强（$W$ 被钉死）；
- 明确了"一般 $\mathcal S$ 是否塌缩"是唯一剩下的问题；
- 两条线的判据在该设计下可直接合并。

## 下一步

一般 $\mathcal S$：找"$\pi_1(\mathcal T_W)$ 与 $E_\lambda(\mathcal T_W)$ 是否只通过某个低维影子依赖 $W$"的判据。
若影子存在（如在 split 设计里是 $\Phi$），搜索塌缩 ⟹ $q1$ 可判；若不存在，那正是硬度的藏身处。

## 相关文件

- [450](450_shadow_idea.md)（启发）
- [406](../../c_stratification/attempts/406_eliminate_W.md)（算法线的 W-消去定理）
- [449](../../c_stratification/attempts/449_expert107_audit.md)（(R)(E) 命题）

## 状态

- split 设计下的塌缩：**[已证-纸面]**。
- 一般 $\mathcal S$：**[未定]**。
