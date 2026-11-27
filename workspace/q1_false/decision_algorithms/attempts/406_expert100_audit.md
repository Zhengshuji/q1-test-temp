# 368 专家 100 号审计：$k$ 块合取被证明；"只给开条件"被撤回

> 送审件 [100](../../../for_expert/archive/100_architecture_limits.md)（已归档），
> 答复 [100-reply](../../../for_expert/archive/100_architecture_limits-reply.md)。
> **总评（他的话）**：两条贡献（纤维级刚性、锚定字面门）成立；**$k$ 块合取可以从猜想升为定理**；
> 但**"本架构只能表达开条件 ⟹ 无硬度"这个中心否定结论不成立**，
> 三处逻辑缺口：纤维级开性 $\ne$ 全局开性；构造性 $\ne$ 可解；模型里**本来就有**行列式等式。

## 目标

1. 记录三处更正与一条新定理（$k$ 块合取）。
2. 落实：361（改称"纤维级刚性"）、366（关块失败的正确解释 + 布尔性缺口）、367（撤回"只给开条件"）。
3. 记录他给的下一步（核等式引理、布尔性/析取、存在性实例可行性）。

## 设想与理由

审计型回复：只记明确裁决。这次他给了**一条完整证明**（$k$ 块），并撤回了我一个**过强的否定结论**。

## 做法：逐条裁决

### 1. 定理 A 的正确形态：**纤维级关系刚性**（不是"所有关系都不可能"）

我的表述"关系型 gadget 任意次数都不可能"**过强**。他的反例逻辑很直接：

> 取 $S=[H;H_A]$。可行点上 $\operatorname{rank}H_A\subseteq\operatorname{row}H$ 且 $\operatorname{rank}H=\omega$，
> 故 $\operatorname{rank}S=\omega$，于是**所有 $(\omega+1)$-子式为零**——这是**自由参数的多项式关系**，
> 且未必在整个参数空间上恒零。

所以架构**确实**表达多项式关系。定理 A 真正证明的是：

> **纤维级刚性**：固定 $W$ 后，谱条件不能在非空纤维 $M_W$ 内部再加任何多项式关系——
> 每个可行点都满足的关系，已经是整个线性空间 $M_W$ 上的恒等式。
> 于是 $\overline{\mathcal F_\omega}=\overline{\bigcup_{W\in\mathcal W^{\rm act}_\omega}M_W}$：
> **谱条件只能"挑哪些纤维是活的"，不能在活的纤维内部再切一刀。**

**建议的措辞**（他的原话）：
> Any nonlinear algebraic restrictions on the full feasible set must therefore arise from the geometry of the
> family of active row spaces $W$, rather than from further algebraic cutting inside an individual active fibre.

**还有一条我漏掉的**：定理 A 要说明**域**——$\mathbb C$ 上非空 Zariski 开集自动稠密；$\mathbb R$ 上需要非空；
$\mathbb Q$ 上还需要"存在有理可行点"（非空复开集**不**保证有理点）。

### 2. 新定理：**核等式引理** + **任意 $k$ 块合取**

> **核等式引理.** 对任何可行的压缩对：$(5b)$ 在 $\lambda=0$ 给 $\operatorname{rank}H_A=\operatorname{rank}H$；
> 与 $(5a)$ 合起来得 $\operatorname{row}H_A=\operatorname{row}H$，从而 $\ker H=\ker H_A$。
> 于是 $H_{\bullet i}=0\iff(H_A)_{\bullet i}=0$，而且**任意列子集的秩也相等**：
> $\operatorname{rank}H_{[:,J]}=\operatorname{rank}(H_A)_{[:,J]}$。

**合取的 soundness（任意 $k$、任意 $m$）**：块构造里 $t_i=0\Rightarrow(H_A)_{\bullet i}=0$，
而锚定保证 $H_{\bullet i}=(1;u_i)\ne0$，与核等式矛盾 ⟹ 不可行 ✓。

**合取的 completeness（$m=k$）**：取
$$H=\begin{pmatrix}\mathbf 1^{\mathsf T}\\ I_k\end{pmatrix},\qquad
H_A=\begin{pmatrix}0\\ D\end{pmatrix},\quad D=\operatorname{diag}(d_1,\dots,d_k)\ (\text{互异非零}).$$
则 $P(\lambda)=\begin{pmatrix}\lambda\mathbf 1^{\mathsf T}\\ \lambda I-D\end{pmatrix}$ 恒满列秩：
$\lambda\notin\{d_i\}$ 时 $\lambda I-D$ 可逆；$\lambda=d_j$ 时 $\ker(\lambda I-D)=\operatorname{span}\{e_j\}$，
而顶行 $\lambda\mathbf 1^{\mathsf T}e_j=d_j\ne0$ 把它消掉 ✓。

