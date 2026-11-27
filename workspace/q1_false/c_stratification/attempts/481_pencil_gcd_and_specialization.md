> **更正（483；专家审阅）**：引理 B 的**第二部分**需补一个条件——要断言"公共因子在特化后仍存在"，
> 只排除 $\operatorname{lc}(\tilde g)=0$ **不够**；还必须用同一个非零多项式 $D$ **清除 $g$ 与所有 $h_J$ 的系数分母**。
> 正确开集为 $V_-=\{p\in\mathcal B_R:\ D(p)\ne0,\ \operatorname{lc}(\tilde g)(p)\ne0\}$，
> 其中 $\tilde g,\tilde h_J\in R[\lambda]$ 满足 $f_J=\tilde g\tilde h_J$ 于 $R_D[\lambda]$。
> **第一部分（Bézout 清分母）保持不变** ✓。

# 481 阶段 3C：铅笔 $P(\lambda;X,Y)$ 的 **函数域 gcd** 与 **leading-coefficient** 引理（仅泛型，不含实点）

> 承接 [480](480_grassmann_parameterization_of_FW.md)（3A/3B）。本文件只做 **(E)** 的代数侧：
> 泛型开集引理 + leading-coefficient 引理；**实点与特殊点明确留给 3D**（不越界）。

## 目标

1. 把 $(E)$ 写成 $P(\lambda;X,Y)$ 的最大子式 gcd 条件；
2. 证明**泛型**引理：函数域 gcd 为常数 $\iff$ 存在非空 Zariski 开集使**每点**满足谱条件；
3. 证明 leading-coefficient 引理：在 $(R)$-轨迹上最大 $\lambda$-次数**恰为 $\omega$**，故次数不会整体退化。

## 做法

把 $(E)$ 写成 $P(\lambda;X,Y)$ 全部 $\omega\times\omega$ 子式的 gcd 条件；再对 (R)-轨迹上的不可约分支，用清分母的 Bézout 恒等式（正向）与公共因子的首项系数（反向）分别处理，得到开集级结论。

## 进展

（见下文引理 A、引理 B 与三层表格。）

## 设想与理由

$P(\lambda;X,Y)=\lambda X_1(X,Y)-X_2(X,Y)$，$(E)\iff\operatorname{rank}P(\lambda;X,Y)=\omega\ \forall\lambda$
$\iff$ 全部 $\omega\times\omega$ 子式 $f_J$ 无公共复根 $\iff\deg_\lambda\gcd_J f_J=0$ ✓（单点判据，精确）。

难点在"**一次函数域计算**能否决定整个参数层"——这正是 471 里我错判的地方（当时以为线性原像保稠密）。

## 做法：两个引理

设 $\mathcal B$ 是**固定的不可约参数分支**（先按 $\operatorname{rank}D_I$ 分层、再取不可约分支，[472](../../decision_algorithms/attempts/472_linear_preimage_fails.md)），
$R=\mathbb Q[\mathcal B]$、$K=\operatorname{Frac}R$；(R) 的轨迹 $\mathcal B_R=\{\operatorname{rank}X_1=\omega\}\cap\mathcal B$ 是**非空开集** ✓。

**引理 A（leading coefficient）.** 在 $\mathcal B_R$ 上，$\max_J\deg_\lambda f_J=\omega$，且取到次数 $\omega$ 的那个 $f_J$ 的
$\lambda^\omega$ 系数是 $X_1$ 的一个 $\omega\times\omega$ 子式，**非零** ✓。

*证明.* $P$ 的 $\lambda^\omega$-系数恰为 $X_1$ 的对应子式；$\operatorname{rank}X_1=\omega$ ⟹ 某子式非零 ✓；而 $\deg f_J\le\omega$ 恒成立 ✓。$\square$

**引理 B（泛型谱判据）.** 设 $g=\gcd_J f_J\in K[\lambda]$。则
1. 若 $\deg g=0$（即 $g$ 是单位）：存在**非空 Zariski 开集** $V\subseteq\mathcal B_R$，使**每一点** $p\in V$ 满足谱条件；
2. 若 $\deg g>0$：存在非空开集 $W\subseteq\mathcal B_R$，使**每一点** $p\in W$ 都**不满足**谱条件。

