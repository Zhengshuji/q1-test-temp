# 404 专家 108 号审计：三处真错误 + 两处撤退 + 一条新命题

> 送审件 [108](../../../for_expert/archive/108_c2_layer.md)（已归档），答复
> [108-reply](../../../for_expert/archive/108_c2_layer-reply.md)。
> 总评："substantial improvement … credible foundation"，但"not yet ready to support its full
> algorithmic and complexity conclusions"。

## 目标

1. 逐条落实专家对 108 号的裁决；
2. 修三处**真错误**（预设行底条件缺失、底分类不完整、$n^{O(c^2)}$ 不成立）；
3. 补两处**证据缺口**（$c=1$ 的缺失射影点、$c=2$ 的完整证书）；
4. 记下他建议的**下一条命题**。

## 设想与理由

他的裁决分三类：**成立**（无界纤维的精确核、$K_0$-split 分解、不变核定理、Grassmann 纤维、单谱有限）、
**要修**（预设行、底分类、复杂度）、**要给证书**（非单调性反例两侧）。逐一处理即可。

## 做法

逐条对照他的 Part I–Part X，把裁决分成"修陈述""补证书""记新命题"三类，先修卷宗，再补脚本 `c404`。

## 进展

### A. 已修的三处真错误

**A1 预设行条件缺失（专家 §3）。** 原来只写 $W_0\subseteq W$，但 $V_0\subseteq V$ 在 $K$-split 下是**两个**
独立条件：

$$P_{K_0}(V_0)\subseteq D^{\perp_{K_0}}\quad(\text{底条件}),\qquad W_0\subseteq W\quad(\text{纤维条件}).$$

所以底的正确表述是

$$\mathcal B_{\rm pres}=\{D\in\mathcal I_c(M):\ P_{K_0}(V_0)\subseteq D^{\perp_{K_0}}\}
\ \bigl(\text{等价 } D\perp P_{K_0}(V_0)\bigr),$$

并且还要 $W_0\subseteq T_D$。**后果**：预设行可以删掉整个底分量（若 $P_{K_0}(V_0)$ 里有一个向量与某个不变
$D$ 内所有向量内积非零，则该 $D$ 不可能承载任何 $W$）。已在 [393](../../c_stratification/attempts/393_c2_fibre_and_base.md) 命题 2 就地改。

**A2 底分类不完整（专家 §4）。** 原版只写"Jordan 块只给链前缀、共轭对给孤立点"，在**多重 Jordan 块**
与**几何重数 $g_\mu>1$** 时不对。已改成主分量三分法，并写明：

- 多重 Jordan 块内还取决于特征向量与广义特征向量的**相对位置**（不是链前缀就能穷尽）；
- 不可约二次主分量的族是 $\mathbb P_{\mathbb C}(E_\mu)\cong\mathbb{CP}^{g_\mu-1}$，**实维数 $2(g_\mu-1)$**，
  由**几何**重数决定；$g_\mu=1$ 才退化为孤立点。

**A3 复杂度结论不成立（专家 §13）。** 撤回 $n^{O(c^2)}$：

- 底项 $c(d_\lambda-c)$ 可以是 $O(cn)$（$c=2$ 而重根特征空间 $\Theta(n)$ 维时就是 $\Theta(n)$）；
  纤维项受 $n-k\le2p$ 控制（$O(p^2)$）。故图表路线给的是 $n^{O(cn+p^2)}$；
- 且"$m$ 个变量"本身不给复杂度界；
- 另：$|\mathcal I_c(M)|$ 可指数（$\binom{k}{c}$），所以"枚举多项式"只在**固定 $c$** 下成立。

已在 [394](394_c2_total_charts.md) 与 [398](398_unified_exists_theta.md) 就地改，并注明撤回。

### B. 已补的两处证据（专家 §9–§11）

