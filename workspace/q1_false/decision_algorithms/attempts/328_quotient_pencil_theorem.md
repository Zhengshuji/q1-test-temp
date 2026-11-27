# 328 商铅笔定理（专家 95 号的 Result A）与三处更正

> 送审件 [95](../../../for_expert/archive/95_hyperplane_experiments_and_conjectures.md)（已归档），
> 答复 [95-reply](../../../for_expert/archive/95_hyperplane_experiments_and_conjectures-reply.md)。
> 95 号把 **H3（商铅笔）** 列为第一优先，并给了三条更正。本文件把 Result A 写成定理，并改正三处。

## 目标

1. 把"商掉强制核方向"写成**定理**（95 号的 Result A），含可验证的尺寸条件。
2. 记录 95 号的三处更正：$\det M$ 的尺寸前提、H1 的降级（度数会跳）、H2 的重述。
3. 明确它对 §325 的 S3 意味着什么（固定参数 ⟺ 可观测性；参数化版本仍是 generic 问题）。

## 设想与理由

95 号 §1 指出：$M(\lambda)=Q(\lambda I-A)N$ 有**参数无关的右核方向** $c_v$（因为 $Qv=QAv=0$），
所以"秩问题应当在商掉该方向之后做"。他要求把它写成：

$$M(\lambda)=\bigl[\widetilde M(\lambda)\ \ 0\bigr],\qquad
\widetilde M(\lambda)=\lambda X-G,\quad X=Q\hat N,\ G=Q A\hat N,$$

其中 $\hat N$ 是 $N$ 的前 $k-1$ 列（基取成最后一列是 $v$）。

## 做法

### 1. 商铅笔定理

> **定理（商铅笔）.** 设 $v\in K_0$ 非特征（$\dim\operatorname{span}(v,Av)=2$），$Q$ 的行张成 $U^\perp$
> （$U=\operatorname{span}(v,Av)$），$\hat N$ 为 $N$ 去掉 $v$ 那一列后的 $n\times(k-1)$ 矩阵。
>
> **前提（97 号审计补充）**：本定理适用于**行空间取满**的情形 $V=\operatorname{row}L=U^\perp$
> （等价于 $q=n-2$）。若 $V\subsetneq U^\perp$，则 $Q$ 只是**辅助铅笔**，$\operatorname{rank}(QN)=k-1$
> 与"$C$ 的行在 $V$ 里"都不再自动成立，结论不能直接搬到观测器铅笔上。则
> 1. $M(\lambda)=Q(\lambda I-A)N$ 的最后一列恒为零，故 $M=[\widetilde M\ 0]$，$\widetilde M=\lambda X-G$
>    且 $X=Q\hat N$、$G=QA\hat N$；
> 2. 若 $\operatorname{rank}X=k-1$（列满秩），则对一切 $\lambda$
>    $$\operatorname{rank}M(\lambda)<k-1\iff\operatorname{rank}\widetilde M(\lambda)<k-1 ;$$
> 3. 于是"坏"$\iff\exists\lambda:\operatorname{rank}\widetilde M(\lambda)<k-1$，
>    而"$\widetilde M$ 处处满列秩"$\iff$ 归一化后 $\operatorname{rank}[\lambda I-G_1;G_2]=k-1\ \forall\lambda$
>    $\iff$ **$(G_1,G_2)$ 可观测**（Hautus）。

*证明.* (1) 最后一列是 $Q(\lambda I-A)v=\lambda Qv-QAv=0$ ✓。(2) 去掉一列零不改变秩，
但两边的"阈值"不同：$\operatorname{rank}M<k-1$ 与 $\operatorname{rank}\widetilde M<k-1$ 都是"某个
$(k-1)$-子式为零"（$\widetilde M$ 有 $k-1$ 列、$X$ 列满秩保证 $k-1$ 阶子式存在）✓。
(3) $X$ 列满秩 ⟹ 行变换可取 $X=[I_{k-1};0]$，此时 $\widetilde M$ 在 $\lambda$ 处降秩 $\iff$
$[\lambda I-G_1;G_2]$ 降秩；Hautus/PBH 给最后一句。$\square$

**尺寸前提（95 号 §1.1 的更正）**：$M$ 是 $(n-2)\times k$，**未必方**。
所以不能写 $\det M\equiv0$，正确的陈述是
$$\operatorname{rank}M(\lambda)\le k-1\quad\forall\lambda$$
（$k\times k$ 子式在存在时恒零）。$\det M\equiv0$ 只在 $n-2=k$（如 E2 的 $3=3$）时有意义。
**326/327 里"$\det M\equiv0$"的写法已按此改正。**

**补充（329）：商铅笔还要再削 $p$ 行。** $U\subseteq K_0\subseteq\ker C$，故 $C$ 的每一行都落在 $U^\perp$ 里，
且它们消去 $\hat N$ 与 $A\hat N$，于是
$$\operatorname{rank}\widetilde M(\lambda)\le n-2-p\qquad\forall\lambda .$$
若 $n-2-p<k-1$（等价于 $\operatorname{rank}[C;CA]=p$），则该层**自动不可行**。
见 [329](../../c_stratification/attempts/329_forced_relations_quotient_pencil.md)。

### 2. 与 S3 的关系（95 号的复杂性三分）

95 号 §9 要求区分三件事，这个区分必须写进文档：

