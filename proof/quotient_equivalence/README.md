# 商等价定理（Theorem Q）

> **对应 docs 条目**：H.1（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

> **2026-11-01 起本目录按约定组织**：[01_描述与意义.md](01_描述与意义.md)（命题与意义）、
> [02_证明.md](02_证明.md)（学术式证明）、[03_验证.md](03_验证.md)（Lean/精确验证）、
> [lean/](lean/README.md)（Lean 归档）。$d=0$ 的姐妹命题已分到 [../d0_boundary/](../d0_boundary/README.md)。与 $d=0$ 边界

> **状态**：**[已证-纸面]**（§2、§4）+ **[精确验证]**（§6：18 个 $Z$、27 个行列式恒等式、40 个 $D0$ 实例）
> + **[Lean]**（§2 的三步内核，`tools/lean/MyProof/QuotientEquivalence.lean`，`check_lean.sh` 退出码 0）。
> **脚本**：[`tools/verification/verify_quotient_equivalence.py`](../../tools/verification/verify_quotient_equivalence.py)（与本文逐条对应）。
> **起因**：专家 2026-11-01 复核的 **第 3 条（最重要）**——报告 v1 把铅笔要保的秩写成 $h-s$；
> 正确值是 $r+t$。这条决定了"用哪个矩阵、哪些子式"，不是文档措辞问题。
> 另：专家 §8 要求补一条 $d=0$ 边界的完整刻画，即本文 §4。

---

## 0. 一句话

$$\boxed{\ \operatorname{rank}\big[(\lambda I-A)V\mid Z\big]=\dim(V+Z)\iff \operatorname{rank}\big[U\mid P(\lambda)\big]=r+t\ }$$

其中 $U=Z/S$、$P(\lambda)=(A-\lambda I)|_{V/S}$。**秩是 $r+t$，不是 $h-s$**；
方阵条件 $r+t=w_m$ 等价于 $q=t$，而 $h-s=w_m$ 等价于 $h=w$（$L_0\subseteq\operatorname{row}C$ 的退化情形），两者无关。

---

## 1. 记号

| 符号 | 含义 | 公式 |
|---|---|---|
| $W$ | $\ker C$ | $w=n-p$ |
| $H$ | $\ker[C;L_0]$ | $h=\dim H$ |
| $V$ | $\ker[C;CA]$ | $v$ |
| $Z$ | $\ker[C;\mathcal L]$ | $d=w-q$ |
| $S$ | $Z\cap V$ | $s$ |
| $E$ | $H/S$ | $m=h-s$（**参数空间**，$U$ 住在里面）|
| $W_m$ | $W/S$ | $w_m=w-s$（**铅笔的底空间**）|
| $U$ | $Z/S$ | $r=d-s$ |
| $\overline V$ | $V/S$ | $t=v-s$ |
| $h_\Theta$ | $\dim(V+Z)$ | $=v+d-s=s+r+t$ |

正确的恒等式（**不是** $r+t=w-q$，那在 c282 上就假）：
$$r+t=w-q+v-2s,\qquad (r+t=w-s)\iff q=t,\qquad \text{在 }q=t\text{ 下 } m=r+t\iff h=w.$$

---

## 2. 定理 Q（商等价）

**定理**：设 $Z\subseteq H$、$\dim Z=d$、$S=Z\cap V$、$A(S)\subseteq Z$（即 $(A)$）。
令 $U=Z/S\subseteq W_m$、$P(\lambda)=(A-\lambda I)|_{V/S}\to W_m$。则对每个 $\lambda\in\mathbb C$
$$\operatorname{rank}\big[(\lambda I-A)V\ \big|\ Z\big]=\dim(V+Z)
\quad\Longleftrightarrow\quad
\operatorname{rank}\big[U\mid P(\lambda)\big]=r+t .$$

**证明**（四步；每步都是精确的维数/商运算）

1. 记 $M(\lambda)=[(\lambda I-A)V\mid Z]$，$n\times(v+d)$。因 $S\subseteq Z$，$Z$ 的列含 $S$ 的一组基，
   故 $S\subseteq\operatorname{col}M(\lambda)$，且 $\operatorname{rank}M(\lambda)=s+\dim(\operatorname{col}M(\lambda)/S)$。
2. 模 $S$ 后：$Z$ 的列张成 $Z/S=U$；$V$ 的列张成 $P(\lambda)$ 的像。
   提升的歧义是 $v\mapsto v+s$（$s\in S$），它把 $(\lambda I-A)v$ 改成 $(\lambda I-A)v+(\lambda I-A)s$；
   因 $\lambda S\subseteq S$ 且（由 $(A)$）$A(S)\subseteq Z$，有 $(\lambda I-A)s\in S+Z$，其模 $S$ 的类落在 $U$ 里。
   所以 $[U\mid P(\lambda)]$ 的**列空间**与提升无关，且
   $$\operatorname{col}M(\lambda)/S=\operatorname{col}\big[U\mid P(\lambda)\big].$$
