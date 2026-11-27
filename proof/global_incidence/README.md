# 全局入射空间 $\mathcal X_{s,k,\ell}$（QA21 里程碑 1）

> **对应 docs 条目**：B.13（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

> **定位**：把 A2（固定 $S$ 的纤维）与 A3（基族选择）合成**一个**对象，使"$\exists S$"与"$\exists U$"同时被建模。
> 依据：[QA21](../../archive/expert_correspondence/QA21_2026-10-31.md) §7（里程碑 1）。
> 证明本体：[A2](../incidence_strata/README.md)、[A3](../base_family/README.md)；本文件只做**联合表述 + 维数 + 投影问题**。

## 1. 全局记号

| 记号 | 定义 | 维数 |
|---|---|---|
| $C\in\mathbb Q^{p\times n}$（行满秩）| — | — |
| $W=\ker C$ | — | $w=n-p$ |
| $\mathcal V=\ker[C;CA]$ | — | $v$ |
| $H=\ker[C;L_0]$ | — | $h$ |
| $G=\mathcal V\cap H$ | — | $b$ |
| $D=G\cap A^{-1}(H)$ | — | $\delta$ |
| $\phi:D\to H/G$，$\phi(x)=Ax+G$ | — | $\operatorname{rank}\rho_\phi$ |
| $S\subseteq D$（$\dim s$）、$Z\subseteq H$（$\dim d=w-q$）| $S=Z\cap\mathcal V$ | — |
| $T_S=(A(S)+S)/S\subseteq H/S$ | 强制方向 | $k=\dim T_S$ |
| $B_S=G/S\subseteq H/S$ | 禁止方向 | $b-s$ |
| $\ell=\operatorname{rank}(\phi|_S)$ | — | $\le k$ |
| $r=d-s$ | 剩余延拓维数 | — |
| $m=\dim(H/S)=h-s$ | 纤维的环绕空间 | — |
| $I_\lambda=\operatorname{im}P(\lambda)\cap(H/S)$ | 谱障碍 | $r_\lambda\le t=v-s$ |

## 2. 联合入射空间（精确定义）

固定 $s,k,\ell$：
$$\boxed{\ \mathcal X_{s,k,\ell}=\left\{(S,U)\ :\ \begin{array}{l}
S\in\operatorname{Gr}(s,D),\quad \dim T_S=k,\quad \operatorname{rank}(\phi|_S)=\ell,\\[2pt]
U\in\operatorname{Gr}(r,\,H/S),\quad T_S\subseteq U,\quad U\cap B_S=0,\\[2pt]
U\cap I_\lambda=0\quad\forall\lambda\in\mathbb C
\end{array}\right\}\ }$$

**关键**（QA21 §7 的更正）：**必须**含 $U\cap B_S=0$，否则 $Z=S\oplus U$ 的 $Z\cap\mathcal V$ 未必等于 $S$
（$B_S=G/S$ 正是"$U$ 里混进 $G$ 的部分"）。

**分层**：
- **代数层** $\mathcal X^{\mathrm{alg}}_{s,k,\ell}$：只保留前四行（去掉谱条件）；
- **谱层** $\mathcal X^{\mathrm{spec}}_{s,k,\ell}$：全条件。

于是
$$\mathrm{DEC}(q)\ \text{可行}\iff \exists(s,k,\ell):\ \mathcal X^{\mathrm{spec}}_{s,k,\ell}\ne\varnothing .$$

## 3. 代数层的纤维维数

**断言**（QA21 §7 给的期望值）：固定 $S$ 时，代数纤维
$$\mathcal F_S=\{U:\ T_S\subseteq U\subseteq H/S,\ \dim U=r,\ U\cap B_S=0\}$$
在非空时维数为
$$\boxed{\ (r-k)\,(m-r)\ }$$
*推导*：先商掉 $T_S$：$\widetilde U=U/T_S\subseteq N:=(H/S)/T_S$（$\dim N=m-k$），$\dim\widetilde U=r-k$，且须避开
$B'=B_S/(B_S\cap T_S)$（$\dim B'=b-s-(k-\ell)$）。纤维 $\cong$ $\operatorname{Gr}(r-k,\,m-k)$ 中避开 $B'$ 的**开子集**，故维数
$$(r-k)\big((m-k)-(r-k)\big)=(r-k)(m-r)\ ✓$$

**非空条件（按 QA22 §1.1 的正确顺序）**：

