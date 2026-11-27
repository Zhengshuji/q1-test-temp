# 557 非平凡 $(5a)$ 例子：可行集为空，判据一致

> 2026-11-27。按 556 的下一步，构造一个 $(5a)$ 非平凡（$\ker H\ne0$）的实例，验证 555 判据。
> **结果：$(5a)$ 非空、但 $(5b)$ 对所有 $R$ 失败——不可行；判据“$(5a)$ 被跳变簇吞掉”成立。**
> 状态：**[已证-纸面]** + **[Lean]**。

## 构造

$n=5$、$k=3$、$q=3$（$r_0=2$ 固定行 + 1 自由行）、$N=I_3$。
$L_0=[e_1;e_2]$、$R=r=(r_1,r_2,r_3)$；$A$ 的 $K_0$ 列为 $Ae_1=e_1$、$Ae_2=e_2$、$Ae_3=e_1$
（其余列只需满足 $CA=e_4$ 的约束）。

压缩数据：
$$H=\begin{bmatrix}1&0&0\\0&1&0\\r_1&r_2&r_3\end{bmatrix},\qquad
H_A=\begin{bmatrix}1&0&1\\0&1&0\\r_1&r_2&r_1\end{bmatrix}.$$

## $(5a)$ 非空

$r_3=0$ 时 $\operatorname{rank}H=2$，$\ker H=\operatorname{span}\{e_3\}$；而
$H_Ae_3=(1,0,r_1)^{\mathsf T}$——只有 $r_1=0$ 时才为零。
所以 $(5a)$ 的解集包含 $\{r_3=0,\ r_1=0,\ r_2\ne0\}$，以及 $r_3\ne0$ 的平凡情形（$\ker H=0$）。

## $(5b)$ 恒失败

$P(\lambda)=\lambda H-H_A$ 的行列式（Lean 核验）：
$$\det P(\lambda)=\lambda(\lambda-1)^2r_3 .$$
- $r_3\ne0$：$\omega=3$，$\det P$ 在 $\lambda=0,1$ 为零 ⇒ 秩掉 ⇒ $(5b)$ 失败；
- $r_3=0$：$\omega=2$，$\lambda=1$ 时前两行给秩 1 ⇒ $(5b)$ 失败。

所以该实例**可行集为空**。

## 与 555 判据的一致性

$(5a)$ 的 $R$-解集（$r_3=0,r_1=0$ 那条线）落在 $\{\det P=0\ \text{对所有}\ \lambda\}$ 的跳变簇里
（$r_3=0$ 时 $\det\equiv0$，所有极大子式都退化）；因此判据正确预测“不可行”。

## Lean 核验

[557_lean_nontrivial_example.lean](557_lean_nontrivial_example.lean)（`namespace Q1Gadget557`，退出码 0）：

| 声明 | 内容 |
|---|---|
| `det_P` | $\det P(\lambda)=\lambda(\lambda-1)^2r_3$ |
| `det_at_zero` | $\lambda=0$ 时 $\det=0$ |

## 下一步

构造一个**可行**的非平凡例子（$(5a)$ 非平凡、$(5b)$ 在某 $R$ 上成立），
验证判据的另一个方向；这需要 $H_A$ 在 $\ker H$ 上为零且 pencil 在其余方向保持秩。

## 状态

- 例子：**[已证-纸面]**；
- Lean：**[Lean]**（2 条声明）；
- 可行非平凡例子：**[未找到]**。
