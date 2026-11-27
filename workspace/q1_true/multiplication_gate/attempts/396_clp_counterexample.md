# 358 CLP 在 $m=2$ 的反例：降秩层是**奇异三次超曲面**，可行集不在任何线性空间里

> 承接 357（$m=1$ 时 CLP 成立）与 356（98 号把 CLP 定为下一步）。
> 本文件给出**反例**：一个合法的 $\omega=2$ 层，两个可行点满足 $\det H=0$，但它们的中点 $\det H\ne0$。
> 于是**没有任何线性空间**能同时容纳这两点并落在该层里。
> 证书：[c358](../../../../tools/verification/c358_nonlinear_stratum_witness.py)（精确算术）。

## 目标

判定 CLP（候选线性原理）在 $m\ge2$ 时是否成立。

## 设想与理由

357 已把 CLP 化归为：**$P_\omega=\{R:\operatorname{rank}H=\omega,(5a)\}$ 的分量是否线性**。

$P_\omega$ 由**子式**定义，所以自然要问：$\operatorname{rank}H=\omega$ 这个条件在
$\omega<\min(k,r_0+m)$ 时是**降秩**条件——它是行列式簇，**不是**线性的。
$\omega=\min(k,r_0+m)$（最高层）与 $\omega=\operatorname{rank}H_0$（最低层）是例外：
前者是开条件（闭包是整空间），后者迫使自由行落进 $\operatorname{row}H_0$（线性）。

所以第一个可能的反例在**中间层**。取最小的中间层：$k=3$、$r_0=1$、$m=2$，则
$$\operatorname{rank}H\in\{\,1,2,3\,\},\qquad \omega=2\ \text{是中间层},$$
而 $H$ 是 $3\times3$，条件 $\operatorname{rank}H=2$ 就是 $\det H=0$——一个**不可约三次超曲面**。

## 做法

实例用 79 号的 $3k$ 通用提升（$k=3$、$n=9$、$p=3$），于是每行的自由对 $(h,g)\in\mathbb C^3\times\mathbb C^3$ **任意**；
固定行只取一行：$H_0=[e_1]$、$H_{A,0}=[e_1]$（协调条件成立）。

**精确搜索**（[c358](../../../../tools/verification/c358_nonlinear_stratum_witness.py)）：$h_1,g_1,h_2,g_2$ 的条目取 $\{-1,0,1\}$，筛出
$(5a)+(5b)$ 成立、$\operatorname{rank}H=2$ 的点（得 300 个），再找**中点满秩**的一对。找到：

$$H_p=\begin{pmatrix}1&0&0\\-1&-1&-1\\-1&-1&-1\end{pmatrix},\qquad
H_q=\begin{pmatrix}1&0&0\\-1&-1&0\\-1&0&0\end{pmatrix},$$

两者都 $\det=0$（$\omega=2$）、都满足 $(5a)$、$(5b)$（$\gcd$ 精确算出为 1），
但中点
$$H_m=\frac{H_p+H_q}{2}\ \text{满足}\ \det H_m=\tfrac14\ne0\quad(\operatorname{rank}H_m=3).$$

两个点的**压缩行空间也不相同**：$\operatorname{row}H_p=\operatorname{span}\{e_1,(1,1,1)\}$、
$\operatorname{row}H_q=\operatorname{span}\{e_1,(1,1,0)\}$。

## 进展

1. **反例已构造并验证**：两个可行点，中点不在该层里。
2. 由此：**任何同时包含这两点的线性空间都含中点，而中点的 $\det\ne0$**，
   所以不存在"包含该可行集的线性空间"——**CLP 的"闭包 = 线性空间"形式为假**。
3. 几何机制被指认：**中间秩层是行列式（奇异）簇**。$\omega=\min(k,r_0+m)$ 与 $\omega=\operatorname{rank}H_0$
   这两层是线性的，中间的层不是。

## 一般判据：CLP $\iff$ 可行集被锁在**单个**行空间里

> **更正（99 号 §1）**：原文写的
> $$\{\operatorname{rank}H=\omega\}=\bigcup_W M_W\qquad\text{（$M_W=\{h_i,g_i\in W\}$）}$$
> 是**错的**：$\operatorname{rank}H=\omega$ 只约束 $h_i$，不约束 $g_i$。
> （$W_0=0$、$m=1$、$\omega=1$ 时取 $h\in W$、$g\notin W$：$\operatorname{rank}H=1$ 但点不在 $M_W$ 里。）
> 正确形式是**可行**秩层的分解（在固定行协调 $\operatorname{row}H_{A,0}\subseteq W_0$ 下）：
> $$\boxed{\mathcal F_\omega=\bigcup_{W\in\mathrm{Gr}(\omega,k),\ W\supseteq W_0}\Bigl[M_W\cap\{\operatorname{rank}H=\omega\}\cap\{(5b)\}\Bigr]}$$
> **开集性不受影响**：$M_W$ 上恒有 $\operatorname{rank}H\le\omega$，故 $\{\operatorname{rank}H=\omega\}$ 是 $M_W$ 里的开集，
> 与 $(5b)$ 的开集相交仍是开集。

对固定的 $\omega$ 与每个 $\omega$ 维子空间 $W\subseteq\mathbb C^k$（含 $W_0=\operatorname{row}H_0$），
$$L_W=\{R:\ h_i,g_i\in W\}\quad(\text{线性空间}),$$
则**可行**集是 Grassmannian 上的并：
$$\mathcal F_\omega=\bigcup_{W\supseteq W_0}L_W\cap\{\operatorname{rank}H=\omega\}\cap\{(5b)\}.$$

