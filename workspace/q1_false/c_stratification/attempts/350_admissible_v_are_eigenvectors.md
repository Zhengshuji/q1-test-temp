# 350 可容许的 $v$ 是**压缩矩阵的特征向量**——层参数其实离散

> 承接 349（纤维判据）与 c350 的 $v$-扫描（随机 $v$ 一个层点都没有）。本轮查清原因，
> 得到一个**结构性简化**：超平面层的核方向 $v$ 只能取压缩矩阵 $M$ 的特征向量——**有限多个**。

## 目标

解释 c350 里"随机 $v$ 的纤维里没有可容许点"，并据此简化层的参数结构。

## 设想与理由

层点要求 $V\subseteq U^\perp$ 且 $\dim(V\cap K_0)=\omega=k-1$。而
$$V\cap K_0\subseteq K_0\cap U^\perp=\{u\in K_0:\ u\cdot v=0,\ u\cdot Av=0\}.$$
记 $\varphi_v(u)=u\cdot v$、$\varphi_{Av}(u)=u\cdot Av=u\cdot\operatorname{proj}_{K_0}(Av)$。则
$$\dim(K_0\cap U^\perp)=k-\operatorname{rank}\{\varphi_v,\varphi_{Av}\}.$$
要 $\ge k-1$ 必须 $\operatorname{rank}\le1$，即 **$\operatorname{proj}_{K_0}(Av)$ 与 $v$ 线性相关**。

## 做法与结果

> **命题（Prop E′，专家 101 号建议的加强版）.** 超平面层（$\omega=k-1$）的**任何**可容许核方向 $v\in K_0\setminus\{0\}$
> （非特征或特征）都满足
> $$\operatorname{proj}_{K_0}(Av)\in\operatorname{span}(v),$$
> 即 $v$ 是**压缩矩阵** $M=(\pi|_{K_0})\circ A|_{K_0}$ 的特征向量。
>
> *证明.* 非特征：由下（两泛函论证）。特征（$Av=\lambda_0v$）：$Mv=\pi_{K_0}(\lambda_0v)=\lambda_0v$，立得。$\square$

> **两处必须的限定（101 号审计）**
>
> 1. **方向不必有限**：特征值有限，但若 $\dim E_\mu=d>1$，方向集是 $\mathbb P(E_\mu)\cong\mathbb P^{d-1}$（无穷多）。
>    所以层 = $\bigcup_{\mu\in\operatorname{Spec}(M)}\mathbb P(\ker(M-\mu I))\times(\text{纤维})$，
>    **不是**"有限个方向 × 纤维"。
> 2. **纤维是 Grassmannian**：记 $D_v=K_0\cap U_v^\perp$（$\dim=k-1$），则 $V$ 由
>    $V/D_v\subseteq U_v^\perp/D_v$ 决定，纤维是
>    $$\operatorname{Gr}\bigl(d_V-(k-1),\ \dim(U_v^\perp/D_v)\bigr),$$
>    只有 $q=k$（即 $V/D_v$ 一维）时才是 $\mathbb P^{r}$。本文件下文与实现都只覆盖 $q=k$。


>
> *证明.* 由上：$\dim(K_0\cap U^\perp)\ge k-1\iff\operatorname{rank}\{\varphi_v,\varphi_{Av}\}\le1$；
> $\varphi_v\ne0$（$v\ne0$），故 $\varphi_{Av}$ 与 $\varphi_v$ 成比例；由 $K_0$ 上内积非退化，
> 成比例蕴含 $\operatorname{proj}_{K_0}(Av)\parallel v$。$\square$

**数值确认**（seed 4242）：压缩 $M$ 满足 $Me_1=e_1$，且 $\operatorname{proj}_{K_0}(A v)=v$（$v=Ne_1$）✓；
随机 $v$ 不满足 ⟹ 无层点（正是 c350 观察到的"tested 0"）。

## 进展

1. **层的 $v$-参数是离散的**：$v$ 只能取 $M$ 的特征向量（$\le k$ 个）。
   于是层 = **有限个纤维** $\mathbb P^{r}$ 的并（$r=\dim U^\perp-\omega$），不是连续族。
2. **这解释了 c350 的失败**：随机 $v$ 连可容许点都没有，所以"$v$-扫描"应有意义地只在特征向量上做。
3. **对既有卷宗的修正**：324 把底 $B^\circ$ 当成正维射影簇——对**超平面层**这不成立（$v$ 离散）。
   331 的"纤维判据"仍成立，但 $v$ 的枚举是有限的。
4. **算法后果**：层判定 = 有限个 $\mathbb P^r$ 上的 PIT（$r=3$，本模式），配合 345 的网格判定，
   整个过程是**多项式时间**的。

## 最终结论

1. 可容许 $v$ 有限（$M$ 的特征向量）——层参数离散化。
2. 因此"层 = 有限个纤维"这一图景比 324 的正维底更准确。
3. 实例判定 = 对每个 $M$ 的特征向量做一次纤维 PIT；每个 PIT 是 $r=3$ 参数的网格/证书问题。

## 放弃原因

- 没有处理 $K_0$ 上内积退化的情形（此时"成比例"要换成"零化子成比例"）；
- 没有枚举本模式全部 $M$ 的特征向量并逐一判定（只验证了一个）；
- 没有回头改写 324/331 的表述（只在本文记录修正）。

## 残留价值

- 一条**结构命题**（可容许 $v$ = 压缩的特征向量），把连续族变有限集；
- 解释了 c350 的"0 可容许点"，并给出正确做法；
- 直接支撑 345 的多项式判定：有限个纤维 × 每个 $\mathbb P^r$ 的网格 PIT。

## 相关文件

- [attempts/349](349_fibre_all_bad_proved.md)（纤维判据）
- [attempts/324](324_hyperplane_component_theorem.md)（底 $B^\circ$ 正维——对超平面层需修正）
- [attempts/331](331_eigenvector_criterion.md)（纤维判据）
- [attempts/345](345_pit_cost_n5_polynomial.md)（PIT 代价）
- [c350](../../../../tools/verification/c350_v_scan.py)

## 状态

- 命题（可容许 $v$ = $M$ 的特征向量）：**[已证-纸面]** + **[精确验证]**（seed 4242 的 $Me_1=e_1$、$\operatorname{proj}=v$）。
- 层参数离散化：**[已证-纸面]**。
- 全部特征向量的逐一判定：**[未做]**。
