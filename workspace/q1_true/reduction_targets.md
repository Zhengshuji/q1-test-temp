# 归约目标与编码方案（Q1-TRUE）

## 0. 要归约到的决策问题

$$\textbf{MIN-ROWS}(A,C,L_0,k):\quad \exists\,\mathcal L=[L_0;R],\ \operatorname{rank}\mathcal L\le k,\ (5a)\wedge(5b)\ ?$$

等价于

$$\exists\ \mathcal V\supseteq\operatorname{row}(L_0),\ \dim\mathcal V\le k,\ \mathcal VA\subseteq\mathcal V+\mathcal J,\ \text{铅笔无零点}.$$

---

## 1. 设计原则（先写死，避免白做）

1. **$(5b)$ 必须由构造自动成立**：选一个族，使铅笔显然无零点（如三角/块三角结构、
   或让 $\mathcal L$ 的行从"显然满足"的子空间里取）。不要把硬度压在开条件上（见 README §2.1）。
2. **硬度落在 $(5a)$ + 秩约束**：即 ci 格结构与 $\rho=\operatorname{rank}(\mathcal VN)$。
3. **$q_{\min}$ 必须精确读出最优值**：不能只读出"是/否"，否则归约不成立。
4. **两个方向都要证**：编码 + 解码（$\text{OPT}(\Pi)=k\iff\text{MIN-ROWS}(...)=k$）。

---

## 2. 候选 Π

### Π1：多约束 conditioned invariant 最小化

$$\min\dim\mathcal V\quad\text{s.t.}\quad \mathcal V\supseteq K_0,\ \ \mathcal VA_i\subseteq\mathcal V+\mathcal J_i\ (i=1,\dots,m).$$

- 本问题是 $m=1$（且 $\mathcal J$ 由 $(A,C)$ 决定）；
- $m=1$ 多项式（Kleiman–Krener）；$m\ge2$ 的复杂度**待查文献**（不要假设它 NP-hard）。
- 编码难点：把 $m$ 组 $(A_i,\mathcal J_i)$ 压进一个 $n\times n$ 的 $A$ 和 $p$ 行的 $C$。
  可行思路：块对角 + 用 $C$ 的行把不同块的 $\mathcal J_i$ 拼起来；
  但 $\mathcal V$ 是**同一个**子空间，会同时与所有块耦合 —— 这正是要利用的。

### Π2：子空间格中的最小元 —— ⚠️ **前提已撤回** ✗（条件不变子空间**不**对交封闭，无最小元；见 RESTRICTED_COMPLETION_MODEL §30）

给定子空间族与包含关系约束，求最小维数元素。一般 NP-hard（待具体引用）。
与本问题的接口：ci 子空间对 $+$ 封闭构成格；若能把"格中的选择"编码成 $A$ 的块，即可。

### Π3：min-rank / 低秩完成

给定矩阵族，求最小秩解。经典 NP-hard（待具体引用）。
与本问题的接口：$\rho=\operatorname{rank}(\mathcal LN)$ 本身就是一个秩约束；
$\rho$ 越小 $q$ 越小，这个"秩—行数"耦合正是目标公式的形态。

### Π4（2026 文献版）：chart 可行性

由 [LITERATURE_2026](../../literature/notes/LITERATURE_2026.md)，问题等价于

$$\exists\ I\in\tbinom{[m_L]}{d},\ \Theta\in\mathbb R^{(m_L-d)\times d}:\quad (14a)\wedge(14b).$$

- $(14a)$：$\operatorname{rank}[Z A Z\ R_ZZ]=d$（**闭**）；
- $(14b)$：pencil 的极大子式 gcd $\neq0$（**开**）；
- $Z=K_LW_I(\Theta)$ 对 $\Theta$ **线性**，$R_Z$ 由 $\ker(CAZ)$ 给出（对 $\Theta$ 非线性）。

两个可攻的子目标见 §3.2。

### Π5（首选）：Z-FORM —— 最大化子空间维数

由 [Z_FORMULATION](../../archive/attempts_2026-10/q1_true/03_z_formulation.md)：