> **定理（任意 $k$ 块合取门）.** 锚定 $k$ 块直和、$m=k$ 时：
> $$\text{可行}\iff\prod_{i=1}^k t_i\ne0 .$$

**这比我的猜想强**：他用核等式（不是"$\lambda$ 两端的秩比较"）一步解决，且对任意 $m$ 给出 soundness。

### 3. 撤回"只给开条件 ⟹ 无硬度"

| 我的说法 | 他的裁决 |
|---|---|
| 可行集在每个 $M_W$ 里开 ⟹ 全局开 | **推理无效**。$M_W$ 随 $W$ 变；**线性空间之并可以非线性**（rank-1 矩阵簇就是例子） |
| 完整可行轨迹可写成 | **有显式描述**：$\mathcal F_\omega=\{\operatorname{rank}H=\omega,\ \operatorname{rank}[H;H_A]\le\omega\}\cap\mathcal O_\omega$——第一项局部闭、第二项**行列式闭**、第三项开 |
| 构造性 ⟹ 无硬度 | **假**。SAT 本身就是一个存在多项式系统（$x_i(1-x_i)=0$ + 子句方程），其解集可构造，而 SAT 是 NP-完全的 |
| 模型里没有等式 | **假**。$(5a)$ 就是行列式等式；$\operatorname{rank}H=\omega$ 是局部闭；$\dim K_0$、$\dim(AK_0)$ 是实例侧的秩条件 |

他的总结：**"$x\ne0$ 与 $1-x\ne0$ 的交非空"不代表"对每个固定输入 $x\in\{0,1\}$ 都成立"**——
必须区分四个层次：自由变量 / 固定输入 / 存在见证 / 布尔源变量。

### 4. 我的两处小错，他也指了

- **关块失败**的正确解释是**秩零见证**（$R=0\Rightarrow H=0,H_A=0\Rightarrow\omega=0$，两条件平凡成立），
  而不是我说的"任何非零单列铅笔都自动可行"；
- **否定**只在**布尔输入**下成立；字面门**不是**布尔性门，它不强制 $x(1-x)=0$。

## 进展

- 三处更正全部落实（361/366/367 已改）；
- $k$ 块合取从猜想升为**定理**（核等式引理 + 显式构造）；
- **核等式引理**（$\ker H=\ker H_A$ 及其全部推论）登记为可复用引理。

## 最终结论

1. **保留**：纤维级刚性（renamed）、字面门、否定（布尔输入下）、两块的证明、**任意 $k$ 块的合取定理**；
2. **撤回**："关系型 gadget 任意次数都不可能"（改为纤维级刚性）、"只给开条件 ⟹ 无硬度"（整个论点撤回）、
   "模型没有等式"（假）；
3. **下一步（他排的序）**：① 形式化核等式引理；② 把合取升级为 $k$ 块定理（已完成）；③ 重写定理 A；
   ④ **研究布尔性与析取**——目标是"一个双分支块，可行轨迹恰好两个分支且无秩零逃逸"；
   ⑤ 按"存在性实例可行性"重估硬度（先分清哪些是固定输入、哪些是存在见证）。

## 放弃原因

- 析取没有进展（他的判断：我的两次失败不是不可能性证明）；
- 布尔性没有解决（字面门只测非零，不强制 $x(1-x)=0$）；
- 没有开始他建议的"双分支块"设计。

## 残留价值

- **一条新定理**（任意 $k$ 块合取），含 soundness（任意 $m$）与 completeness（$m=k$）；
- **核等式引理**：$\ker H=\ker H_A$、逐列零型一致、任意列子集秩相等——**这是设计/排除门的有力工具**；
- 三处更正的完整记录，尤其是"线性空间之并可以非线性"这个几何要点。

## 相关文件

- [100](../../../for_expert/archive/100_architecture_limits.md)、[100-reply](../../../for_expert/archive/100_architecture_limits-reply.md)
- [361](../../c_stratification/attempts/399_relation_gadgets_impossible.md)（已改称纤维级刚性）
- [366](../../../q1_true/multiplication_gate/attempts/404_or_not.md)（关块失败的解释已更正；布尔性缺口已记）
- [367](../../c_stratification/attempts/405_layer_separation_and_equations.md)（"只给开条件"已撤回）
- [365](../../../q1_true/multiplication_gate/attempts/403_k_block_soundness.md)（$k$ 块：猜想 → 定理）

## 状态

- $k$ 块合取定理：**[已证-纸面]**（专家给证）。
- 核等式引理：**[已证-纸面]**。
- 纤维级刚性：**[已证-纸面]**（含域限定）。
- "只给开条件 ⟹ 无硬度"：**[已撤回]**。
