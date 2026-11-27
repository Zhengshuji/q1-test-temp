# 374 完整的超平面层参数化定理（专家 101 号 §17 的目标）

> 承接 373（101 号审计：方向不必有限、纤维是 Grassmannian、实 vs 复）。
> 本文件给出那个"完整参数化定理"及其证明，并说明它对 Prop G 的意义（Stage 1 只在**单谱**时成立）。

> **专家 103 号审计后的更正（必须与本文件同时读）**：
> 1. **漏了预设行**：原问题要求 $V_0=\operatorname{row}L_0\subseteq V$ 且 $L_0v=L_0Av=0$。
>    正确的底是 $E_\mu^0=E_\mu\cap\ker L_0\cap\ker(L_0A)$，正确的纤维是
>    $$\operatorname{Gr}\bigl(s-\delta,\ \mathcal Q_v/\overline V_{0,v}\bigr),\qquad \delta=\dim V_0-\dim(V_0\cap K_0),$$
>    维数 $(s-\delta)(r(v)-s)$，非空 $\iff\delta\le s\le r(v)$。本文件写的 $\operatorname{Gr}(s,r)$ 是 $\delta=0$（$L_0$ 为空）的特例。
> 2. **相对 Graßmannian，不是乘积**：$\mathcal Q_v=U_v^\perp/D_v$ 随 $v$ 变、未必全局平凡，不能写成 $\mathbb P\times\operatorname{Gr}$。
> 3. **特征层维数**：底是 $\mathbb P(E_\mu\cap\ker A_{21})$，维数 $h_\mu-1$（**不是** $d_\mu-1$）：
>    $\dim X_{\text{eig}}=h_\mu-1+s(\rho-s)$，$\dim X_{\text{non}}=d_\mu-1+s(\rho-1-s)$。
> 4. **非退化假设多余**：标准欧氏内积正定 ⟹ 自动成立。
> 5. **全行秩归一化**：$q$ 是行数；存在性可假设满行秩（当 $q\le\dim U_v^\perp$）。
>
> 详见 [377](../../decision_algorithms/attempts/377_expert103_audit.md)。

## 目标

对压缩 $M=\pi_{K_0}A|_{K_0}$ 的每个**实**特征值 $\mu$，刻画 $\mathbb P(E_\mu)$ 上**完整**的可容许行空间族
（含特征与非特征两种方向），并证明它是**有限个不可约实代数簇**（Grassmann 丛）。

## 设想与理由

三件事让参数化可以做得显式：

1. **可容许方向 = $\mathbb P(E_\mu)$**（Prop E′，373 的审计确认）；
2. **特征方向在 $E_\mu$ 里是线性子空间**：$Av\in\operatorname{span}(v)\iff\pi_{K_0^\perp}(Av)=0$；
3. **纤维是 Graßmannian**：$V$ 由 $V/D_v\subseteq U_v^\perp/D_v$ 决定，$D_v=K_0\cap U_v^\perp$ 固定维数 $k-1$。

## 做法：四个引理

记 $A_{21}=\pi_{K_0^\perp}A|_{K_0}$（$K_0$ 到 $K_0^\perp$ 的分量），$E_\mu=\ker(M-\mu I)$。

> **全篇假设（非退化）**：$K_0$ 上的内积限制**非退化**（即 $K_0\cap K_0^\perp=0$）。
> 这保证 $v\in K_0\setminus0\Rightarrow\varphi_v\ne0$。一般 $C$ 满足；特殊实例可能违背，此时须把"平行"换成"零化子成比例"。


> **引理 1（方向集）.** 设 $\mu\in\operatorname{Spec}_{\mathbb R}(M)$，$v\in E_\mu\setminus0$。则
> $$\dim(K_0\cap U_v^\perp)=k-1,$$
> 即每个方向都**可容许**（不仅非特征）。
>
> *证明.* $Mv=\mu v$ 给出 $\pi_{K_0}(Av)=\mu v$，故两泛函 $\varphi_v,\varphi_{Av}$ 在 $K_0$ 上相关
> （$\varphi_{Av}=\mu\varphi_v$），于是 $\dim(K_0\cap U_v^\perp)=k-\operatorname{rank}\{\varphi_v,\varphi_{Av}\}=k-1$。$\square$

> **引理 2（特征方向的线性结构）.** 在 $E_\mu$ 里，
> $$E_\mu^{\mathrm{eig}}:=E_\mu\cap\ker A_{21}$$
> 是一个**线性子空间**，对应 $Av\in\operatorname{span}(v)$ 的方向；其补（Zariski 开集）对应非特征方向。
>
> *证明.* $Av\in\operatorname{span}(v)\iff Av-\mu v\in\operatorname{span}(v)$；而 $Av-\mu v=A_{21}v$，
> 且 $A_{21}v\in K_0^\perp$、$\mu v\in K_0$ ⟹ $A_{21}v=0$（$K_0\cap K_0^\perp$ 只含 0，$K_0$ 非退化时）。$\square$

> **引理 3（商丛）.** 在 $\mathbb P(E_\mu)$ 上，$v\mapsto D_v$ 与 $v\mapsto U_v^\perp/D_v$ 是**常秩向量丛**，
> 秩分别为 $k-1$ 与
> $$r(v)=\begin{cases}\rho-1,&v\ \text{非特征},\\ \rho,&v\ \text{特征},\end{cases}\qquad \rho=\operatorname{rank}[C;CA].$$
> *证明.* 两泛函的秩在 $\mathbb P(E_\mu)$ 上恒为 1（引理 1），故 $D_v=\ker\{\varphi_v,\varphi_{Av}\}$ 有常维数；
> 商空间维数 $=(n-\dim U_v)-(k-1)$，$\dim U_v=2$ 或 $1$ 由引理 2 的线性条件分层。$\square$

