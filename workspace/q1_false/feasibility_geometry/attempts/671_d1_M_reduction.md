# 671 $d=1$ 的 $M$ 系统约化与 $d=2$ 的秩层条件

> 2026-11-27。把 670 的秩分层在 $d=1$ 上显式化，验证它精确复现 663；并列出 $d=2$ 的各秩层条件。
> 状态：**[已证-纸面]**。

## $d=1$：$M$ 的显式约化

$P=(\lambda I-Z)H$，$H=uv^{\mathsf T}$，$z=Zu$。条目
$$f_{ij}(\lambda)=(\lambda u_i-z_i)v_j=\alpha_{ij}\lambda+\beta_{ij},\qquad \alpha_{ij}=u_iv_j,\ \beta_{ij}=-z_iv_j .$$
$M$ 是 $2\times m$ 矩阵（$m=qk$），第 $(i,j)$ 列为 $[\beta_{ij};\alpha_{ij}]^{\mathsf T}=v_j\,[-z_i;\,u_i]^{\mathsf T}$，$e_0=(1,0)^{\mathsf T}$。

**秩**：因某个 $v_j\ne0$，$\operatorname{rank}M=\operatorname{rank}\{[-z_i;u_i]\}_i\le2$。

**列空间条件**：$e_0\in\operatorname{col}M$ $\iff$ 存在 $h_i$ 使
$$\sum_i h_i z_i=-1,\qquad \sum_i h_i u_i=0 .$$
（取 $g_{ij}=h_i/v_j$ 即可，$v_j\ne0$ 的 $j$ 固定。）

- 若 $z=\mu u$（即 $u$ 是 $Z$ 的特征向量）：第二式 ⇒ $\sum h_i z_i=\mu\sum h_i u_i=0\ne-1$ ⇒ 不可行；
- 若 $z\notin\operatorname{span}\{u\}$：可取 $h$ 满足两式（两个线性泛函线性无关）⇒ 可行。

所以
$$\boxed{(5b)\iff u\ \text{不是}\ Z\ \text{的特征向量}},$$
与 663 的结论一致；$M$ 的秩为 1 或 2，分别对应 $X_1$ 与 $X_2$（$X_0$ 需 $P\equiv0$，即 $H=0$，与秩 1 矛盾）。

## $d=2$：$M$ 的秩层

$M(H)\in\mathbb C^{4\times2m}$（669 的块结构：第 $i$ 组两列 $[c_i;b_i;a_i;0]$、$[0;c_i;b_i;a_i]$）。
按 $M$ 的秩分 $r=0,1,2,3,4$：

| $r$ | 条件 | 说明 |
|---|---|---|
| 0 | $M=0$ | 所有 2-子式 $f_i\equiv0$；需 $P$ 的所有 2-子式为 0，但 $\operatorname{rank}H=2$ 时一般不可能 |
| 1 | 所有 2-子式为 0，且存在 1-子式非零；$e_0\in\operatorname{col}M$ | 退化为“秩 1 型” |
| 2 | 所有 3-子式为 0，某 2-子式非零；$e_0\in\operatorname{col}M$ | 641B 落在此层（$\operatorname{rank}M=2$，$e_0\notin$） |
| 3 | 所有 4-子式为 0，某 3-子式非零；$e_0\in\operatorname{col}M$ | — |
| 4 | 某 4-子式非零 | 此时 $\operatorname{col}M=\mathbb C^4\ni e_0$ 自动成立；638 落在此层 |

每层条件都是 $M$ 的子式（$M$ 条目次数 $\le2$，$r$-子式次数 $\le2r$）。

## 与 668 的对应

- 638（可行）：$\operatorname{rank}M=4$ ⇒ $X_4$，$e_0$ 自动在列空间；
- 641B（不可行）：$\operatorname{rank}M=2$ ⇒ $X_2$，但 $e_0\notin\operatorname{col}M$ ⇒ 不在可行集。

## 意义

- $d=1$ 的 $M$ 约化精确复现 663，说明统一判据没有“丢失信息”；
- $d=2$ 的秩层是 $\le5$ 个显式条件，均为 $M$ 的子式——**不再需要为 $d=2$ 单独引入新的几何对象**；
- 下一步是把这些子式条件写成 $R$ 的显式多项式系统，研究消元。

## 状态

- $d=1$ 的 $M$ 约化：**[已证-纸面]**；
- $d=2$ 的秩层表：**[已证-纸面]**；
- 消元：**[未做]**。
