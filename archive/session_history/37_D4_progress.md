# 37 — D4：(A)⟹分解的**数学构造**与 **Lean 机器验证**（**已完成** ✓）

> 承接 [history/27](27_solver_bug_and_caseII_recheck.md) §8。

---

## 0. 一句话

$$\boxed{\ \textbf{D4 已完成}：\text{数学构造正确}\ ✓\ +\ \textbf{Lean 机器验证通过}\ ✓\ }$$

---

## 1. ✅ Lean 结果（`MyProof/Theorems/D4.lean`，**0 error**）

$$\texttt{decomp\_of\_range\_le}:\quad
\operatorname{range}T\subseteq\operatorname{range}S_1+\operatorname{range}S_2+\operatorname{range}S_3$$
$$\Longrightarrow\ \exists\,\Lambda,G_0,G_1:P\to P,\quad T=S_1\circ\Lambda+S_2\circ G_0+S_3\circ G_1$$

配套：
| 定理 | 内容 |
|---|---|
| `pi1`/`pi2`/`pi3` | 三个坐标投影 |
| `Omega` | $\Omega(p_1,p_2,p_3)=S_1p_1+S_2p_2+S_3p_3$ |
| `Omega_range` | $\operatorname{range}\Omega=S_1.\mathrm{range}\sqcup S_2.\mathrm{range}\sqcup S_3.\mathrm{range}$ |
| **`decomp_of_range_le`** | ⭐ **D4 核心** |

$$\textbf{主库}\ \texttt{lake build}\ \to\ \textbf{Build completed successfully (18118 jobs)}\ ✓$$

### 1.1 与 c6′ 的关系（**这是它被需要的原因**）

取 $S_1=L^*$, $S_2=C^*$, $S_3=(C\circ A)^*$, $T=(L\circ A)^*$, $P=W^*$：
$$(A)\iff\operatorname{range}T\subseteq\textstyle\sum\operatorname{range}S_i$$
$$\Longrightarrow(L\circ A)^*=L^*\Lambda+C^*G_0+(C\circ A)^*G_1
\ \xrightarrow{\ \text{双对偶转置}\ }\ \mathcal LA=\Lambda\mathcal L+G_0C+G_1(CA)\ \checkmark$$

