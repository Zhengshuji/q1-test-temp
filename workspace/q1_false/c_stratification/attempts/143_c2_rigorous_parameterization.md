> **重要更正（2026-11-08）**：$V=\ker H$ 且 $H,H_A$ 的顶部 $r$ 行固定，故可容许 $V$ 必须满足
> $V\subseteq W_L=\ker[L_0N;L_0AN]$。六层应理解为 $\operatorname{Gr}(2,W_L)$ 上的分类；
> 在 $r=1,k=\omega+2$ 时若 $\dim W_L=2$，$V$ 被唯一确定。见 153 的更正。

# $c=2$ 严格参数化：精确参数空间、互斥穷尽、非空条件与算法

> 2026-11-08。按专家 56 号 §1.2 的裁决，把 136 的 $c=2$ 结构分解补成**精确参数空间**：
> 每个子型的底空间、纤维、非空条件，以及互斥/穷尽证明。状态：**M2（纸面）**。
> 这是专家建议的“严格 $c=2$ 结果 + 算法”的第一半。

## 目标

对 $c=2$、$V\in\operatorname{Gr}(2,K_0)$、$W=V\cap A^{-1}V$、$t=\dim W$，给出六个子型的：

1. **精确参数空间**（底 + 纤维）；
2. **互斥与穷尽**的证明；
3. **非空条件**；
4. 可直接实现的**判定算法**。

## 设想与理由

* 135 的精确纤维：$\mathcal F_W=\{V\supseteq U:\operatorname{rank}\Phi_V=2-t\}$，$\Phi_V:V\to\mathcal X/V$；
* $t=2$：$V$ 是 $A$-不变 2-平面，按 $A|_V$ 的 Jordan 型三分；
* $t=1$：$L=W$ 是 $A$-不变线（$AL\subseteq L$）或不是；前者 $V=L+\langle x\rangle$，后者 $V=L+AL$；
* $t=0$：开条件 $\operatorname{rank}\Phi_V=2$。

## 做法

### $t=2$：$A(V)\subseteq V$

$A|_V$ 是 $V$ 上的自同态（$A$ 不必保持整个 $K_0$）。按 $\mathbb C$ 上的 Jordan 型：

**(2a) 两个不同特征值 $\lambda\ne\mu$。**
$$V=\ell_\lambda\oplus\ell_\mu,\qquad \ell_\lambda\subseteq E_\lambda\cap K_0,\ \ell_\mu\subseteq E_\mu\cap K_0,$$
其中 $E_\lambda=\ker(A-\lambda I)\subseteq\mathcal X$。参数空间
$$\mathcal P_{2a}=\big(\mathbb P(E_\lambda\cap K_0)\times\mathbb P(E_\mu\cap K_0)\big)/\sim,\qquad (\ell_\lambda,\ell_\mu)\sim(\ell_\mu,\ell_\lambda),$$
（无序对；若固定 $\lambda<\mu$ 的次序则免去商）。**非空** $\iff E_\lambda\cap K_0\ne0$ 且 $E_\mu\cap K_0\ne0$。
参数化是单射：$V$ 的分解 $\ell_\lambda\oplus\ell_\mu$ 由 $V$ 唯一决定。

**(2b) 单个特征值、标量型 $A|_V=\lambda I_V$。**
$$V\subseteq E_\lambda\cap K_0,\qquad \mathcal P_{2b}=\operatorname{Gr}(2,E_\lambda\cap K_0).$$
**非空** $\iff\dim(E_\lambda\cap K_0)\ge2$。

