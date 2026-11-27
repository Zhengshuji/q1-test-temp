# 猜想 C31：$\rho\ge3$、$c=1$ 时 $(5b)$ 是"无害"的

> 2026-10-29。**猜想**，不是定理。它的价值在于：若成立，则 $c=1$、$\rho\ge3$ 的层判定塌成"类型条件 + $(5a)$"，
> 那是一个纯子空间存在问题（不需要 $\lambda$ 的论证）。

## 陈述

**猜想 C31**：设 $c=1$ 且 $\rho\ge3$。则第 $(\rho,1)$ 层可行当且仅当

$$\exists\,\mathcal V\supseteq\operatorname{row}L_0:\quad
\dim\pi(\mathcal V)=\rho,\quad \dim(\mathcal V\cap\mathcal J)=1,\quad \pi(\mathcal V A)\subseteq\pi(\mathcal V)\qquad\big((5a)\big).$$

即：**只要存在满足类型条件与 $(5a)$ 的 $\mathcal V$，就存在同时满足 $(5b)$ 的 $\mathcal V$**（可以是另一个）。

## 支持证据

| 证据 | 内容 |
|---|---|
| 固定 $(\mathcal U,\mathcal H)$ 的测量（[PROBE_31](PROBE_31.md) §2）| 约 200 例中，$\mathrm{Bad}=\mathcal A$ 仅 4 例（≈2%）⟹ $(5b)$ 泛型成立 |
| 层级别小样本扫描（[PROBE_31](PROBE_31.md) §5）| 7 个 $(\rho,c)=(3,1)$ 且 $(5a)$ 的真实实例，**7 个全部可行**，0 个不可行 |

## 反面证据（说明它为什么"不能"推广到 $\rho=2$）

**$(2,1)$、$w=0$ 的层**：类型条件与 $(5a)$ 可满足，但据（已证）定理 9.12，该层**恒不可行** ✗。
（数值复核 423/423 全部不可行。）

$$\boxed{\ \text{C31 在 }\rho=2\text{ 时是假的；}\rho\ge3\text{ 时才可能成立 —— 这正是它值得验证的原因}\ }$$

## 若 C31 成立，会得到什么

$q1$ 在 $c=1$ 部分归结为"$\exists\mathcal V$ 满足类型条件 + $(5a)$"，即
$$\exists\rho\text{-维 }U,\ \dim U_0\subseteq U,\ T(U)\subseteq U,\ \dim(B\cap U)\ge1$$
—— 这是一个**纯线性代数/子空间格**问题（不需要 $\forall\lambda$）。
它是否多项式可判是另一个独立问题，但至少**不再是投影型**。

## 如何证伪它（最直接的实验）

找一个 $(\rho,c)=(3,1)$ 的实例，使：
1. 存在满足类型条件 + $(5a)$ 的 $\mathcal V$（至少一个）；
2. **所有**这样的 $\mathcal V$ 都让 $(5b)$ 失败。

到目前为止（[scan_31_layer.py](../../proof/rho1_layer/scan_31_layer.py)、7 个实例）没有找到 ✗；
但样本极小，且构造只覆盖"$A$-不变闭包"这一子类 ✗。

## 如何证明它（若要证）

需要说明：当 $\rho\ge3$ 时，"$\mathcal V$ 让 $(5b)$ 失败"这一条件定义的子簇，**不**包含整个"类型 + $(5a)$"族
（除非该族为空）。目前的工具：$\mathrm{Bad}$ 的仿射性只在 $\rho=2$ 时成立（容器唯一），$\rho\ge3$ 时不成立 ✗。

## 诚实标注

- 本猜想**未证**，也**未被否** ✗✓；
- 支持证据来自小样本（$n\le6$、7 个实例）与固定 $(\mathcal U,\mathcal H)$ 的 200 例测量 ✗；
- 它与已知的否定结果（R7：秩型不变量不决定可行性）**不冲突** ✗：C31 讲的是"存在性"，不是"判据"。

---

## 6. 2026-10-30 更新：找到**候选反例**（但还不是反例）

放大扫描（[scan_31_refute.py](../../proof/rho1_layer/scan_31_refute.py)，$n\in\{6,7\}$、模 $\mathcal J$ 的 $A$-闭包、$\tau$ 方向 20 个）找到
**1 个实例**：$n=6$、$\dim\mathcal J=2$、$\dim\mathcal V=4$、$(\rho,c)=(3,1)$，其中

$$(5a)=\mathrm{True},\qquad (5b)=\ \textbf{False}$$

且该实例上**所有**（20 个方向的）$\tau$ 变体都让 $(5b)$ 失败 ✗。
数据：[candidate_c31_counterexample.json](../../proof/rho1_layer/candidate_c31_counterexample.json)（已独立复核上面的两个布尔值 ✓）。

