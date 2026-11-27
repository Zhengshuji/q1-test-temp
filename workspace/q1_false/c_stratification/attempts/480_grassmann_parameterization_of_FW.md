# 480 阶段 3A/3B：$\mathcal U$ 的 Grassmann 参数化 与 (R) 的秩条件（(FW) 的商空间形式）

> 承接 [479](479_fixed_W_with_row_budget.md)（(FW) 已证）与专家对 479 的审阅。本文件只做阶段 3A 与 3B，
> 不做 gcd（留待 481），以保证几何参数化结果独立成立。

## 目标

1. **(3A)** 把 (FW) 的候选 $\mathcal U$ 与 $\operatorname{Gr}(t,\mathcal T_W/\mathcal W_0)$ **一一对应**，给出局部有理参数化；
2. **(3B)** 把 (R) 化成**最大子式非零**的秩条件。

## 做法

把 (FW) 里的 (R) 先用 $\pi_1(\mathcal W_0)=V_0$ 化简成 $\pi_1(\mathcal U)=W$；
再把"包含 $\mathcal W_0$、商维数 $t$"的子空间与商的 $t$ 维子空间对应起来；最后把 $\pi_1(\mathcal U)=W$ 写成第一个分量矩阵的秩条件。

## 进展

（见下文两个小节的命题。）

## 设想与理由

**简化的 (FW)**（专家的观察，采纳）：由 $\mathcal W_0\subseteq\mathcal U$ 且 $\pi_1(\mathcal W_0)=V_0$，
$$\operatorname{span}\bigl(V_0\cup\pi_1(\mathcal U)\bigr)=\pi_1(\mathcal U),$$
故 (R) 等价于更简的
$$\textbf{(R)}\quad\pi_1(\mathcal U)=W .$$
于是 (FW) 为：$\exists\mathcal U$，$\mathcal W_0\subseteq\mathcal U\subseteq\mathcal T_W$、$\dim(\mathcal U/\mathcal W_0)\le m$、$\pi_1(\mathcal U)=W$、$\pi_\lambda(\mathcal U)=W\ \forall\lambda$。

## 进展：3A（商空间 Grassmannian）

**前提**：相容性 $U\subseteq W$（$U=\operatorname{span}\{h_i^0,g_i^0\}$）$\iff$ $\mathcal W_0\subseteq\mathcal T_W$ ✓
（$(h_i^0,g_i^0)\in\mathcal S$ 且两分量都在 $W$ 里）。

> **命题 (3A).** 记 $\overline{\mathcal T}_W=\mathcal T_W/\mathcal W_0$，$N_W=\dim\overline{\mathcal T}_W$。对 $0\le t\le N_W$，
> $$\bigl\{\mathcal U:\ \mathcal W_0\subseteq\mathcal U\subseteq\mathcal T_W,\ \dim(\mathcal U/\mathcal W_0)=t\bigr\}
> \ \cong\ \operatorname{Gr}(t,\overline{\mathcal T}_W),$$
> 即：包含 $\mathcal W_0$、商维数恰为 $t$ 的子空间，与商的 $t$ 维子空间**一一对应**（$\mathcal U\leftrightarrow\mathcal U/\mathcal W_0$，逆映射为取原像）✓。

**局部参数化**：在固定秩层上取 $\ker D_I(X)$ 的有理基 $Z(X)$（[472](../../decision_algorithms/attempts/472_linear_preimage_fails.md) 的 $Z_{Q,P}$），
把 $\mathcal W_0$ 在该基下表示出来，取商基 $\overline Z(X)$；在 $\operatorname{Gr}(t,N_W)$ 的标准仿射卡上用 $t\times(N_W-t)$ 矩阵 $Y$ 表示，
$$\mathcal U(X,Y)=\mathcal W_0+\operatorname{row}\bigl(\overline Z(X)\,Y_{\text{lift}}\bigr),$$
其中 $Y_{\text{lift}}$ 是 $Y$ 提升到 $\mathcal T_W$ 的坐标。**这是局部参数化**——不同卡必须分别处理，不能以一卡代全 ✓。

**预算枚举**：只需
$$0\le t\le\min\{m,\ N_W\}\quad(\text{(FW)}).$$

**重要限制（分层）**：$\dim\mathcal T_W$ 随 $W$ 变化 ⟹ 参数空间不是全局向量丛，而是**相对于 $W$ 的 Grassmannian 纤维族**
（分层后才是丛）⟹ 必须先按 $\operatorname{rank}D_I(X)$ 分层，再在层内做上述参数化 ✓（与 [468](../../decision_algorithms/attempts/468_three_levels_and_minimal_example.md) 的三层区分一致）。