3. 因 $V\cap Z=S$，商空间 $V/S$ 与 $Z/S$ 不交，故 $\dim(V+Z)=s+t+r$。
4. 合并：$\operatorname{rank}M(\lambda)=s+\operatorname{rank}[U\mid P(\lambda)]$，
   于是 $\operatorname{rank}M(\lambda)=\dim(V+Z)=s+r+t\iff\operatorname{rank}[U\mid P(\lambda)]=r+t$。$\square$

**为什么假设 $(A)$ 不能去掉**：没有 $A(S)\subseteq Z$ 时 $(\lambda I-A)s$ 的模 $S$ 类不落在 $U$ 里，
$[U\mid P(\lambda)]$ 的列空间**依赖提升**，左右两边的"秩"就不是同一个对象。$(A)$ 的作用正是让商铅笔良定义。

**推论（方阵）**：$r+t=w_m\iff q=t$。此时 $Q_U(\lambda)=[U\mid P(\lambda)]$ 是方阵，
条件 $\iff\det Q_U(\lambda)\ne0\ \forall\lambda\iff\det Q_U$ 为非零常数（多项式在 $\mathbb C$ 上无非零常数以外的"到处非零"）。

> **这正是判据矩阵的域条件**（[HANDOVER v2 §3](../../archive/handovers/HANDOVER_2026-11-01_v2.md)）：
> 单个 $\det$ 判据只在 $q=t$ 存在；$q\ne t$ 时矩阵是 $(w_m)\times(r+t)$ 的**宽**矩阵，
> 必须用"全部 $(r+t)$-子式的 gcd"。

---

## 3. 系数恒等式（$q=t$ 域）

$q=t$ 时 $\det[U\mid P(\lambda)]$（$w_m\times w_m$）按 $U$ 的 $r$ 列做 Laplace 展开：
$$\det[U\mid P(\lambda)]=\sum_{|I|=r}s_I\,p_U(I)\,\det P_{I^c}(\lambda)
=\sum_j\lambda^j\Big(\sum_{|I|=r}s_I\,p_U(I)\,a_j[I]\Big),$$
$s_I=(-1)^{\sum_{i\in I}(i+1)+r(r+1)/2}$ 是**逐坐标**符号（由坐标子空间 $U=\operatorname{span}(e_I)$ 定出），
$p_U(I)=\det U_{I}$。实现：[`coeff_of_S.laplace_sign`](../../tools/verification/coeff_of_S.py) 与 `coeff_forms_full`。
**等级**：纸面（Laplace 展开）+ [精确验证 27 例]（§6，每个 $I$ 都在基向量上验过，故对全部 $U$ 成立）。

---

## 4. 命题 D0（$d=0$ 的边界刻画）

**命题**：设 $d=0$（即 $q=w=n-p$，$Z=0$）。则 $(A)$ 自动成立，且
$$(S)\iff V\cap\ker(\lambda I-A)=\{0\}\quad\forall\lambda
\iff A\ \text{在}\ V\ \text{里没有特征向量}.$$
若还要求 $[C;\mathcal L]$ 行满秩且 $\mathcal L$ 含 $L_0$，则完整条件是
$$\operatorname{rank}[C;L_0]=p+r_0\quad\text{且}\quad V\cap\ker(\lambda I-A)=0\ \forall\lambda .$$

**证明**：$d=0$ 时 $S=Z\cap V=0$，故 $A(S)=0\subseteq Z$，$(A)$ 自动。
$(S)$ 变成 $\operatorname{rank}[(\lambda I-A)V]=v$ 对一切 $\lambda$；这就是 $(\lambda I-A)|_V$ 单射，
即 $\ker(\lambda I-A)\cap V=0$。最后一句：$L_0$ 的行必须与 $C$ 的行线性无关。$\square$

> **这一条直接解释第二实例**（$n=6,p=1$，$Ae_5=e_0$，$Ae_i=e_i\ (i\le4)$）：
> $e_1..e_4\in V$ 且是 $\lambda=1$ 的特征向量，故 $q=w=5$ **也不可行** ⟹ $q_{\min}=\infty$。
> 这与 [STATUS:9](../../STATUS.md) 的撤回一致；**"$q=w$ 时 $(5a)(5b)$ 平凡"是错的**——
> $Z=0$ 只让 $(A)$ 平凡，$(S)$ 仍有内容（$A$ 的特征值可以造成秩降）。

---

