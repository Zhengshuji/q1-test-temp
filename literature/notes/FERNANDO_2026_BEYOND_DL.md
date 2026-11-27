# Fernando 2026《Beyond Darouach and Luenberger》—— 读后记（2026-11-02）

> 文件：`literature/papers/2609.33615.pdf`
> 文本提取：`literature/txt/A_Minimum_Order_Functional_Observer_Beyond_DL.md`（16 页，pypdf 提取）。
> **就是我们的 [P1] arXiv:2609.33615**（同一作者 Fernando，同一线）。

## 1. 它把两件事分开（与我们的记号对应）

论文把观测器存在性拆成：

* **条件 (A)**：$\operatorname{row}(LA)\subseteq\operatorname{row}\begin{pmatrix}L\\CA\\C\end{pmatrix}$
  ——**就是本项目的 $(5a)$**；
* **条件 (S)**：谱条件 —— **就是本项目的 $(5b)$**。

## 2. $(5a)$ 在本文里是**完全解决**的

| 结论 | 内容 |
|---|---|
| 最小维数 | $q_0=\sum_{j=1}^{r}\eta_j$，$\eta_j$ 是由 $(A,C,L)$ 读出的**functional observability indices**；$r\le q_0\le n-p$ |
| **Theorem 1** | **显式构造**的增广 $R$（式 (11)）满足 (A)：$\operatorname{row}(LA)\subseteq\operatorname{row}(L;CA;C)$ |
| **Theorem 2** | 该构造的增广行数是**最小**的 |
| **Theorem 3（§V）** | 给出**最小条件-(A) 增广的完备族**（up to row equivalence）：完备族 = 所有达到 $q_0$ 的增广 |
| 谱条件 | $\nu_{\min}=q_0\iff$ 完备族里**至少一个成员**满足 (S) |

**⟹ 结论**：$(5a)$ 不是硬度来源；它既有显式构造，又有完备族刻画。
（我们项目自己的 A.3 只给出 $q_0$ 的一个**较弱**下界 $\rho_{ci}=P(T,B,U_0)\le q_0$，写作时必须注明。）

## 3. 剩下的是什么

由本文：$\nu_{\min}=q_0$ 与否，取决于**完备族里是否存在满足 (S) 的成员**。
所以 $q1$ 的精确形状（与我们 docs/05 一致）是：

$$\textbf{DEC}:\quad \exists\,R\in\{\text{最小条件-(A) 增广的完备族}\}:\ R\ \text{满足}\ (S)\ ?$$

**本文没有给它的复杂度**（只给存在性、构造与例子）。

## 4. 我们这边对这一步的贡献（B.6 + B.7）

我们在 [docs/02](../../docs/02_theorems_proven.md) B.6/B.7 证明了（都**只用 $(5a)$**，不需要 $(5b)$）：

* 右最小指标全为 $0$（B.6）；
* 无穷初等因子全是 1 次、$d_\infty=h-\operatorname{rank}L$（B.7）；
* 因此（配合全局恒等式）**$(5b)$ 等价于一个离散等式**：

$$(5b)\iff d_{\rm fin}=0\iff \boxed{\sum_j\varepsilon_j=\operatorname{rank}L}$$

即"左最小指标之和 $=$ 增广矩阵的秩"。这把 $\forall\lambda$ 的谱条件换成了**Kronecker 不变量的一次等式**，
而左最小指标又 $=$ 约化 descriptor 铅笔 $[\lambda E-EX^{\mathsf T}\,B]$ 的右指标 $=$
descriptor 系统 $(-E,-EX^{\mathsf T},B)$ 的**可控性指标**（[proof/descriptor_reduction](../../proof/descriptor_reduction/README.md)，
文献对接见 [DESCRIPTOR_CONTROLLABILITY_INDICES.md](DESCRIPTOR_CONTROLLABILITY_INDICES.md)）。

**于是 DEC 的"离散化"版本**是：

> 在 Fernando 的完备增广族里，是否存在一个成员，使它的（descriptor 可控性）指标之和 $=\operatorname{rank}L$？

## 5. 与之前工作的关系（诚实标注）

1. 本项目早期的 $q_0$/$\rho_{ci}$ 讨论**弱于**本文的 $q_0=\sum\eta_j$（A.3 已注明）；
   **不要**把 A.3 当作"重新发现 q0"——它只是下界。
2. 我们 2026-11-02 的 B.6/B.7 **不是**在解 $(5a)$：它们以 $(5a)$ 为**假设**，
   描述"给定 $L$ 时铅笔的 Kronecker 数据"。价值在于把 $(5b)$ 变成离散等式（见 §4）。
3. 本文的完备族（Theorem 3）是我们**还没用起来**的关键结构：后续应直接在族上做 DEC，
   而不是继续按图卡 $\Theta$ 枚举。

## 6. 待核

* 本文式 (11)–(12) 的构造细节与 Theorem 3 的"完备族"参数化（我目前只读了摘要、§I、
  Theorem 1 的陈述与证明开头、§V 的标题与 Theorem 3 的陈述位置，**未逐行核对**公式）；
* 本文与 [P2] arXiv:2609.37992 的关系（两篇同作者；P2 给了图卡 $Z_I(\Theta)$ 的版本）。
