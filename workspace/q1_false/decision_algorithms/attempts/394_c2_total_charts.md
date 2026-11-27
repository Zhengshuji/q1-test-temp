# 394 Phase 5：$c=2$（$K$-split）的总图卡与判定算法

> 承接 393（两个纤维 + $\mathcal I_2(M)$ 的三情形 + 单谱有限可判）。
> 本文件把 $(5b)$ 加到**总参数空间**上，给出 $c=2$ 的图卡定理与算法。

## 目标

在 $K$-split 假设下，把 $c=1$ 论文里的"图卡 + 满秩首项系数 + 函数域 gcd"搬到 $c=2$：
底是 $\mathcal I_2(M)$ 的一个分量（可以是正维的），纤维是 $\operatorname{Gr}(t-w_0,T_D/W_0)$。

## 设想与理由

$c=1$ 时底是**有限个点**（$\mathbb P(E_\mu)$ 每点一维），所以只需纤维图卡。$c=2$ 重根时底是
$\operatorname{Gr}(2,E_\lambda)$（维 $2(d_\lambda-2)$）或 $\mathbb P\times\mathbb P$，于是：
**底也要取图卡**，并且 $D\mapsto(D^{\perp_K},T_D,W_0)$ 需要**局部平凡化**（因为 $D^{\perp_K}$ 与 $T_D$
随 $D$ 变动）。这与 $c=1$ 论文 Definition 11 的"总图卡"是同一套模式，只是底从射影空间换成 Grassmannian。

## 做法

**记号**（沿 393）：$U_D=D+AD$，$T_D=K^\perp\cap(A_{21}D)^\perp$，$W_0=P_{K^\perp}(V_0)$，
$r(D)=\rank(A_{21}|_D)\in\{0,1,2\}$，$t=q-\rho$，$w_0=\dim W_0$。

### 定理 1（$c=2$ 的总图卡）

设 $\mathcal C$ 是 $\mathcal I_2(M)$ 的一个分量（$M$ 的 Jordan 型决定的三类之一），$\mathcal C$ 上 $r(D)\equiv r$ 常数。
则：

1. $\mathcal C$ 上的可容许设计构成**相对 Grassmann 丛**：纤维 $\operatorname{Gr}(t-w_0,\ T_D/W_0)$，$\dim T_D=\rho_{\rm amb}-r$（$\rho_{\rm amb}:=n-k=\dim K^\perp$；**不是** $\rho=\rank H$）；
2. 该族被**有限个仿射图卡**覆盖，每个图卡是三个因子的乘积：
   - **底图卡**：$\mathcal C$ 的标准仿射图卡（$\operatorname{Gr}(2,E_\lambda)$ 的 $2\times(d_\lambda-2)$ 坐标，或 $\mathbb P\times\mathbb P$ 的坐标，或单点）；
   - **平凡化图卡**：$D\mapsto D^{\perp_K}$ 与 $D\mapsto T_D$ 的指定枢轴子式非零的开集（把两个丛局部平凡化），在这张卡上它们有**多项式**基；
   - **纤维图卡**：$\operatorname{Gr}(t-w_0,\rho_{\rm amb}-r-w_0)$ 的 Grassmann 图卡；
3. 每张图卡上 $L$ 的行是联合坐标的**有理函数**，分母为枢轴子式；清分母后 $\lambda H-H_A$ 的条目是多项式；
4. 再细化到"某个 $\omega\times\omega$ 子式 $\Delta$ 非零"的图卡，则 $\rank H\equiv\omega$ **恒成立**；
5. 因此在每张图卡上，函数域 $K(x)[\lambda]$ 上的 gcd 判定**整张图卡**。

*证明.* 1 由 393 命题 2 给出（$T_D$ 常秩、$W_0\subseteq T_D$ 固定）；2 是 Grassmann 丛的有限图卡覆盖加上
两个丛的枢轴平凡化（每个枢轴选择是一个开条件，故仍是仿射）；3 是平凡化的直接结果；4、5 与 $c=1$
论文的引理（满秩首项系数）逐字相同——该引理只用到"$\rank H\equiv\omega$ 在图上恒成立"。$\square$

### 算法（$c=2$，$K$-split）——**三值语义**（按专家 108 号 §7 与 405 的判据）

1. 算 $K$、$\rho$、$t=q-\rho$、$M$、$A_{21}$、$W_0$；
2. 枚举 $\mathcal I_2(M)$ 的分量（按 $M$ 的实 Jordan 型），按 $r(D)\in\{0,1,2\}$ 分层，
   **并把底限制到** $\mathcal B_{\rm pres}=\{D:P_K(V_0)\subseteq D^{\perp_K}\}$（专家 108 号 §3）；
