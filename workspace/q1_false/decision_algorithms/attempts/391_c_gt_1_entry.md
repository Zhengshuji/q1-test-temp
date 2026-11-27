# 391 $c\ge2$ 的入口：历史工作盘点与一个必须先修的量（$\omega$ 的定义）

## 目标

用户问：下一步是否是 $c>1$？项目以前有没有这方面的工作？本文件回答这两问，并把 $c\ge2$
的**第一块基石**（方向定理的推广）写清；同时记录一个在做 $c\ge2$ 之前必须先定的记号问题。

## 设想与理由

$c=1$ 的整套结果（方向 = 压缩特征向量、纤维 = Grassmann、逐图卡 gcd）都是围绕
$\ker H$ 是**一条直线**。$c\ge2$ 时 $\ker H$ 是 $c$ 维，直觉上的推广是"$\ker H$ 必须是压缩 $M$
的**不变子空间**"（$c=1$ 时退化为特征向量）。要做这件事，先得确认：

1. 项目里已有的 $c>1$ 工作用什么语言、到什么程度；
2. "层号 $c$" 到底该定义为 $k-\rank H$ 还是 $k-\dim(V\cap K_0)$ —— 这两者一般**不相等**。

## 做法

1. 在仓库里检索层相关工作（`claim_index --grep 层`、`docs/04`、`docs/05`、`proof/rho*`、`proof/layer*`）。
2. 用 4242 的实例做精确核对：$\rank(LN)$、$\dim(K_0\cap V^\perp)$、$\dim(V\cap K_0)$ 三者的关系。

## 进展

### 1.5 修正后的 c=2 精确核查（`c391` v2，已跑）

实例：4242 的 $A$、$K_0$ 块换成 $\operatorname{diag}(1,1,2,3)$，故 $M=\operatorname{diag}(1,1,2,3)$、
$K_0=\operatorname{span}\{e_5,\dots,e_8\}$、$k=4$、$n=8$。构造：取 $D\le K_0$，令 $U=D+AD$、$V=U^\perp$（行空间）。

| $D$ | $\dim D$ | $\dim U$ | $\dim V(=q)$ | $c=\dim(K_0\cap V^\perp)$ | $\dim(V\cap K_0)$ | $k-c$ | (5a) | $M(D)\subseteq D$ |
|---|---|---|---|---|---|---|---|---|
| $\operatorname{span}\{e_1,e_2\}$（不变，$\mu=1$） | 2 | 3 | 5 | **2** | 2 | 2 ✓ | ✓ | **✓** |
| $\operatorname{span}\{e_1,e_4\}$（不变，$\mu=1,3$） | 2 | 3 | 5 | **2** | 2 | 2 ✓ | ✓ | **✓** |
| $\operatorname{span}\{e_1,e_1+e_3\}$（其实是 $\operatorname{span}\{e_1,e_3\}$，仍不变） | 2 | 4 | 4 | 2 | 2 | 2 ✓ | ✓ | ✓ |
| $\operatorname{span}\{e_1+e_2,e_3+e_4\}$（**非**不变） | 2 | 3 | 5 | 2 | **1** | 2 ✗ | ✓ | **✗** |

**两条结论**：

1. **横截前提不是自动的**：最后一行 (5a) 成立、$c=2$，但 $\dim(V\cap K_0)=1\ne k-c=2$。
   此时 $\ker H=D$ 而 $M(D)\not\subseteq D$ —— 所以"$M(\ker H)\subseteq\ker H$"**离开横截前提是假的**。
2. 由此 **论文的 (S2)（$\dim(V\cap K_0)=k-1$）也不是自动的**：它是**额外假设**，不是 $(5a)$ 的推论。
   $c=1$ 的实例里（$q=k$、$V=D_v\oplus$ 一条自由行）它恰好成立，所以早期没有暴露。

### 1.6 两套语言的对齐表（步骤 2，已用 `c392` 精确核对修正）

**先记三个不同的量**（$q$ = 行数、$k=\dim K_0$、$\rho=\dim\pi_{K_0}(V)$）：

