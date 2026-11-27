# 755 外部复核：固定 $U$ 的仿射判据与 $\delta$ 预筛选

> 2026-11-27。与 ChatGPT 讨论阶段固定（754）后的回应整理；它建议的“固定 $U$ 仿射可行性引理”已在 697 中，$\delta$ 指标是新的可算预筛选。
> 状态：**[已证-纸面]**（两条）+ **[整理]**（讨论）。

## 定理 1（固定 $H$ 的 $(5a)$ 判据）

设 $H$ 行满秩（$U=\operatorname{row}H$，$\dim U=d'$）、$T=\{lW:lN=0\}$。则存在 $Z$ 使
$$ZH-HZ'\in T^q$$
当且仅当
$$\boxed{UZ'\subseteq U+T\quad(\text{即 }H_iZ'\in U+T,\ \forall i).}$$

**证明**：

- （⇒）$Z_iH\in U$、$G_i\in T$ ⇒ $H_iZ'=Z_iH-G_i\in U+T$；
- （⇐）若 $H_iZ'\in U+T$，写 $H_iZ'=u+t$（$u\in U,t\in T$）；取 $G_i=-t\in T$，则 $H_iZ'+G_i=u\in U$。由 $H$ 行满秩，$z\mapsto zH$ 满射，故存在 $Z_i$ 使 $Z_iH=u$。逐行拼接即得 $Z$。$\square$

（这正是 697/751 的“$F_i\ne\varnothing\iff H_iZ'\in U+T$”，此处写成矩阵形式。）

## 定理 2（$\delta$ 预筛选）

令 $\pi_U:\mathbb C^k\to\mathbb C^k/U$ 为商投影，定义
$$\delta(U,Z')=\operatorname{rank}\big(\pi_U\circ Z'|_U\big).$$
若 $(5a)$ 可解，则
$$\boxed{\delta(U,Z')\ \le\ t-a,\qquad a=\dim(U\cap T),\ t=\dim T.}$$

**证明**：$UZ'\subseteq U+T$ ⇒ $Z'(U)\subseteq U+T$ ⇒ $\pi_U(Z'(U))\subseteq(U+T)/U$，后者维数 $t-a$。$\square$

$\delta$ 依赖 $U$（即候选 $H$），是逐层预筛选量；它比“$UZ'\subseteq U+T$”多给一个秩上界。

## ChatGPT 的建议与我们的回应

| 它的建议 | 状态 |
|---|---|
| 固定 $U$ 的仿射可行性引理（$UZ'\subseteq U+T\iff$ $(5a)$ 可解） | **已在本文件定理 1**（等价于 697/751 的 $F_i\ne\varnothing$ 判据） |
| 方向性指标 $\delta(U,Z')\le t-a$ | **已证**（定理 2），可加入预筛选 |
| Grassmann 预筛选 $\{U: U_0\subseteq U,\ UZ'\subseteq U+T\}$ 非空是必要条件 | 成立（定理 1 的直接推论） |
| 两阶段框架：结构相容 + 代数非退化（$\gcd=1$） | 与 744/754 一致；第二阶段仍是 PIT 缺口 |
| 不要再用 $s,t,d'$ 单独判可行 | 与 733（$d'=2>t=s=1$ 可行）一致 |

它没有提供超出 754 的新证明；但 $\delta$ 指标是可直接加入链的量。

## 加入预筛选链（v3）

$$704\to726\to725\to690\to\boxed{\text{定理 1}}\to\boxed{\delta\le t-a}\to695\to705\to\gcd.$$

## 状态

- 定理 1/2：**[已证-纸面]**；
- ChatGPT 复核：**[已记录]**；
- 下一步：把 $\delta$ 写成脚本，与 744 的七条一起批量检验。