| 层次 | 内容 | 现状 |
|---|---|---|
| **固定参数** | 给定有理 $v$，判该铅笔是否谱可行 | **可判**：等价于 $(G_1,G_2)$ 可观测（Hautus），多项式时间 |
| **generic 分量** | 判分量的 generic 点是否谱可行 | 即 §325 的 **S3**（参数化版本），**未解决** |
| **原有有理可行性** | $\exists$ 有理行选择满足全部条件 | 还多一层有理点问题，**更远** |

即使 H3 完整成立，也**不**解决原有有理 DEC——这句话要写死。

### 3. 三处更正（95 号）

**(a) $\det M$ 的尺寸前提** —— 见上，已改成秩形式。

**(b) H1 降级：度数会跳。** 95 号给了显式反例
$$B_t(\lambda)=\begin{bmatrix}\lambda&0\\0&\lambda\\0&t\end{bmatrix},\qquad
\{m_I\}=\{\lambda^2,\ \lambda t,\ 0\},\qquad
\gcd=\begin{cases}\lambda,&t\ne0\\ \lambda^2,&t=0\end{cases}$$
度数从 1 跳到 2，**而且它同样有固定核方向**（拼一列零即得）。
所以"固定核方向 ⟹ 全分量度数恒定"是**错的**；本项目的 H1 应拆成：
- **H1a（generic 恒定）**：在每个不可约分量上，$\deg\gcd$ 在某个稠密开集上恒定。
  这条其实**自动**（$\deg\gcd$ 上半连续），是"平凡真"；
- **H1b（全分量恒定）**：连例外点也恒定——这是真正有意思的猜想，**需要结构解释**，目前没有。

**(c) H2 重述。** 95 号指出"有限覆盖 + 根移动"在代数几何里是**常态**，不该被排除；
正确的区分是根入射簇 $\mathcal E=\{(y,\lambda):m_I(y;\lambda)=0\ \forall I\}\to Y$ 的**投影结构**：
固定根截面 / 生成有限 / 正维纤维。本项目的"三分"按此重述为 **H2′**。

## 进展

- 商铅笔定理已写出并证明（含尺寸条件）；它把非特征层上的坏性化归为
  **$(n-2)\times(k-1)$ 仿射铅笔的"某 $\lambda$ 降秩"**，固定参数下即**可观测性检验**。
- 三处更正已落实（$\det M$ → 秩形式；H1 → H1a/H1b；H2 → H2′）。
- 优先级按 95 号改为：**H3（本文件）→ H1a → H2′ → H4（先找反例）**。

## 最终结论

1. **H3 已从猜想升为定理**（在 `rank X = k−1` 与"非特征"两个前提下）；
   这正是 95 号要求的 Result A。
2. **但 S3 没被解掉**：定理只把被测对象换成更小的铅笔，并把它解释成"generic 可观测性"；
   参数化版本仍是 generic 问题。
3. H1 必须降级：全分量度数恒定是**错的**（95 号的反例），只能做 H1b 的结构解释或 H1a 的平凡版。
4. 下一步（95 号 §8）：在具体分量上算 **generic gcd**（对函数域）而不是采样点，
   并对**特殊参数值**（秩跌落、判别式零点、根碰撞）单独算，比较 $\deg g_{\text{generic}}$ 与 $\deg g_{\text{special}}$。

## 放弃原因

- 没有证明 $\operatorname{rank}X=k-1$（应由 $H=QN$ 的秩推出，但本文件只作前提；需补证或实例核对）。
- 没有做 95 号 §8 的 Result B/C（generic gcd 的符号计算、特征纤维的判定）。
- 没有找 H4 的反例（95 号建议先找）。

## 残留价值

- 一个可写进论文的**商铅笔定理**（含 Hautus 解释），以及"固定参数可判 / generic 未决 / 有理更远"的三层区分；
- 两条**撤回**（$\det M\equiv0$ 的尺寸问题；H1 的全分量版本），防止后续会话按错的前提工作；
- 95 号的显式反例 $B_t$ 已记录，可作"度数不恒定"的标准例子。

## 相关文件

- 送审件：[95](../../../for_expert/archive/95_hyperplane_experiments_and_conjectures.md)
- 答复：[95-reply](../../../for_expert/archive/95_hyperplane_experiments_and_conjectures-reply.md)
- [attempts/327](../../c_stratification/attempts/327_lambda_movement_experiment.md)（E3/E4 与 $\det M$ 的原始写法）
- [attempts/326](326_eigenvector_form_of_badness.md)（谱形式引理）
- [attempts/325](../../c_stratification/attempts/325_theorem_c_cost_model.md)（S3）
- [attempts/324](../../c_stratification/attempts/324_hyperplane_component_theorem.md)（分量）

## 状态

- 商铅笔定理：**[已证-纸面]**；前提 $\operatorname{rank}X=k-1$ 已由专家 96 号**证明**
  （$\ker(QN)$ 恰是 $v$ 的坐标方向，故 $QN$ 在补空间上单射），并在 5 个随机实例上核对
  （[c336](../../../../tools/verification/c336_quotient_pencil_check.py)）。见 [335](../../c_stratification/attempts/335_expert96_verdict.md)。
- 三处更正：**[已落实]**。
- H1a：**平凡真**（上半连续）；H1b：**未证，且不能只靠固定核方向**（95 号反例）。
- H2′：**重述完成，未做**。