**B1 射影缺口（关键）。** 专家指出 $D=\operatorname{span}\{e_1+se_2\}$ 漏掉 $[0:1]=\operatorname{span}\{e_2\}$。
`c404` 补算：$\operatorname{span}\{e_2\}$ 的 $H=\begin{pmatrix}1&0&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}$、
唯一非零 3 阶子式的 gcd $=(\lambda-1)(\lambda-2)(\lambda-3)$ —— **与 $[1:s]$ 分支相同、也是坏的**。
又抽查 $\operatorname{span}\{2e_1-e_2\}$、$\operatorname{span}\{-e_1+3e_2\}$ 同样坏；孤立方向 $e_3,e_4$ 也坏。
⟹ **$c=1$ 层在该阶上完整不可行**（缺口已闭合）。

**B2 $c=2$ 侧完整证书。** `c404` 输出 $N$、$D$ 的 $K$ 坐标、$V$ 的基、$H$、$H_A$、六个非零 2 阶子式
与 gcd$=1$，并核对 $\dim V=3$、$\omega=2$、$\dim(K_0\cap V^\perp)=2$、$(5a)$。

### C. 新增的待证命题（专家 §6、§7、§12）

**命题（实一般点判据，待证）.** 设图卡 $X$ 定义在实代数数域上、实点 Zariski 稠密、且每个实点上
铅笔有 $(\omega,\omega)$ 首项系数满秩。则"一般点 gcd $=1$"$\iff$"图卡上存在实的铅笔可行点"。

配套改写算法语义为**三值**（并且只对"实可容许"的图卡计数）：可行（给出实点或判据适用）；
不可行（每个实可容许图卡都有已证的正次数一般点 gcd）；未定。

**另记两处措辞更正**：gcd 次数随 $D$ 变化（同一 $D$ 上次数确定）；"一般点 gcd $=1$"**不**推出整卡可行，
只推出非空 Zariski 开集好（再加上实点稠密才给存在性）。

### D. 专家建议的下一条命题

> **$K_0$-split $c=2$ 设计族的完整结构**：可容许核方向 = 满足预设行正交条件的实 $M$-不变 2-平面；
> 在 $A_{21}|_D$ 的每个常秩层上，与预设行相容的行空间选择构成相对 Grassmann 丛；铅笔可行的设计是
> 其中"压缩铅笔的极大子式无公共实仿射谱根"的子集。

以及随后的问题：**铅笔条件能否化到 $D$ 上（消掉 $W$）**，还是 $W$ 本质必需。

## 最终结论

1. 三处真错误已修（预设行底条件、底分类、复杂度撤回）；
2. 两处证据已补（射影点闭合、$c=2$ 完整证书）；
3. 新增一条待证命题（实一般点判据）与三值算法语义；
4. 下一条论文级命题按专家建议定为"$K_0$-split $c=2$ 的完整结构"，核心是 $W$ 能否消掉。

## 放弃原因

- 没有证"实一般点判据"（需要实代数几何的实点稠密性论证，本轮只登记）；
- 没有做专家列为 Priority 3 的位复杂度；
- 没有形式化剩余两条等价（Lean 侧只做了集合/维数部分，见 [403](../../c_stratification/attempts/403_lean_c2_and_selfcheck.md)）。

## 残留价值

- 一份**逐条落实的审计**（三修、两补、一新命题）；
- 修正后的核心陈述：预设行底条件 $\mathcal B_{\rm pres}$、$\mathbb{CP}^{g_\mu-1}$ 的实维数
  $2(g_\mu-1)$、撤回后的复杂度表述；
- 明确下一步 = "$K_0$-split $c=2$ 完整结构 + 消 $W$"。

## 相关文件

- 专家问答：[108 与回复](../../../for_expert/archive/)
- 卷宗：[393](../../c_stratification/attempts/393_c2_fibre_and_base.md)、[394](394_c2_total_charts.md)、[397](../../c_stratification/attempts/397_layer_nomonotone.md)、[398](398_unified_exists_theta.md)、[403](../../c_stratification/attempts/403_lean_c2_and_selfcheck.md)
- 脚本：[c404](../../../../tools/verification/c404_projective_coverage.py)（射影覆盖 + 两侧证书）
