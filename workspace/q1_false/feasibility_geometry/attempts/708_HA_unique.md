# 708 $U\cap T=0$ 时 $H_A$ 唯一确定

> 2026-11-27。在 638 的 $U+T=\mathbb C^3$ 情形（707），证明 $H_A=ZH$ 与 $Z$ 在 $\operatorname{row}$ 上都被数据唯一确定。
> 状态：**[已证-纸面]**。

## 定理

设 $U=\operatorname{row}H$、$T=\operatorname{span}\{e_1\}$、$U+T=\mathbb C^3$（故 $U\cap T=0$，$\dim U=2$）。则对每个 $i$，向量 $H_iZ'$ 有**唯一**分解
$$H_iZ'=u_i-g_i,\qquad u_i\in U,\ g_i\in T .$$
于是 $H_A=ZH$ 的各行 $u_i$ 被唯一确定；$Z$ 在 $\operatorname{row}$ 意义上唯一（差左零空间不影响 $ZH$，687）。

**证明**：$U+T=\mathbb C^3$ 且 $U\cap T=0$ ⇒ 映射 $U\oplus T\to\mathbb C^3$、$(u,g)\mapsto u-g$ 是线性同构 ⇒ 分解唯一。$\square$

## 推论（638）

638 的相容秩 2 的 $H$ 都满足 $U+T=\mathbb C^3$（707），故 $H_A$ 由 $H$ 唯一确定：
$$H_A=\Pi_U(HZ')\quad(\text{沿 }T\text{ 投影}),$$
铅笔 $P(\lambda)=\lambda H-H_A$ 唯一。

因此 638 的 $\rho_2$ 不是 $Z$ 的自由度问题，而是 $H\mapsto H_A$ 这个**投影映射**的结构问题。

## 意义

- 排除了“$Z$ 的自由参数影响 $\rho_2$”的可能；
- 把 638 的 $\rho_2=1$ 归结为投影 $\Pi_U$ 与 $Z'$ 的相互作用；
- 也说明 706 中对自由参数取随机值不影响结论（结论本来与自由参数无关）。

## 待证（下一步）

对 $U$（2 维、$e_1\notin U$）、$H$（行空间 $U$、秩 2）与 $H_A=\Pi_U(HZ')$，证明 $P(\lambda)=\lambda H-H_A$ 的全部 2-子式成比例（$\rho_2=1$）。

## 状态

- 定理：**[已证-纸面]**；
- 638 的 $\rho_2=1$：**[猜想]**（但已排除 $Z$ 自由度的干扰）。