**第一步：$\ell=k$ 是必要条件**（与维数无关）。因 $T_S\subseteq U$ 且 $U\cap B_S=0$ ⟹
$$T_S\cap B_S=0\ \Longrightarrow\ \ell=k\quad(\text{由 A3 恒等式 }\dim(T_S\cap B_S)=k-\ell).$$
所以 **$\ell<k$ 时纤维为空，无论余量多大**。

**第二步：在 $\ell=k$ 的可容许层上**，非空性才是"余量够不够"：
$$r-k\le\dim N-\dim\overline{B}_S\iff r\le h-b+\ell-k\iff\boxed{r\le h-b}\ (\ell=k\text{ 时}).$$

> **排序很重要**（专家更正）：先证 $\ell=k$，再谈维数余量；否则会给人"维数不等式可以补偿
> $T_S\cap B_S\ne0$"的错觉。上一版把两步写混了，已更正。

> **机器核对（`c277`）**：三个实例上图表维数 $=(r-k)(m-r)$ ✓；并记下一个**易错点**——
> 图表维数**不是** $\dim(N/B')$，后者只是非空性所需的余量。

## 4. 投影与核心问题

$$\pi_S:\mathcal X_{s,k,\ell}\longrightarrow\mathcal B_{s,k,\ell},\qquad (S,U)\mapsto S .$$

**核心问题**（QA21）：
$$\boxed{\ \text{对哪些 }S\in\mathcal B_{s,k,\ell}\ \text{有 }\pi_S^{-1}(S)\ne\varnothing\ ?\ }$$

**要回答的量**：
1. $\pi_S$ 是否**支配**（dominant）？若支配，一般 $S$ 有可行延拓；
2. 一般纤维的维数（预期 $(r-k)(m-r)$，待核）；
3. 哪些层的纤维**恒空**；
4. 哪些层含**谱好点**；
5. **实点**：$\mathcal X_{s,k,\ell}(\mathbb R)\ne\varnothing$？（G4，见 A2 §18）

> **警告**（QA21 §2.1）：支配性**不**推出每个实基点都有实纤维；实点问题须单独处理。

## 5. 与 A2 / A3 的依赖图

```
        A3: S ⊆ D, φ, (k,ℓ) 分层, dim(T_S∩B_S)=k−ℓ  [§13, §18, A3id.lean]
                 │
                 ├── 剪枝 k ≤ r, ℓ = k                    [A3 §18]
                 │
                 ▼
        A2: 固定 S 的纤维 F_S, 障碍 I_λ, 判据 Gr∩L⊄{q0=0}   [A2 §1–§11]
                 │        │
                 │        └── G3: span(Gr∩L)=L ?           [A2 §15–16, 待 §19]
                 │        └── G4: 实点                      [待 §18]
                 ▼
        本文件: X_{s,k,ℓ}, π_S, 纤维维数 (r−k)(m−r)        ← 现在的里程碑 1
                 │
                 ▼
        除子几何: ℙ¹ 无补空间 / 𝔸¹ 常值判据                  [A2 §17, 待提升为命题]
```

## 6. 假设台账（QA21 §3.2 要求）

| 项 | 域 | 参数范围 | 秩假设 | 几何 | 实/复 | 量词 | 等级 |
|---|---|---|---|---|---|---|---|
| $\mathcal X_{s,k,\ell}$ 定义 | 任意 | — | — | 代数簇 | 复（实另论）| — | 定义 |
| 纤维维数 $(r-k)(m-r)$ | $\mathbb C$ | — | 商空间上常数秩 | 开子集 | 复 | 一般 $U$ | [纸面]，待 `c277` 核 |
| 非空条件 $r\le h-b+\ell-k$ | $\mathbb C$ | — | — | — | 复 | 存在 | [纸面] |
| $\pi_S$ 的支配性 | $\mathbb C$ | — | — | — | 复 | 一般 | **开放** |
| 实点 | $\mathbb R$ | — | — | — | 实 | 存在 | **开放（G4）** |

## 7. 待解决问题清单（本阶段的产出目标）

| # | 问题 | 依赖 |
|---|---|---|
| J1 | 纤维维数 $(r-k)(m-r)$ 的机器核对（R17、第二、第三实例 + 一个 $r=2$ 例）| `c277` |
| J2 | 非空条件 $r\le h-b+\ell-k$ 的核对 | `c277` |
| J3 | $\pi_S$ 在三个实例上是否支配 | `c277` + 符号计算 |
| J4 | 退化截面（G3）对 $\mathcal X$ 的影响 | A2 §19 |
| J5 | 实点（G4）| A2 §18 |