**为什么它还只是"候选"** ✗：C31 的否证要求"**不存在**任何满足类型 + $(5a)$ 的 $\mathcal V$ 使 $(5b)$ 成立"，
而扫描只检查了"从该 $\mathcal V$ 出发的 20 个 $\tau$ 变体" ✗ ——
类型层 $\{(\mathcal U,\mathcal H)\}$ 是一个 Grassmannian，未被穷尽 ✗。

**要坐实它需要**：证明该实例的整个 (3,1) 型层上 $(5b)$ 恒失败 ✗（等价于"$\mathrm{Bad}$ 覆盖全族"，即专家 Q3 的问题）。
目前没有工具 ✗。

**注记**：这个候选反例**不与** §2 的"200 例中 2% 覆盖"矛盾 ✓（那是固定 $(\mathcal U,\mathcal H)$ 的统计 ✓），
也与 §5 的"7/7 可行"不矛盾 ✓（不同实例 ✓）。

### 6.1 候选反例的**加强**（2026-10-30）

在原实例上做了一次独立的**型层随机搜索**：随机取 $4$ 维 $\mathcal V\supseteq\operatorname{row}L_0$，
保留 $(
ho,c)=(3,1)$ 且 $(5a)$ 成立者，再对每个 $\mathcal V$ 抽 15 个 $	au$（给后两行加 $\mathcal J$ 元素）。

| 项 | 结果 |
|---|---|
| 有效型层样本（$(3,1)$ 且 $(5a)$）| **14 个** |
| 其中使 $(5b)$ 成立的 | **0 个** ✗ |

⟹ 候选反例被加强 ✓，但**仍不是证明** ✗（14 个样本不是穷尽 ✓）。

### 6.2 要坐实它需要的**穷尽枚举**（可行，但未做）

关键观察：$(5a)$ 只要求 $T$-不变（在商 $X=\mathbb C^n/\mathcal J$ 上），所以「型层」= $\{T$-不变的 $3$ 维 $\mathcal U\}$ × $\{$一维 $\mathcal H\subseteq\mathcal J\}$ × $\{$提升的 $\tau$ 自由度$\}$。

若 $T$ **循环**（最小多项式次数 $=d$），则
$$\{\dim 3\text{ 的 }T\text{-不变子空间}\}\ \longleftrightarrow\ \{\text{首一 }g\mid m_T,\ \deg g=3\},\qquad \mathcal U=\ker g(T),$$
**有限**且可枚举 ✓；对每个 $\mathcal U$ 再枚举 $\mathcal H$（有限 ✓）与 $\tau$（$\mathcal A$ 是仿射集，可抽样或枚举有理点 ✓）。
于是"该实例的 $(3,1)$ 层是否可行"可以**穷尽判定** ✓。

未做的原因：需要先实现商坐标下的 $T$（本项目在商算子上曾两次出错 ✗），且 $T$ 非循环时还需处理连续族 ✗。

---

## 7. 2026-10-30：**在 $\mathbb F_3$ 上 C31 被穷尽证伪**（$\mathbb C$ 上仍开放）

[enum_31_finitefield.py](../../proof/rho1_layer/enum_31_finitefield.py)：把候选反例实例的整数数据（$A$、$C$、$L_0$ 全是 $\pm1/0$）
**模 3**，然后在 $\mathbb F_3$ 上**穷尽枚举**全部 4 维子空间（RREF 唯一表示），筛出：

- $\mathcal V\supseteq\operatorname{row}L_0$；
- 类型 $(\rho,c)=(3,1)$；
- $(5a)$ 成立；

再对每个测 $(5b)$（$\mathbb F_3[\lambda]$ 上极大子式的 $\gcd$ 是否为非零常数 ⟺ 在 $\overline{\mathbb F_3}$ 上常秩 ✓）。

$$\textbf{结果：满足前三条的 }\mathcal V\ \textbf{恰有 }18\text{ 个，其中 }(5b)\text{ 成立的 }\ \textbf{0 个}$$

$$\boxed{\ \text{在 }\mathbb F_3\text{ 上，该实例的 }(3,1)\text{ 层}\textbf{不可行}；\text{C31 在此实例上被穷尽证伪}\ }$$

### 7.1 这个结论的准确边界

| 命题 | 状态 |
|---|---|
| 该实例在 $\mathbb F_3$ 上的 $(3,1)$ 层不可行 | **穷尽计算成立** ✓（18 个候选全失败）|
| 该实例在 $\mathbb C$ 上的 $(3,1)$ 层不可行 | **未证** ✗（$\mathbb C$ 上的型层比 $\mathbb F_3$-有理点大得多）|
| C31 在 $\mathbb F_3$ 上为假 | **成立** ✓（一个实例即可） |
| C31 在 $\mathbb C$ 上为假 | **未证** ✗ |

