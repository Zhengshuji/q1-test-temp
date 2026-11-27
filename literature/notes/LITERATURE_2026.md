# 文献更新（2026-09）：Fernando 的两篇新论文

> 2026-10-24 检索。目的：确认 q1（最小阶功能观测器的复杂度）在文献中的现状。
> 原始 PDF 与抽取文本在 [`papers/`](../papers/)。

---

## 0. 结论先行

| 问题 | 结论 |
|---|---|
| 有没有新的复杂度结果？ | **没有**。两篇全文 `complexity` 0 次、`NP-hard` 0 次；`polynomial` 只用于"子式 gcd 是多项式"这类表述 |
| 有没有给出完整刻画？ | **有**。order spectrum $\Sigma_{FO}(L)\subseteq[q_0,\ n_0-p]$ 被完整刻画（Theorem 9） |
| 有没有给出算法？ | Algorithm 1 只写"逐个 chart 测试 (14a)–(14b)"，**没有说明如何搜 $\Theta$** |
| q1 现状 | **仍开放**。文献 = 完整刻画 + 指数级 chart 枚举 + 未指定的非线性可行性搜索 |

$$\boxed{\ \text{q1 的现代形式：}\ \exists\ \text{chart }I\ \text{与}\ \Theta\ \text{满足 (14a)–(14b) 的复杂度}\ }$$

---

## 1. 两篇论文

| arXiv | 标题 | 提交 |
|---|---|---|
| [2609.33615](https://arxiv.org/abs/2609.33615) | A Minimum-Order Functional Observer Beyond the Darouach and Luenberger Constructions | 2026-09-27 |
| [2609.37992](https://arxiv.org/abs/2609.37992) | Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger | 2026-09-29 |

作者均为 **T. Fernando**（2010 IEEE TAC 那篇的作者）。

---

## 2. 37992 的核心结构

### 2.1 两个端点

$$q_0=\sum_{j=1}^{r}\eta_j\quad(\text{功能可观测性指标之和，代数下界}),\qquad
\text{上端}=n_0-p\quad(n_0=\operatorname{rank}\mathcal O_C).$$

### 2.2 固定阶判据（Theorem 5）

阶 $q$ 的观测器存在 $\iff$ 存在列满秩 $Z\in\mathbb R^{n\times d}$（$d=n-p-q$）使

$$CZ=0,\quad LZ=0,\tag{8a}$$

$$\operatorname{rank}\big[Z\ \ AZ\ \ R_Z\,Z\big]=d,\qquad \operatorname{im}R_Z=\ker(CAZ),\tag{8b}$$

$$\operatorname{rank}\big[(\lambda I-A)V\ \ Z\big]=\operatorname{rank}\big[V\ \ Z\big],\quad \lambda\in\Omega_S,\tag{8c}$$

其中 $V$ 是 $\ker[C;CA]$ 的基。（与项目的 $(5a)/(5b)$ 同一件事，只是坐标不同。）

### 2.3 Chart 参数化（Theorem 6）

$$Z=K_L\,W_I(\Theta),\qquad W_I(\Theta)=P_I^{\mathsf T}\begin{pmatrix}I_d\\ \Theta\end{pmatrix},\quad
\Theta\in\mathbb R^{(m_L-d)\times d}.$$

$I$ 取遍 $\{1,\dots,m_L\}$ 的 $d$-子集 —— 这正是 Grassmann 流形 $\mathrm{Gr}(d,m_L)$ 的**标准坐标卡**。

$$\boxed{\ \text{共}\ \binom{m_L}{d}\ \text{张 chart —— 指数级}\ }$$

### 2.4 全阶刻画（Theorem 9）与算法

$$\Sigma_{FO}(L)=\{q_k:\ \mathcal Z^{AS}_{d_k}(L)\neq\varnothing\},\qquad
\nu_{\min}=q_0+\min\{k:\ \mathcal Z^{AS}_{d_k}(L)\neq\varnothing\}.$$

Algorithm 1 的第 11–12 行：参数化 $Z=K_LW_I(\Theta)$，然后 **"Test (14a)–(14b)"**。
**没有给出搜 $\Theta$ 的方法**，也没有 chart 数目的任何约化。

---

## 3. 与项目的关系（重要）

1. **等价性确认**：他们的 $(A)/(S)$ 就是项目的 $(5a)/(5b)$；$q_0=\sum\eta_j$ 就是项目记录的"代数下界"。
2. **"2010 example" 的来源**：37992 的 illustrative example 就是项目里的 `2010 example`
   （$n=8$、同一个 $A,C,L_0$，答案 $\nu_{\min}=5$）—— 说明项目一直在跟这条线的最新版本对话。
3. **分层 vs order spectrum**：项目按 $\rho=\operatorname{rank}(\mathcal LN)$ 分层；他们按阶 $q$ 枚举。
   两者不同，但都指向"可行阶/层的集合"这一结构。
4. **q1 没有被回答**：文献给的是"完整刻画 + 指数枚举"，不是算法。

---

## 4. 对 Q1-TRUE 的意义：硬度只能在这两个地方

$$\text{复杂性} = \underbrace{\binom{m_L}{d}\ \text{张 chart 的枚举}}_{\text{(i) 组合}}\ +\ \underbrace{\text{每张 chart 的}\ \exists\Theta\ \text{可行性}}_{\text{(ii) 非线性}}$$

- **(ii) 每张 chart**：$(14a)$ 是闭条件（秩 $=d$），$(14b)$ 是开条件（gcd $\neq0$）。
  可行集 = 闭 ∩ 开。若"$\exists\Theta$"可以多项式判定（例如取一般位置 $\Theta$ 再验一个闭条件），
  那么全部复杂度就落在 (i) 的 chart 枚举上 —— 这与"集合覆盖"式硬度最接近。
- **(i) chart 枚举**：$\binom{m_L}{d}$ 是 Grassmannian 的坐标卡数。一般位置论证可能把它消掉
  （若每张 chart 的可行性只依赖 $I$ 的"线性代数类型"，则可用拟阵/交比技巧合并）。

$$\boxed{\ \textbf{q1 的两个方向现在有了同一个干净靶子：}\ \exists I,\Theta\ \text{的可行性}\ }$$

---

## 5. 引用与存档

- PDF：`papers/2609.37992.pdf`、`papers/2609.33615.pdf`
- 抽取文本：`papers/2609.37992.txt`、`papers/2609.33615.txt`
- 关键词计数（用于本页结论）：
  - 2609.37992：`complexity` 0、`NP-hard` 0、`polynomial` 1（"finite polynomial test"）、`algorithm` 3
  - 2609.33615：`complexity` 0、`NP-hard` 0、`polynomial` 2（均指 gcd/多项式矩阵）、`algorithm` 0

> ⚠️ 本页只依据两篇论文的公开文本；若作者后续版本加入复杂度讨论，需要重查。