$$q_{\min}=n-p-d_{\max},\qquad
d_{\max}=\max\Big\{\dim Z:\ Z\subseteq\ker C,\ Z\subseteq L_0^{\perp},\
A(Z\cap K)\subseteq Z,\ \dim((\lambda I-A)K\cap Z)=\dim(K\cap Z)\ \forall\lambda\Big\}.$$

**为什么它是首选靶子**：

1. 目标是**最大化**（不是最小化），与集合函数的"规模"直接对应；
2. 可行集**不是格**（$Z_1+Z_2$ 不一定可行），所以没有免费的"最大元算法"；
3. 两个条件都可写成秩条件，便于块 gadget 设计。

**归约要造的东西**：一个 $A,K,C,L_0$ 的族，使 $d_{\max}$ 等于某个组合量（如最大独立集/最小覆盖的对偶）。

---

## 3. 编码方案

### 3.1 块对角（先做）

目标：造一个族，使

$$q_{\min}=\max(r,\ \rho^*+1)=f(\Pi),$$

其中 $f$ 是 $\Pi$ 的最优值。**先攻 $\rho^*$**：让 $A$ 的块结构使"哪些 $\rho$ 可达"编码 $\Pi$ 的组合选择。

具体地，尝试

$$A=\begin{pmatrix}A_1&&&\\&A_2&&\\&&\ddots&\\&&&A_m\end{pmatrix},\qquad
C=\begin{pmatrix}C_1&C_2&\cdots&C_m\end{pmatrix},$$

并让 $L_0$ 只"看见"一个块。此时 $K=\bigoplus K_i$，$N$ 分块，$\mathcal LN$ 的秩是各块贡献之和 ——
**$\rho$ 变成各块"激活数"之和**，这正是组合优化最喜欢的形态。

先在小 $m$（2、3）上用 [c166](../../tools/verification/c166_layer_audit.py) 做精确枚举，
确认 $q_{\min}$ 确实等于某个组合量，再推广。

### 3.2 chart 形式（2026 文献）

**目标 A（优先）：每张 chart 的 $\exists\Theta$ 是否多项式可判？**

若可以（例如 $(14a)$ 的解集是线性/仿射的，$(14b)$ 在一般位置成立），
则全部复杂度落在 $\binom{m_L}{d}$ 张 chart 的枚举上：

- 若 chart 可行性只依赖 $I$ 的**线性代数类型**（如拟阵秩），可用拟阵技巧合并 ⟹ **q1 = 假**的强候选；
- 若不能合并，就是"集合覆盖"式结构 ⟹ **q1 = 真**的强候选。

**目标 B：把 set cover 编进 chart 可行性。**

让每张 chart 对应一个子集，$(14a)$ 可满足对应"覆盖某需求"。难点：$I$ 是 Grassmannian 坐标卡的
坐标子集，不是任意组合对象；要让它编码组合结构，需要 $A,C,L_0$ 的块结构使

$$\mathrm{feasible}(I)\ \text{只依赖}\ I\cap B_1,\dots,I\cap B_m\quad(\text{块划分}).$$

**目标 C（后备）：per-chart 归约到低秩可行性。**
若能把 $(14a)$ 写成"某矩阵的秩 $\le d$"，则 $\exists\Theta$ 就是低秩可行性 —— 经典 NP-hard 形态。

---

## 4. 验收标准

| 项 | 标准 |
|---|---|
| 归约时间 | 多项式，且不依赖 $q_{\min}$ |
| 正确性 | 双向证明，写进本文 |
| 小实例 | 用精确求解器（c166 或独立实现）逐个核对 |
| 反例防护 | 至少 3 个"边界参数"（$k$ 最小/最大/中间）手工验证 |

---

## 5. 与 Q1-FALSE 的界面

- 若 Q1-FALSE 证明 $q_{\min}=\max(r,\rho^*+1)$ 且 $\rho^*$ 多项式可算 ⟹ 本方向终止。
- 若 Q1-FALSE 的 `tests/` 找到层公式反例 ⟹ 本方向把它当硬实例种子（先看它是否可块扩展）。
- 若本方向先完成归约 ⟹ Q1-FALSE 终止（问题已答）。

**当前判断**：本方向尚无任何归约；最现实的第一步是 §3 的块对角实验，用计算先找"$q_{\min}$ 像什么组合量"。