## 5. 与判据矩阵的关系

| 判据 | 域 | 强度 | 依据 |
|---|---|---|---|
| 全部 $(r+t)$-子式的 gcd 为非零常数 | 任意 $q$（$r+t\le w_m$）| $(S)$ 充要 | 定理 Q + 行列式因子 |
| $\det[U\mid P]$ 为非零常数 | $q=t$ | $(S)$ 充要 | 定理 Q 推论 + §3 |
| 系数判据 $p_U\in K,\ a_0(p_U)\ne0$ | $q=t$ | $(S)$ 充要（**还要"$p_U$ 可分解 + 可容许"**）| §3 + C1 |
| 线性松弛 $a_0|_K\ne0$ | 任意 $q$ | 只**必要**（C1 ⟹ C2）；$q\ne t$ 时对 $(S)$ 不必需 | C2 |

---

## 6. 验证记录（[精确验证]，脚本见上）

| 实例 | $(q,s)$ | 核对的 $Z$ 个数 | 秩不符 | det 恒等式 | 不符 |
|---|---|---|---|---|---|
| R17 | (3,2) | 3 | 0 | — | — |
| R17 | (2,2)（$q=t$）| 3 | 0 | 9 | 0 |
| R17 | (2,3) | 3 | 0 | — | — |
| c282 | (4,1) | 3 | 0 | — | — |
| c282 | (3,1) | 0（该 $(q,s)$ 下无 $U$：$(Z/S)\cap(G/S)=0$ 不可满足）| — | — | — |
| 第二实例 | (2,2)（$q=t$）| 3 | 0 | 9 | 0 |
| 第二实例 | (3,1)（$q=t$）| 3 | 0 | 9 | 0 |

- 构造方式：$S\subseteq V\cap D\cap H$（$D=\{x:Ax\in H\}$）、$U\supseteq A(S)/S$ 且 $U\cap V/S=0$
  ⟹ $Z=S\oplus U$ 自动满足 $(A)$（**不是随机采样**；薄集问题见 CLAUDE §7 第 12 条）。
- $\lambda\in\{0,\pm1,\pm2,3,1/2\}$ 逐点比较两个秩（含"同时失败"方向）。
- **命题 D0**：40 个随机对角整数实例（$n\le6$，$p\le2$），"gcd 为常数"与"$V$ 无特征向量"**40/40 一致**。

**这些覆盖不到什么**：$\lambda$ 只取了 7 个点——$\forall\lambda$ 的结论来自 §2 的纸面证明，不是来自逐点检查；
$q\ne t$ 的等价（gcd 判据）用的是行列式因子（Smith 形）理论，未在本文重证。

---

## 7. 复现

```bash
python tools/verification/verify_quotient_equivalence.py
# 期望：Theorem Q ✓  系数恒等式 ✓  命题 D0 ✓（18 个 Z、27 例 det、40/40）
```

## 8. 文献位置

- 专家复核（2026-11-01）§3 提出维数问题、§8 提出 $d=0$ 边界；本文是它们的完整版本。
- 行列式因子/Smith 形用于"固定 $U$ 的谱判据多项式可判"：Kaltofen–Krishnamoorthy–Saunders（并行 Hermite/Smith）、
  Storjohann–Labahn（多项式矩阵 Smith 形的 Las Vegas 算法）。

---

## 9. 复杂度含义（2026-11-01 补）

| 层 | 判定 | 复杂度 | 实现 |
|---|---|---|---|
| **固定 $U$** | $\Delta_{r+t}$ 是否非零常数（Smith 形/行列式因子）| **多项式**（精确算术模型，$\mathrm{poly}(w_m,r+t,\deg)$）| [poly_smith.py](../../tools/verification/poly_smith.py)，交叉验证 [verify_smith.py](../../tools/verification/verify_smith.py)（84 随机 + 86 铅笔，0 不一致）|
| **$\exists U$** | Grassmannian 上的存在性 | **未知**（只有 $\in\exists\mathbb R$ 上界）| — |

$$\boxed{\ \text{所以 }q1\ \text{的全部难度落在 }\exists U\ \text{（以及 }\exists Z\supseteq U\text{）上，不在谱判据里}\ }$$

两点限定：(i) "多项式"是对**精确算术**说的，输入须是可有效表示的系数（本项目用 $\mathbb Q$）；
(ii) 界里含系数增长项，实现里用 `ScaleError` 在 $14\times12$ / 次数 $>10$ 时退回枚举路径并**打印**。

## 10. 复现

```bash
python tools/verification/verify_quotient_equivalence.py   # Theorem Q / 系数恒等式 / D0
python tools/verification/verify_smith.py                 # Smith vs 枚举子式 vs 逐点秩
```