### 7.2 它说明了什么（有价值的部分）

1. **"$\mathrm{Bad}$ 覆盖整个型层"这件事在 $\rho=3$ 时确实会发生** ✓ —— 不是空想 ✗
   （此前只有 $\rho=2,w=0$ 的已证例子 ✓）；
2. 因此 C31 **不可能靠"结构原因"自动成立** ✗ —— 若它真在 $\mathbb C$ 上成立，必须有**特征 0** 的机制 ✗（$\mathbb F_3$ 上的反例说明不能是纯组合/格的原因 ✓）；
3. 这给"$(5b)$ 泛型无害"的观察（§5、§2）加了一个**反面锚点** ✓。

### 7.3 为什么 $\mathbb F_3$ 的结论不能直接搬到 $\mathbb C$

$\mathbb C$ 上的型层（固定 $(
ho,c)$ 且 $(5a)$ 成立的 $\mathcal V$ 全体）是**正维数**的 ✓，
而 $\mathbb F_3$ 上只有 18 个点 ✓。所以"$\mathbb F_3$ 上无解"**不**推出"$\mathbb C$ 上无解" ✗。
反过来，$\mathbb F_3$ 上有解会推出 $\mathbb C$ 上有解 ✓（同一个整数矩阵 ✓）——这个方向有用 ✓。

### 7.4 下一步（若要判定 $\mathbb C$ 上）

需要 $\mathbb C$ 上的**覆盖判定**（专家 Q3）：即证明/否证"$\mathrm{Bad}$ 覆盖 $(3,1)$ 型层"。
$\mathbb F_3$ 上的 18 个点可以作为一个**起点**：它们的 $\mathbb Q$-提升给出 18 个"特别"的候选 ✗，
但 $\mathbb C$ 上还有无穷多 ✗。

---

## 8. $\mathbb C$（$\mathbb Q$）侧的搜索：进展与**未解决的技术障碍**

尝试把 §7 的 $\mathbb F_3$ 穷尽做法搬到 $\mathbb Q$：$\mathbb Q$ 上不能枚举，只能**参数化**型层：

1. $T$-不变的 3 维 $\mathcal U$：用 Krylov 闭包**构造** ✓（[scan_31_param.py](../../proof/rho1_layer/scan_31_param.py) 扫到 84–101 个不同的 $\mathcal U$）；
2. $\mathcal H$：需 $\beta(h)\in\mathcal U$，$h\in\mathcal J$（$\dim\mathcal J=2$，$h$ 的选取是 1 维族 ✓ 已抽样）；
3. $\tau$（lift 自由度）：给 $\mathcal U$ 的代表元加 $\mathcal J$ 元素 ✓。

**结果**：所有尝试都没能得到一个同时满足"$\dim\mathcal V=4$、$\rho=3$、$c=1$、$(5a)$"的 $\mathcal V$ ✗ ——
即**构造本身**没跑通 ✗：在抽样到的 $T$-不变 $\mathcal U$ 上，
"$\{L_0$ 的行$,\ u_2,\ u_3\}$ 与 $\mathcal J$ 的并"秩常小于 $j+3$ ✗，说明这些 $\mathcal U$ 多半满足 $\mathcal U\cap\mathcal J\neq0$ ✗
（于是 $\mathcal V\cap\mathcal J\supseteq(\mathcal U\cap\mathcal J)+\langle h\rangle$ 维数 $\ge2$ ✗，根本不是 $(3,1)$ 型 ✗）。

**结论（诚实）**：

- $\mathbb Q/\mathbb C$ 侧的型层**没有被有效采样** ✗ —— 这需要一个正确的"型层参数化"实现 ✗，本轮**没做成** ✗；
- 因此 $\mathbb C$ 上 C31 的状态仍是**开放** ✗✓；
- 已有的两个**确定**结论（$\rho=2$ 假 ✓、$\mathbb F_3$ 假 ✓）不依赖这个失败 ✗。

## 9. C31 的最终状态（本轮收官）

| 域 / 情形 | 状态 | 依据 |
|---|---|---|
| $\rho=2$ | **假** ✓ | 定理 9.12（$(2,1),w=0$ 恒不可行）+ 423/423 复核 |
| $\mathbb F_3$（$\rho=3$，候选实例） | **假** ✓ | [enum_31_finitefield.py](../../proof/rho1_layer/enum_31_finitefield.py)：18 个型层候选，0 个满足 $(5b)$，**穷尽** |
| $\mathbb C$（$\rho=3$） | **开放** ✗✓ | 候选反例 1 个（20+14 个样本全失败）+ 型层参数化未跑通 ✗ |
| 支持侧 | 200 例 2%、层级别 7/7 | PROBE_31 |

