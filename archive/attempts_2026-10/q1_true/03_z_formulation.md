# Z 形式：MIN-ROWS = 最大化一个子空间维数

## 目标
把 MIN-ROWS 写成"最大化一个子空间维数"的 $Z$ 形式，再对该形式做归约。

## 最终结论
**未完成**：$Z$ 形式的等价性只做到近似（(8c) 有缺项，已被一个实例打假），且没有找到可归约的对象。

## 相关文件
- `archive/old_scripts/q1_true_routes/c176_verify_fernando_8c.py`、`c179_verify_idea5.py`
- [../../q1_false/tests/zform/zform_check.py](../../q1_false/tests/zform/zform_check.py)


> 2026-10-24。把 Fernando 2026（[LITERATURE_2026](../../../literature/notes/LITERATURE_2026.md)）的 nullspace 判据
> 翻译成"对偶子空间 $Z$"的形式。结论：**$q_{\min}=n-p-d_{\max}$，其中 $d_{\max}$ 是一个
> 带两条线性代数约束的最大化问题**。这给 Q1-TRUE 提供了新的归约靶子。

---

## 0. 结论

$$\boxed{\ q_{\min}=n-p-d_{\max}\ }$$

$$d_{\max}=\max\Big\{\dim Z:\ Z\subseteq\ker C,\ Z\subseteq L_0^{\perp},\
A(Z\cap K)\subseteq Z,\
\dim\big((\lambda I-A)K\cap Z\big)=\dim(K\cap Z)\ \forall\lambda\Big\}$$

其中 $K=\ker[C;CA]$。

---

## 1. 推导

### 1.1 从论文的 $Z$ 开始

论文（Theorem 3/5）令 $L\in\mathbb R^{q\times n}$ 是阶 $q$ 的增广功能矩阵，
$Z\in\mathbb R^{n\times d}$ 是 $\ker\binom{C}{L}$ 的基，$d=n-p-q$。于是

$$q=n-p-d\quad(\text{关键：}q\ \text{与}\ d\ \text{互补}).$$

### 1.2 三条条件逐条翻译

**(8a)** $CZ=0,\ LZ=0$：由 $Z=\ker[C;L]$ 自动成立；
可恢复性 $\operatorname{row}(L_0)\subseteq\operatorname{row}[C;L]=Z^{\perp}$ 即 $L_0Z=0$，等价于 $Z\subseteq L_0^{\perp}$。

**(8b)** $\operatorname{rank}[Z\ \ AZR_Z]=d$，其中 $\operatorname{im}R_Z=\ker(CAZ)$。

$$\ker(CAZ)=\{\xi:\ Z\xi\in\ker(CA)\}=\{\xi:\ Z\xi\in \operatorname{im}Z\cap\ker(CA)\},$$

故 $\operatorname{im}(AZR_Z)=A(\operatorname{im}Z\cap\ker CA)$。于是

$$(8b)\iff A\big(Z\cap\ker(CA)\big)\subseteq Z\iff\boxed{\,A(Z\cap K)\subseteq Z\,}$$

（用了 $Z\subseteq\ker C$，故 $Z\cap\ker(CA)=Z\cap K$）。

**(8c)** $\operatorname{rank}[(\lambda I-A)V\ \ Z]=\operatorname{rank}[V\ \ Z]$，$V$ 是 $K$ 的基。
两边的像分别是 $(\lambda I-A)K+Z$ 与 $K+Z$。注意

$$\dim(\lambda I-A)K=\dim K-\dim(K\cap E_\lambda),\qquad E_\lambda=\ker(\lambda I-A),$$

再由 $\dim(A+B)=\dim A+\dim B-\dim(A\cap B)$ 得

$$(8c)\iff\boxed{\ \dim\big((\lambda I-A)K\cap Z\big)=\dim(K\cap Z)-\dim(K\cap E_\lambda)\quad\forall\lambda\ }$$

> **2026-10-24 勘误**：本文早期版本漏掉了 $-\dim(K\cap E_\lambda)$ 这一项。反例：`counterexample_d4` 的合法解在
> $\lambda=5,3$ 处 $\dim((\lambda I-A)K\cap Z)=1$、$\dim(K\cap Z)=2$、$\dim(K\cap E_\lambda)=1$，
> 修正后 $1=2-1$ ✓（独立复核见根目录 ATTACK_LOG 的 D5x 条目）。

---

## 2. 干净形式

$$\textbf{Z-FORM}:\quad \max\ \dim Z\quad\text{s.t.}\quad
\begin{cases}
Z\subseteq\ker C,\\[2pt]
Z\subseteq L_0^{\perp},\\[2pt]
A(Z\cap K)\subseteq Z,\\[2pt]
\dim\big((\lambda I-A)K\cap Z\big)=\dim(K\cap Z)-\dim(K\cap E_\lambda)\ \ \forall\lambda.
\end{cases}$$

$$q_{\min}=n-p-d_{\max},\qquad d_{\max}\le n-p-r .$$

**与项目原形式（最小化 $\dim V$）相比**：
- 变量从 $V\subseteq\mathbb R^n$（含 $\operatorname{row}L_0$）换成了 $Z\subseteq\ker C$（维数 $n-p$ 的固定环境）；
- **目标从"最小化"变成了"最大化"** —— 对归约更友好；
- 条件只剩两条线性代数的：一条"半不变性"、一条"交维数恒定"。

