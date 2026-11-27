# 378 带预设行的完整参数化定理（103 号 §7.8 修正的落实）

> 承接 377（103 号审计：漏了预设行 $L_0$、相对 Graßmannian、特征层维数）。
> 本文件把 374 的定理**补全并改正**，给出带 $V_0=\operatorname{row}L_0$ 的版本。

> **专家 105 号审计后的两处更正（必须与本文件同时读）**：
> 1. **$L_0$ 的秩**：记 $t_0=\operatorname{rank}L_0$，则 $\dim V\le t_0+(q-r_0)$。所以除非 $\operatorname{rank}L_0=r_0$，
>    行空间**达不到** $q$ 维——**引理 7（全行秩归一化）的前提不足**。
>    **已解决（385）**：问题定义要求 $\mathcal L$ 行满秩 ⟹ $t_0=r_0$ 是**可行性必要条件**（否则任何 $q$ 都不可行）。
>    所以这是**前置检查**，不是额外假设；Route B 不需要。
> 2. **满秩首项系数引理**：图表上 $\operatorname{rank}H\equiv\omega$ ⟹ 每点至少有一个极大子式的 $\lambda$-次数恰为 $\omega$；
>    于是函数域 gcd 次数为正 ⟹ **每个特化点**都有非平凡公因子 ⟹ 整图卡全坏。
>    这是"generic gcd 正次数 ⟹ 整图卡坏"的**唯一正确理由**。
>
> 详见 [384](../../decision_algorithms/attempts/384_expert105_audit.md)、[385](385_L0_rank_resolution.md)。

## 目标

把 374 的参数化定理改成**原问题**（有预设行）的正确版本。

## 设想与理由

原问题的设计变量是 $\mathcal L=[L_0;R]$，所以：

1. 预设行 $V_0=\operatorname{row}L_0$ **必须**含于行空间 $V$；
2. 预设行本身也要消去 $v,Av$，即 $L_0v=L_0Av=0$——这会**削掉**整个特征空间；
3. 纤维不是"任意 $s$ 维子空间"，而是"**包含** $\overline V_{0,v}$ 的 $s$ 维子空间"。

## 做法：补两个引理，改定理

**记号**：$M=\pi_{K_0}A|_{K_0}$，$A_{21}=\pi_{K_0^\perp}A|_{K_0}$，$E_\mu=\ker(M-\mu I)$，
$$E_\mu^0=E_\mu\cap\ker(L_0N)\cap\ker(L_0AN)\qquad(\text{即 }L_0v=L_0Av=0),$$
$h_\mu^0=\dim(E_\mu^0\cap\ker A_{21})$，$d_\mu^0=\dim E_\mu^0$，$s=q-k+1$，
$\mathcal Q_v=U_v^\perp/D_v$（$D_v=K_0\cap U_v^\perp$），$V_0=\operatorname{row}L_0$。

> **引理 5（预设行与纤维相容）.** 设 $[v]\in\mathbb P(E_\mu^0)$。则 $V_0\subseteq U_v^\perp$ 自动成立，且
> $$V_0\cap D_v=V_0\cap K_0,\qquad \delta:=\dim V_0-\dim(V_0\cap K_0)\ \text{与 }v\text{ 无关}.$$
> 记 $\overline V_{0,v}=(V_0+D_v)/D_v\subseteq\mathcal Q_v$（$\dim=\delta$）。
>
> *证明.* $E_\mu^0$ 的定义就是 $L_0v=L_0Av=0$，故 $V_0$ 的每行都消去 $v,Av$，即 $V_0\subseteq U_v^\perp$ ✓。
> 于是 $V_0\cap D_v=V_0\cap K_0\cap U_v^\perp=V_0\cap K_0$ ✓；而 $V_0\cap K_0$ 与 $v$ 无关，故 $\delta$ 固定。$\square$