---

## 10. A′ 尝试（商算子 + 枚举）的**技术结果**：仍未跑通（2026-10-30）

按计划做 A′：显式算商算子 $T$、用 $\ker g(T)/\operatorname{im}(T-\lambda)$ 枚举 3 维不变子空间、再重建 $\mathcal V$ 判定。

| 步骤 | 结果 |
|---|---|
| 商算子 $T$ 的矩阵（$d=4$）| 算出 ✓（[quotient_T.py](../../proof/rho1_layer/quotient_T.py)）|
| **自检**（$T(\mathcal U)\subseteq\mathcal U$ vs 直接 $(5a)$）| **297/298** ✗ —— 有 1 例不一致 ✗ ⟹ 实现**未通过**自检 |
| 特征多项式 | $\lambda^4-2\lambda^3-7\lambda^2+18\lambda-10$，有理特征值**只有** $\lambda=1$ |
| $\dim\operatorname{im}(T-1)$ | $3$ ✓ ⟹ 3 维 $T$-不变子空间在 $\mathbb Q$ 上**唯一** |
| 重建 $\mathcal V$（$=L_0$ 行 + 两个提升 + $h$）| 得到 **0 个**合法 $\mathcal V$ ✗ ⟹ 与"候选反例的 $\mathcal V$ 确实存在（$(5a)$ 真、类型 $(3,1)$）"矛盾 ✗ |

$$\boxed{\ \text{结论：商坐标实现仍有 bug（自检 297/298、重建 0/…），}A'\text{ 未跑通}\ }$$

### 10.1 为什么这仍是"诚实的状态"

- 候选反例本身**不依赖**商算子 ✓（它的两个布尔值是对 $C^n$ 里的堆叠矩阵直接算的 ✓，已独立复核 ✓）；
- $\mathbb F_3$ 的穷尽结论**不依赖**商算子 ✓（在 $\mathbb F_3$ 上直接枚举子空间 ✓）；
- 失败的是"$\mathbb Q$ 上的型层参数化"这一**工具** ✗，不是任何已记录的结论 ✓。

### 10.2 下一步（若要修）

自检的 1/298 不一致说明坐标/提升的某个细节错了 ✗。最小修法：
对**候选反例自己的 $\mathcal V$** 做端到端核对 —— 取它的 $\pi(\mathcal V)$ 坐标，验证
$\dim=3$、$T(\mathcal U)\subseteq\mathcal U$、以及 $\operatorname{im}(T-1)$ 是否等于它 ✗。
这一步能把 bug 定位到"坐标映射"还是"不变子空间的计算" ✗。

---

## 11. A′ 为什么**注定**跑不通（一个更深的发现，2026-10-30）

自检的 1/298 不一致不是实现细节，而是**概念错误** ✗：

$\pi(xA)$ 在 $X=\mathbb C^n/\mathcal J$ 上**不是良定义的单值映射** ✗ —— 因为 $A(\mathcal J)\not\subseteq\mathcal J$，
偏差恰好是 $B=\pi(\mathcal J A)$。于是：

$$\pi(\mathcal V A)\subseteq\pi(\mathcal V)\iff T(U)\subseteq U+B\quad(\text{而**不是**}T(U)\subseteq U),$$

其中 $T$ 只在商 $X/B$ 上良定义 ✓。（这一条已在 [docs/02 A.0](../../docs/02_theorems_proven.md) 里更正 ——
我此前把 $T(U)\subseteq U+B$ "更正"成 $T(U)\subseteq U$ 是**错的** ✗，现已回正 ✓。）

**后果（对 A′）**：$(5a)$ **依赖 $\mathcal V$ 的提升**，不只依赖 $U=\pi(\mathcal V)$ ✗ ⟹
"枚举 $T$-不变子空间"这个做法**没有意义** ✗ —— 不存在把 $(5a)$ 化归为 $U$ 上条件的单值映射 ✗。

**对已有结论的影响**：

| 结论 | 是否受影响 |
|---|---|
| 候选反例（$(5a)$ 真 / $(5b)$ 假）| **不受影响** ✓ —— 两个值都用 $C^n$ 上的**堆叠判据**直接算 ✓ |
| $\mathbb F_3$ 穷尽（18 候选 / 0 可行）| **不受影响** ✓ —— 用的是同一个堆叠判据 `cond_5a_orig` ✓ |
| PROBE_31 的测量 | **不受影响** ✓（同一个判据）|
| A′ 的"商算子枚举" | **作废** ✗ —— 基于错误判据 ✗ |

$$\boxed{\ \text{A′ 作废}；\ \mathbb C\ \text{侧只能靠 }(5a)\text{ 的仿射形式（} \tau\in\mathcal A\text{）直接搜索}}\ }$$