**(2c) 单个特征值、非平凡 Jordan 块。**
$$(A-\lambda I)u=v,\qquad (A-\lambda I)v=0,\qquad v\ne0,\qquad u,v\in K_0,$$
$V=\operatorname{span}\{u,v\}$。**链提升条件**：
$$\ell=\mathbb Cv\subseteq E_\lambda\cap K_0,\qquad \ell\subseteq(A-\lambda I)(K_0).$$
第二式**不能**由第一式推出（专家 56 号 §1.2）。底空间
$$\mathcal B_{2c}=\{\ell\in\mathbb P(E_\lambda\cap K_0):\ \ell\subseteq(A-\lambda I)(K_0)\};$$
纤维（固定 $\ell$）
$$\mathcal F_{2c}(\ell)=\{u\in K_0:(A-\lambda I)u\in\ell\setminus\{0\}\}/\sim,\qquad u\sim u+\alpha v;$$
当非空时是**仿射空间**，方向为 $E_\lambda\cap K_0/\ell$，维数 $\dim(E_\lambda\cap K_0)-1$。
**非空** $\iff\mathcal B_{2c}\ne\emptyset$ 且存在 $u$ 使 $(A-\lambda I)u\in\ell\setminus\{0\}$
（即 $\ell\subseteq(A-\lambda I)(K_0)$）。

**互斥穷尽**：$A|_V$ 的 Jordan 型只有 (2a)(2b)(2c)；三者互斥；$t=2$ 即 $V$ 不变。

### $t=1$：$W=L=\mathbb Cv$

**(1A) $AL\subseteq L$**（含 $Av=0$）。$U=L$；$V=L\oplus\langle x\rangle$，精确条件
$$\operatorname{rank}\Phi_V=1\iff Ax\notin L+\langle x\rangle.$$
参数空间：底 $\mathcal B_{1A}=\{\ell\in\mathbb P(K_0):A\ell\subseteq\ell\}$（$A$-不变线，含零像线）；
纤维 $\mathcal F_{1A}(\ell)=\{x\in K_0/L:\ Ax\notin L+\langle x\rangle\}$，是 $\mathbb P(K_0/L)$ 中
“$Ax\in L+\langle x\rangle$”的补集（一个锥的补，Zariski 开）。**非空** $\iff\exists x$ 使 $Ax\notin L+\langle x\rangle$。

**(1B) $AL\not\subseteq L$**。$V=L+AL=\operatorname{span}\{v,Av\}$；精确条件
$$\operatorname{rank}\Phi_V=1\iff A^2v\notin L+AL\iff\operatorname{rank}[v,Av,A^2v]=3.$$
参数空间：
$$\mathcal P_{1B}=\{v\in D:\operatorname{rank}[v,Av,A^2v]=3\}/\mathbb C^\times$$
（$v\mapsto cv$ 同一 $V$；$V$ 唯一决定 $L=\langle v\rangle$，因为 $W=\langle v\rangle$）。**非空** $\iff$ 存在这样的 $v$。
**注意**：旧条件“$D\ne0$ 且 $A|_D$ 非标量”**不够**（幂零 $J_2$ 反例，136 §t=1 B）。

**互斥穷尽**：$AL\subseteq L$ 与 $AL\not\subseteq L$ 互斥且穷尽；$t=1$ 即 $\dim W=1$。

### $t=0$：$W=0$

$U=0$；$V\in\operatorname{Gr}(2,K_0)$ 满足 $\operatorname{rank}\Phi_V=2$（即 $V\cap A^{-1}V=0$）。
这是 $\operatorname{Gr}(2,K_0)$ 的开子集。**非空** $\iff\exists V$ 使 $V\cap A^{-1}V=0$。

## 互斥与穷尽（总）

* $t=\dim W\in\{0,1,2\}$，穷尽且互斥（维数）。
* $t=2$：按 $A|_V$ 的 Jordan 型分 (2a)(2b)(2c)，穷尽且互斥。
* $t=1$：按 $AL\subseteq L$ 与否分 (1A)(1B)，穷尽且互斥。
* $t=0$：单一开层。
故六层构成 $\operatorname{Gr}(2,K_0)$ 的一个**有限分层**，每层是某个底空间上的（开）纤维丛。

## 非空条件汇总

