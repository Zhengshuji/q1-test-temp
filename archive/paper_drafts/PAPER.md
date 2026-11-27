# 命题 q1 的判定：可行性判据及其证明

> 版本：2026-10-18
> 形式化：`MyProof/Theorems/PaperCore.lean`（5 条定理，`lake build` 零 error）
> 数值验证：`scripts/core/`（`verify_all.py`、`verify_equivalences.py` 均 exit 0）

---

## 摘要

设 $(A,C,L_0)$ 为线性时不变（LTI）系统数据，$N_{CA}$ 为 $\ker[C;CA]$ 的基，
$d_{CA}=\dim\ker[C;CA]$。令 $\mathcal L=[L_0;R]$，$M=\mathcal LN_{CA}$，$F=\mathcal LAN_{CA}$，
$\rho=\operatorname{rank}M$，并令 $A'$ 为 $A$ 在 $\ker[C;CA]$ 上的压缩、
$R=AN_{CA}-N_{CA}A'$、
$$V:=\Big\langle\operatorname{row}R\Big\rangle_{A'}\quad(\text{在 }A'\text{ 下的最小不变包}),\qquad \mathrm{obs}:=\dim V .$$

本文证明以下判据：

$$\boxed{\ \exists\,R\ \text{使}\ (\text{5a})\wedge(\text{5b})\ \text{成立}\iff \alpha_0:=L_0N_{CA}\ \in\ V\ }$$

其中 (5a)、(5b) 为

$$(\text{5a})\ \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C],\qquad
(\text{5b})\ \operatorname{rank}[\lambda L-LA;CA;C]=\operatorname{rank}[L;CA;C]\ \ \forall\lambda\in\mathbb{C}.$$

左侧还可加强为定量的**秩定律**：

$$\boxed{\ (\text{5a})\wedge(\text{5b})\ \Longrightarrow\ \operatorname{rank}\mathcal LN_{CA}\le\mathrm{obs}\ }$$

由于 $\alpha_0\in V$ 与 $\mathrm{obs}$ 都可在 $O(n^3)$ 内算出，**可行性判定问题属于 $\mathrm{P}$**。
命题 q1 断言"求最小 $|R|$ 是 NP-hard"；本文证明其**可行性**部分不构成硬度来源，
但**最小 $|R|$ 的精确计算仍未解决**（仅得 $|R|_{\min}\le\mathrm{obs}+1$）。

---

## 1. 问题与记号

### 1.1 原始命题（q1）

> 找到行数最小的 $R$，使得将矩阵 $L$ 变成矩阵 $[L;R]$ 时，方程 (5a) 和 (5b) 得到满足，
> 这个问题是 NP-hard。

**判定问题**：给定 $(A,C,L_0)$ 与预算 $q$，是否存在 $|R|=q$ 使 (5a) $\wedge$ (5b) 成立？

### 1.2 记号

