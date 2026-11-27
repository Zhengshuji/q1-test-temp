# 375 Stage 2：单谱时 $c=1$ 的判定是多项式时间（位复杂度）

> 承接 374（完整参数化定理：有限个 Grassmann 丛）与 370（Prop G 的条件性陈述）。
> 本文件补上 Stage 2，得到一条**带明确适用条件**的定理。

> **专家 103 号审计后的更正**：
> 1. 适用条件应从"**代数**单谱"改为"**几何**单谱"：只需 $\dim\ker(M-\mu I)=1$（代数重数可 $>1$），覆盖面更大；
> 2. 这是 **promise-class 定理**：超出承诺类时必须**拒绝**（报"未判定"），不能报不可行；
> 3. 位复杂度需要显式界：变量数 $d\le p^2$、每个参数次数 $O(n)$、$\lambda$ 次数 $O(n)$、极大子式个数 $n^{O(p)}$、系数位长、数域次数 $\le k$（还要控高度）、图卡数 $\binom{r}{s}$（固定 $p$ 为常数）；
> 4. 预设行 $L_0$ 的修正会改变纤维（$\operatorname{Gr}(s-\delta,\cdot)$），但 $(s-\delta)(r-s)\le p^2$ 仍成立。
>
> 详见 [377](../../decision_algorithms/attempts/377_expert103_audit.md)。

## 目标

证明：**若压缩的实特征值都是单根**，则固定 $p$ 时超平面层的判定是多项式时间（位复杂度）。

## 设想与理由

374 已经把参数空间写成有限个 Grassmann 丛。两点让位复杂度可控：

1. **单谱** ⟹ $d_\mu=\dim E_\mu=1$ ⟹ 底 $\mathbb P(E_\mu)$ 是**一个点**，不再贡献参数；
2. 于是每块只是一个 Grassmannian 的仿射图卡，参数个数 $d=m(r-m)$，其中
   $$m=q-k+1,\qquad r\le2p\ \Longrightarrow\ d\le(2p)^2/4\ \text{（固定 }p\text{ 时与 }n\text{ 无关）}.$$

## 做法：把复杂度逐项记账

**输入规模**：$A\in\mathbb Q^{n\times n}$、$C\in\mathbb Q^{p\times n}$、$L_0$、$q$，二进制编码长度记 $L$。

| 步骤 | 代价 | 说明 |
|---|---|---|
| $K_0$、$N$、压缩 $M$ | $\mathrm{poly}(n,L)$ | 有理线性代数 |
| 特征多项式（整数 $k\times k$） | $\mathrm{poly}(n,L)$ | 分数自由 |
| 分解 over $\mathbb Q$ | $\mathrm{poly}(n,L)$ | 标准（LLL 型） |
| 判"实根是否单根" | $\mathrm{poly}$ | 单根 ⟺ 该不可约因子重数为 1 |
| 每个实单根 $\mu$：特征向量、$D_v$、$U_v^\perp/D_v$ | $\mathrm{poly}(n,L)$ | 数域次数 $\le k$、维数 $\le n$ |
| 每块：$H(x),H_A(x)$ 与极大子式 | 子式个数 $\binom{q}{\omega}\binom{k}{\omega}=k\binom{q}{q-k+1}$ | $q-\omega\le\rho+1\le2p+1$ ⟹ 对固定 $p$ 是 $\mathrm{poly}(n)$ |
| 每块：$K(x)[\lambda]$ 上的 gcd | $\mathrm{poly}\bigl(n^{O(d)}\bigr)=\mathrm{poly}(n)$ | $d\le(2p)^2/4$ **固定** |
| 块数 | $\le k\cdot\#\{\text{图卡}\}$ | 图卡数 $=\binom{r}{m}$，对固定 $p$ 是常数 |

各项之积是 $n^{O(p^2)}$——**固定 $p$ 时是 $n$ 的多项式**。（指数随 $p^2$ 增长，但 $p$ 固定。）

## 定理

> **定理（Stage 2 + 374）.** 设压缩 $M=\pi_{K_0}A|_{K_0}$ 的**实特征值都是单根**，$K_0$ 上内积非退化。
> 则对固定的 $p$，超平面层（$c=1$）的判定在 $\mathrm{P}$ 中。

*证明.* 374 给出"层 = 有限个 Grassmann 丛"；单谱使每个丛退化为**一个点 × 一个 Grassmannian**；
取 Grassmannian 的有限个仿射图卡（每个是仿射空间 $\mathbb C^d$，$d\le(2p)^2/4$），逐块做 generic gcd；
上表逐项多项式。实性：$\mu$ 实 ⟹ 特征向量 $v$ 实；图卡是 $\mathbb R^d$，其 Zariski 稠密性给出实可行点。$\square$

## 进展

1. **Prop G 收口为条件定理**：单谱 + 非退化 ⟹ 固定 $p$ 多项式。
2. "单谱"是**可判**的（特征多项式分解后的重数），所以这不是空洞假设——算法可以先检查，不满足时报告"超出本定理范围"。
3. 与 101 号的要求对齐：这正是他建议的 Stage 1（几何计数，此处单谱）＋ Stage 2（位复杂度）。

## 最终结论

1. 固定 $p$ 的多项式结论在**单谱**下成立（生成情形）。
2. 重根（$d_\mu>1$）时底维 $d_\mu-1$ 随 $n$ 增长，指数变成 $n^{O(d_\mu+p^2)}$——不再是多项式界的证明。
3. 实现的适用范围仍是 $q=k$（$m=1$，纤维 $\mathbb P^{r-1}$）。

## 放弃原因

- 重根情形未处理（只指出障碍，没做降维或"按 $\mathbb P(E_\mu)$ 分层再递归"）；
- 位复杂度是**记账式**的：用了"固定变量数的多变量 gcd 是多项式"与"整系数多项式分解是多项式"这两条标准事实，没有在本项目内证明；
- 没有实现一般 $q$（$m>1$ 的 Grassmann 图卡）。

## 残留价值

- **一条条件明确的定理**：单谱 + 非退化 ⟹ 固定 $p$ 多项式；
- 一张可直接复用的记账表；
- 明确了重根是下一个障碍。

## 相关文件

- [attempts/374](374_complete_parameterization.md)（参数化定理）
- [attempts/370](370_c1_layer_complexity.md)（Prop G 的两阶段）
- [attempts/373](../../decision_algorithms/attempts/373_expert101_audit.md)（101 号的要求）
- [attempts/357](357_rational_function_decider.md)（判定器实现）

## 状态

- 单谱情形的多项式判定：**[已证-纸面]**（记账式，依赖两条标准事实）。
- 重根情形：**[未做]**。
- 一般 $q$ 的实现：**[未做]**。
