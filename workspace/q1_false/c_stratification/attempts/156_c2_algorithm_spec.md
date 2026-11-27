> **更正（2026-11-08，自查）**：逐行公式 $H_{A,i}=h_iAN+\Gamma(g_i)$ **维度不对**：
> $h_i$ 是 $1\times k$、$AN$ 是 $n\times k$，乘积无定义。正确的是
> $$H_{A,i}=l_i^{(0)}AN+g_iAN,$$
> 其中 $l_i^{(0)}$ 是 $l_iN=h_i$ 的一个**特解提升**；$H_A$ 依赖特解，不能只用 $h_i$ 表达。
> 逐行自由度 $g_i\in\operatorname{ann}(K_0)$ 仍独立。v7 的搜索把 $HAN$ 算错了，但最终 $L$ 由
> `check_candidate` 直接验证通过，故 **seed10 见证仍然有效**；搜索判据需按上述正确公式重写。

# $c=2$ 算法的正确形式：逐行提升、三行铅笔与变量清单

> 2026-11-08。前几轮的 v1–v3 在 $W_L$、$H_A=HAN+\Gamma(X)$、两行约化之间反复；本文件把**正确形式**
> 一次写清，作为实现与后续修正的基准。状态：**M2（结构 + 算法规格）**。

## 目标

给定 $(A,C,L_0)$、$r=1$、$q=\omega+1$、$c=k-\omega=2$，判定是否存在 $L=[L_0;R]$ 满足
$(5a),(5b),\operatorname{rank}[C;L]=p+q$，并给出构造。

## 设想与理由：逐行提升

$H=L N_K$、$H_A=L A N_K$。对第 $i$ 行：
$$H_i=l_iN,\qquad H_{A,i}=l_iAN.$$
给定压缩行 $h_i$，所有满足 $l_iN=h_i$ 的 $l_i$ 是
$$l_i=l_i^{(0)}+g_i,\qquad g_i\in\operatorname{row}[C;CA]$$
（因为 $\operatorname{ann}(K_0)=\operatorname{row}[C;CA]$）。于是
$$\boxed{H_{A,i}=h_iAN+\Gamma(g_i),\qquad \Gamma(g)=gAN.}$$
**每一行的修正 $g_i$ 独立**；顶部行 $h_0=L_0N$ 固定、$g_0=0$。

## 做法

### 自由数据

1. $V\in\operatorname{Gr}(2,W_L)$，$W_L=\ker[L_0N;L_0AN]$（$V=\ker H$，顶部行必须湮灭 $V$）；
2. $H$ 的 $q=3$ 行，秩 $\omega=2$，核 $V$：取 $\operatorname{ann}(V)$ 的基 $u_0,u_1$（维 $2$），
   行 $h_i=a_i u_0+b_i u_1$，$i=0,1,2$，且 $h_0=L_0N$（固定）；
3. 修正 $g_i\in\operatorname{row}[C;CA]$，$i=1,2$（$g_0=0$）。

### 铅笔与条件

$$P(\lambda)_i=\lambda h_i-h_iAN-\Gamma(g_i),\qquad i=0,1,2.$$
- $(5b)$：$P(\lambda)$ 的秩 $\forall\lambda$ 等于 $\omega=2$
  $\iff$ 全部 $2\times2$ 子式的 gcd 为常数（且 $\operatorname{rank}P\equiv2$）；
- $(5a)$：$\ker H\subseteq\ker H_A$，即 $H_A v=0$ 对 $v\in V$；
- 秩条件：$\operatorname{rank}[C;L]=p+q$（用 152 的完成判据）。

### 构造 $L$

由 $h_i,g_i$ 解 $l_iN=h_i$（特解 + $g_i$），得 $L=[L_0;l_1;l_2]$；回代检验。

### 变量与搜索

- $V$：$\operatorname{Gr}(2,W_L)$（seeds 上 $W_L$ 2 维 → 唯一）；
- $a_i,b_i$：$H$ 在 $\operatorname{ann}(V)$ 中的系数（每行 2 个）；
- $g_i$：$\dim\operatorname{row}[C;CA]$（seeds 上 3）个系数，每行一套。

对 seeds（$k=4$，$\dim\operatorname{ann}(V)=2$，$\dim\operatorname{row}[C;CA]=3$）：
固定 $h_0$ 后，变量为 $(a_i,b_i)_{i=1,2}$（4 个）与 $g_1,g_2$（$2\times3=6$ 个），共 10 个；
可在小整数网格上搜，或固定 $V$ 后对 $g$ 做线性/符号消元。

## 实现状态（2026-11-08）

按本规格写了 v4 的**暴力搜索**（`c2_algorithm4.py`，scratch）：$V=W_L$、$H$ 在 $\operatorname{ann}(V)$ 的系数、
每行 $g_i$ 的小整数网格，逐组合算 $3\times k$ 铅笔的 $2\times2$ 子式 gcd。**太慢**（每个组合一次 sympy gcd，
组合数约 $2.6\times10^4$），已中止。下一步实现应：
1. 预计算每个子式的系数（λ 的二次多项式，系数是变量的多项式）；
2. 用快速有理多项式 gcd（自写 Euclid），不用 sympy；
3. 先固定 $g=0$ 扫 $H$，再对候选加 $g$，减少组合数。