*证明.*
(1) $g=1$ ⟹ 存在 Bézout 恒等式 $\sum_J a_J f_J=1$，$a_J\in K[\lambda]$。**清分母**得
$$D=\sum_J A_J\,f_J,\qquad A_J\in R[\lambda],\ D\in R\setminus\{0\}.$$
对 $p$ 使 $D(p)\ne0$：$\sum_J A_J(p)f_J(p)=D(p)\ne0$ ⟹ 特化后的 $f_J(p)$ **生成单位理想** ⟹ 无公共根 ⟹ 谱条件成立 ✓。
取 $V=\{D\ne0\}\cap\mathcal B_R$：非空开 ✓，且**每点**成立 ✓（这是"整卡"结论，不是泛型点结论——分歧就在清分母后保留 $D\ne0$）。
(2) $\deg g>0$ ⟹ $f_J=g h_J$。取 $p$ 使 $\operatorname{lc}(g)(p)\ne0$（非空开集）：
则 $\deg g(p)=\deg g>0$ ⟹ 特化后的公共因子非常数 ⟹ 有复根 ⟹ 谱条件失败 ✓。取 $W=\{\operatorname{lc}(g)\ne0\}\cap\mathcal B_R$ ✓。$\square$

## 结果与边界（必须分清的三层）

| 层次 | 结论 |
|---|---|
| **单点** | $(E)\iff\deg_\lambda\gcd_J f_J(p)=0$（精确判据）✓ |
| **一个不可约分支上的开集** | 引理 B：函数域 gcd 为常数 $\iff$ 存在**非空开集**内每点满足；常数 ⟹ 该开集上**全部**成立 ✓ |
| **整个分支（含特殊点）** | **未解决**：开集可能不含实点，特殊点也可能单独可行 ✗ |

$$\boxed{\text{引理 B 是"开集级"结论；从开集到"整个分支含实点"仍需 3D}}$$

## 最终结论

1. **引理 A**（leading coefficient）成立：$(R)$-轨迹上最大 $\lambda$-次数恰为 $\omega$ ⟹ 次数不会整体退化 ✓
   （这正是 Paper III 的 right-of-way，但**只在 $(R)$-轨迹上**成立，不能无条件引用）；
2. **引理 B**（泛型谱判据）成立，且方向是"开集级"：常数 $\Rightarrow$ 开集上处处可行；非常数 $\Rightarrow$ 开集上处处不可行 ✓；
   ——这比"泛型点"强，比"整个分支"弱 ✓；
3. **与 471 的区别**：471 错在"线性原像保稠密"；本文件的结论**不依赖**稠密性，只依赖清分母后保留的开集 ✓；
4. **明确未做（3D）**：开集是否有实点；特殊（降秩）点上是否另有可行点。

## 放弃原因

- 没有判断 $V$（或 $W$）是否含实点（3D）；
- 没有处理"开集为空但分支非空"的退化情形（需 $\mathcal B_R$ 非空，已假设）；
- 没有把 $a_J$ 的次数与位长估出来（复杂度，属 3E）。

## 残留价值

- **引理 A + 引理 B**：把 Paper III 的谱判定迁移到中间层的**开集级**，并说清边界；
- **清分母保留开集**这一技术点写明白了（这是 471 出错的真正位置）；
- 三层表格（单点 / 开集 / 整分支）可直接作为后续 3D 的出发点。

## 下一步（3D）

对 $V=\{D\ne0\}$：判断它是否含实点（或 $\mathbb Q$-点）。这里**不能**假设稠密性（[472](../../decision_algorithms/attempts/472_linear_preimage_fails.md)），
必须用具体结构：$D$ 是清分母得到的行列式型多项式，其零点集是 $\mathcal B$ 里的一个除子；
$V$ 非空开 ⟹ 在 $\mathcal B$ 上稠密，但实点是否存在取决于 $\mathcal B(\mathbb R)$ 的形状。

## 相关文件

- [480](480_grassmann_parameterization_of_FW.md)（3A/3B）
- [479](479_fixed_W_with_row_budget.md)（(FW)）
- [472](../../decision_algorithms/attempts/472_linear_preimage_fails.md)（线性原像反例，3D 的警示）
- [478](../../decision_algorithms/attempts/478_E_lambda_coupled.md)（(E) 不能弱化）

## 状态

- 引理 A（leading coefficient）：**[已证-纸面]**。
- 引理 B（泛型谱判据，开集级）：**[已证-纸面]**。
- 实点/特殊点（3D）：**[未做]**。
- 复杂度（3E）：**[未做]**。
