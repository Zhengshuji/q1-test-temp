# 验证：矩阵、复现命令、**未形式化清单**

> **验证 ≠ 证明**。本目录的定理等级都是【已证-纸面】；下面的数字只是**独立的复核**，
> 用来发现错误，不用来替代证明（项目纪律 §4、§18）。

---

## 1. 验证矩阵

| 定理 | 纸面证明 | Lean | (a) 抽象模型 | (b) 真实实例 | (c) 端到端 |
|---|---|---|---|---|---|
| **C.1**（$\mu=3$）| [theorem.md](theorem.md) §3 | — | 200/200 | 200/200 | 未做 ✗ |
| **C.2**（$\mu=1$）| 同上 | `Perturbation.lean` | 199/199 | 17/17；另有"好"实例（七项 PASS ✓）与"被覆盖"实例（**独立论证** ✓）| 未做 ✗ |
| **C.3**（$\mu=2$）| 同上 | `Perturbation.lean` + `QuadraticMu2.lean` | 295/295 | 43/43 | **12/12（十条逐项）** |
| **C.4**（$\mu=0$）| 同上 | `Theorem12.lean` | 42/42 | — | — |
| **C.5**（$w=0$）| 同上 | `Theorem12.lean` | 120/120 | — | — |
| 引理 0（谱判据）| 同上 §2 | — | 352/352、114/114 | — | — |
| 归约定理 | [admissibility.md](admissibility.md) §2 | — | — | — | — |
| $(N)$=条件不变性 | [admissibility.md](admissibility.md) §3 | — | 28/28 | — | — |

**"(c) 端到端"的含义**：从"判据说可行"出发，**构造**真正的 $\mathcal V\subseteq\mathbb C^n$，
再用**原始堆叠判据**（与商空间实现无关 ✓）验 $(5a)\wedge(5b)$ ✓，并**逐项**检查十条必要条件 ✓
（`verify_end2end_fixed.py`）。

---

## 2. 复现命令

```bash
# 商空间实现的自检（必须 5 条全 100%）
python proof/rho1_layer/quotient_selfcheck.py

# (a) 抽象模型
python proof/rho1_layer/verify_spectral_criterion.py      # 引理 0
python proof/rho1_layer/verify_mu2_criterion.py           # C.3（三分法）
python proof/rho1_layer/verify_mu0_always_fails.py        # C.4
python proof/rho1_layer/verify_checkpoint.py              # 二次式与维数计数

# (b) 真实实例
python proof/rho1_layer/verify_cell_criteria_genuine.py   # C.2
python proof/rho1_layer/verify_cell_mu23_genuine.py       # C.3
python proof/rho1_layer/verify_mu3_genuine.py             # C.1（200/200）
python proof/rho1_layer/verify_mu1_r0.py                  # μ=1"被覆盖"实例的**独立论证**（子式次数）
python proof/rho1_layer/verify_mu1_good_instance.py       # μ=1"好"实例（七项全 PASS）
# 注：verify_mu1_instance_cell.py / verify_mu1_covered_instance.py 目前**自相矛盾** ✗
#     （两次算出的 T 不同），**不**作为证据引用。

# (c) 端到端（十条逐项）
python proof/rho1_layer/verify_end2end_fixed.py           # C.3：12/12
python proof/rho1_layer/verify_cell_all_conditions.py     # 规格的逐条实现

# 结构结果
python proof/rho1_layer/verify_classical_ci.py            # (N) = 条件不变性（28/28）

# Lean（WSL）
cd ~/WorkSpace/lean4/MyProof && export PATH="$HOME/.elan/bin:$PATH"
lake env lean MyProof/Perturbation.lean
lake env lean MyProof/Theorem12.lean
lake env lean MyProof/QuadraticMu2.lean
```

---

## 3. **未形式化**的清单（知情即可）

| # | 未形式化的内容 | 覆盖方式 |
|---|---|---|
| 1 | C.3 的**坐标变换**与"$T$ 无 $E^{\perp}$ 特征向量 $\iff(a,b)\ne(0,0)$" | 纸面 ✓ + 295/295 + 43/43 |
| 2 | C.3 的**特征向量–特征值对应**（$v=(0,z)$ 是 $C$ 的特征向量 $\iff$ $z$ 是 $D$ 的特征向量且 $g^{\mathsf T}z=0$）| 纸面 ✓ + 精确验证 |
| 3 | C.3 构造的**结论**（上三角 $C$ 的三条特征线都不 $\perp w$）| 纸面 ✓ + 12/12 端到端 |
| 4 | C.4/C.5 的"非零三次必有根"（代数基本定理在 Lean 里的 API 未接通）| 纸面 ✓ + 42/42 |
| 5 | $\mu=1$ 的"**判据 vs 实例一致**" ✗ | **已定位（2026-10-30）** ✓：该实例实际 **$w=0$**（$H=\langle e_5\rangle$、$w=\pi(e_6)=0$）⟹ 归 **C.5**（恒被覆盖），C.2 不适用；旧表里的 $T$ 是错的，正确 $T=\begin{smallmatrix}0&1&0\\0&0&1\\1&1&0\end{smallmatrix}$，修正后的 [../rho1_layer/verify_mu1_covered_instance.py](../rho1_layer/verify_mu1_covered_instance.py) 三组一致 ✓。**"被覆盖"方向已补** ✓：[../rho1_layer/verify_mu1_w_ne_0_instance.py](../rho1_layer/verify_mu1_w_ne_0_instance.py)（$w\ne0$、判据 gcd 次数 2、直接验 25/25）；**"不被覆盖"方向也已补** ✓：[../rho1_layer/verify_mu1_w_ne_0_not_covered.py](../rho1_layer/verify_mu1_w_ne_0_not_covered.py)（判据 gcd 次数 0、见证 $\mathcal L=[e_1;e_2;e_3;e_6]$） |

—— 这四项的**纸面证明是完整的** ✓；缺的只是机器检查 ✓。按用户 2026-10-29 的决定，**暂不形式化** ✓。

---

## 4. 已知的、本目录**不**覆盖的东西

| 项 | 说明 |
|---|---|
| 层级别的判定 | 见 [admissibility.md](admissibility.md) §4 的开放问题 ✓ |
| $\mu=3$ 的端到端 | 结构刚性已知（$n=j+3$、$\mathcal U=B=X$ ✓），但两次搜索未找到实例 ✗ |
| $c\ge2$ | C.1–C.5 都是 $c=1$ ✗ |
| $q1$ | 仍开放 ✗ |

撤回清单（不要引用）：[../../proof/layer_program/RESTRICTED_COMPLETION_MODEL.md](../layer_program/RESTRICTED_COMPLETION_MODEL.md) §44。