## 进展：3B（(R) 是秩条件）

设 $\mathcal U(X,Y)$ 的一组局部基（行对）为 $(x_1,y_1),\dots,(x_s,y_s)$，记
$$X_1(X,Y)=\begin{pmatrix}x_1\\ \vdots\\ x_s\end{pmatrix},\qquad X_2(X,Y)=\begin{pmatrix}y_1\\ \vdots\\ y_s\end{pmatrix}.$$

> **命题 (3B).** $\pi_1(\mathcal U)=W\iff\operatorname{rank}X_1(X,Y)=\omega$。

*理由.* $\pi_1(\mathcal U)\subseteq W$ 恒成立（$\mathcal U\subseteq W\oplus W$），且 $\dim\pi_1(\mathcal U)=\operatorname{rank}X_1$ ✓；
故等于 $W$（$\dim=\omega$）$\iff$ 秩为 $\omega$ ✓。
等价地：(R) 是"至少一个 $\omega\times\omega$ 子式非零"的**开条件** ✓。

**（E）的形态（留给 481）**：$P(\lambda;X,Y)=\lambda X_1(X,Y)-X_2(X,Y)$，(E) $\iff\operatorname{rank}P(\lambda;X,Y)=\omega\ \forall\lambda$，
即 $P$ 的全部 $\omega\times\omega$ 子式 $f_J$ 有 $\deg_\lambda\gcd_J f_J=0$ ✓。

**专家的 leading-coefficient 观察（记录，待 481 证明）**：在满足 (R) 的参数点上 $\operatorname{rank}X_1=\omega$ ⟹
至少一个最大子式的 $\lambda$-次数**恰为 $\omega$** ⟹ 最高次项不会整体退化 ✓——这是 Paper III 的引理可迁移的起点，
但**不能**直接说该引理原样成立（见 481 的三条待证细节）。

## 最终结论

1. **3A 完成**：候选 $\mathcal U$ 与 $\operatorname{Gr}(t,\overline{\mathcal T}_W)$ 一一对应，含局部有理参数化与预算枚举 $0\le t\le\min\{m,N_W\}$；
2. **3B 完成**：$(R)\iff\operatorname{rank}X_1(X,Y)=\omega$（开条件）；
3. **关键结构提醒**：$\dim\mathcal T_W$ 随 $W$ 变 ⟹ 参数空间是**相对 Grassmannian 纤维族**，必须先分层再参数化；
4. **$q_{\min}$ 的正式写法**（采纳专家的变量显式化）：
$$q_{\min}=r_0+\min_{\substack{W\ \text{相容}\\ \text{满足 (FW)}}}\ \dim(\mathcal U/\mathcal W_0),$$
其中 $r_0$ 是 $L_0$ 的**行数**（不是 $\operatorname{rank}L_0$；冗余固定行仍计入阶数）✓。

## 放弃原因

- 没有写出 $\overline Z(X)$ 的**显式**形式（只给了构造方式）；
- 没有处理 Grassmannian 卡之间的衔接（只在单卡内参数化）；
- 没有做 (E) 的 gcd（按专家建议留给 481）。

## 残留价值

- **3A 的一一对应**与局部参数化框架；
- **3B 的秩条件**（(R) 变成开条件，可直接接代数判定）；
- "$r_0$ = 行数不是秩"与 $q_{\min}$ 的正式形式；
- **相对 Grassmannian 纤维族**这一结构定位（避免了"全局向量丛"的错误假设）。

## 下一步

481：在分层后的每个不可约分支上，对 $P(\lambda;X,Y)$ 做 $(\lambda,X,Y)$ 的极大子式 $\gcd$，
证明（或限定）leading-coefficient 引理，并明确"函数域 gcd 为常数 ⟺ 存在非空开集内每点满足谱条件"这一**泛型**命题，
同时把分母非零的开集显式保留。

## 相关文件

- [479](479_fixed_W_with_row_budget.md)（(FW)）
- [472](../../decision_algorithms/attempts/472_linear_preimage_fails.md)（$Z_{Q,P}$ 与线性原像反例）
- [469](469_D_I_general.md)（正合列）
- [468](../../decision_algorithms/attempts/468_three_levels_and_minimal_example.md)（三层区分）

## 状态

- 3A：**[已证-纸面]**（一一对应 + 局部参数化框架）。
- 3B：**[已证-纸面]**。
- (E) 的 gcd 与 leading-coefficient：**[未做]**（481）。