$$\boxed{\ \rho=\rank(LN),\qquad c_{\rm new}:=k-\rho=\dim(K_0\cap V^\perp),\qquad
c_{\rm old}:=q-\rho=\dim(V\cap K_0^\perp).\ }$$

`c392` 的精确表（4242，$n=8,k=4$）：

| $q$ | $\rank H$ | $c_{\rm new}=k-\rho$ | $\rho$ | $c_{\rm old}=q-\rho$ | $\dim(V\cap K_0)$ |
|---|---|---|---|---|---|
| 3 | 3 | 1 | 3 | 0 | 0 |
| 4 | 3 | 1 | 3 | 1 | 0 |
| 5 | 4 | 0 | 4 | 1 | **2** |
| 6 | 4 | 0 | 4 | 2 | 2 |

要点：
- **$\rho=\rank H$ 恒成立**（压缩后的秩 = 投影维数），所以"$\omega:=\rank H$"就是旧框架的 $\rho$；
- $c_{\rm new}$ 与 $c_{\rm old}$ **相差 $q-k$**，只在 $q=k$ 时相等 —— $c=1$ 的论文正好是 $q=k$，所以没暴露；
- $\dim(V\cap K_0)$ 是**第三个**量（表里 $q=5$ 那行给出 2，既不等于 $c_{\rm new}=0$ 也不等于 $c_{\rm old}=1$）。

| 旧框架（环境语言） | 新框架（压缩语言） | 关系 |
|---|---|---|
| $\mathcal J=\operatorname{row}[C;CA]$ | $K_0^\perp$（即 $K_0=\mathcal J^\perp$） | 互为对偶 |
| $\mathcal V=\operatorname{row}\mathcal L$ | $V$ | 同一空间 |
| $\rho=\dim\pi(\mathcal V)$ | $\rank H=\dim(LK_0)=\dim\pi_{K_0}(V)$ | **同一个量** |
| $c=\dim(\mathcal V\cap\mathcal J)$ | $c_{\rm old}=q-\rho=\dim(V\cap K_0^\perp)$ | **同一个量** |
| $q=\rho+c$ | $q=\rho+c_{\rm old}$ | 同一恒等式 |
| — | $c_{\rm new}=k-\omega=\dim(K_0\cap V^\perp)$ | 新框架独有；$q=k$ 时 $=c_{\rm old}$ |
| $\mathcal D_s=\{V:\dim(V+AV)\le s\}$ | $\{D:\dim(D+AD)\le s\}$，$D=\ker H$ | 同一分层（$s$ 从 $c$ 到 $\min(2c,k)$）|
| 最低层 $\iff AV\subseteq V$（$A$-不变） | $M$-不变（**更细**：不要求 $A_{21}D=0$） | 新框架更强 |
| 固定 $(\mathcal U,\mathcal H)$："容器唯一 $\iff\dim\beta(\mathcal H)=\rho-1$" | $c=1$ 的"纤维是单点" | 同一件事 |

### 1.7 $c=2$ 的参数化（步骤 3，草案）

- **底**：$\{D\in\operatorname{Gr}(2,K_0): M(D)\subseteq D\}$（$M$-不变的 2-子空间簇；$c=1$ 时就是论文的
  "有限个 $\mathbb P(E_\mu)$ 的并"，因为不变直线 = 特征向量）；
- **分层**：按 $\dim(D+AD)\in\{2,3,4\}$ 分三层（旧框架的 $\mathcal D_s$）；
- **纤维**：$V$ 满足 $V_0+D\subseteq$…、$V\subseteq(D+AD)^\perp$、$\dim V=q$ ⟹ 是
  $\operatorname{Gr}(q-\cdot,\ (D+AD)^\perp/(\ldots))$；维数与 $c=1$ 的 $(s-\delta)(r-s)$ 同型但多一个"$D$ 变化"的底维；
- **横截条件**必须**显式作为图卡条件**（否则定理不成立），即要求
  $\dim(V\cap K_0)=k-2$，等价于某个秩条件，可在图卡上用"某子式非零"实现。