---

## 3. 数值验证（`counterexample_refute_dimV1`）

$n=5,p=2,q=1$，取证书里的解 $L$，令 $Z=\ker[C;L]$：

| 检查 | 结果 |
|---|---|
| $\dim Z$ | $2$，等于 $n-p-q=2$ ✓ |
| $CZ=0$，$L_0Z=0$ | ✓ |
| $\dim(Z\cap\ker CA)$ | $1$ |
| $\operatorname{rank}[Z\ \ AZ_{K}]$ | $2=\dim Z$ ⟹ (8b) ✓ |
| $\dim((\lambda I-A)K+Z)$，$\lambda\in\{0,\pm1,2,-3,5\}$ | 恒为 $2=\dim(K+Z)$ ✓（抽点） |

> 精确的 (8c)（所有 $\lambda$）等价于项目的 $(5b)$；c164 已用子式 gcd 精确验证过该证书。

---

## 4. 为什么这个形式对 q1 有用

### 4.1 可行集**不是格**

若 $Z_1,Z_2$ 都满足 $A(Z_i\cap K)\subseteq Z_i$，$Z_1+Z_2$ **不一定**满足：
$(Z_1+Z_2)\cap K$ 可能严格大于 $(Z_1\cap K)+(Z_2\cap K)$，而多出来的向量 $z=z_1+z_2$
并不满足 $z_i\in K$，无法用 $Az_i\in Z_i$ 拼出 $Az\in Z_1+Z_2$。

$$\boxed{\ \text{可行集对}\ +\ \text{不封闭} \Longrightarrow \text{没有唯一的"最大元"} \Longrightarrow \text{最大化可能真难}\ }$$

**已验证的反例**（$n=4$，精确算术）：

$$K=\operatorname{span}\{e_1,e_2\},\quad A e_1=e_2\ (\text{其余为 }0),$$

$$Z_1=\operatorname{span}\{e_3\},\qquad Z_2=\operatorname{span}\{e_1-e_3\}.$$

| 检查 | 结果 |
|---|---|
| $Z_1\cap K$，$Z_2\cap K$ | 都是 $0$ ⟹ $A(Z_i\cap K)\subseteq Z_i$ 空真成立 ✓ |
| $Z_1+Z_2$ | $=\operatorname{span}\{e_1,e_3\}$ |
| $(Z_1+Z_2)\cap K$ | $=\operatorname{span}\{e_1\}$ |
| $A e_1$ | $=e_2\notin Z_1+Z_2$ ⟹ 并**不可行** ✗ |

$$\Longrightarrow\ \text{两个可行子空间的并不可行 —— \textbf{条件 (ii) 的族}不是格，最大元不唯一。}$$

（完整可行集还要加 (iii)，是它的子集；所以也不能指望"免费的格算法"。）

这既是 **Q1-TRUE 的入口**（非格结构 = 组合复杂性的温床），也是 **Q1-FALSE 的障碍**。

### 4.2 与已有障碍的关系

- $Z\subseteq K$ 时：$A(Z\cap K)=AZ\subseteq Z$ 就是 $A$-不变；此时问题退回多项式（最大不变子空间）。
- $Z\cap K=0$ 时：第二条条件变成"$Z$ 与所有 $(\lambda I-A)K$ 的交为 0"，是**一般位置**条件。
- 中间情形（$0<\dim(Z\cap K)<\dim Z$）才是可能难的地方 —— 与项目"D38：中间层不能放大"是同一现象的两个面。

---

## 5. 对 Q1-TRUE 的下一步

| 编号 | 目标 | 说明 |
|---|---|---|
| **D1** | 在受限族上证明 Z-FORM 的 $\max$ 是 NP-hard | 例如让 $Z$ 被迫取"坐标子空间"形式，$d_{\max}$ 变成集合函数 |
| **D2** | 造 gadget：每个组合选择对应一个 $Z$ | 需要 $A,K,C,L_0$ 的块结构使 $Z\cap K$ 的"半不变性"只在选定块上成立 |
| **D3** | 反证：若 Z-FORM 有拟阵结构 | 那 q1 = 假（交给 `q1_false/`）|

**当前判断**：Z-FORM 是目前 q1 最干净的靶子 —— 一个"最大化子空间维数 + 半不变性"的问题。
它既可能被证成 NP-hard（D1/D2），也可能被拟阵化（D3）。

---

## 6. 待严格化的地方

1. (8c) 的"$\forall\lambda$"与项目 $(5b)$ 的精确等价（本文用抽点 + 引用 c164 的 gcd 验证）。
2. $Z\subseteq L_0^\perp$ 与"字面前缀 $L=[L_0;R]$"的等价（依赖 $\operatorname{row}(L_0)\subseteq\operatorname{row}[C;L]$，
   即 $L_0$ 的行可挪进 $L$；由 $V\mapsto V+\operatorname{row}C$ 不改变 $(5a)(5b)$ 保证）。
3. 论文的 $V$ 是 $\ker[C;CA]$ 的基（即本文的 $K$），记号与论文一致。
