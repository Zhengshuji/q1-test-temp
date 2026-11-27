# A-1 前置清单（分支 4 → 分支 1 交接）

> 由分支 4（E-1：Smith/Hermite 文献 + adapted basis 验证）产出。
> **目的**：让分支 1 在做 A-1（逐 $U$ 验证行列式恒等式）时不再踩已踩过的坑。

---

## 0. 一句话结论

$$\boxed{\ \text{固定 }S\text{ 可行的判据}=\gcd\big(\text{all }(r+t)\text{-minors of }[U\mid P(\lambda)]\big)\in\mathbb C^\times\ }$$

——即 `tools/verification/coeff_of_S.py` 的 `feasible_by_minors` ✓。
**"单行列式"版本只在 $q=t$ 时成立**，且那时它给出的仍只是**充分**条件（缺可分解性）。

---

## 1. 三个条件，按顺序检查

### (C1) 方阵条件：$q=t$

$$[U\mid P(\lambda)]\ \text{是}\ (w-s)\times(r+t);\qquad r+t=w-s\iff q=t.$$

- **不是** $r+t=m=\dim(H/S)$（这是分支 4 之前误用的条件）；
- **不是** $q\le t$。
- 脚本里必须 `assert r + t == w - s`（否则单行列式无意义）。

### (C2) 平衡/非平衡

| 情形 | 判据 |
|---|---|
| $q=t$（方阵）| $\det[U\mid P(\lambda)]$ 是非零常数 |
| $q\ne t$（非方阵）| **全部** $(r+t)$-子式的 gcd 是常数（`feasible_by_minors`）|
| $r+t>w-s$ | 恒不可行 |

### (C3) 可分解性（QA25，**独立于坐标**）

$$a_0\notin\operatorname{span}\{a_j\}\iff K\not\subseteq\ker a_0\ \text{（线性代数）}$$
但真可行性要求 $p_U$ **可分解**：
$$\text{真条件}\iff D(K)\not\subseteq\ker a_0,\qquad D(K)=\operatorname{span}\{\text{可分解点}\}.$$
**只有 $D(K)=K$ 时线性判据才成立**——这就是 G3。$r=1$ 时自动成立；$r\ge2$ 时必须单独查。

---

## 2. 已验证的事实（可直接用）

| 事实 | 证据 |
|---|---|
| `adapted_basis` 给出 $T$ 使 $T^{-1}(H/S)=\operatorname{span}(e_1..e_m)$ | `verify_adapted_basis.py`（c282 ✓）|
| 换基缩放 $\det[U_{\rm new}|P_{\rm new}]=\det(T^{-1})\det[U_{\rm old}|P_{\rm old}]$ | `verify_square_case.py` 6/6 ✓（两个方阵实例）|
| **截断（只用前 $m$ 行）是错的** | 同上，**0/6** ✗ |
| `feasible_by_minors` 与逐 $U$ 的 `spectral_gcd` 一致 | c282 的 80 个点 0 不一致 |
| **行列式恒等式** $\det[U\mid P(\lambda)]=\pm\sum_j\lambda^j\langle a_j,u\rangle$（方阵、$r=1$）| `verify_det_identity.py`：第二实例 $q=2$、$q=3$ 各 **8/8** ✓ |
| **同一恒等式，$r=2$**（R17 $q=2,s=2$）| `verify_det_identity_r2.py`：**8/8** ✓ |
| **同一恒等式，$r=3$**（$p=3$ 的两个实例）| `verify_det_identity_r3.py`：**8/8 ×2** ✓；符号是**逐坐标** $s_I=\pm1$ |

---

## 3. 已踩过的坑（不要重复）

| # | 坑 | 症状 |
|---|---|---|
| 1 | 缺 $U\cap G=S$ 的可容许性 | 假阳性 |
| 2 | $G$、$D$ 用"基"当"零化子" | `S ⊄ H` 断言失败 |
| 3 | 删行代替换基 | 随机实例全错（c282 恰好对）|
| 4 | 适用条件写成 $r+t=m$ | 单行列式用错 |
| 5 | 忘了把 $P$ 也做换基 | 缩放恒等式 1/6 |
| 6 | 想"截断到前 $m$ 行" | 0/6 |
| 7 | 混淆 Plücker 空间与向量空间（$K$ vs $G/S$）| 类型错误 |

---

## 4. A-1 的具体做法（建议）

1. **只做方阵情形**（$q=t$）先：判据干净、无截断、无换基需求；
2. 对每个 $U$（$r=1$ 先做）：
   - 算 $\det[U\mid P(\lambda)]$（多项式）；
   - 算 $\sum_j\lambda^j a_j(p_U)$（用 `coeff_forms`，$p_U$ = $U$ 的 Plücker 坐标）；
   - **逐系数比较**，必须**恒等**（不是"相差常数"——因为这里不换基）；
3. 再做 $r\ge2$：$[U\mid P]$ 的列是 $r$ 个 $U$ 列 + $t$ 个 $P$ 列，行列式对 $p_U$ 线性 ✓；
4. 最后做非方阵（$q\ne t$）：用 `feasible_by_minors` 对照。

**验收（按用户标准）**：这一步只能到"精确验证"；要达标必须 Lean 化（D-1）。

---

## 5. 与 Lean 的关系

| 内容 | Lean 可行性 |
|---|---|
| 行列式恒等式（固定 $U$）| 中（需要多项式矩阵行列式 + Plücker 展开）|
| $\gcd$ 判据 | 难（需要 $\mathbb C[\lambda]$ 的 gcd）|
| 可分解性（$D(K)=K$）| 难（Grassmannian）|

**建议**：先把"方阵情形的行列式恒等式"作为 Lean 的第一个目标（D-1 的试点）。

---

## 6. 相关文件

- 判据实现：`tools/verification/coeff_of_S.py`（`feasible_by_minors`、`adapted_basis`、`coeff_forms_of_S`）
- 验证脚本：`workspace/A3_basefamily/scripts/verify_adapted_basis.py`、`verify_square_case.py`
- 文档：A2 §27（gcd 判据）、§33–§40（系数判据的适用范围与更正）
- 文献：`literature/notes/LIT_SMITH_HERMITE_2026-11-01.md`
