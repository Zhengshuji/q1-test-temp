> **已撤回（467）**：本命题**假**——$\mathbb Q$-不可约**不蕴含**有理点 Zariski 稠密（反例 $X=V(x^2+y^2)$）。
> 正确版需假设 (D)「有理点 Zariski 稠密」，或更强地「参数层是仿射空间的非空 Zariski 开子集」。
> 见 [467](467_two_more_retractions.md)。

# 464 命题 A：固定秩层上的**泛型秩判据**（含实/有理点），以及它在我们几何里成立的理由

> 承接 463（专家建议先做命题 A）。本文件给出**带证明**的版本，并处理实点条件。

## 目标

证明：在参数空间的每个（不可约）局部层上，"$\exists$ 点使两个秩条件成立" $\iff$ "两个函数域秩条件成立"，
并解决**实/有理点**的存在性。

## 设想与理由

秩条件 $\operatorname{rank}\ge r$ 是**开**条件（某个 $r\times r$ 子式非零）。于是：

- 若某层 $X$ 上有一个 $r$-子式**不恒为零**，则 $\{x\in X:\operatorname{rank}\ge r\}$ 是**非空开集**；
- 两个这样的开集在**不可约**的 $X$ 上交仍**非空**（不可约空间里两个非空开集必相交）✓。

**这就是泛型秩判据**，它比最大子式 $\gcd$ 简单，且**不需要 leading-coefficient 引理** ✓（后者是 Paper III 为处理 $\lambda$-次数下降而需要的）。

## 做法

把两个秩条件写成子式非零，用「开集 + 不可约推出交非空」以及「Q-局部闭非空集含 Q-点」来证明。

## 进展


### 命题 A（泛型秩判据，$\mathbb Q$ 与 $\mathbb R$ 上）

> 设 $X\subseteq\mathbb A^d$ 是 $\mathbb Q$ 上的**非空局部闭**集，$F_1,F_2$ 是 $X$ 上**多项式**矩阵。
> 则
> $$\exists x\in X(\mathbb Q):\ \operatorname{rank}F_1(x)\ge r_1\ \wedge\ \operatorname{rank}F_2(x)\ge r_2
> \iff
> \operatorname{rank}_{\mathbb Q(X)}F_1\ge r_1\ \wedge\ \operatorname{rank}_{\mathbb Q(X)}F_2\ge r_2 .$$

*证明.* $(\Rightarrow)$ 显然（特化不升秩）。$(\Leftarrow)$ 每个条件给一个 $r_i$-子式 $g_i\not\equiv0$；
非空开集 $O_i=\{g_i\ne0\}\cap X$。两开集在不可约 $X$ 上交非空 ✓。**有理点**：$X$ 非空且 $\mathbb Q$-局部闭、
$g_1g_2$ 是非零多项式 ⟹ 它在 $\mathbb Q^d$ 上不恒为零 ⟹ 存在 $\mathbb Q$-点使 $g_1g_2\ne0$ ✓。$\square$

### 实点/有理点条件在我们的几何里**自动满足**

命题的证明只用了"$\mathbb Q$-局部闭的非空集含 $\mathbb Q$-点 + 非零多项式在 $\mathbb Q^d$ 上不恒零" ✓。
我们的参数空间恰是这样：

| 对象 | 是否 $\mathbb Q$-仿射/局部闭 |
|---|---|
| Grassmannian 坐标卡 | **是**（仿射空间 $\mathbb A^{(\omega-d)(k-\omega)}$，$\mathbb Q$-定义） |
| 秩层 $\{\operatorname{rank}M(q)=r\}$ | **是**（由 $\mathbb Q$-系数的子式定义） |
| 相容性 $U\subseteq W$ | **是**（线性、$\mathbb Q$-定义） |

⟹ **实/有理点不需要额外的实代数几何** ✓——这一点比专家担心的乐观，**原因是我们的参数空间是 $\mathbb Q$-仿射的**，
不是一般的实代数簇。

**反例说明为何不能一般化**：$X=\{x^2+y^2=0\}\subset\mathbb A^2$ 在 $\mathbb R$ 上不可约、
其非空开集 $\{x\ne0\}$ **没有实点** ✗。所以在**一般**实代数簇上命题 A **不成立**——只在 $\mathbb Q$-仿射情形成立 ✓。

### 对中间层的推论

$$\text{层 }\omega\text{ 在层 }X\text{ 上可行}\iff
\operatorname{rank}_{\mathbb Q(X)}\begin{bmatrix}H_0\\Z_1(X)\end{bmatrix}=\omega
\ \wedge\ \operatorname{rank}_{\mathbb Q(X)}Z_2(X)=\omega .$$

于是判定 = **在每个（卡 × 秩层 × 不可约分支）上一次函数域秩计算** ✓。

## 最终结论

1. **命题 A 成立**（在 $\mathbb Q$-仿射/局部闭的参数空间上），且**给有理点** ⟹ 实点问题解决 ✓；
2. **不能一般化**到任意实代数簇（给出 $x^2+y^2=0$ 的反例）；
3. 我们的几何（Grassmann 卡 + $\mathbb Q$-定义的秩层与相容性）**恰好落在适用范围内** ✓；
4. 复杂度：层数 = 卡数 × 秩层数 × 分支数 ⟹ 结合 463 的估计仍是 **XP**（$n^{O(\ell)}$），不是 FPT ✓。

## 放弃原因

- 没有处理**不可约分支**的 $\mathbb Q$-定义性（$\mathbb Q$ 上分支可能不单独 $\mathbb Q$-定义，需要讨论）；
- 没有把命题 A 写成完整算法（含分层与分支枚举的实现）；
- 复杂度只有粗略界（未算单层符号秩的代价）。

## 残留价值

- **命题 A 有了证明**，并且实点条件在**我们的几何**里自动满足（这条最有价值）；
- 反例划清了适用范围（避免把结论推广到一般实代数簇）；
- 中间层判定有了明确形态：每（卡×秩层×分支）一次函数域秩计算。

## 下一步

处理"不可约分支是否 $\mathbb Q$-定义"这一细节（可能需要按 $\mathbb Q$-分支而非 $\mathbb C$-分支分层），
再把整套写成可实现的算法。

## 相关文件

- [463](../../decision_algorithms/attempts/463_expert108_audit.md)（专家建议与裁决）
- [461](461_whole_chart.md)（被撤回的"整卡"）
- [452](452_E_simplified.md)（(R)(E) 判据）

## 状态

- 命题 A（$\mathbb Q$-仿射情形）：**[已证-纸面]**。
- 实点条件：**[已解决，限 $\mathbb Q$-仿射]**。
- 不可约分支的 $\mathbb Q$-定义性：**[未处理]**。
- 复杂度：**[XP 界]**。