3. 每个分层：枚举**满秩图卡**（某 $\omega$ 阶子式的 $\lambda$-首项系数非零）；
4. 每张满秩图卡：清分母、算一般点 gcd：
   - 次数 $=0$ 且该图卡**有实点**（Grassmannian 图卡 + $\mathcal B_{\rm pres}$ 开条件自动满足）⟹ **可行**；
   - 次数 $>0$ ⟹ 整卡坏（"一般点坏 ⟹ 处处坏"，见 405 引理 1）；
5. 全部实可容许满秩图卡都正次数 ⟹ **不可行**；
6. 有图卡既未算出正次数 gcd、也无法给出实点证据 ⟹ **未定**（绝不报不可行）。

**依据**（405）：一般点 gcd 次数是 specialization 的**下界**，而"次数取最小值"的集合是**非空开集**；
在实点 Zariski 稠密 + 每个实点满秩的条件下，"一般点次数 0"$\iff$"存在实可行点"。

### 推论 2（单谱：无需底图卡）

若 $M$ 的特征值互异，$\mathcal I_2(M)$ 是有限集（393 推论 4），于是底图卡与平凡化都退化为**逐点计算**：
每个 $D$ 只算一次纤维 gcd ⟹ 判定 = **有限多次精确计算**，无需函数域的底变量。

### 复杂度（粗账；**$n^{O(c^2)}$ 的说法已撤回**，见专家 108 号 §13 与 404）

- 分量数：$c=2$ 时由 $M$ 的谱型决定，$O(k^2)$ 量级；但**一般 $c$ 时分量数可指数**
  （$M$ 有 $k$ 个互异实特征值 $\Rightarrow|\mathcal I_c(M)|=\binom{k}{c}$），故"枚举是多项式的"只在**固定 $c$** 下成立；
- 每分量的图卡数：$\binom{d_\lambda}{2}$ 或（$\mathbb P\times\mathbb P$ 的 $d_\lambda d_\mu$）乘枢轴选择数；
- 每张图卡的变量数：$\dim\mathcal C + (t-w_0)((n-k)-r(D)-t)$，即
  $$2(d_\lambda-2)+(t-w_0)((n-k)-r-t)\quad\text{或}\quad (d_\lambda-1)+(d_\mu-1)+(t-w_0)((n-k)-r-t).$$
- **底维 $2(d_\lambda-2)$ 随 $k$ 增长**（重根时）：$c=2$ 而重根特征空间 $\Theta(n)$ 维时底维是 $\Theta(n)$，
  所以"固定变量数"需要额外的谱假设；纤维项受 $n-k\le2p$ 控制（$O(p^2)$）。
- 由变量数**不能**直接读出复杂度界：诚实的说法是"固定 $c$ 且谱型受限时可判，位复杂度另算"。

## 进展

- 定理 1 与算法已写出（纸面）；关键点是把 $c=1$ 的三个引理（图卡、满秩、gcd）逐字复用，
  只把"射影底"换成"Grassmann 底"；
- 推论 2 给出单谱时的**有限判定**（与 393 推论 4 一致，但这里给了算法形态）；
- 诚实标注：**重根时底维随 $k$ 增长**，所以"固定变量数"的复杂度定理在 $c=2$ 需要额外的谱假设
  （例如"重根特征空间的维数有界"）。

## 最终结论

1. Phase 5 的图卡定理与算法成立（$K$-split，$c=2$）。
2. 单谱：有限可判、无底变量。
3. 重根：底是正维 Grassmannian，图卡数有限但底维随 $k$ 增长 ⟹ 复杂度需额外假设。
4. 下一步 Phase 6：把上述账算成显式界（模仿 386 的六个引理），并确定 $c=2$ 的 promise class。

## 放弃原因

- 没有证"重根时底维有界的替代路线"（例如只在 $\operatorname{Gr}(2,E_\lambda)$ 的**不变子空间**里再分层）；
- 没有处理 $K$-split 归一化定理（full 问题的缺口，专家明确说未证）；
- 复杂度只给了粗账。

## 残留价值

- **$c=2$ 的总图卡定理**（有限覆盖 + 满秩 + gcd 判整卡）；
- **单谱时不需底图卡**的算法形态；
- 重根时"底维随 $k$ 增长"这一**结构性障碍**的明确陈述（与 $c=1$ 的几何单谱对应）。

## 相关文件

- [attempts/393](../../c_stratification/attempts/393_c2_fibre_and_base.md)（纤维与底几何）
- [attempts/392](../../c_stratification/attempts/392_expert107_audit.md)（专家 107 号裁决）
- [attempts/386](386_bit_complexity_proof.md)（$c=1$ 的复杂度记账，可就地改造）
- [attempts/374](../../c_stratification/attempts/374_complete_parameterization.md)/[378](../../c_stratification/attempts/378_parameterization_with_L0.md)（$c=1$ 的总图卡构造）
