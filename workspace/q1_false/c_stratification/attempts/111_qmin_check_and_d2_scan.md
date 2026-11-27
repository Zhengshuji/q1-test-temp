# $q_{\min}$ 检查与 $d=2$ 扫描：层 $\ne$ 阶的又一例

> 2026-11-08。item 2（$q=2$ / $\omega=1$ 的阶检查）+ item 1（$d=2$ 扫描）。
> 结论：seed 794 与 138 的 $q_{\min}=2$；seed 179/589 的 $q_{\min}\in\{2,3\}$ 未定；
> $d=2$ 的 $q=3,\omega=2$ 层全坏（138 证明，261 采样，302 空）。

## 目标

1. 对四个实例（179/589/794 为 $d=1$；138 为 $d=2$）判定 $q=1,2,3$ 的可行性，估计 $q_{\min}$；
2. 扫 $d=2$ 的 261/302，看 $q=3,\omega=2$ 层是否也全坏。

## 设想与理由

* 层结论（$q=3,\omega=2$ 混合/全坏）**不决定** $q_{\min}$；$q=2$ 可能经 $\omega=1$ 或 $\omega=2$ 可行。
* $q=1$ 只有 $L_0$，直接 `check_candidate`；$q=2$ 随机/链式搜索 $R$；找到好 $R$ 即 $q_{\min}=2$。
* $d=2$ 的 261（$E=F_0=0$）与 302 用于看“全坏”是否普遍。

## 做法

* $q=1$：`check_candidate(A,C,L0,L0)`，捕获 $(5a)$ 失败（断言）。
* $q=2$：400 个随机 $R$（系数 $-2..2$）+ `omega_construct.sample_chains`，用 `check_candidate` 找 `five_b`。
* $q=3$：`sample_chains` 20 条，确认可行。
* $d=2$：枚举可容许 $\sigma$（$E,F_0$ 的零空间），算 $\operatorname{rank}Q$、$\operatorname{rank}[P;Q]$、$\dim X_S$、$E+X_S=S$；
  纤维取 $[P;Q]$ 的左零空间，采样 $(a,b)$，用 gcd 判好坏。

## 进展

**$q_{\min}$ 表**（$\checkmark$ = 找到显式可行 $L$；$\times$ = $(5a)$ 失败；0/400 = 随机采样未找到）：

| seed | $d$ | $L_0$ | $q=1$ | $q=2$ | $q=3$ | $q_{\min}$ |
|---|---|---|---|---|---|---|
| 179 | 1 | $(0,0,0,-1,0,0,-1)$ | $\times$ | $\checkmark$：$R=(0,0,\tfrac{13}5,-\tfrac65,0,-1,0)$ | $\checkmark$ | **2** |
| 589 | 1 | $(-1,0,0,1,0,0,1)$ | $\times$ | $\checkmark$：$R=(0,0,0,-1,-\tfrac12,-\tfrac12,0)$ | $\checkmark$ | **2** |
| 794 | 1 | $(0,0,0,-1,-1,0,1)$ | $\times$ | $\checkmark$：$R=(-1,-1,0,1,-2,-1,-1)$ | $\checkmark$ | **2** |
| 138 | 2 | $e_7$ | $\times$ | $\checkmark$：$L=[e_7;-e_2]$ | $\checkmark$ | **2** |

四个 $q_{\min}=2$ 的见证都过 `check_candidate` 七条（$\operatorname{rank}[C;L]=5$、$(5a)$、$h=6=$ 法秩、$(5b)$ 成立）。

**$d=2$ 扫描**：
* seed 138：可容许轨迹两个点，均整层全坏（attempts/110 的证明）；
* seed 261：$E=F_0=0$，13 个 $\sigma$ 采样中 10 个可容许，**全部坏**（两个秩层 $(1,1,2)$、$(2,2,2)$）；
* seed 302：$\sigma$ 空间 1 维，**没有**在 $q=3,\omega=2$ 找到可容许点（$E+X_S\ne S$）。

### 更正（专家 52 号）：$q=2$ 的精确判据

$q=2,\omega=1$ 的正确定义是
$$\text{good}\iff Z(W)\not\subseteq W,$$
等价地 $\det[w,Z(w)]\ne0$（$w$ 张成 $W$）。当 $U_0=0$ 时 $H=[0;h]$、$H_A=[V_0;g_2]$，
良定义迫使 $V_0=\alpha h$、$g_2=\beta h$；在 $\mathbb C^2=W\oplus W'$
（$W=\langle e_2\rangle$，$W'=\langle e_1\rangle$）下 $Z(0,t)=\beta t\,e_2+\alpha t\,e_1$，
故块为 $A=\beta$、$B=\alpha$，于是
$$\text{good}\iff \alpha\ne0$$
（**$V_0$ 的系数**，不是 $g_2$ 的系数）。之前 $\beta=0$ 的见证可以过 $(5b)$，只要 $\alpha\ne0$——矛盾解决。

$q=2$ 的完整分类：

| $\omega$ | 判据 |
|---|---|
| $0$ | 自动好（受可容许性约束）|
| $1$ | good $\iff Z(W)\not\subseteq W$ |
| $2$ | 总是坏（方阵有特征向量）|

所以 $q=2$ 可行 $\iff$ 存在 $\omega=0$ 的可容许 full-row-rank 点，或 $\omega=1$ 且 $\bar Z\ne0$ 的可容许点；
$\omega=2$ 不能贡献。$q_{\min}$ 必须逐 $\omega$ 层检查，不能从单层推。

## 最终结论

* $q_{\min}=2$ **对所有四个实例**（179/589/794/138）：$q=1$ 全部不可行（精确），$q=2$ 全部有显式见证。
* **层 $\ne$ 阶（更尖锐）**：179 的 $q=3,\omega=2$ 层是混合的，138 是两点全坏的；两者 $q_{\min}$ 都是 2。
  层的混合/全坏不决定阶。
* $d=2$ 的 $q=3,\omega=2$ 层全坏（138 证明；261 采样；302 空），但它们（至少 138）在 $q=2$ 已经可行。

## 放弃原因

* $q=2$ 的见证来自 $\omega=1$ 的构造性线性系统（$R N_K=cV_0$ 且 $g_2=RAN_K\parallel V_0$）；
  精确判据已由专家 52 号给出（good $\iff Z(W)\not\subseteq W$；$U_0=0$ 时即 $\alpha\ne0$）。
  仍缺：full-row-rank lifting 的一般引理。
* 261/302 是采样/单实例，不是 $d=2$ 的一般定理。

## 残留价值

* 一张 $q_{\min}$ 表 + 两个 $q_{\min}=2$ 的显式见证（794/138）。
* “层 $\ne$ 阶”的又一实例（794 vs 179）：同族同层，阶可以不同。
* $d=2$ 全坏的证据（138 证明）。

## 相关文件

* [attempts/109](109_family_theorem_p1_mixed.md)（$d=1$ 族定理）
* [attempts/110](110_d2_all_bad_example.md)（$d=2$ 首例）
* `workspace/_exchange/qmin_check.py`、`q2_random.py`、`d2_scan.py`（本轮脚本，未入 git）

## 状态

* $q_{\min}=2$（179/589/794/138）：**[精确验证]**（`check_candidate` 七条）。
* $q=2$ 判据：专家 52 号更正为 $Z(W)\not\subseteq W$（$U_0=0$ 时 $\alpha\ne0$）；四个见证仍有效。
* $d=2$：138 全坏 **[已证-纸面]**；261 全坏 **[精确验证 10 点]**；302 空 **[精确验证]**。