### 1. 项目已有的 $c>1$ 工作（**相当多**）

| 位置 | 内容 |
|---|---|
| `docs/04_structure.md` §4.1–4.3 | 主分解 $q=\rho+c$（定义性）；$\rho$ 一侧 $=P(T,B,U_0)$ 已多项式；**$c$ 一侧与可达性标为开放** |
| `docs/05_open_questions.md`（"一般余维 $c>1$"） | 用零化子 $V\subseteq K_0$（$\dim V=c$）、底 $\operatorname{Gr}(c,K_0)$、约束 $RV=RAV=0$；分量 = **Grassmannian degeneracy locus** $\mathcal D_s=\{V:\dim(V+AV)\le s\}$；**最低层** $\dim(V+AV)=c\iff AV\subseteq V$（$A$-不变）；$c=2$ 是第一个受控情形；精确纤维（attempts/134，专家 55）是 $\operatorname{Gr}(c-\dim U,K_0/U)$ 的**开子集**；型 = 受限 pair 的 Kronecker 型（Berger–Trunk–Winkler / Berger–Trenn）；开放：$\mathcal D_s$ 的分量/次数、复杂度、实点 |
| `proof/rho0_layer`、`proof/rho1_layer` | $c=1$ 的系统整理；`rho1_layer/theorem.md` §9–§31（含 §29 的固定 $(\mathcal U,\mathcal H)$ 判据、§30 有限签名 → 可判定、§31 与 $q_{\min}$ 的桥） |
| `proof/layer_program` | $c=1$ 一支的总览（"层程序"） |
| `proof/layer_31_theorems` | $(3,1)$ 层的定理包 |
| `proof/B.28`、`B.31`、`proof/delta1_feasible`、`proof/incidence_strata` | 层参数、中间层必要条件、$\delta=1$ 可行证书、入射分层 |
| `proof/refuted` R4 | "$\dim(V+AV)$ 的闭式"被推翻 |
| `proof/rho1_layer/theorem.md` §21/§29 | 一般 $(\rho,c)$ 的**固定** $(\mathcal U,\mathcal H)$ 判据：容器唯一 $\iff\dim\beta(\mathcal H)=\rho-1$，此时坏集仿射、层判定 = 维数比较 |

**结论**：$c>1$ 有明确的先前工作，但用的是**环境语言**（$\mathcal V$、$\pi$、$\mathcal J$、$\beta$、$Q_{\mathcal V}$），
而 $c=1$ 的论文用的是**压缩语言**（$K_0$、$M$、$H$、Grassmann 丛）。两套语言尚未对齐——
这就是 $c\ge2$ 的第一件正事。

### 2. 必须先修的记号：$\omega$ 不是 $\dim(V\cap K_0)$

论文（以及 $c=1$ 的若干卷宗）写 $\omega=\rank H=\dim(V\cap K_0)$、$c=k-\omega$。
精确核对（4242，$K_0=\operatorname{span}\{e_5,\dots,e_8\}$，$k=4$）：

| 随机 $L$（4 行） | $\rank H$ | $\dim(K_0\cap V^\perp)=k-\rank H$ | $\dim(V\cap K_0)$ |
|---|---|---|---|
| trial 0–4 | 4 | 0 | 0 |
| trial（前一轮，另一个实例） | 3 | 1 | 0 |

即 **$\rank H=\dim(LK_0)=k-\dim(K_0\cap V^\perp)$**，而 $\dim(V\cap K_0)$ 是**另一个量**
（$\dim(V\cap K_0)=q+k-\rank[V;K_0]$）。两者一般不等：
$$\dim(K_0\cap V^\perp)=k-\rank H,\qquad \dim(V\cap K_0)=q+k-\rank[V;K_0].$$

- $c=1$ 时二者数值上恰好都给出"$\ker H$ 是一维、$V\cap K_0$ 是 $k-1$ 维"，所以早期的推导没有暴露这个差别；
- 但**一般 $c$ 必须选一个**：$\dim\ker H = k-\rank H = \dim(K_0\cap V^\perp)$ 才是"核方向的维数"，
  也是旧框架的 $\dim(\mathcal V\cap\mathcal J)$（$c$ 的原义）。

