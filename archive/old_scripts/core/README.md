# scripts/core — 可运行脚本（41 个）

> **定位**：本目录只放**结论仍然有效**的脚本（库 / 复现装置 / 结论依据）。
> 被取代的实验脚本已归档到 [`../../history/scripts/2026_10_experiments/`](../../history/scripts/2026_10_experiments/)（259 个），
> 更早的两批在 [`../../history/scripts/`](../../history/scripts/) 与 `archive_early/`。
> 归档脚本**没有修改**：它们用 `__file__` 定位库文件，**在原位置才能跑**。

---

## 使用前必读

1. **不要移动或改名本目录的文件**：脚本用 `_HERE = dirname(__file__)` 定位库，
   移动脚本到子目录即失效；库文件（`exact_count_thm7.py` 等）被 20+ 个脚本共用。
2. **Python**：本机 `python` 3.12（anaconda）。`numpy`/`sympy` 实测可用，
   但**结论性判定一律用本目录的精确有理算法**（`Fraction` + 子式 gcd），不要用浮点或 sympy 的泛型秩。
3. **不要用旧 `condS` 判据**检验 (5b)：必须用 `exact_gcd.cond_5b`。它现在同时检查
   **上界**（$(ρ+1)$ 阶子式恒零）与**下界**（$\rho$ 阶子式 gcd 为非零常数）；
   只查 gcd 会在 $F\ne\Lambda M$ 时产生假阳性（见 `proof/5b_upper_bound/`）。
4. 新增脚本请在下表登记"支撑哪条结论"，否则下次整理会被当作实验脚本归档。

---

## 一、库（5）

| 脚本 | 作用 |
|---|---|
| **`exact_count_thm7.py`** | 根库：`rk`/`toF`/`p1`/`condA`/`orb`/`mm`/`tr`/`inv`/`ker_basis`/`build_norm_T`。⚠️ 其 `solve` 的零空间基**不满足残差**，勿用它展开解集 |
| **`exact_gcd.py`** | (5b) 的唯一正确判据 `cond_5b`：**上界**（$(ρ+1)$ 阶子式恒零）+ **下界**（$\rho$ 阶子式 gcd，过滤零多项式）；`cond_5b_diagnose` 可定位哪边失败；含 5 个回归用例 |
| **`linalg_q.py`** | 独立精确线代层：维数断言 + **强制残差校验**（`solve` 失败即 raise）——关键判定的标准底座 |
| **`linalg_exact.py`** | 另一个独立实现（Gauss-Jordan），用作**交叉裁判** |
| **`reliable_S_test.py`** | ⭐ 最常用：(S) 判据 + 按 $d_{CA}$ 分情形实验 + 扰动开性 + **内置地基检查**（三块约化 ≡ 原始 4 块） |

## 二、一键复现 / 验证器（9）

| 脚本 | 验证什么 | 期望 |
|---|---|---|
| **`verify_all.py`** | 无穷族 $n{=}4..10$、$k{=}0$ 见证、NO 侧一致性（**完全独立实现**，不 import 项目库） | 全 ✓，exit 0 |
| **`verify_equivalences.py`** | 四条等价关系（(5a)⟺核条件；(5b)⟺(S)；(5b)⟺$\operatorname{rank}\mathcal L P_\lambda$ 恒定；(5a)⟺几何避让） | 各 400/400 |
| **`verify_family.py`** | 任意 $n\ge4$ 都有 YES 实例（情形 II，$k{=}1$） | $n{=}4..10$ 全 ✓ |
| **`exact_gcd.py`** | (5b) 判据的 5 个回归用例（含上界假阳性、ρ=0、合法 (5b)） | 全部通过 |
| **`verify_pencil_v2.py`** | 铅笔既约形式 $(\text{A})\iff q_i\in\operatorname{row}P$ | 31/31 × 8 |
| **`verify_T12.py`** / **`verify_T12_full.py`** / **`verify_T12_r2.py`** | T12（情形 II 不平行 ⟹ 判定 NO） | 10/10、140 样本、0 秩降 |
| **`verify_witness_independent.py`** | $k{=}0$ 见证的**完全独立**复核（自带 Fraction 消元/多项式算术） | 13/13 |
| **`verify_witness2_independent.py`** | 支 B 见证的独立复核 | 14/14 |