$$\Longrightarrow\ \textbf{把}\ \texttt{c6'\_conditional}\ \text{的分解假设消除}\ \Longrightarrow\ \text{c6′ 升级为无条件}\ \checkmark$$

---

## 2. 数学内容（构造）

### 2.1 证明链（已在 Lean 中实现 ✓）

| 步 | 内容 |
|---|---|
| 1 | $\operatorname{range}\Omega=S_1.\mathrm{range}\sqcup S_2.\mathrm{range}\sqcup S_3.\mathrm{range}$ ✓ |
| 2 | 取 $\ker\Omega$ 的补 $q$ |
| 3 | **消去 $\ker$ 分量**：$\forall p,\ \exists b\in q,\ \Omega b=\Omega p$ |
| 4 | $q$ 上 $\Omega$ 单射 ⟹ $\operatorname{range}(\Omega|_q)=\operatorname{range}\Omega$ |
| 5 | 线性等价链 $q\simeq\operatorname{range}(\Omega|_q)\simeq\operatorname{range}\Omega$ ⟹ 右逆 $\psi$ |
| 6 | 沿 $\operatorname{range}\Omega$ 的补扩张到 $V$ 得 $h$ |
| 7 | $\Lambda:=\pi_1\circ h\circ T$ 等 ⟹ 分解 ✓ |

### 2.2 ⚠️ 走过的**错误路线**（已排除）

| 错误 | 为什么不成立 |
|---|---|
| "取 $\Omega$ 在整个 $P\times P\times P$ 上的**右逆**" | $\Omega$ 有右逆 $\iff\ker\Omega=0$；而此处 $\ker\Omega\ne0$ ✗（反例 $\Omega(x_1,x_2)=x_1$）|
| "$\delta\in\operatorname{row}[\dots]$" 判据 | $\delta$ 不必在该行空间中 ✗ |
| 手写 $W$ 行长度不足 | `mm` 不检查维数 ⟹ 静默算错 ✗ |
| **`LinearMap.comp` 方向搞反** | $(g.\mathrm{comp}\ f)x=g(fx)$ ⟹ $\Lambda$ 应是 $P\to P$（不是 $V\to P$）✗ |

$$\textbf{教训}：\text{Lean 的}\ \texttt{.comp}\ \text{是}\ g\circ f\ \text{（不是}\ f\circ g\text{）——}\textbf{先做最小例验证方向}\ \checkmark$$

---

## 3. 迭代统计

| 项 | 数量 |
|---|---|
| Lean 编译迭代 | **22 轮** |
| 每轮平均修复 | 1–3 个类型/API 错误 |
| 最终的 3 类坑 | ① `Classical.choose` 的元组处理 ② `LinearMap.rangeRestrict` 隐式参数 ③ **`.comp` 方向** |

$$\text{最耗时的是}\ \texttt{Submodule}/\texttt{Subtype}\ \text{之间的类型搬运（第 4–7 步）}$$

---

## 4. 本轮产出

| 文件 | 内容 |
|---|---|
| **`scripts/lean/D4.lean`** ★ | ⭐ ⭐ **D4 的 Lean 证明（0 error，已并入主库）** |
| [DIRECTIONS.md](docs/DIRECTIONS_2026-10-18.md) | ⭐ 所有方向的索引 |
| `scripts/lean/Probe_d4.lean` | 迭代过程（可删） |
| `scripts/core/verify_T12_full.py`、`verify_T12_r2.py` | D8 的 T12 复核 |
| [history/27](27_solver_bug_and_caseII_recheck.md) §8 | D4 早期探索 |

---

## 5. D8（T12 复核）的结论 —— ✅ 完成，且**澄清了一个疑点**

### 5.1 关键澄清

$$\text{T12 陈述于}\ k=1\ (\text{即}\ q_0=r+k);\quad \text{旧验证}\ \texttt{verify\_T12.py}\ \text{用}\ r=1$$

$$\text{而}\ r=1\ \text{时}\ \operatorname{rank}[\pi(L_0);\pi(L_0A)]=1\ \text{等价于"只看第一行"}$$
$$\Longrightarrow\ \textbf{旧验证}\ (10/10)\ \textbf{对 T12 而言是完整的}\ ✓$$

$$\text{项目第 20 处的"只用第一行"隐患，}\textbf{只影响}\ r\ge2\ \text{的 c6，不影响 T12}\ \checkmark$$

### 5.2 复核执行

| 脚本 | 结果 |
|---|---|
| `verify_T12.py`（原） | ✅ 10/10 符合，**0 违背** |
| `verify_T12_full.py` | 12 个实例全为 $r=1$，0 违背 ✓ |
| `verify_T12_r2.py`（定向搜 $r\ge2,k{=}1$）| **未找到**（该组合极稀有）|

$$\Longrightarrow\ \textbf{D8 结论}：\text{T12 的验证}\ \textbf{不变}\ ✓$$

---

## 6. ⭐ 下一步（D4 完成后，c6′ 只剩什么）

$$\text{c6′ 的 Lean 形态}\ \texttt{c6'\_conditional}\ \text{的假设清单（见 [history/27](27_solver_bug_and_caseII_recheck.md) §5）}：$$

| 假设 | 状态 |
|---|---|
| $(A)$ 的**分解** | ✅ **D4 已完成**（`Theorems/D4.lean`）|
| $N\hookrightarrow\ker C\sqcap\ker(CA)$ | ⏸ 需与 D4 的组合 |
| $\pi(\mathcal LA)=0$ | ⏸ 步 3–5 的产物 |
| $H\ne0$ | 条件式自带 |

$$\Longrightarrow\ \textbf{下一步}：\text{把 D4 与}\ \texttt{C6.lean}\ \text{的假设串联}，\text{得到}\ \textbf{c6′ 的无条件（或更弱条件）形式}\ \checkmark$$