**v5 快速 gcd 的初步扫描**（$g=0$、$H$ 系数 $\{-1,0,1\}$）：
* seed10：36 个秩 2 的 $H$ **全部可容许**，但 $3\times k$ 铅笔的 gcd **全部非常数**；
* seed16：36 个秩 2 的 $H$，**0 个可容许**（$g=0$ 不够，需要 $\Gamma$ 修正）；
* seed21：0 个秩 2 的 $H$（$\operatorname{ann}(V)$ 的基选取需避开与 $h_0$ 成比例的情形，实现待修）。
结论：$g=0$ 不够；必须在搜索中纳入 $g_i$（$\Gamma$ 修正），先修 seed21 的基选取，再做 $g$ 的联合搜索。

**v6 联合搜索（\(H\) 系数 + \(g_i\) 在 \(V\) 上线性求解）**：
* seed10：找到 **好铅笔**（\(a=(-1,0)\)、\(b=(-1,-1)\)、修正组合 \((1,0)\)）；
* seed16/21：所测网格内无可容许 \(H\)（需要更大网格或更多修正方向）。
* v7 干净重写后，seed10 **完整闭环成功**：
  $$a=(-1,-1),\quad b=(-1,1),\quad \text{修正组合 }(1,0),$$
  构造出的 \(L\) 通过 `check_candidate` 的七条检查（$(5a)$、$(5b)$、秩、域等）——
  **seed10 的 \(q=3\) 可行**（\(c=2\)、\(q=\omega+1\)）。这是算法第一次在真实实例上给出完整见证。
  见证 \(L\)（第一行 \(L_0\)）：
  $$L=\begin{bmatrix}0&0&-1&1&0&0&-3\\0&-1&0&0&-1&0&0\\2&-1&2&0&-1&0&0\end{bmatrix},$$
  可复现脚本：[tools/verification/c2_seed10_witness.py](../../../../tools/verification/c2_seed10_witness.py)（`python tools/verification/c2_seed10_witness.py` 输出 PASS）。
* seed16/21：所测网格内仍无可容许 \(H\)（需要更大网格，或它们 \(q=3\) 不可行，待定）。

## v8（正确公式）结果（2026-11-08）

按 $H_{A,i}=l_i^{(0)}AN+g_iAN$ 重写（$l_i^{(0)}$ 为 $h_i$ 的特解提升）后：
* seed10：**再次找到完整见证**（$a=(-1,0)$、$b=(-1,-1)$、修正组合 $(1,0,0)$），通过七条检查；
  这验证了更正后的公式；
* seed16/21：网格内 **adm=0**（修正方程在 $V$ 上无解）。说明需要把 $H$ 系数与 $g$ 的**可容许性**
  作为联合线性系统求解，而不是先枚举 $H$ 再解 $g$。

**v9 联合线性求解**：把 $(a,b,c)$ 一起作为未知量，解 $H_{A,i}|_V=0$（每行），再在解空间的自由参数上
随机采样算 gcd：
* seed10：线性系统相容（自由维 5,5），**再次找到完整见证**；
* seed16/21：线性系统**也相容**（自由维 4,4），但 600 个随机自由参数内无好铅笔——
  它们可能是 $q=3$ **不可行**，也可能好点很稀有；需在自由参数上做符号 gcd 判定。

## 进展

* 逐行公式 $H_{A,i}=h_iAN+\Gamma(g_i)$、变量清单、判据与构造已写清；
* 明确了 155 的两行约化为何错：$g_3$ 独立，第三行不能由前两行组合；
* 明确了 v2 的失败点：$H_A$ 被当作自由变量、$\omega$ 用顶部块。

## 最终结论

* $c=2,r=1,q=\omega+1$ 的可行性是一个**有限变量**的多项式 gcd 问题：
  $V$（$W_L$ 内）、$H$ 的系数、每行修正 $g_i$；
* 正确判据是 **3 行铅笔的全部 $2\times2$ 子式 gcd + 可容许性 + 秩完成**；
* 不存在“两行约化”。

## 放弃原因

* 未实现完整的 10 变量搜索；未做参数 gcd 的符号判定；
* 未处理 $r>1$、$\dim W_L>2$ 的一般情形。

## 残留价值

* 作为实现的唯一正确规格，替代之前散落的 v1–v3 叙述；
* 变量数小，可直接网格/线性搜索。

## 相关文件

* [attempts/152](152_lift_completion_fixed_l0.md)（提升、$H_A=HAN+\Gamma$）
* [attempts/155](155_c2_top_pencil_obstruction.md)（两行约化，已更正）
* [attempts/153](153_c2_complete_theorem.md)（$c=2$ 分类）

## 状态

* 规格：**[已证-纸面，M2]**。
* 实现/判定：**[未做]**。
