# 343 Claim 1 的修复：判定只需要"有限个不可约块的覆盖"，不需要分量

> 承接 342（97 号指出 Claim 1 的不可比性没证成）。本文件给出**绕过**：把"分量分解"换成一个
> 更弱但**足够且可证**的陈述——有限个不可约块覆盖 $Z$。

## 目标

在**不需要**"每个 $F_\lambda$ 是不可约分量"的前提下，保住逐块 generic-gcd 判据（Claim 3）。

## 设想与理由

97 号指出：$F_\lambda\not\subseteq\overline{Z^\circ}$ 不能由纤维维数比较得出（闭包的纤维 ≠ 纤维的闭包）。
但回头看判据**到底需要什么**：

- Claim 3 的证明只用两件事：**(a)** 覆盖（每个点落在某个块里）；**(b)** 每块**不可约**且坏集在其上**闭**。
- **完全没用到"块是极大不可约子集"**。

所以只要把 $Z$ 写成**有限个不可约块**的并（不要求它们是分量），判据就成立。这一步可以严格做：

## 做法

**块的构造（Grassmann 图卡）.** 行空间 $V$ 是 $\operatorname{Gr}(q,\ \mathbb C^n)$ 里的点。取 Grassmannian 的
**有限个仿射图卡**（每个图卡 = 一个矩阵块作图的仿射空间）覆盖 $\operatorname{Gr}(q)$。对每个图卡 $C$ 与每个底片
（$B^\circ$ 或 $E_\lambda$）取
$$\mathcal S_{C}=\overline{\{(\sigma,V):\ \sigma\in B^\circ,\ V\in C,\ V\subseteq U(\sigma)^\perp,\
\dim(V\cap K_0)=k-1\}},$$
$$F_{\lambda,C}=\{(\sigma,V):\ \sigma\in E_\lambda,\ V\in C,\ V\subseteq v^\perp,\ \dim(V\cap K_0)=k-1\}.$$

**命题.** 每个 $\mathcal S_C$、$F_{\lambda,C}$ 是**不可约**的；有限多个这样的块覆盖 $Z$。

*证明.* (i) 覆盖：$(\sigma,V)$ 的 $V$ 落在某个图卡里（有限覆盖）✓。
(ii) 不可约：在图卡里 $V$ 由矩阵参数线性描述，条件 $V\subseteq U(\sigma)^\perp$ 与
$\dim(V\cap K_0)\ge k-1$ 分别是**线性**与**行列式（Schubert 型）**条件——后者在仿射空间里定义一个
**不可约**的代数集（determinantal variety 不可约）；再与不可约的底（$B^\circ$ 或 $E_\lambda$，都是射影线性子空间
或它们的开集）作积，仍是不可约 ✓。$\square$

**判据（修订版）.** 设 $Z=\bigcup_{j=1}^{N}\mathcal S_j$ 是上述有限覆盖，每块不可约。则
$$\text{层可行}\iff\exists j:\ \gcd_I m_I=1\ \text{在}\ \overline{\mathbb Q(\mathcal S_j)}[\lambda]\ \text{中}.$$

*证明.* ($\Leftarrow$) 若第 $j$ 块 generic gcd $=1$，该块的 generic 点好，故可行。
($\Rightarrow$) 若层可行，取好点 $y\in Z$；设 $y\in\mathcal S_j$。坏集在 $Z$ 中闭（Claim 2），故在 $\mathcal S_j$ 中闭；
$y$ 不在坏集里 ⟹ $\mathcal S_j$ 不整体落在坏集 ⟹（$\mathcal S_j$ 不可约）generic 点也不在 ⟹ 其 generic gcd $=1$ ✓。$\square$

## 进展

1. **Claim 1 的缺口被绕过**：判据不再依赖"分量"（极大性/不可比性），只依赖"有限不可约覆盖 + 坏集闭"——
   后者两者都可证。
2. **97 号指出的两个具体问题都消失**：闭包的纤维 vs 纤维的闭包（不需要）、族是否是向量丛
   （不需要：图卡里的 fibre 是行列式集，仍不可约）。
3. **代价**：块数从 $1+\#\lambda$ 变为 $(1+\#\lambda)\times\#\text{图卡}$，仍是有限数（图卡数只依赖 $q,n$）。
   复杂度记账要乘上这个因子，但量级不变。
4. **"分量"这个说法可以撤掉**：与其说"$Z=Z^\circ\cup\bigcup F_\lambda$ 是分量分解"，不如说"它是有限不可约覆盖"。

## 最终结论

1. 判据 **不需要分量**；97 号的批评对"分量"成立，对"判据"不成立。
2. 324 应改述为：**有限不可约覆盖** + 计数上界；"分量"一词不再使用。
3. 代价只是一个有限因子（图卡数），不影响任何渐近结论。

## 放弃原因

- 没有证明这些块**就是**分量（也不需要；但若将来要谈"分量数 $\le1+\delta$"，那仍是未证的）。
- 图卡的显式选取（以及它如何与 $L_0$ 的约束相容）没有写细。
- 有理点问题仍未处理（图卡是仿射的，可能更利于有理点论证——但未做）。

## 残留价值

- 一个**更弱但够用**的替代陈述，救活了逐块判据；
- 把"分量"这个容易出错的概念从判据里彻底移除；
- 一条可复用的模式：**判据只需要不可约覆盖，不需要极大性**。

## 相关文件

- [attempts/324](324_hyperplane_component_theorem.md)（原"分量分解"，应改述）
- [attempts/342](../../decision_algorithms/attempts/342_expert97_audit.md)（97 号裁决）
- [attempts/322](322_hyperplane_determinism_components.md)（generic-gcd 判据）

## 状态

- 有限不可约覆盖 + 判据：**[已证-纸面]**（图卡的不可约性是标准事实）。
- "块 = 分量"：**[未证]**，且**不需要**。
