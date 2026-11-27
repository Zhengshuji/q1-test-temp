# incidence 纤维论证：$B_{u,v}$ 的分量到 exact $(t,u,v)$ 层（175 的完整化）

> 2026-11-08。175 的分量界引用了专家 60 号 §5 的“每个 $B_{u,v}$ 分量贡献至多一个分量”。
> 本文件把这个论证写全（用 enlarged incidence，不需要 $V\cap A^{-1}V=W$ 的闭条件）。
> 状态：**M2（纸面）**。

## 目标

证明：对每个 $(t,u,v)$，exact 层 $S_{t,u,v}\subseteq\operatorname{Gr}(c,K_0)$ 的不可约分量数不超过
$B_{u,v}$ 的不可约分量数；从而
$$N(c)\le N_{\rm inv}(c)+\sum_{t<c}\sum_{u}\sum_{v}b_{u,v}.$$

## 设想与理由

exact 层由 $W=V\cap A^{-1}V$ 定义，条件较强。为了**上界**，可以把它 enlarge 成一个
incidence 空间 $\mathcal I$，只保留
$$W\subseteq U\subseteq V\subseteq K_0,\quad A(W)\subseteq U,\quad U=W+A(W),\quad \dim W=t,\ \dim U=u,$$
并丢掉 $V\cap A^{-1}V=W$（只保留 $W\subseteq U\cap A^{-1}U$，由 $A(W)\subseteq U$ 自动）。
$S_{t,u,v}$ 含于 $\mathcal I$ 的像（因为 exact 情形满足全部 incidence 条件），所以
$\mathcal I$ 的分量数给 $S$ 的上界。

## 做法

固定 $(t,u,v)$，$v=\dim(U\cap A^{-1}U)$。

### 1. 底空间

$$B_{u,v}=\{U\in\operatorname{Gr}(u,K_0):\ \dim(U\cap A^{-1}U)=v\}.$$
固定 $U$ 后，$\mathcal E_U:=U\cap A^{-1}U$ 是 $v$ 维子空间；$\{\mathcal E_U\}_U$ 是 $B_{u,v}$ 上的
秩 $v$ 子丛（171 的 $\ker\varphi$）。

### 2. $W$ 的纤维

$W$ 必须是 $U$ 的 $t$ 维子空间且 $A(W)\subseteq U$，即 $W\subseteq\mathcal E_U$：
$$W\in\operatorname{Gr}(t,\mathcal E_U)=\operatorname{Gr}(t,v).$$
再加 $U=W+A(W)$（开条件：$\operatorname{rank}$ 达到 $u$），得到相对 Grassmannian 的**开子集**。
$B_{u,v}$ 的每个不可约分量上，$\operatorname{Gr}(t,\mathcal E)$ 是相对 Grassmannian，不可约；
其非空开子集仍不可约。

### 3. $V$ 的纤维

固定 $(W,U)$ 后，$V$ 是 $K_0$ 中含 $U$ 的 $c$ 维子空间：
$$V\in\operatorname{Gr}(c-u,K_0/U),$$
不可约（Grassmannian），且不依赖 $(W,U)$ 的具体选取（只依赖 $U$）。
（exact 条件 $V\cap A^{-1}V=W$ 被丢掉；保留它只会减小集合。）

### 4. 传递

于是 $\mathcal I$ 在 $B_{u,v}$ 的每个不可约分量上是
$$\text{相对 }\operatorname{Gr}(t,\mathcal E)\ \text{的开子集}\ \times\ \operatorname{Gr}(c-u,K_0/U),$$
两个不可约空间的积，故不可约。投影 $(W,U,V)\mapsto V$ 是态射，像是 exact 层的超集，
不可约像的分量数 $\le1$（每个 $B_{u,v}$ 分量）。

因此
$$\#\operatorname{Irr}(S_{t,u,v})\le\#\operatorname{Irr}(B_{u,v})=b_{u,v}.$$

### 5. 汇合

$$\boxed{N(c)\le N_{\rm inv}(c)+\sum_{t=0}^{c-1}\sum_{u=t}^{\min(2t,c)}\sum_{v=t}^{u}b_{u,v}.}$$

**注**：对 exact 等式 $W=V\cap A^{-1}V$，实际上必有 $v=t$（因为
$U\cap A^{-1}U\subseteq V\cap A^{-1}V=W$ 且 $W\subseteq U\cap A^{-1}U$）；
所以 $v>t$ 的项对 exact 层是多余的，保留它们只是让上界更松、但更简单。

## 进展

* incidence 纤维论证写全：底 $B_{u,v}$、$W$-纤维 $\operatorname{Gr}(t,v)$（开条件）、
  $V$-纤维 $\operatorname{Gr}(c-u,K_0/U)$；
* 不需要 exact 条件 $V\cap A^{-1}V=W$（enlarge 给上界）；
* 175 的界不再依赖专家 §5 的引用。

## 最终结论

* 每个 $B_{u,v}$ 的不可约分量至多贡献一个不可约 exact 分量；
* 175 的界（$c=3$ 时 $s+s^2+s^3+1953$，$k=4$）现在是完整纸面证明；
* exact 层实际只需 $v=t$，所以 175 的界偏松但正确。

## 放弃原因

* 未证 $\mathcal E$ 的代数性/相对 Grassmannian 的不可约性细节（标准事实）；
* 未把 $v>t$ 的多余项去掉（更紧的界需要 $v=t$ 的论证）；
* 未 Lean 化。

## 残留价值

* 175 的完整化；一个可复用的“enlarged incidence”上界技巧；
* 明确了 exact 层只需 $v=t$。

## 相关文件

* [attempts/175](../../decision_algorithms/attempts/175_c3_bound_via_Buv.md)（$c=3$ 界）
* [attempts/171](171_Buv_rank_strata.md)（$B_{u,v}$）
* [attempts/161](161_general_c_invariant_and_rank_strata.md)（归约）

## 状态

* incidence 论证：**[已证-纸面，M2]**。
* 更紧的 $v=t$ 界 / Lean：**[未做]**。
