# 覆盖判据（行/列约定显式）

> 专家 QA8 第 2 项：把判据按**明确的行/列约定**重写并证明基无关。
> 本文件是判据的**权威表述**；`theorem.md` 的 C.2/C.3 是它的坐标版特例。

---

## 1. 约定（先说清楚）

- $\mathcal U$ 是 3 维空间，$\rho=\dim\mathcal U=3$。
- $T$ 是 $\mathcal U$ 上的**线性算子**。取 $\mathcal U$ 的一组基后，$T$ 用矩阵表示，按**列向量**作用：
  $x\mapsto Tx$。
- $w$ 是**行**（covector，即 $\mathcal U^*$ 的元素），按 $x\mapsto wx=\sum_i w_ix_i$ 作用。
- 铅笔是**竖着**增广的
  $$P(\lambda)=\begin{bmatrix}\lambda I-T\\ w\end{bmatrix}\qquad(\rho+1\ \text{行},\ \rho\ \text{列}).$$

## 2. 判据 [已证]

> **定理 2.1**：格子被覆盖 **当且仅当**
> $$\exists\lambda\in\mathbb C:\ \operatorname{rank}P(\lambda)<\rho .$$
> 等价地：$\exists\lambda:\ w\in\operatorname{row}(\lambda I-T)$；
> 再等价地：$\exists\lambda$ 与 $\exists v\ne0$ 使 $Tv=\lambda v$ 且 $wv=0$。

*证明*：$\operatorname{rank}P(\lambda)<\rho$ ⟺ $\rho+1$ 个行在 $\rho$ 维列空间里线性相关 ✓ ⟺ 第 $\rho+1$ 行
（即 $w$）落在前 $\rho$ 行（即 $\lambda I-T$ 的行）的张成里 ✓ ⟺ $w\in\operatorname{row}(\lambda I-T)$ ✓。
而 $\operatorname{row}(\lambda I-T)=\{y^{\mathsf T}(\lambda I-T)\}$ ✓ ⟹ $w\in$ 它 ⟺ $w$ 杀死 $\ker(\lambda I-T)$ ✓
⟺ 存在 $0\ne v\in\ker(\lambda I-T)$ 使 $wv=0$ ✓ ✓。$\square$

**特例（简单特征值）**：若 $\lambda$ 是简单特征值 ✓，$\ker(\lambda I-T)=\langle v\rangle$ ✓，
则条件就是 $wv=0$ ✓ —— 这正是 C.2/C.3 的写法 ✓。

## 3. 基无关性 [已证 + 精确验证 30/30]

> **命题 3.1**：换基 $P$（列按 $P$、行按 $P^{-1}$）后，$T'=PTP^{-1}$、$w'=wP^{-1}$，判据结果**不变**。

*证明*：$\lambda I-T'=P(\lambda I-T)P^{-1}$ ✓ ⟹ $\operatorname{row}(\lambda I-T')=\operatorname{row}(\lambda I-T)P^{-1}$ ✓；
于是 $w'\in\operatorname{row}(\lambda I-T')$ ⟺ $wP^{-1}\in\operatorname{row}(\lambda I-T)P^{-1}$ ⟺ $w\in\operatorname{row}(\lambda I-T)$ ✓。$\square$

**验证**：`proof/layer_program/verify_criterion_convention.py` —— 30/30 一致 ✓；
对照：若把行按 $P$ 变换（错误 ✗），只有 26/30 ✗（RCP §79）。

## 4. 一个用得上的充分条件 [已证]

> **命题 4.1**：若 $\operatorname{rank}T\le\rho-1$ 且 $w\in\operatorname{row}(T)$，则格子被覆盖（在 $\lambda=0$ 处）。

*证明*：$w\in\operatorname{row}(T)=\operatorname{row}(0\cdot I-T)$ ✓ ⟹ 定理 2.1（$\lambda=0$）✓。$\square$

**这是"整族都坏"的结构入口** ✓：若 $\operatorname{rank}T\le\rho-1$ 与 $w\in\operatorname{row}(T)$ 对**每个**允许的
$(\mathcal U,\tau)$ 都成立，则整族被覆盖 ✓ —— RCP §82 的证书正是这个形状 ✓（那里更强：全部子式恒为零 ✓）。

## 5. 我此前写错的地方（记录 ✗）

| 位置 | 错误 | 正确 |
|---|---|---|
| RCP §78 | 说"$w^{\mathsf T}v$ 不是不变量、要改成像" ✗ | $w$ 是**行**，按 $wP^{-1}$ 变换 ⟹ $wv$ **不变** ✓ |
| RCP §80 命题 1 | 写 $w\in\operatorname{im}(\lambda I-T)$ ✗（像 = 列空间 ✗）| $w\in\operatorname{row}(\lambda I-T)$ ✓ |
| RCP §80 命题 2 | "$w\in\operatorname{im}f$" ✗ 类型错（$f$ 的靶是 $X/B$ ✓）| 见 RCP §80 顶部警告 ✓ |

**C.2/C.3 原本的写法是对的** ✓ —— 错的只是我的"更正" ✗。