| $t$ | 子型 | 非空条件 |
|---|---|---|
| 2 | (2a) $\lambda\ne\mu$ | $E_\lambda\cap K_0\ne0$ 且 $E_\mu\cap K_0\ne0$ |
| 2 | (2b) 标量 | $\dim(E_\lambda\cap K_0)\ge2$ |
| 2 | (2c) Jordan | $\exists\ell\subseteq E_\lambda\cap K_0$，$\ell\subseteq(A-\lambda I)(K_0)$，且 $\ell\subseteq(A-\lambda I)(K_0)\setminus\{0\}$（即链可提升）|
| 1 | (1A) | $\exists x\in K_0/L:\ Ax\notin L+\langle x\rangle$ |
| 1 | (1B) | $\exists v\in D:\ \operatorname{rank}[v,Av,A^2v]=3$ |
| 0 | 开 | $\exists V\in\operatorname{Gr}(2,K_0):\ V\cap A^{-1}V=0$ |

## 判定算法（$c=2$）

1. 计算 $K_0=\ker[C;CA]$、$D=K_0\cap A^{-1}K_0$（线性代数，$O(n^3)$）。
2. 对 $t=2$：枚举 $A$ 的特征值 $\lambda$（特征多项式，$O(n^3)$）；计算 $E_\lambda\cap K_0$；
   * 若存在 $\lambda\ne\mu$ 且两交非零：层 (2a) 非空；
   * 若某 $\dim(E_\lambda\cap K_0)\ge2$：层 (2b) 非空；
   * 若某 $\ell\subseteq E_\lambda\cap K_0$ 满足 $\ell\subseteq(A-\lambda I)(K_0)$ 且存在 $u$：层 (2c) 非空
     （判定 $\ell\subseteq(A-\lambda I)(K_0)$ 是线性方程，$O(n^3)$）。
3. 对 $t=1$：枚举 $A$-不变线 $L\subseteq K_0$（解 $A\ell\subseteq\ell$，即 $A$ 的特征线，$O(n^3)$）；
   * (1A)：对每个 $L$，判定 $\exists x$ 使 $Ax\notin L+\langle x\rangle$（线性/二次条件，$O(n^3)$）；
   * (1B)：对每个 $v\in D$（$D$ 的参数化），判定 $\operatorname{rank}[v,Av,A^2v]=3$（$O(n^3)$）。
4. 对 $t=0$：判定 $\exists V$ 使 $V\cap A^{-1}V=0$（开条件；等价于某个 $2\times2$ 行列式非零，$O(n^3)$）。
5. **注意**：层非空只说明存在**可容许**的 $V$（即 $W=V\cap A^{-1}V$ 的精确纤维非空）；
   要判定 $q=\omega+1$ 可行，还需在该层的 $V$ 上检验**好性**（块判据，见下节）。

**复杂度**：固定 $c=2$ 时，枚举特征线/特征值为 $O(n^3)$ 级；总多项式。

### 好性条件（可行性的另一半）

层参数化只给出**可容许**的 $(W,V)$；$q=\omega+1$ 可行还要求 $V$ 是**好**的：
令 $H=LN_K$、$H_A=LAN_K$（$L=[L_0;R]$ 由 $V$ 的选择给出），$W_0=\operatorname{im}H$，
$A_{W_0}$ 为 $A$ 在 $W_0$ 上的诱导，$B_\perp$ 为 $W_0\to\mathbb C^q$ 的补块；坏条件为
$$\exists\,0\ne y\in\ker B_\perp,\qquad A_{W_0}y\in\mathbb C y.$$
对每个子型，需在参数空间上解这个“特征向量落在指定子空间”的条件；其非空性才是该层的**可行性**。
本文件的“非空条件”表是**可容许非空**，不是可行性；两者不能混。

## 算法实现尝试（失败记录，2026-11-08）

对 c=2 实例（k=4,ω=2，seeds 10/16/21），尝试由 V 直接构造 L：
取 $V\subseteq\ker(L_0N_K)$ 的 2 维子空间，令 $R N_K$ 为 $V$ 的零化子（2×4），
取 $R=M\cdot N_K^{+}$（$N_K^{+}$ 为左逆），再检验 `check_candidate`。