## 三、主判据的两侧证明 + 审计（9）

| 脚本 | 支撑的结论 |
|---|---|
| **`c79_LAW_PROOF.py`** | 充分性（构造 $A_0{=}I$、$A_1{=}A'{+}B$ + pole placement） |
| **`c80_NECESSITY_PROOF.py`** | 必要性 A20（$\alpha_0\in V$） |
| **`c81_AUDIT_pbh.py`** | A19 步 1–2（PBH 等价）的审计 |
| **`c86_RECHECK.py`** / **`c87_AUDIT_FIXED.py`** | 修正 gcd bug 后的重跑（60/60 一致） |
| **`c39_construction.py`** | 充分性的构造性版本（5/5） |
| **`c43_diagnose_necessity.py`** / **`c44_rank_vs_5a.py`** | 按 $\operatorname{rank}(A_0)$ 分层的必要性诊断（3/3） |
| **`c139_liftability_scan.py`** 🆕 | 卡点扫描：固定实例下逐个合格 $\mathcal A$ 判 "(b)-liftable"（$d{=}3,\rho{=}2,q{=}3$），见证用原始判据复核 |
| **`c140_p6b_counterexample.py`** 🔴 | **P6b 的反例**（sympy 独立复核）：$\mathcal AA'\subseteq\mathcal A$ 却有 (5a)∧(5b) ⟹ 见 [`../../archive/2025-10_旧工作/proof/I_P6b_反例_2026-10-20.md`](../../archive/2025-10_旧工作/proof/I_P6b_反例_2026-10-20.md) |
| **`c141_invariant_family.py`** 🆕 | 检验 $\mathcal A=\langle\alpha_0,\beta_0,S\rangle_{A'}$ 在 $q=\rho+1$ 处是否 liftable（20/20 与 $\alpha_0\in V$ 一致）⟹ [`../../archive/2025-10_旧工作/proof/J`](../../archive/2025-10_旧工作/proof/J_不变族检验_2026-10-20.md) |
| **`c142_rho1_family.py`** 🆕 | $\rho{=}1$ 层：构造 $\beta_0\propto\alpha_0$ 的实例并检验 $q{=}2$（0/24，说明可行集是薄的；$n{=}7$ 的例子成功）⟹ [`../../archive/2025-10_旧工作/proof/J`](../../archive/2025-10_旧工作/proof/J_不变族检验_2026-10-20.md) §6 |
| **`c143_rho1_family_n7.py`** 🆕 | 在计数允许区（$p{=}2,n{=}7,d{=}3$）批量构造：$q{=}2$ 仍 0/30，原因是 $\forall\ell\in V_{\mathcal A}:\mu=ct$ ⟹ [`../../archive/2025-10_旧工作/proof/K`](../../archive/2025-10_旧工作/proof/K_维数计数_2026-10-20.md) §6 |
| ⛔ **`c156_modular_lift.py`** | **不可用**：$(b)$ 用随机 $\lambda$ 采样 ⟹ 系统性假阳性（(b) 的失败集是有限点集）。**勿引用其任何结果** |
| ⚠️ **`c157_modular_gcd.py`** | **半成品**：改用多项式 gcd 判 $(b)$（思路正确），但实现有性能/死循环问题，未通过校准。**暂勿引用**；精确有理数版（`c141`/`c154`/`c155`）才是可信的 |
| ⚪ `c153_m_scan.py` | **已被取代**：扫 $\mathcal A\cap S$ 的线族；与项目 `c135`/`c136` 重复，结论并入 [proof/S](../../archive/2025-10_旧工作/proof/S_维数下界定理_2026-10-21.md) §7.2 |
| **`c161_upper_bound_grid.py`** ⭐⭐ | 上界构造在任意 $(p,d)$ 上的验证：$\mathcal A$ 构造 + c160 的 lift + 精确 $(5a)(5b)$。已通过 $(1,4),(2,4),(2,5)$（$n\le9$；$n\ge10$ 精确算术过慢）|
| **`c159_admissibility_equivalence.py`**' ⭐⭐ | 验证 §1.5：admissible 时 $(L\text{-}1)\iff\mathcal A+S=\mathbb R^d$（饱和 46 例 / 非饱和 7 例，0 违反）|
| **`c158_lower_bound_audit.py`** ⭐⭐⭐ | **下界的单一验证入口**：[C1] 恒等式 42/42、[C2] (L-1) 42/42、[C3] (L-2) 18/18（[`../../archive/2025-10_旧工作/proof/S`](../../archive/2025-10_旧工作/proof/S_维数下界定理_2026-10-21.md)）|
| **`c155_dimension_law.py`** ⭐⭐⭐ | **维数下界定理**：$\dim\{\ell N\}=2\rho-d+p-|\mathcal A\cap S|$（16/16）⟹ $\rho\ge d-p+|\mathcal A\cap S|$ ⟹ $q_{\min}\ge d+2-p$（[`../../archive/2025-10_旧工作/proof/S`](../../archive/2025-10_旧工作/proof/S_维数下界定理_2026-10-21.md)）|
| **`c154_verify_rho_min_formula.py`** ⭐⭐ | **重验项目的 $\rho_{\min}$ 公式**（`c136` 的 0/560 是 bug）：33/33 候选可 lift，168 例 0 反例，含 9 个 $\rho{=}2$ ⟹ [`../../archive/2025-10_旧工作/proof/P`](../../archive/2025-10_旧工作/proof/P_rho_min公式重验_2026-10-20.md) |
| **`c152_q4_test.py`** ⭐ | $q{=}3$ 失败的实例测 $q{=}4$（$\rho{=}3$）：**326/326 全成功** ⟹ 一般实例 $q_{\min}{=}\mathrm{obs}{+}1$（[`../../archive/2025-10_旧工作/proof/O`](../../archive/2025-10_旧工作/proof/O_qmin分层_2026-10-20.md)）|
| **`c151_rho2_rescue.py`** ⭐ | 在 P7 假的实例上测 $q{=}3$：可行 516 个里只救回 26（≈5%）⟹ 一般实例 $q_{\min}\ge4$（[`../../archive/2025-10_旧工作/proof/N`](../../archive/2025-10_旧工作/proof/N_从P7到rho2_2026-10-20.md) §7）|
| **`c150_S_full.py`** ⭐ | $S{=}\mathbb{R}^d$ 区（$d{=}2,n{=}6,p{=}2$）：$q{=}2$ **120/120**；并实测 $\operatorname{rank}(R_0){=}\min(p,d)$ ⟹ [`../../archive/2025-10_旧工作/proof/L`](../../archive/2025-10_旧工作/proof/L_小q族_2026-10-20.md) §8 |
| **`c149_real_spectrum.py`** 🆕 | 试探"商映射实谱 ⟹ $q{=}2$"：$\dim S{=}1$ 的 8 个实例全部失败 ⟹ 负结果（[`../../archive/2025-10_旧工作/proof/L`](../../archive/2025-10_旧工作/proof/L_小q族_2026-10-20.md) §7）|
| **`c148_alpha0_linear.py`** ⭐ | 把 $\alpha_0$ 的网格换成**解方程**（$K_0=\{\alpha_0\in S:\alpha_0A'\in S\}$）+ 解 $k$ 使 $\beta_0\parallel\alpha_0$：**400/400** 实例 $q{=}2$ 成功 ⟹ [`../../archive/2025-10_旧工作/proof/L`](../../archive/2025-10_旧工作/proof/L_小q族_2026-10-20.md) §6 |
| **`c147_family_by_perturbation.py`** 🆕 | 命中实例的 24 个单元素 $\pm1$ 扰动：$q{=}2$ 仍有 16 个成立 ⟹ 非孤立点（[`../../archive/2025-10_旧工作/proof/L`](../../archive/2025-10_旧工作/proof/L_小q族_2026-10-20.md) §5）|
| **`c146_q2_family.py`** ⭐ | 按 [K] 的三层条件搜索 $q{=}2,\rho{=}1$ 实例：命中 3 个（seed 1080/1406/3871），$q_{\min}{=}2<\mathrm{obs}{+}1{=}4$ ⟹ [`../../archive/2025-10_旧工作/proof/L`](../../archive/2025-10_旧工作/proof/L_小q族_2026-10-20.md) |
| **`c145_construct_with_intersection.py`** 🆕 | 按 $S\cap\mathrm{span}\{\alpha_0\}\ne0$ 正面构造：线性系统恒不相容，暴露下一层条件 $\alpha_0A'\in S$ ⟹ [`../../archive/2025-10_旧工作/proof/K`](../../archive/2025-10_旧工作/proof/K_维数计数_2026-10-20.md) §8 |
| **`c144_filter_by_functional.py`** 🆕 | 按"功能泛函 $\ell\mapsto\ell AN-c\ell N$ 在 $V_{\mathcal A}$ 上不恒零"筛实例：40 个实例全部不通过 ⟹ 引出 `K` §7 的**可证必要条件** $S\cap\mathrm{span}\{\alpha_0\}\ne0$ |
| **`attack_chart_rigorous.py`** | 子式插值：生成器实例不存在 2 行 (A)-增广 ⟹ $q_0$ 未高估 |

## 四、判据与结构实验（6）

| 脚本 | 内容 |
|---|---|
| **`c125_rho1_criterion.py`** | $\rho\le1$ 的完整多项式判据（148/148 + 185/185） |
| **`c130_intersection_basis.py`** | 交空间/交维数计算 |
| **`c131_phi_closure.py`** | $\Phi$-闭包（第 70 处更正：$\Phi$ 是收缩的） |
| **`c134_exhaustive_beta.py`** | 穷尽 $\beta\in\mathbb{P}^1$（单调性检验，0/38 救回） |
| **`c137_cyclic_candidate.py`** | $A'$-循环候选（0/77，$A'$-不变 ⟹ P6b，**否定路线**） |
| **`c138_S_extension.py`** | $\mathcal A_*+\langle s\rangle$（0/86，不 admissible，**否定路线**） |

## 五、见证 / 支 B / 其他（13）

| 脚本 | 内容 |
|---|---|
| **`audit_independent.py`** 🆕 | **独立复核**（2026-10-20）：自带 Fraction 线代与多项式算术，在**原始 4 块 (5a)** 与**原始铅笔 (5b)** 上检验 P1 必要性 / $\rho\le\mathrm{obs}$ / $\rho\le q-1$；报告见 [`../../archive/2025-10_旧工作/proof/G_独立复核_2026-10-20.md`](../../archive/2025-10_旧工作/proof/G_独立复核_2026-10-20.md)（618 个真实解、0 违规；$\mathrm{obs}=1$ 上双向穷举 14/14） |
| **`mainline_witness2.py`** | ⭐ 支 B 的 (A)∧(S) 见证（输出并保存 `witness_branchB.json`） |
| **`batch_c6p_k.py`** | 通用 (A)-增广构造辅助（被 `mainline_witness2.py` exec） |
| **`gen_A_system.py`** | 通用 (A)-构造器（任意 $q_0=r+k$） |
| **`exact_count_14_elim.py`** | 支 B 的精确单变量消元（$(1,3){=}2$、$(1,4){=}2$–$3$） |
| **`test_caseII_YES.py`** | 情形 II 的 YES 检验装置（`p1`、`build_norm_T` 的真实来源） |
| **`test_S0_conjecture.py`** | 证伪猜想 (S0)（$\operatorname{rank}H\equiv d_{CA}$） |
| **`test_star3_fast.py`** | $(\star''')$ 的决定性实验（56/56） |
| **`test_C1_wider.py`** | 猜想 (C1) 的多形状检验 |
| **`check_C1_on_affine.py`** | 仿射退化集上逐点检验 (C2)（486/486） |
| **`decide_caseII_empty.py`** | $\{\operatorname{rank}H<q_0\}$ 是否为空（二次型符号，不用优化器） |
| **`recompute_rho_fixed.py`** | 修正 `mm(RNC,Kr)` 错配后重算 $\operatorname{rank}(RN_CK)$（480/480） |
| — | `witness_branchB.json`、`witness_caseII_parallel_YES.json`：两个见证数据 |

---

## 依赖关系（库 → 使用者）

```
exact_count_thm7.py  ← 根库
 ├── reliable_S_test.py        ├── verify_pencil_v2.py     ├── verify_T12{,_full,_r2}.py
 ├── verify_equivalences.py    ├── attack_chart_rigorous.py├── c39_construction.py
 ├── c43/c44/c79/c80/c81/c86   ├── gen_A_system.py        ├── recompute_rho_fixed.py
 └── batch_c6p_k.py ← mainline_witness2.py

exact_gcd.py（cond_5b）
 └── c125/c130/c131/c134/c137/c138/c87

linalg_q.py、linalg_exact.py   独立底座（互为裁判）
verify_all.py、verify_family.py、verify_witness*_independent.py   完全独立（不依赖项目库）
```

---

## 一键复现

```bash
python scripts/core/verify_all.py           # exit 0
python scripts/core/verify_equivalences.py  # exit 0
python scripts/core/verify_family.py        # exit 0
python scripts/core/exact_gcd.py            # 回归全过
python scripts/core/mainline_witness2.py    # 支 B 见证（会重写 json，内容相同）
```

### 输出判读

**`reliable_S_test.py`**：每行形如

```
 n  p  r  q0 | d_CA d_CA>=q0 |   (A)命中  (A)∧(S) |  扰动保持 | rankH=[…] full=… | A2: …
 5  2  1   2 |    1    False |  40/40    40/40   |  12/12   | rankH=[1] full=40/40 | A2: 40/40 rawT=40 redT=40
```

- `d_CA>=q0 = False` ⟹ (A)∧(S) 应 **100%**；`True` ⟹ 应 **0/40**
- `A2:` 中 **`rawT` 必须等于 `redT`**（三块约化 ≡ 原始 4 块 (A)）

**`exact_count_14_elim.py`**：$(1,3)$ 列全为 **2**；$(1,4)$ 列在 **{2,3}**。

---

## 验证铁律（血的教训，来自 74 处自我更正）

1. **等价性检验必含至少一个 True 点**——否则"一致"可能只是"两边都 False"。
2. **不可用"优化器没找到"当"不存在"**——已两次因此误判。
3. **拼接矩阵前先查维度**——曾因 ragged list 让秩计算"成功"于错误的列。
4. **不要用旧 `condS` 判据**。
5. **不要用随机采样验证零测集上的性质**（可行集是零测代数集时，采样必错过）。
6. **`mm(X,Y)` 不检查维数**（用 `k=len(Y)` 收缩）——每次调用前断言 `len(X[0])==len(Y)`，或用带断言的包装。
7. **约化/投影表述必须先在"最简例之外"校准**：只对 $q_0=2$ 成立的 (I)∧(II) 表述曾造成连续 4 处错误。
8. **齐次系统的"相容"是空洞的**：右端为 0 时零解恒存在——必须要求非零解。
9. **推导与数值冲突时，用手算最小反例定案**。
10. **不要用库 `exact_count_thm7.solve` 展开解集**——改用 `linalg_q.solve`（强制残差校验）。
11. **判据里的 `∀λ` / `∃λ` 必须写成显式反例自检**（曾把 (S) 误写成 `∃λ`）。
12. **判"秩恒定"不能用 `sympy.rank()`**（它算泛型秩）——必须用 $\rho$ 阶子式 gcd。
13. **判 `im ⊆ im` 必须用列拼接**（行堆叠算的是行空间）。

## 已证无效的做法（勿重复）

- 随机采样找稀有实例（$k\ge2$ 且 $d_{CA}\ge q_0$）——连续 5–6 轮超时；
- 暴力枚举轨道行 $\{CA^k,L_0A^k\}$ 的子集验证 $q_0$ 下界——**不完备**；
- 随机方向验证 $q_0$ 下界——零测集，采样必错过；
- 用 `build()` 直接处理 $L_0=CA^m$ 类实例（其 $\operatorname{rank}(RN_CK)=k$，在图卡内）。