> **引理 6（带预设行的纤维）.** 固定 $[v]\in\mathbb P(E_\mu^0)$。可容许行空间恰为
> $$\{V:\ V_0+D_v\subseteq V\subseteq U_v^\perp,\ \dim V=q\},$$
> 在商里等价于"包含 $\overline V_{0,v}$ 的 $s$ 维子空间"，即
> $$\operatorname{Gr}\bigl(s-\delta,\ \mathcal Q_v/\overline V_{0,v}\bigr),$$
> 维数 $(s-\delta)\bigl(r(v)-s\bigr)$，非空 $\iff\delta\le s\le r(v)$。
>
> *证明.* 标准 Grassmann 对应：$\{W:\overline V_0\subseteq W\subseteq\mathcal Q_v,\ \dim W=s\}\leftrightarrow$
> $\{W':W'\subseteq\mathcal Q_v/\overline V_0,\ \dim W'=s-\delta\}$，后者是 Grassmannian。$\square$

> **定理 1′（带预设行的完整参数化）.** 层的参数空间是有限个**相对 Graßmann 丛**
> $$\operatorname{Gr}_{B_\mu^{\mathrm{eig}}}\bigl(s-\delta,\ \mathcal Q^{\mathrm{eig}}/\overline V_0\bigr)
> \quad\text{与}\quad
> \operatorname{Gr}_{B_\mu^{\mathrm{non}}}\bigl(s-\delta,\ \mathcal Q^{\mathrm{non}}/\overline V_0\bigr),$$
> 底分别是 $B_\mu^{\mathrm{eig}}=\mathbb P(E_\mu^0\cap\ker A_{21})$、$B_\mu^{\mathrm{non}}=\mathbb P(E_\mu^0)\setminus B_\mu^{\mathrm{eig}}$；
> 维数
> $$\dim X_{\mathrm{eig}}=h_\mu^0-1+(s-\delta)(\rho-s),\qquad
> \dim X_{\mathrm{non}}=d_\mu^0-1+(s-\delta)(\rho-1-s);$$
> 非空 $\iff\delta\le s\le\rho$（特征）或 $\le\rho-1$（非特征）。每个非空分量不可约、定义在 $\mathbb R$ 上。
>
> *证明.* 引理 5+6 逐方向给纤维；常秩性给出丛结构；维数按丛公式。$\square$

> **引理 7（全行秩归一化）.** 若存在可行解且 $q\le\dim U_v^\perp$，则存在**满行秩**的可行解
> （把行空间扩张到 $q$ 维，保持 $V_0$ 与 $V_0+D_v$，不改变 $V\cap K_0=D_v$）。
>
> *证明.* 扩张不改变压缩秩与消去条件（都在 $U_v^\perp$ 内进行），且 $V\cap K_0$ 仍为 $D_v$。$\square$

## 进展

1. **定理 1′** 把 103 号指出的三处问题都补齐：预设行（$E_\mu^0$、$\delta$、$\overline V_0$）、
   相对丛（不是乘积）、特征层维数（$h_\mu^0-1$ 而非 $d_\mu-1$）。
2. **纤维维数仍 $\le p^2$**：$(s-\delta)(r-s)\le p^2$，所以 Stage 1 的界不受影响。
3. **$L_0$ 为空时**（$\delta=0$、$E_\mu^0=E_\mu$）退化为 374 的定理——我们三个实例都属于这种。

## 最终结论

1. 带预设行的参数化定理成立（相对丛 + 显式维数 + 非空条件）。
2. 关键新增量是 $\delta=\dim V_0-\dim(V_0\cap K_0)$ 与 $E_\mu^0$——前者进入纤维维数、后者进入底。
3. 实现仍只覆盖 $L_0$ 为空（$\delta=0$）的情形；带 $L_0$ 的版本**未实现**。

## 放弃原因

- 没有实现带 $L_0$ 的判定器（需要在商 $\mathcal Q_v/\overline V_{0,v}$ 上建图卡）；
- 没有验证引理 5 的退化情形（$V_0\cap K_0$ 维数跳变）；
- 没有重写 374 正文（只在本文件给修正版）。

## 残留价值

- **修正后的完整定理**（含预设行、相对丛、正确维数）；
- $\delta$ 与 $E_\mu^0$ 两个新量，可直接用于实现与复杂度；
- 退化检查：$L_0$ 为空时与 374 一致。

## 相关文件

- [attempts/374](374_complete_parameterization.md)（被修正的版本）
- [attempts/377](../../decision_algorithms/attempts/377_expert103_audit.md)（103 号的修正要求）
- [attempts/375](375_stage2_bit_complexity.md)（复杂度，用同一 $\delta$）
- [c357](../../../../tools/verification/c357_counterexample_certificates.py)（反例证书）

## 状态

- 定理 1′：**[已证-纸面]**。
- 带 $L_0$ 的实现：**[未做]**。
- 与 374 的一致性（$L_0=\varnothing$）：**已验证**（三个实例）。
