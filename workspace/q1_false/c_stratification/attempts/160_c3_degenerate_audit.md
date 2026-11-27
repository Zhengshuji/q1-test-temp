# $c=3$ 分量界的退化情形审计：每块“空或不可约”

> 2026-11-08。159 的分量界依赖“每个 Jordan 型块不可约”；本文件逐块核对**退化情形**
> （链不可提升、特征空间为零、重根、纤维为空/点），确认它们只让块变空，不增加分量数。
> 状态：**M2（审计）**；159 的界不需要分段。

## 目标

对 $c=3$ 的每个不变层块，检查其参数空间在退化情形下是否仍为“空或不可约”，从而 159 的
$$\binom{s}{3}+\binom{s}{2}+2s^2+4s+3$$
无需分段修正。

## 设想与理由

每个块形如
$$\text{底（射影线性子空间）}\ \times\ \text{纤维（仿射空间或空）},$$
底由**线性**条件（$A\ell\subseteq\ell$、$\ell\subseteq\operatorname{im}(A-\lambda I)$ 等）给出，
纤维由**线性**方程（$(A-\lambda I)u\in\ell$ 等）给出；故底是射影线性子空间（不可约或空），
纤维是仿射空间（不可约或空）。乘积不可约或空。退化的唯一效果是其中一项为空。

## 做法：逐块核对

### $t=3$（$A(V)\subseteq V$）

| 块 | 底 | 纤维 | 退化情形 | 结论 |
|---|---|---|---|---|
| 三个不同特征值 | $\mathbb P(E_\lambda)\times\mathbb P(E_\mu)\times\mathbb P(E_\nu)/S_3$ | 点 | 任一 $E_\star\cap K_0=0$ → 空 | 空或不可约 |
| $1+1+1$ | $\operatorname{Gr}(3,E_\lambda\cap K_0)$ | 点 | $\dim<3$ → 空 | 空或不可约 |
| $1+1$ 与 $\mu$ | $\operatorname{Gr}(2,E_\lambda)\times\mathbb P(E_\mu)$ | 点 | 任一空 → 空 | 空或不可约 |
| $2+1$ | $\{\ell\subseteq E_\lambda\cap K_0:\ \ell\subseteq\operatorname{im}(A-\lambda I)\}$ | $\{u:(A-\lambda I)u\in\ell\setminus0\}/E_\lambda$ | 链不可提升 → 底空；$E_\lambda\cap K_0=0$ → 空；纤维为空 → 空 | 空或不可约 |
| $2$ 与 $\mu$ | 同 $2+1$ 的底 $\times\mathbb P(E_\mu)$ | 同 $2+1$ | 任一空 → 空 | 空或不可约 |
| $3$ | $\{\ell_2\subseteq E_\lambda\cap K_0:\ \ell_2\subseteq\operatorname{im}(A-\lambda I),\ \ell_1\subseteq\operatorname{im}(A-\lambda I)^2\}$ | 仿射（2 步提升） | 任一步不可提升 → 底空；纤维空 → 空 | 空或不可约 |

**重根**：块按“不同特征值”定义，$\lambda\ne\mu$ 强制；同一 $\lambda$ 的重数只体现在分拆
$1+1+1$/$2+1$/$3$ 内，不产生跨块重叠。

### $t=2$（$A(W)\subseteq W$）

| 块 | 底 | 纤维 | 退化 | 结论 |
|---|---|---|---|---|
| 不同特征值 | $\mathbb P(E_\lambda)\times\mathbb P(E_\mu)/S_2$ | 点 | 空 | 空或不可约 |
| 标量 | $\operatorname{Gr}(2,E_\lambda\cap K_0)$ | 点 | 空 | 空或不可约 |
| Jordan | $\{\ell\subseteq E_\lambda\cap K_0:\ \ell\subseteq\operatorname{im}(A-\lambda I)\}$ | 仿射，$\dim E_\lambda-1$ | 链不可提升 → 底空；纤维空 → 空 | 空或不可约 |

### $t=1$（$A(L)\subseteq L$）

$L$ 是特征线；底 $\bigcup_\lambda\mathbb P(E_\lambda\cap K_0)$，每个 $\lambda$ 一个射影子空间（不可约），
不同 $\lambda$ 不交。退化：$E_\lambda\cap K_0=0$ → 该块空。结论：$\le s$ 个块。

### 开层

$t=0$、$t=1$ 的 $A(L)\not\subseteq L$、$S_{2,3}$：开子集于不可约 Grassmannian/射影空间，
空或不可约；各 $\le1$。

## 进展

* 每个块的“空或不可约”逐项核对；退化（链不可提升、特征空间为零、纤维为空/点）只让块变空；
* 重根不产生跨块重叠（块按不同特征值定义）；
* 159 的界无需分段；退化只影响“哪些块非空”，不影响力上界。

## 最终结论

* 159 的 $\binom{s}{3}+\binom{s}{2}+2s^2+4s+3$ 在退化情形下仍成立；
* 每块是“射影线性子空间 × 仿射空间”（空或不可约），故分量数不超过块数；
* 这是 159 的配套审计（M2）。

## 放弃原因

* 未给“精确分量数/下界”（需要每块非空性）；
* 未处理 $c\ge4$ 的中间 exact-rank 层（$t<u<2t$，可能可约）。

## 残留价值

* 使 159 的界在退化情形下也成立；
* 给出“底线性 + 纤维仿射 ⟹ 空或不可约”的可复用论证。

## 相关文件

* [attempts/159](159_c3_component_bound_corrected.md)（界）
* [attempts/158](158_c3_s23_audit.md)（开层）
* [attempts/147](147_c2_component_bound.md)（$c=2$）

## 状态

* 退化审计：**[已证-纸面，M2]**。
* 精确分量数/下界/实点：**[未做]**。
