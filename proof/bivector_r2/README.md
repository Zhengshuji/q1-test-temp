# $r=2$ 的双向量问题（可分解性的第一道非线性门槛）

> **对应 docs 条目**：K.1（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

> **状态**：三条命题 [已证-纸面]（§2–§4），算法 [精确验证]（§6，可靠性交叉核对）。
> **脚本**：[`tools/verification/bivector.py`](../../tools/verification/bivector.py)、
> [`verify_bivector.py`](../../tools/verification/verify_bivector.py)、
> [`c302_bivector_m5.py`](../../archive/attempts_2026-10/A3_basefamily/scripts/c302_bivector_m5.py)。
> **动机**：专家 2026-11-01 §5.3 —— 这是 $q1$ 的第一个真正非线性靶子；$r=1$ 时 Plücker 条件为空。

---

## 0. 一句话

$r=2$ 时"$U$ 存在"$\iff$ 线性空间 $K\subseteq\Lambda^2E$ 含**非零可分解元**（斜对称矩阵秩 $\le2$）。
**$m=3$ 恒真、$m=4$ 恒真（$\ell\ge2$）、$m\ge5$ 且 $\ell\ge N-(2m-4)$ 恒真**；只有 $m\ge5,\ \ell\le3$ 需要计算。

$$\boxed{\ \text{可分解性在 }r=2\text{ 的"大半"情形里是自动的 ⟹ hardness 不可能来自它：只能来自可容许性}+\exists S\ }$$

---

## 1. 设定

$E=\mathbb C^m$，$N=\binom m2$，$K\subseteq\Lambda^2E$ **复线性**子空间，$\ell=\dim K$。

> **实/复说明（专家 2026-11-01 §3.3）**：下面的"必有可分解元"全部是**复**意义（$E=\mathbb C^m$）。
> 若最终要求**实**观测器，射影维数定理只保证复交点，需要额外的实点论证——这是**独立缺口**，不在本文覆盖内。
$p\in\Lambda^2E$ 对应斜对称矩阵 $M(p)$；$p$ 可分解 $\iff\operatorname{rank}M(p)\le2$ $\iff$ 全部 $4\times4$ 主 Pfaffian 为零。
$\mathrm{Gr}(2,m)\subset\mathbb P^{N-1}$ 的维数是 $2m-4$。

在 $\mathrm{DEC}(q)$ 里：$K=\bigcap_{j\ge1}\ker a_j$（系数判据的线性部分），$p=p_U$ 是 $U$ 的 Plücker 坐标；
"$U$ 可容许"另含 $T_S\subseteq U_p$（**线性**）与 $U_p\cap(G/S)=0$（**开条件**）。

---

## 2. 命题 K1（$m=3$：可分解性无约束）

$m=3$ 时 $\dim\Lambda^2\mathbb C^3=3=\dim\mathrm{Gr}(2,3)+1$，且 $\mathrm{Gr}(2,3)=\mathbb P(\Lambda^2\mathbb C^3)$ 是**整个**射影空间。
故每个非零双向量都可分解。**等级**：[已证-纸面]。

> 这条解释了 [c301](../../archive/attempts_2026-10/A3_basefamily/scripts/c301_g3_square.py) 的 $m=3$ 实例为什么测的是"可容许性"：
> 那里的 $D_{\rm adm}(K)=0$ 与可分解性无关（$K$ 里每个点都可分解）。

## 3. 命题 K2（$m=4$：$\ell\ge2$ 时恒真）

$K\subseteq\Lambda^2\mathbb C^4$，$\dim K=\ell\ge2$。$\mathrm{Gr}(2,4)$ 是 Klein 二次超曲面
$$q(p)=p_{12}p_{34}-p_{13}p_{24}+p_{14}p_{23}.$$
$q|_K$ 是 $\ell$ 元二次型；$\mathbb C$ 代数闭 $\Rightarrow$ **任意 $\ge2$ 元二次型都有非零零点**（取一条射影直线，二次型在 $\mathbb P^1$ 上必有根）。
故 $\exists\,0\ne p\in K$ 可分解。$\ell=1$ 时退化为 $q(p_0)=0$ 的一次判定。**等级**：[已证-纸面] + [精确验证 20/20]（`verify_bivector.py`）。

## 4. 命题 K3（维数计数：$\ell$ 大时恒真）

