# 703 ChatGPT 对 638 外幂退化与 $T$ 修正的框架

> 2026-11-27。把 638 的“子式成比例”观察发给 ChatGPT（新对话），它给出 $\rho_d$/$\beta_d$ 框架、结构性不可行判据与 $T$ 的适用范围。
> 状态：**[M2 评估]** + **[已证]**（与 695 对应部分）。

## 关键区分：两种“秩”

- $\bigwedge^dP$ 在有理函数域上的秩：只要有一个非零分量就是 1，意义不大；
- **系数张成空间维数**
  $$\rho_d(H)=\dim_{\mathbb F}\operatorname{span}\{\Delta_I(H,\lambda):|I|=d\}.$$
  638 的观察是 $\rho_2(H)=1$（所有 2-子式成比例）。

对应地定义 $\beta_d(H)=\operatorname{rank}M(H)$，可行要求 $\beta_d=2d$。

## 结构性不可行判据（它提出）

若存在固定多项式子空间 $\mathcal V$（$\dim=r$）使所有 $\Delta_I(H,\lambda)\in\mathcal V$（对相容的秩 $d$ 的 $H$），则 $\rho_d\le r$；若进一步 $\beta_d\le2r$，则当 $2r<2d$ 时不可行。

**注意**：第二步（$\beta_d\le2r$）必须对具体 Bézout 构造证明，不能对任意定义一概而论。

## 638 的证明目标（它建议）

1. 相容空间 $\mathcal A=\{H:Q\operatorname{vec}(HZ')=0\}$ 的线性参数化；
2. 证明在 $\mathcal A$ 上所有 2-子式的系数矩阵 $C(x)$ 的 2 阶子式恒为零（即 $\rho_2\le1$）；
3. 由 $1<2$ 与 $\beta\le2$ 得 $\operatorname{rank}M\le2<4$ ⇒ 不可行。

它同时给了一个**否定性命题**：仅“$\operatorname{rank}H=2$、$HZ'\in U+T$、$Z'$ 循环”**不足以**推出 $\bigwedge^2P$ 退化（给了 $2\times3$ 的反例，$U$ 取全空间），所以必须用 638 特有的 $U,H_A$ 结构。

## 690-T 与 695 一致

它给出的强化
$$r_\mu+t-j_\mu\ge d',\quad r_\mu=\operatorname{rank}(H(\mu I-Z')),\ j_\mu=\dim(\operatorname{row}(R_\mu)\cap T)$$
正是 695 的 $\dim(\operatorname{row}(HM)+T)\ge d'$（两者等价：$\dim(V+T)=r_\mu+t-j_\mu$）。

## $T$ 的适用范围（它的表）

| 判据 | 是否直接换 $T$ |
|---|---|
| 690/695 | **是**（固定 $H$ 的自由度） |
| 678 | 不能直接换（涉及整体 $W$ 行空间） |
| 682 | 需重新推导 |
| 665 | 需重新推导 |
| 689 | 需重新线性消元 |

## $H_0$ 方向预筛选（它建议）

- 必要条件（$\lambda=0$）：$\operatorname{rank}H_A=d'$；否则所有 $d'$-子式在 0 处为零 ⇒ 公共根。
- 对固定 $H$：$H_A=HZ'+G$，$G\in E=T\cap U$；检查
  $$\exists G\in E:\ \operatorname{rank}(H_{A,0}+G)=d' .$$
- 这是可直接计算的预筛选，但只是必要。

## 下一步（按它）

1. 对 638 做 $C(x)$ 的符号计算（相容参数化 + 2 阶子式恒零）；
2. 检验 $\beta_d\le2r$ 在我们 Bézout 构造下是否成立（若是，结构性不可行判据可用）；
3. 用 $\operatorname{rank}H_A=d'$ 作为新预筛选，重跑 700 的四类统计。

## 状态

- $\rho_d/\beta_d$ 框架：**[M2]**；
- 690-T：**[已证]**（=695）；
- 638 符号证明：**[未做]**；
- $H_0$ 预筛选：**[待实现]**。
