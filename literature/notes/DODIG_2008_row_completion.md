# Dodig 2008（矩阵铅笔完成问题）对本项目的可用性

> M. Dodig, *Matrix pencils completion problems*, Linear Algebra Appl. 428 (2008) 259–304。
> 全文抽取：`txt/dodig2008_matrix_pencils_completion.txt`。本文只记**我们能用什么、缺什么**。

## 1. 论文解决了什么

Loiseau–Mondié–Zaballa–Zagalak (LAA 1998) 提出的 **"挑战问题"**：给定铅笔 $A(\lambda)$，
**行补全**（右乘/下加 $B(\lambda)$）或**列补全**后，Kronecker 不变量能被赋成什么。
Dodig 在任意域上给出了**完整解**（Theorem 3 列补全无行最小指标情形；**Theorem 4 行补全**）。

## 2. Theorem 4（行补全）的结论形状

设 $A(\lambda)\in\mathbb F[\lambda]^{(n+p)\times n}$ 的不变量为 $\tilde\alpha_1|\cdots|\tilde\alpha_n$（齐次不变因子）
与行最小指标 $r_1\ge\cdots\ge r_r>0$，目标为 $[\begin{smallmatrix}A\\B\end{smallmatrix}]$ 的不变量
$\tilde\gamma_1|\cdots|\tilde\gamma_n$、$\bar r_1\ge\cdots$。则**行补全存在 $\iff$**

$$\text{(i) } r\le\bar r\le r+l;\quad
\text{(ii) } \tilde\gamma_i\mid\tilde\alpha_i\mid\tilde\gamma_{i+\bar r-r};\quad
\text{(iii) } \bar r_{i+\bar r-r}\le r_i;\quad
\text{(iv) 一组求和不等式};\quad \text{(v) 维数守恒}.$$

$$\boxed{\ \text{"能补成指定 Kronecker 型" = 一组}\textbf{关于不变量（次数/最小指标）的不等式}\ }$$

即：**型条件是"多面体式"的有限条不等式** ⟹ 判定是多项式 ✓（这正是路线 F12 想要的形状）。

## 3. 对我们 $(5b)$ 的对接（关键观察）

先注意一个恒等式：

$$Q_{\mathcal V}(\lambda)=\lambda\,\pi(\mathcal L)-\pi(\mathcal L A)=\pi\big(\mathcal L(\lambda I-A)\big).$$

所以我们的铅笔**不是任意的**：它是"行空间 $\mathcal V$ 乘 $(\lambda I-A)$"。于是 $(5b)$ 的说法变成

$$\operatorname{rank}\big(\mathcal L(\lambda I-A)\big)=\rho\ \forall\lambda
\iff\ \text{在商空间 }X/\mathcal J\text{ 里，}\mathcal V\text{ 的}\ (\lambda I-A)\text{-像恒为 }\rho\text{ 维}$$

即：**$\mathcal V$ 在 $\mathrm{mod}\ \mathcal J$ 意义下"无剩余特征结构"**（既无有限初等因子、也无无穷初等因子），
Kronecker 型只剩**零块 + 行最小指标**。这与 Jaffe–Karcanias 的 almost $(A,Z)$-不变子空间的铅笔刻画同一族。

## 4. 能用什么 / 缺什么

| 项 | 状态 |
|---|---|
| **型条件是有限条不等式**（Theorem 4）| ✓ 可直接借：它把"能否补成指定型"化成多项式判定 |
| 我们的铅笔有**额外结构** $Q=\pi(\mathcal L(\lambda I-A))$ | ✗ **Dodig 的 $B(\lambda)$ 是任意铅笔**，我们的自由部分是**子空间 $\mathcal V$**，不是任意行 |
| 因此 Dodig 的条件对我们 | **必要但不充分** ✗ |

$$\Longrightarrow\ \text{F12 的正确提法：把"行补全"换成"子空间补全"（}\mathcal V\supseteq L_0\text{ 且 }(\lambda I-A)\text{-型被钉住）。}$$

## 5. 由此得到的具体待做（比之前更清楚）

1. 把 $(\lambda I-A)$ 在 $X/\mathcal J$ 上的**限制/诱导**写成标准铅笔，用 Theorem 4 的 (i)–(v) 作为**必要条件**，
   检查它们是否已经把允许的 $\rho$ 钉死（若钉死 ⟹ 层判定立刻多项式）；
2. 若必要条件不够，剩下的缺口恰是"子空间结构"——这与 §21 的 $\dim\beta(\mathcal H)=\rho-1$ 判据可能是同一件事的两种说法。

## 6. 相关

- [SURVEY_2026-10-28.md](SURVEY_2026-10-28.md)（第 C 线）
- [workspace/q1_false/attempts/09_pencil_completion.md](../../workspace/q1_false/attempts/09_pencil_completion.md)（路线 F12）
- [proof/rho1_layer/theorem.md](../../proof/rho1_layer/theorem.md) §14–§21