**后果**：论文里"(S2) $\dim(V\cap K_0)=k-1$"与"$\omega=\dim(V\cap K_0)$"这两句在 $c=1$ 的实例上
数值正确、但**作为一般陈述是错的**；$c\ge2$ 的程序必须用 $c=\dim(K_0\cap V^\perp)=k-\rank H$。
（论文已移交另一 agent，此条需转告。）

### 3. $c\ge2$ 的方向定理（待完成的形式）

**设定**：$D:=\ker H=K_0\cap V^\perp$，$\dim D=c$；$V\subseteq D^\perp$；$(5a)$ 给 $V\perp AD$，
即 $AD\subseteq V^\perp$。

**命题（草稿）**：若 $\dim(V\cap K_0)=k-c$（等价于 $\rank[V;K_0]=q$，即 $V$ 与 $K_0$ 横截），
则 $M(D)\subseteq D$，其中 $M=\pi_{K_0}A|_{K_0}$。

*证明思路*：对 $d\in D$，泛函 $\varphi_{Ad}:u\mapsto\langle u,Ad\rangle$（$u\in K_0$）在 $V\cap K_0$ 上为零
（因 $V\perp AD$）；而 $\operatorname{ann}(V\cap K_0)$ 是 $c$ 维，且 $\{\varphi_d:d\in D\}$ 是其中 $c$ 个
线性无关的元素 ⟹ $\varphi_{Ad}\in\operatorname{span}\{\varphi_d\}$ ⟹ $\pi_{K_0}(Ad)\in D$。$\square$

- $c=1$ 时正是论文 Theorem 3（$\varphi_{Av}=\mu\varphi_v$ ⟹ $Mv=\mu v$）；
- 关键前提 $\dim(V\cap K_0)=k-c$ **不是自动的**（见 §2），必须作为假设或另行证明；
- 旧框架的"最低层 $AV\subseteq V$"是其**特例**（还要 $A_{21}D=0$）。

## 最终结论

1. **是**：$c>1$ 是下一步；项目已有大量工作，但都在**环境语言**里，且一般 $c$ 的层判定是开放的。
2. **先修记号**：$c=\dim(K_0\cap V^\perp)=k-\rank H$；论文里"$\omega=\dim(V\cap K_0)$"作为一般陈述是错的。
3. **$c\ge2$ 第一块基石**是上面的命题（$M(D)\subseteq D$），前提是 $V$ 与 $K_0$ 横截。

## 放弃原因

- 对齐表只做了第一版（§1.6），`q` 与 `ρ` 那一行还没对齐；
- $c=2$ 的参数化只写了草案，没有证明纤维维数与横截条件的可实现性；
- 横截前提的必要性只在 4 个例子上核对，没有一般论证。

## 残留价值

- 一张**先前工作地图**（$c>1$ 的 6 处，含 $\mathcal D_s$、Kronecker 型、固定 $(\mathcal U,\mathcal H)$ 判据）；
- **$\omega$ 的定义问题**（两个量一般不等，附精确核对），这是 $c\ge2$ 之前必须定的；
- $c\ge2$ 方向定理的命题草稿与证明思路，以及它与 $c=1$ 论文 Theorem 3 的退化关系。

## 相关文件

- [docs/04_structure.md](../../../../docs/04_structure.md)、[docs/05_open_questions.md](../../../../docs/05_open_questions.md)
- [proof/rho1_layer/theorem.md](../../../../proof/rho1_layer/theorem.md)、[proof/layer_program](../../../../proof/layer_program)
- 本线 $c=1$：[attempts/374](../../c_stratification/attempts/374_complete_parameterization.md)、[378](../../c_stratification/attempts/378_parameterization_with_L0.md)、[390](../../c_stratification/attempts/390_hyperplane_lean.md)
- 脚本：[c391](../../../../tools/verification/c391_c2_direction_check.py)（需重写）
