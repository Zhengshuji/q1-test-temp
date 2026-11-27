# 路线 9：矩阵铅笔的完成问题（Kronecker 型判据）

> 状态：**提出，未做**（2026-10-28）。这是对 $q1$ 走向"假"最被看好的新路线之一。

## 目标

把 $(5b)$ 的判定归约到**矩阵铅笔的完成问题**（matrix pencil completion），
后者在文献里有**完整的多项式解**（Barañana–de Hoyos–Zaballa 等；本项目 `literature/pdf/` 里已有两篇）。

## 设想与理由

$(5b)$ 是"$\operatorname{rank}(\lambda\mathcal L-\mathcal L A)=$ 常数 $\forall\lambda$"。用 Kronecker 理论语言：

> 一个**奇异铅笔**在相似意义下分解成四类块：$L_\varepsilon$（无穷初等因子）、$L_\eta$（零块）、$J_k(\lambda)$（有限初等因子）、$L_k$（右最小指标）。
> **"秩恒为 $\rho$" $=$ 没有 $J_k$ 块、也没有 $L_\varepsilon$ 块**——即铅笔的 Kronecker 型只含零块与右最小指标。

于是 $(5b)$ 是一个**Kronecker 型条件**，而"我们只能选 $\mathcal L$ 的部分行（$L_0$ 固定）"正是**完成问题**的形状：

> 给定部分铅笔，能否补全成指定 Kronecker 型？

这类完成问题有经典定理（可解性的**型条件**：一组关于各块大小与行列数的线性不等式），因此**多项式可判**。

## 做法（计划）

1. 把 $[\mathcal L;CA;C]$（或商化后的 $Q_{\mathcal V}$）写成**部分铅笔**的标准形，明确"哪些位置是自由的"（由 $(5a)$ 与 $L_0$ 决定）；
2. 查出完成理论里"可补成"只含零块+右最小指标"的铅笔"的**型条件**；
3. 把型条件翻回 $\tau$（或 $\mathcal U$）的约束，检查它是否给出与 §21 一致的"维数比较"。

## 为什么值得做

- 它**绕开** $\forall\exists$ 投影：Kronecker 型是**离散不变量**，完成问题问的是"能否达到某个型"，是**组合-线性**问题；
- 若成功，$(k,1)$ 与 $c\ge2$ 的一般层都可能一并解决（T11 不再必要）；
- 与 §21 的"$\dim\beta(\mathcal H)=\rho-1$"判据**独立**，是交叉验证的好机会。

## 风险

- 完成理论的条件是"型的不等式"，而我们的自由位置受 $(5a)$ 约束，可能不能直接套用；
- 需要先读懂 `literature/pdf/pencils/Dodig_2008_matrix_pencils_completion.pdf` 与 `Reduction and Normal Forms of Matrix Pencils.pdf`（Verdier）两篇。

## 相关文件

- [../../../proof/rho1_layer/theorem.md](../../../proof/rho1_layer/theorem.md)（§14–§21）
- `literature/pdf/pencils/Dodig_2008_matrix_pencils_completion.pdf`、`literature/pdf/pencils/Reduction_and_Normal_Forms_of_Matrix_Pencils.pdf`
- [../mainline_logic.md](../mainline_logic.md)

## 最终结论

**尚未有结论**（提出于 2026-10-28，未开始做）。若成功，$(5b)$ 的判定将归约到"铅笔完成问题的型条件"，
预期得到多项式判定 ⟹ 支持 **$q1$ = 假**。

## 放弃原因

不适用（未放弃）。

## 残留价值

- 一个**新的判据语言**（Kronecker 型 / 完成问题），与 §21 的维数比较判据独立，可交叉验证；
- 明确了两篇必读文献的位置。

## 进展（2026-10-28 补读 Dodig 2008 之后）

1. **型条件是有限条不等式**（Theorem 4：$\tilde\gamma_i\mid\tilde\alpha_i\mid\tilde\gamma_{i+\bar r-r}$、$\bar r_{i+\bar r-r}\le r_i$、求和不等式）⟹
   "能否补成指定 Kronecker 型"是**多项式判定** ✓ —— 这正是本路线想要的形状；
2. **但我们的铅笔不自由**：恒等式
   $$Q_{\mathcal V}(\lambda)=\pi\big(\mathcal L(\lambda I-A)\big)$$
   说明我们的行空间与 $\lambda$-系数**是同一个** $\mathcal L$；Dodig 的 $B(\lambda)$ 是任意铅笔 ⟹ 他的条件对我们是**必要不充分** ✗；
3. 于是本路线的正确提法变成：**子空间补全**（$\mathcal V\supseteq L_0$ 且 $\mathcal L(\lambda I-A)$ 的 Kronecker 型被钉住）。

详见 [literature/notes/DODIG_2008_row_completion.md](../../../literature/notes/DODIG_2008_row_completion.md)。