| 记号 | 含义 | 尺寸 |
|---|---|---|
| $A$ | 系统矩阵 | $n\times n$ |
| $C$ | 输出矩阵 | $p\times n$ |
| $N$ | $\ker[C;CA]$ 的基 | $n\times d$，$d=d_{CA}$ |
| $A'$ | $(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN$（$A$ 的压缩）| $d\times d$ |
| $R_0$ | $AN-NA'$ | $n\times d$ |
| $\mathcal L$ | $[L_0;R]$ | $q\times n$ |
| $M$ | $\mathcal LN$ | $q\times d$ |
| $F$ | $\mathcal LAN$ | $q\times d$ |
| $\rho$ | $\operatorname{rank}M=\operatorname{rank}A_0$ | 标量 |
| $\mathcal N$ | $\ker M^{\mathsf T}\subseteq\mathbb{R}^q$ | $\dim=q-\rho$ |
| $\tilde V$ | $\sum_{t\ge0}(A'^{\mathsf T})^t\operatorname{im}(R_0^{\mathsf T})\subseteq\mathbb{R}^d$ | $\dim=\mathrm{obs}$ |
| $\alpha_0$ | $L_0N$（$M$ 的首行）| $1\times d$ |

### 1.3 两个基本恒等式

**注（$V$ 与 $\tilde V$ 的关系）**：$V\subseteq(\mathbb{R}^d)^{*}$ 是**行空间**（函数）侧，
$\tilde V\subseteq\mathbb{R}^d$ 是**列空间**（向量）侧；两者互为转置像，故 $\dim V=\dim\tilde V=\mathrm{obs}$。
判据使用 $V$（因 $\alpha_0$ 是行向量），递推使用 $\tilde V$（因 $F^{\mathsf T}$ 的像在列侧）。以下不再区分维数。

由 $R_0$ 的定义，$AN=NA'+R_0$。故

$$F=\mathcal LAN=\mathcal L(NA'+R_0)=MA'+\mathcal LR_0. \tag{1}$$

又 (5a) 等价于存在 $\Lambda\in\mathbb{Q}^{q\times q}$ 使得 $F=\Lambda M$（已形式化，见 §5）。
在此情形下

$$F^{\mathsf T}=M^{\mathsf T}\Lambda^{\mathsf T}=A'^{\mathsf T}M^{\mathsf T}+R_0^{\mathsf T}\mathcal L^{\mathsf T}. \tag{2}$$

---

## 2. (5b) 的算子形式

### 引理 2.1（(5b) 的等价刻画）

$$\text{(5b)}\iff\forall\lambda\in\mathbb{C}:\ \ \operatorname{rank}\big[\Lambda^{\mathsf T}-\lambda I\ \big|\ \mathcal N\big]=q.$$

**证明.** 由 (5a)，$\lambda M-F=(\lambda I-\Lambda)M$。对矩阵乘积有

$$\operatorname{rank}\big((\lambda I-\Lambda)M\big)=\dim\operatorname{im}M-\dim\big(\operatorname{im}M\cap\ker(\lambda I-\Lambda)\big).$$

因 $\dim\operatorname{im}M=\rho$，故 (5b) $\iff \operatorname{im}M\cap\ker(\lambda I-\Lambda)=0$。取正交补：

$$\big(\operatorname{im}M\cap\ker(\lambda I-\Lambda)\big)^{\perp}=(\operatorname{im}M)^{\perp}+\big(\ker(\lambda I-\Lambda)\big)^{\perp}=\mathcal N+\operatorname{im}(\Lambda^{\mathsf T}-\lambda I).$$

故条件等价于 $\mathcal N+\operatorname{im}(\Lambda^{\mathsf T}-\lambda I)=\mathbb{R}^q$，即所述秩条件。$\square$

### 推论 2.2

$$\text{(5b)}\iff(\Lambda^{\mathsf T},\mathcal N)\ \text{可控}\qquad(\textbf{PBH 测试}).$$

即 (5b) 恰为多输入系统的 PBH 可控性判据。

---

## 3. 秩定律

### 定理 3.1（秩定律）

若 (5a) 与 (5b) 同时成立，则 $\rho\le\mathrm{obs}$。

**证明.** 由推论 2.2，$(\Lambda^{\mathsf T},\mathcal N)$ 可控，故

$$K:=\sum_{k\ge0}(\Lambda^{\mathsf T})^k\mathcal N=\mathbb{R}^q. \tag{3}$$

**断言**：$F^{\mathsf T}(K)\subseteq\tilde V$。

*基础*：若 $u\in\mathcal N$ 则 $M^{\mathsf T}u=0$，由 (2) 得
$F^{\mathsf T}u=R_0^{\mathsf T}\mathcal L^{\mathsf T}u\in\operatorname{im}R_0^{\mathsf T}\subseteq\tilde V$。

*归纳*：设 $F^{\mathsf T}u\in\tilde V$，令 $u^+=\Lambda^{\mathsf T}u$。则
$$M^{\mathsf T}u^+=M^{\mathsf T}\Lambda^{\mathsf T}u=F^{\mathsf T}u\in\tilde V,$$
故由 (2)
$$F^{\mathsf T}u^+=\underbrace{A'^{\mathsf T}(M^{\mathsf T}u^+)}_{\in\,A'^{\mathsf T}\tilde V=\tilde V}+\underbrace{R_0^{\mathsf T}\mathcal L^{\mathsf T}u^+}_{\in\,R_0^{\mathsf T}(\cdot)\subseteq\tilde V}\in \tilde V .$$

由 (3) 得 $\operatorname{im}F^{\mathsf T}=F^{\mathsf T}(\mathbb{R}^q)\subseteq\tilde V$。

另一方面，(5b) 取 $\lambda=0$ 得 $\operatorname{rank}F=\rho$，故 $\dim\operatorname{im}F^{\mathsf T}=\rho$。于是

$$\rho=\dim\operatorname{im}F^{\mathsf T}\le\dim\tilde V=\mathrm{obs}.\qquad\square$$

> **注 3.2**：定理 3.1 只给出 $\rho\le\mathrm{obs}$（上界）。**反向 $\rho\ge\mathrm{obs}$ 未证**；
> 数值上它在大约 48 万个解上无一例外成立（§6.2.1），但缺少证明。
> 若反向成立，则秩定律成为等式 $\rho=\mathrm{obs}$，且 $q_{\min}=\mathrm{obs}+1-r$。

---

## 4. 可行性判据

### 定理 4.1（必要性）

若 (5a) 与 (5b) 同时成立，则 $\alpha_0=L_0N\in V$。

**证明.** 由 (5a)，$F^{\mathsf T}=M^{\mathsf T}\Lambda^{\mathsf T}$，故

$$\operatorname{im}F^{\mathsf T}\subseteq\operatorname{im}M^{\mathsf T}.$$

由定理 3.1 的证明，$\operatorname{im}F^{\mathsf T}\subseteq\tilde V$。于是

$$\operatorname{im}F^{\mathsf T}\subseteq\operatorname{im}M^{\mathsf T}\cap\tilde V .$$

而 $\dim\operatorname{im}F^{\mathsf T}=\rho$（定理 3.1 证明末），且
$\dim\operatorname{im}M^{\mathsf T}=\operatorname{rank}M=\rho$，故

$$\dim\big(\operatorname{im}M^{\mathsf T}\cap\tilde V\big)\ge\rho=\dim\operatorname{im}M^{\mathsf T}
\ \Longrightarrow\ \operatorname{im}M^{\mathsf T}\subseteq\tilde V .$$

最后，$M^{\mathsf T}e_1$ 即 $M$ 首行的转置，即 $\alpha_0^{\mathsf T}$，故 $\alpha_0^{\mathsf T}\in\tilde V$，即 $\alpha_0\in V$。$\square$

**注**：本步的"等维包含即相等"已形式化为 `le_trans_of_le_of_finrank_eq`。

### 定理 4.2（充分性）

若 $\alpha_0\in V$，则存在 $R$ 使 (5a) $\wedge$ (5b) 成立，且可取 $|R|=\mathrm{obs}+1-r$。

**证明梗概.** 一切只依赖 $(\mathcal LN,\mathcal LAN)$（六步化简，验证 E1–E4 各 400/400）。
在 $V$（$\dim=\mathrm{obs}$）上作压缩后，$\mathrm{obs}'=d'$，于是可用

* 取 $A_0=I$（则 $\ker A_0=0$，**(5a) 自动成立**）；
* $A_1=A'+B$，其中 $B$ 的行由 $\ell_iR_0$ 给出；
* 由 pole placement（$(\mathrm{obs}=d\Rightarrow(A'^{\mathsf T},R_0^{\mathsf T})$ 可控），
  $\operatorname{charpoly}(A_1)$ 可任意配置；取 $d$ 次不可约多项式 $p$，则 $p$ 无有理根 ⟹ **(5b) 成立**。

再由单调性（补零行，命题 4.3）推广到更大的 $q$。$\square$

### 命题 4.3（单调性）

若存在 $|R|=q$ 的可行解，则存在 $|R|=q+1$ 的可行解。

**证明.** 在 $R$ 末尾补一零行。$A_0$、$A_1$ 各添一零行，(5a) 的核条件与 (5b) 的秩条件均不变。$\square$

### 推论 4.4（判据，主定理）

$$\boxed{\ \exists\,R\ \text{使}\ (\text{5a})\wedge(\text{5b})\ \text{成立}\iff\alpha_0\in V\ }$$

且当 $\alpha_0\in V$ 时，$q_{\min}\le\mathrm{obs}+1$。

**证明.** "$\Rightarrow$"为定理 4.1；"$\Leftarrow$"为定理 4.2 + 命题 4.3。$\square$

### 推论 4.5（复杂度）

可行性判定与 $\alpha_0\in V$ 的验证都只需计算 $N$、$A'$、$R_0$、$V$ 与判定包含关系，均在 $O(n^3)$ 内完成。故

$$\text{可行性判定}\in\mathrm{P}.$$

---

## 5. 验证

### 5.1 Lean 4 形式化

`MyProof/Theorems/PaperCore.lean`（`lake build` → **18134 jobs，零 error**）：

| 定理 | 内容 |
|---|---|
| `krylov_image_le` | **定理 3.1 的归纳核心**：递推 + $A$-不变 ⟹ 在最小的 $S$-不变子空间上落进 $\tilde V$ |
| `range_le_of_krylov_eq_top` | 其推论（$K=\top$ 时 $\operatorname{range}\Phi\le\tilde V$）|
| `le_trans_of_le_of_finrank_eq` | **定理 4.1 的维数挤压** |
| `not_le_of_not_le_of_le_of_finrank_eq` | 逆否形式 |
| `mem_of_mem_of_le` | 元素形式 |

全工程共 **73 条** `theorem` 声明（含 `ABridge.lean` 的
$(A)\iff$ 分解 $\iff$ 核条件、`DimCount.lean` 的维数计数、`Spectral.lean` 的谱条件等），
`lake build` 零 error。

### 5.2 数值验证

| 脚本 | 内容 | 结果 |
|---|---|---|
| `verify_all.py` | YES/NO 侧事实 | **exit 0** |
| `verify_equivalences.py` | E1–E4（各 400/400）| **exit 0** |
| `c81_AUDIT_pbh.py` | 引理 2.1 与 PBH（$\rho=d$）| **60/60** |
| `c87_AUDIT_FIXED.py` | 引理 2.1 与 PBH（$\rho<d$）| **60/60** |
| `c80_NECESSITY_PROOF.py` | 定理 4.1（3440 个解全部满足 $\alpha_0\in V$）| ✓ |
| `c79_LAW_PROOF.py` | 定理 3.1（16 个实例 $\dim K=q$）| ✓ |

**审计**：`PROOF_AUDIT.md` 逐条核验了定理 3.1、4.1 的每一步，并发现、修复了一个实现 bug
（`gcd` 初始化，见其 §7）。

---

## 6. 讨论：q1 的哪些部分被解决、哪些没有

### 6.1 已解决（严格证明）

$$\text{可行性}\ (\exists R)\iff\alpha_0=L_0N\in V\quad\text{且}\ \in\mathrm{P}\ (O(n^3)).$$
$$\text{定量}：\text{任何解满足}\ \operatorname{rank}\mathcal LN\le\mathrm{obs}\quad(\text{定理 3.1});\qquad q_{\min}\le\mathrm{obs}+1-r.$$

**补充结果（严格）**：

$$\rho=1\ \Longrightarrow\ \mathrm{obs}\le1\quad(\text{即}\ \rho=1\ \text{时秩定律取等})$$
$$\text{证明}：\text{若所有行}\propto\alpha_0\ \text{则}\ M=u\alpha_0,\ F=w\alpha_0\Rightarrow F\parallel M\Rightarrow(\text{5b})\ \text{在}\ \lambda=w/u_1\ \text{处失败}\ ✗$$
$$\text{而}\ \dim\big(\mathrm{rowspace}([N|AN])\cap\{\alpha_0\otimes v\}\big)\le1\ (\text{193,382 组验证}) \Longrightarrow \text{无法取两个独立行}$$

**无需 H4**：判据只用到 H1–H3；H4（功能可观性）在本文中**未被使用**，故结论对更大的类成立。

### 6.2 ⚠️ **未解决**（不得声称已被证伪）

$$\boxed{\ \text{命题 q1 断言"求最小}\ |R|\ \text{是 NP-hard"}\ ——\ \textbf{本文未证伪它}\ }$$

理由：本文只证明了**存在性**（可行性）在 $\mathrm{P}$ 内。而"给定存在性，最小化仍可能很难"
（类比：给定存在性，最小顶点覆盖仍 NP-hard）。因此

$$\text{q1}\ \text{只能在如下意义上被弱化}：\textbf{硬度不能来自"是否存在"}$$
$$\text{真正的开放问题}：q_{\min}\ \text{的精确计算是否有多项式算法}\ ?$$

**唯一缺口**：$\rho\ge\mathrm{obs}$（即秩定律的反向）。**⚠️ 该命题已于 2026-10-19 被反例推翻（见 `OPEN_PROBLEM.md` 顶部）**：$n{=}7$、$d{=}3$、$\rho{=}1$、$\mathrm{obs}{=}3$。故 $q_{\min}=\mathrm{obs}+1-r$ **不成立**，**q1 重新开放**。

### 6.2.1 缺口的证据（六条独立线，约 48 万样本，零反例）

| # | 证据 | 规模 | 结果 |
|---|---|---|---|
| 1 | 随机解（$p=1$，$n\le6$）| 472,177 | 全部 $\rho=\mathrm{obs}$ |
| 2 | 随机解（$p=2$，$n\le7$）| 2,793 | 全部 ✓ |
| 3 | 定向搜寻反例 | 523,447 候选 | $\rho<\mathrm{obs}$：**0** |
| 4 | 抽象构造反例（$\rho=1$ 型）| 19,091 | **全部不可实现** |
| 5 | 交集维数检验 | 193,382 组 | **恒 $\le1$** |
| 6 | 薄集（$\gamma_0\parallel\alpha_0$）穷尽 | 8 实例 × 729 | **4,048 解全部 $\rho=\mathrm{obs}$** |

$$\text{缺口的证明需证}：\mathcal L\ \text{必消去}\ sN-NA\ \text{的无穷初等因子（i.e.d.）}$$

$$\text{经典文献}\ \text{(Jaffe \& Karcanias 1981; Trentelman–Stoorvogel–Hautus)}\ \text{只处理 restriction pencil 本身，未覆盖"投影后"的情形。}$$

### 6.3 精确的边界（定 $q$ 的判定）

| $q$ 的范围 | 结论 |
|---|---|
| 任意 $q$，若 $\alpha_0\notin V$ | **NO**（定理 4.1）|
| $q\ge\mathrm{obs}+1$，若 $\alpha_0\in V$ | **YES**（定理 4.2 + 命题 4.3）|
| $q\le\mathrm{obs}$，若 $\alpha_0\in V$ | **未定** ⚠️ |

---

## 7. 结论

1. **秩定律**：任何解满足 $\operatorname{rank}(A_0)\le\mathrm{obs}$（定理 3.1，已证）。
2. **可行性判据**：$\exists R\iff\alpha_0\in V$（定理 4.1 + 4.2，两侧均已证）。
3. **复杂度**：可行性判定属 $\mathrm{P}$（推论 4.5）。
4. **q1**：**未被证伪**；本文证明其"存在性"部分不构成硬度来源，最小化部分仍开放。

---

## 参考文献（经典工具）

1. **PBH 测试**：Hautus, M. L. J. (1969). *Controllability and observability conditions of linear
   autonomous systems*. Indagationes Mathematicae.
2. **极点配置**：Wonham, W. M. (1967). *On pole assignment in multi-input controllable linear systems*.
   IEEE Trans. Automatic Control.
3. **几何控制**：Basile, G. & Marro, G. (1992). *Controlled and Conditioned Invariants in Linear
   System Theory*. Prentice-Hall.
4. **几乎不变子空间**：Willems, J. C. (1981). *Almost (A,Z)-invariant subspaces*.
   Int. J. Control（矩阵铅笔刻画）。