若 $K\subseteq\Lambda^2E$ 满足 $\ell\ge N-(2m-4)$，则 $K$ 含非零可分解元。
*证明*：若 $\mathbb P(K)\cap\mathrm{Gr}(2,m)=\varnothing$，则从 $\mathbb P(K)$ 的投影给出态射
$\mathrm{Gr}(2,m)\to\mathbb P^{N-1-\ell}$，故 $2m-4\le N-1-\ell$，即 $\ell\le N-1-(2m-4)<N-(2m-4)$，矛盾。$\square$
**等级**：[已证-纸面]（$m=5$ 时给出 $\ell\ge4$ 恒真）。

---

## 5. 剩下要算的：$m\ge5,\ \ell\le3$

| $\ell$ | 判据 | 复杂度 |
|---|---|---|
| 1 | $\operatorname{rank}M(p_0)\le2$ | $O(1)$ |
| 2 | $q_i(p_0+t p_1)$（5 个二次式）的 **gcd $\ne1$**（外加 $t=\infty$）| 一元多项式 gcd |
| 3 | $\mathbb P^2$ 上 5 个二次型：$(x,y,z)^s\subseteq I$ ⟹ **无**公共零点（可靠 NO）；找到有理点 ⟹ **有**（可靠 YES）；都不是 ⟹ 未决 | 次数匹配的理想成员判定（线性代数）|

$m>5$ 时把 4-子集换成 $\binom m4$ 个 Pfaffian；$\ell\le3$ 的算法同样适用（$\mathbb P^2$ 上的二次型组）。

---

## 6. 验证记录（[精确验证]，可靠性而非完备性）

`verify_bivector.py` 检查"算法不说谎"：判 `False` 的必须在小整数格点上**找不到**可分解元；给了见证的必须**确实**可分解。

| 检查 | 结果 |
|---|---|
| 随机 $K$（$m=3,4,5$；$\ell=1,2,3$）| 65 判 True、43 判 False、**0 未决**；无"说谎"情形 |
| $m=4,\ell=2$ 恒真（K2）| 20/20 ✓ |
| 有解/无解示例 | 各至少一个（非空检验）|

**覆盖不到**：格点搜索只能证伪；$\ell=3$ 的"未决"不是错误，是算法的诚实输出。

---

## 7. 实例层（`c302`，$m=5$）与一个新的观察

构造：$n=9,p=2$、$C=[e_1;e_2]$、$L_0=e_3$，随机搜索到 $v=5$、$h=6$、$\dim(V\cap D\cap H)=3$ 的 $A$。
于是 $s=1$、$q=4$、$d=3$、$r=2$、$t=4$、$m=5$、$w_m=6$（$q=t$ 方阵域 ✓）。

| 量 | 值 |
|---|---|
| $\dim K$（系数条件）| 6 |
| $\dim K'$（再加线性可容许 $T_S\subseteq U_p$）| 2 |
| `has_decomposable(K',5)` | **True**（5 个限制二次式的 gcd 次数 2）|
| 枚举到的可容许 $U$（$720$ 个）/ 其中 $\det$ 为非零常数 | 720 / **0** |
| 有理见证 | **无**（gcd 无有理根）|

$$\boxed{\ \text{可分解点在，但参数在二次扩张里——所以"用有理格点搜 }U\text{"必然漏掉它}\ }$$

这条对项目有直接后果：**"$\exists$ 可容许 $U$"的精确判定不能只靠有理数搜索**；
要么把判据写成代数条件（本节的 gcd/理想判定），要么承认见证可能需要代数数。
它同时是"薄集不许采样"（CLAUDE §7.12）的又一个实例。

---

## 8. 复现

```bash
python tools/verification/verify_bivector.py
python archive/attempts_2026-10/A3_basefamily/scripts/c302_bivector_m5.py
```

## 9. 与 $q1$ 的关系

- 若 $m\le4$ 或 $\ell$ 大，可分解性**自动**成立 ⟹ $r=2$ 的难度在可容许性（$U\cap B=0$ 是开条件）与 $\exists S$；
- 若 $m\ge5$ 且 $\ell\le3$，可分解性是**真的**约束，但这里给出的是**判定算法**（固定 $\ell$ 时是常数规模），
  不是复杂度结论——`$\exists K$`（Grassmannian 上的搜索）仍未解决。