**结果**：全部失败——
* seed 10：`rank[C;L]=4 != p+q=5`（R 的行与 C、L0 线性相关）；
* seed 16/21：一般 λ 处秩 6 != h=5（法秩不等于目标秩）。

**原因**：$R N_K$ 只保证 $V=\ker H$，**不保证 $(5a)$**；提升必须同时满足 $\operatorname{row}(RN)\subseteq S$
与 $\operatorname{row}(RAN)\subseteq S$（即 114 的提升引理的 rowspace 约束），不能只靠 $N_K$ 的左逆。
**第二步尝试**：按 114 增加齐次部分（$R=R_0+$ 零空间）以补满 $\operatorname{rank}[L_0;R]$；仍失败——
`rank[C;L]=4 != p+q=5`。原因：提升还要求 $\operatorname{rank}[C;L]=p+q$（C 与 L 的行独立），
而 V/H 构造只控制 $\ker H=V$ 与 $\operatorname{rank}H=\omega$，不控制 C 的交互。

**第三步尝试**：改用 `modJ_candidates` 产生 $(5a)$-可行的 L；但 `lift_rows` 的 q 由闭包维数 $d$ 决定，
seeds 10/16 的 61 个候选全部 $q\ne3$，seed 21 的候选 0 个通过 $(5a)$——**不是 q=3 的工具**。

**诊断**：$c=2$ 的决策算法需要**固定 $q=\omega+1$** 的专用管线：
(a) 固定 $V$（2-平面）与 $H$ 的 $\omega$ 行；(b) 解 $R N=H_b$、$R A N=H_{A,b}$ 的线性系统；
(c) 在解空间中同时满足 $\operatorname{rank}[L_0;R]=q$ **与** $\operatorname{rank}[C;L]=p+q$；
(d) 再检验好性。现有工具（`modJ_candidates`、`check_candidate`）各自只覆盖一部分，需新写一个固定 q 的模块。
**下一步**：写 `tools/verification/c2_decision.py`（固定 $q=\omega+1$，按 (a)–(d) 实现），而不是在 scratch 里拼。

## 进展

* 六个子型的精确参数空间、互斥穷尽、可容许非空条件已写出；**可行性还差好性（块判据）**。
* 关键修正：$t=2$ 的链提升条件 $\ell\subseteq(A-\lambda I)(K_0)$；$t=1$ B 的秩 3 条件；
  $t=2$ (2a) 的无序对商。
* 每层的底空间/纤维都是（开）代数簇；**未**证各层的不可约性/分量数。

## 最终结论

* $c=2$ 的六层是 $\operatorname{Gr}(2,K_0)$ 的有限分层，每层参数空间精确；
* 可容许非空性化为线性代数判定；可行性需另加好性检验（块判据）。
* 这是专家 56 号建议的“严格 $c=2$ 结果 + 算法”的纸面版本（M2）。

## 放弃原因

* 各层不可约性/分量数已补：见 [147](147_c2_component_bound.md)（上界 $\binom{s}{2}+3s+2$）；
* 实点未做；
* 算法未实现/未跑精确验证（下一步）。

## 残留价值

* 可直接用于 $c=2$ 的算法实现与 $c=3$ 的模板；
* 修正了 136 的链提升条件与参数空间细节。

## 相关文件

* [attempts/135](135_exact_fibre_theorem.md)（精确纤维，$\mathcal X/V$）
* [attempts/136](136_c2_rewrite.md)（$c=2$ 结构表）
* [attempts/142](142_general_incidence_theorems.md)（一般 $(t,u)$ 分层）
* [attempts/123](123_hyperplane_algorithm.md)（算法模板）

## 状态

* 参数化/互斥穷尽/非空/算法：**[已证-纸面，M2]**。
* 不可约性/分量数：**[未做]**。
* 精确验证/实现：**[未做]**。