> **引理 4（纤维）.** 固定方向 $[v]$ 与行数 $q$。可容许行空间恰为
> $$\{V:\ D_v\subseteq V\subseteq U_v^\perp,\ \dim V=q\}=\operatorname{Gr}\bigl(q-k+1,\ r(v)\bigr),$$
> 非空 $\iff 0\le q-k+1\le r(v)$。
> *证明.* $\dim(V\cap K_0)$ 自动 $=k-1$（因 $D_v\subseteq V\subseteq U_v^\perp$ 且 $K_0\cap U_v^\perp=D_v$）；
> 其余由标准 Grassmann 对应。$\square$

## 定理（完整参数化）

> **定理.** 超平面层（$\omega=k-1$，行数 $q$）等于
> $$\bigsqcup_{\mu\in\operatorname{Spec}_{\mathbb R}(M)}\Bigl(\ \underbrace{\mathbb P(E_\mu^{\mathrm{eig}})\times\operatorname{Gr}(q-k+1,\rho)}_{\text{特征部分}}\ \sqcup\ \underbrace{\bigl(\mathbb P(E_\mu)\setminus\mathbb P(E_\mu^{\mathrm{eig}})\bigr)\times\operatorname{Gr}(q-k+1,\rho-1)}_{\text{非特征部分}}\Bigr),$$
> 其中每条是 $\mathbb P(E_\mu)$ 上的 **Grassmann 丛**（非特征部分为开子丛），因而是**不可约实代数簇**；
> 层的维数
> $$\dim=(d_\mu-1)+\bigl(q-k+1\bigr)\bigl(r-(q-k+1)\bigr),\qquad d_\mu=\dim E_\mu .$$
> 非空性：特征部分需 $q\le k-1+\rho=n-1$；非特征部分需 $q\le k-1+\rho-1=n-2$；两者都需 $q\ge k-1$。

*证明.* 引理 1–4 逐个固定方向给出纤维；丛结构由引理 3 的常秩；不可约性由"不可约底 + 常秩纤维"；
维数按丛的标准公式。$\square$

## 对 Prop G 的意义（Stage 1）

$$q-k+1\le r\le2p\ \Longrightarrow\ \text{纤维维数}\le(2p)^2\ \text{（固定 } p\text{ 时一致有界）},$$

但**底维 $d_\mu-1$ 随 $n$ 增长**。所以：

> **推论.** 若压缩的**实特征值都是单根**（$d_\mu=1$，生成情形），则层的每个不可约块
> 图卡维数 $\le(2p)^2$，与 $n$ 无关 ⟹ Prop G 的 **Stage 1 成立**。
> 若有重根（$d_\mu>1$），底 $\mathbb P(E_\mu)$ 贡献 $d_\mu-1$ 个参数，图卡维数不再一致有界。

这解释了 101 号为什么强调"必须把 $\mathbb P(E_\mu)$ 的维数计入参数"：**Stage 1 的正确陈述应带单谱条件**。

## 进展

1. **完整参数化定理已证**（特征/非特征两支、Grassmann 丛、维数公式、非空条件）。
2. 顺带得到 $\dim(K_0\cap U_v^\perp)=k-1$ 对**所有**方向成立（不只非特征）——引理 1。
3. **Stage 1 的正确边界**：单谱时成立；重根时底维随 $n$ 增长。
4. 判据形状随之精确：层的判定 = 对这有限个**不可约丛**逐个做 generic gcd。

## 最终结论

1. 专家指定的"完整参数化定理"给出了：**有限个 Grassmann 丛，每个不可约、实、显式参数化**。
2. 非空条件 $k-1\le q\le n-1$（特征）或 $n-2$（非特征）是**免费的必要条件筛查**。
3. Prop G 的 Stage 1 在单谱（生成情形）下成立，重根时退化——这与 101 号的判断一致。

## 放弃原因

- 没有把重根情形处理成"参数化 + 降维"（只指出底维增长）；
- 没有实现一般 $q$（Grassmann 纤维，而非 $\mathbb P^r$）；
- 实性：只指出"实点 Zariski 稠密"对仿射/射影参数化成立，没有处理 $L_\mu$ 上的实点存在性细节。

## 残留价值

- **一个完整的参数化定理**（正是 101 号点名的下一个目标）；
- 引理 1（所有方向都可容许）与引理 2（特征方向是线性子空间）都可复用；
- Stage 1 的正确边界（单谱 vs 重根）。

## 相关文件

- [attempts/373](../../decision_algorithms/attempts/373_expert101_audit.md)（101 号审计）
- [attempts/350](350_admissible_v_are_eigenvectors.md)（Prop E′）
- [attempts/370](370_c1_layer_complexity.md)（Prop G）
- [attempts/357](357_rational_function_decider.md)（判定器）

## 状态

- 完整参数化定理：**[已证-纸面]**（在 $K_0$ 非退化假设下）。
- Stage 1（单谱）：**[已证-纸面]**；重根：**[未做]**。
- 一般 $q$ 的实现：**[未做]**。