> **判据.** 若可行集 $\mathcal F_\omega$ 中两个点的压缩行空间 **不同**（$W\ne W'$），且其中点秩 $>\omega$，
> 则 CLP 的"闭包线性"读法为假。反之，若 $\mathcal F_\omega$ 只落在**一个** $W$ 里（即行空间被锁死），
> 则 $\mathcal F_\omega\subseteq L_W$，而 $L_W$ 线性——CLP 成立。

**两端的对应**（这正是 354/355 的结论）：

| 情形 | 行空间 | CLP |
|---|---|---|
| **钉住**（$\dim(A K_0)=\operatorname{rank}H_0$） | 被锁死 $W=W_0$ | **成立**（线性开集） |
| $m=1$（$\omega=r$） | $h\in\operatorname{row}H_0$ | **成立**（定理 A，357） |
| **未钉住的中间层** | 在 Grassmannian 上变化 | **假**（本文件的反例） |

所以 CLP 不是"对所有秩层都成立"或"都不成立"，而是一条**分界线**：
**行空间被锁 $\Rightarrow$ 线性；行空间能变 $\Rightarrow$ 非线性。**

这条判据同时解释了 354 的 pinned no-go 为什么能成立（那里行空间被钉死），
以及为什么"未钉住 + 中间层"才是乘法唯一可能的藏身处。

## 最终结论

1. **CLP 的"闭包是线性空间"形式在 $m=2$、$\omega=2$ 时为假**，有精确证书，而且**不需要不可约性**。
   **论证按 99 号 §3.1 更正**（原文说"精确秩层是闭的"是错的——精确秩层只是局部闭）：

   > 每个可行点的 $\operatorname{rank}H=\omega=2$，故可行集的 Zariski 闭包含于**闭**行列式簇
   > $D_2=\{H:\operatorname{rank}H\le2\}$。若闭包是线性空间 $L$，则 $H_p,H_q\in L$，故中点 $\in L$；
   > 而 $H_m\notin D_2$（$\det=\tfrac14\ne0$）——矛盾。$\square$

2. **证书补全（99 号 §3.2 要求）**：两点连同 $H_A$ 与极大子式如下（$C=[I_3\ 0\ 0]$、
   $A=\begin{pmatrix}0&0&I_3\\0&0&0\\0&I_3&0\end{pmatrix}$、$L_0=[0\,|\,e_1^{\mathsf T}\,|\,e_1^{\mathsf T}]$）：

   | | $H$ | $H_A$ | 非零极大子式 | $\gcd$ |
   |---|---|---|---|---|
   | $p$ | $\begin{pmatrix}1&0&0\\-1&-1&-1\\-1&-1&-1\end{pmatrix}$ | $\begin{pmatrix}1&0&0\\-1&0&0\\0&-1&-1\end{pmatrix}$ | $-\lambda^2+\lambda,\ -\lambda^2+2\lambda-1,\ 1-2\lambda$ | $1$ |
   | $q$ | $\begin{pmatrix}1&0&0\\-1&-1&0\\-1&0&0\end{pmatrix}$ | $\begin{pmatrix}1&0&0\\-1&0&0\\0&-1&0\end{pmatrix}$ | $-\lambda^2+\lambda,\ \lambda-1,\ -\lambda^2-\lambda+1$ | $1$ |

   中点 $H_m=(H_p+H_q)/2$ 的 $\det=\tfrac14$。全部可复现：[c358](../../../../tools/verification/c358_nonlinear_stratum_witness.py)
   （脚本会打印 $H,H_A$、子式与 $\gcd$，并对 $\det$ 与 $\gcd$ 逐条断言）。
3. **哪种读法为真、哪种为假**：

   | 读法 | 结论 |
   |---|---|
   | $\overline{\mathcal F_\omega}$ 是线性空间 | **假**（本文件的反例） |
   | $\mathcal F_\omega$ 在某个线性子空间里稠密（且**含于**该子空间） | 同上，假 |
   | $\mathcal F_\omega$ 在某个更小的线性子空间里稠密（不要求含于） | 未被反驳，但这是弱到几乎无用的读法 |

4. **这正是 98 号说的"同样有价值"的分支**：反例指出乘法的几何藏身处——
   **降秩（行列式）层的奇异几何**，而不是线性开集。
5. **一个几何判据**：若中间层上存在两个可行点、其压缩行空间不同，则取中点常把秩抬高；
   而最高层（开）与最低层（$\operatorname{rank}H_0$，线性）没有这个自由度。

## 放弃原因

- 没有判定 $C$ 的不可约性，因此结论停在"朴素形式为假"；
- 没有在小实例上系统统计"哪些 $(\omega,k,r_0,m)$ 组合会出现非线性"；
- 没有利用这个反例去构造乘法门（那需要把 $\det H=0$ 的几何与编码变量对上）。

## 残留价值

- **一个精确证书的反例**，把 98 号的候选原理从"可能为真"改为"朴素形式为假"；
- 把 CLP 的失效位置精确定位到**中间秩层**（降秩条件 = 行列式簇）；
- 给出下一步的明确技术问题：$\{\operatorname{rank}H=\omega\}\cap(5a)$ 的不可约性。

## 相关文件

- [357](395_clp_single_row.md)（$m=1$ 的 CLP：成立）
- [356](394_expert98_audit.md)（98 号把 CLP 定为下一步）
- [355](../../../q1_false/c_stratification/attempts/393_maximality_lemma.md)（极大性引理）
- [c358](../../../../tools/verification/c358_nonlinear_stratum_witness.py)

## 状态

- 反例（朴素形式）：**[精确验证]**（c358，严格算术，含 det 与 gcd 的断言）。
- 分量级结论：**[未定]**（依赖 $C$ 的不可约性）。
- 中间层非线性的**一般**判据：**[未做]**。
