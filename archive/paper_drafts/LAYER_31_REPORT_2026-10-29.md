> ⚠️ **2026-10-29 总说明**：本文件中涉及"层级别判据/定理 8/定理 13/最小元/交封闭"的结论**已全部撤回** ✗；
> 以 [RESTRICTED_COMPLETION_MODEL.md §44](../proof/layer_program/RESTRICTED_COMPLETION_MODEL.md) 为准 ✓。

# $(3,1)$ 层报告（2026-10-29）

> 阶段性总结。范围**只覆盖** $(\\rho,c)=(3,1)$ 层与它的四个 $\\mu$-通道。
> 所有结论按项目纪律 §4 的分级标注：**【Lean】** / **【已证-纸面】** / **【精确验证 n/N】** / **【猜想】**。
> 完整证明在 [proof/rho1_layer/rho3c1_spectral.md](../proof/rho1_layer/rho3c1_spectral.md) 与
> [proof/layer_program/RESTRICTED_COMPLETION_MODEL.md](../proof/layer_program/RESTRICTED_COMPLETION_MODEL.md)。

---

## 1. 问题与归约

给定 $A\\in\\mathbb C^{n\\times n}$、$C\\in\\mathbb C^{p\\times n}$、$L_0\\in\\mathbb C^{r\\times n}$，求最小 $q$ 使存在 $R$，
$\\mathcal L=\\binom{L_0}{R}$（$q$ 行、行满秩），满足

$$(5a)\\ \\operatorname{rank}[\\mathcal LA;\\mathcal L;CA;C]=\\operatorname{rank}[\\mathcal L;CA;C],\\qquad
(5b)\\ \\operatorname{rank}[\\lambda\\mathcal L-\\mathcal LA;CA;C]=\\operatorname{rank}[\\mathcal L;CA;C]\\ \\ \\forall\\lambda .$$

记 $\\mathcal J=\\operatorname{row}[C;CA]$、$j=\\dim\\mathcal J$、$X=\\mathbb C^n/\\mathcal J$、$\\pi$ 为商映射、$B=\\pi(\\mathcal JA)$、
$\\mathcal V=\\operatorname{row}\\mathcal L$、$\\rho=\\dim\\pi(\\mathcal V)$、$c=\\dim(\\mathcal V\\cap\\mathcal J)$，则 $q=\\rho+c$。

$$q_{\\min}=\\min\\{\\rho+c:\\ (\\rho,c)\\ \\text{可达}\\},\\qquad \\text{层数}=O(n^2).$$

**一个格子** = 固定 $(\\mathcal U,\\mathcal H)$（$\\dim\\mathcal U=\\rho$、$\\mathcal H\\subseteq\\mathcal J$、$\\dim\\mathcal H=c$、$\\beta(\\mathcal H)\\subseteq\\mathcal U$）。
固定格子后，提升自由度使 $C=T+\\sum_{k=1}^{\\mu}s_ka_k^{\\mathsf T}$，其中 $E=B\\cap\\mathcal U$、$\\mu=\\dim E$、$T$ 是格子的 $3\\times3$ 数据。

**两个必须记清的事实**（本项目在它们上面错过多次）：

1. $(5a)\\iff\\pi(\\mathcal VA)\\subseteq\\pi(\\mathcal V)$，但 $\\pi(xA)$ 在 $X$ 上**不良定义**（偏差是 $B$）⟹ **不存在** $A$ 在 $X$ 上诱导的自同态；
   唯一良定义的是 $f:X\\to X/B$，$f(\\pi x)=\\pi(xA)\\bmod B$，且它**不**下降到 $X/B$ ✗。
2. $(5b)\\iff$ 铅笔的秩恒为 $\\rho$；$(5a)$ 已保证秩 $\\le\\rho$，故 $(5b)$ 只说"秩不下降"。

---

## 2. 主结果：四条格子级判据（+ 一条补充）

固定格子后，"被覆盖" = 所有 $s$ 都使 $(5b)$ 失败。记 $w=\\beta(h)\\in E$。

| 编号 | 陈述 | 等级 |
|---|---|---|
| **C.1** | $\\mu=3$（即 $\\mathcal U\\subseteq B$）、$w\\ne0$ ⟹ **不被覆盖** | 已证-纸面 + 精确验证 200/200 |
| **C.2** | $\\mu=1$、$w\\ne0$：不被覆盖 $\\iff$ $T$ 没有与 $a$ 正交的特征向量（$E=\\langle a\\rangle$）| 已证-纸面 + Lean（扰动引理）+ 199/199 |
| **C.3** | $\\mu=2$、$w\\ne0$：不被覆盖 $\\iff$ $T$ 没有落在 $E^{\\perp}$ 里的非零特征向量 | 已证-纸面 + Lean（二次式）+ 295/295 |
| **C.4** | $\\mu=0$ ⟹ **恒被覆盖**（恒不可行）| 已证-纸面 + **Lean**（因式分解）+ 42/42 |
| **C.5** | 任意 $\\mu$、$w=0$ ⟹ **恒被覆盖** | 已证-纸面 + 精确验证 120/120 |

### 2.1 三个关键的证明思路

- **C.2/C.3 的"$\\Leftarrow$"**：若 $v\\in E^{\\perp}$ 是 $T$ 的特征向量，则 $Cv=Tv$ 对**所有** $s$ 成立（扰动项被 $a_k^{\\mathsf T}v=0$ 杀掉），
  所以每个 $C$ 都有特征向量 $\\perp w$ ⟹ 由谱判据失败。
- **C.2 的"$\\Rightarrow$"**：取 $s=0$；2 维特征空间必与超平面 $a^{\\perp}$ 有非零交，故所有特征空间 1 维，再由谱判据得无降秩点。
- **C.3 的"$\\Rightarrow$"（专家构造）**：取坐标使 $E=\\langle e_1^{\\mathsf T},e_2^{\\mathsf T}\\rangle$、$w^{\\mathsf T}=e_1^{\\mathsf T}$，
  则"每行差 $\\in E$" $\\iff$ 第三列为零；写 $C=\\begin{pmatrix}x&g^{\\mathsf T}\\\\0&D\\end{pmatrix}$，
  坏条件等价于 $\\det[z,Dz]=0$（$z=(a,-y)$），**展开得二次式** $p=a^2s+a(u-c)y-by^2$；
  $(a,b)\\ne(0,0)$（= 假设）保证 $p\\not\\equiv0$，于是可取参数使 $p\\ne0$ 并配上 $u\\ne c$、$x\\notin\\{u,c\\}$，
  得到谱简单、每个特征向量都 $\\not\\perp w$ 的上三角 $C$。
- **C.4**：$w=0$ ⟹ 第 4 行为零 ⟹ $(5b)\\iff\\det(\\lambda U-C)\\ne0\\ \\forall\\lambda$，而它是三次（或恒零）⟹ 必有根。

---

## 3. 验证：三层结构与证据等级

"验证"分三层，三层的**独立性**是关键：

| 层 | 内容 | 结果 |
|---|---|---|
| **(a) 抽象模型** | 手工设定的 $(\\mathcal U,B,\\beta,T)$ 数据 | C.1 200/200、C.2 199/199、C.3 295/295、C.4 42/42 |
| **(b) 真实实例** | 真 $(A,C,L_0)$ + **实现**的商空间（$X,B,f$）| C.1 200/200、C.2 17/17、C.3 43/43 |
| **(c) 端到端** | 从判据说"可行"出发，**构造**真正的 $\\mathcal V\\subseteq\\mathbb C^n$，用**堆叠判据**（独立于商空间实现）验 $(5a)\\wedge(5b)$ | **C.3（$\\mu=2$）12/12，10 条逐项全 PASS** ✓；C.1/C.2 未做 ✗ |

**商空间实现的自检**（五条，全部 100%）：坐标往返、$\\pi(xA)-\\pi((x+j)A)\\in B$、$f$ 良定义、
**堆叠判据 $\\iff\\pi(\\mathcal VA)\\subseteq\\pi(\\mathcal V)$（120/120，最关键）**、维数公式。
（这一条曾以 297/298 暴露过"把差一个 $B$ 的量当成良定义"的错误。）

### 3.0 更正（2026-10-29 晚）

**旧的端到端数字（$\mu=1$ 12/12、$\mu=2$ 60/60、$\mu=3$ 12/12）作废** ✗ ——
它们没有检查 $\operatorname{row}(L_0)\subseteq\mathcal V$ ✗：用任意截面构造的 $\mathcal V$ 一般**不含** $L_0$；
把它并入后 $\dim\mathcal V$ 从 4 变 5、类型从 $(3,1)$ 变 $(3,2)$ ✗。
修法：取截面时令 $s(u_0):=\ell_0$ ✓。用修法重跑：**12/12，且每条实例逐项通过 10 个条件**
（$\dim\mathcal U=3$、$W_0\subseteq\mathcal U$、$w\ne0$、$(N)$、$\mu\ge1$、$\operatorname{row}(L_0)\subseteq\mathcal V$、
$\dim\mathcal V=4$、类型 $(3,1)$、$(5a)$、$(5b)$），全部落在 $\mu=2$ ✓。
脚本：[verify_end2end_fixed.py](../proof/rho1_layer/verify_end2end_fixed.py)、
逐项检查器：[verify_cell_all_conditions.py](../proof/rho1_layer/verify_cell_all_conditions.py)。

### 3.1 Lean 覆盖（32 条，12 模块，全部 `lean` 退出码 0）

| 模块 | 覆盖 |
|---|---|
| `PRecursion` 系 + `PVal` | 算术侧 $P$ 的递归与 $\\mathcal P$ 的定义（与本节无关，另见 docs/02）|
| `Perturbation` | C.2/C.3 的扰动引理（秩一、秩二）|
| `Theorem12` | C.4 的因式分解 $\\det(\\lambda U-U T^{\\mathsf T})=\\det U\\cdot\\det(\\lambda I-T^{\\mathsf T})$ |
| `QuadraticMu2` | C.3 的二次式 $\\det[z,Dz]=a^2s+a(u-c)y-by^2$ 及其**非恒零** |

### 3.2 **未**形式化的（明确清单）

1. C.3 的**坐标变换 + $(a,b)\\ne(0,0)$ 等价**（"$T$ 无 $E^{\\perp}$ 特征向量" $\\iff Te_3\\notin\\langle e_3\\rangle$）；
2. C.3 的**特征向量–特征值对应**（$v=(0,z)$ 是 $C$ 的特征向量 $\\iff$ $z$ 是 $D$ 的特征向量且 $g^{\\mathsf T}z=0$）；
3. C.3 构造的**结论**（上三角 $C$ 的三个特征向量第一坐标全非零）；
4. C.4 里"非零三次必有根"（代数基本定理；Lean API 名字未对上）。

—— 这四项的**纸面证明是完整的**；缺的只是机器检查。**决定**：暂不形式化（用户 2026-10-29 指示），
在此明确登记，避免以后误以为"全部已 Lean 化"。

---

## 4. 专家四步路线与它的三个结构结果

| 步 | 内容 | 状态 |
|---|---|---|
| 1 | 冻结 C.1–C.5 + 形式化 $\\mu=2$ 二次构造 | 定理冻结 ✓；形式化**部分** ✓（见 §3.2）|
| 2 | 必要条件几何与固定行约束分开 | ✓ |
| 3 | 用一对映射 $(f,q_B)$ 重述外层 | ✓（表述 + 三个结果）|
| 4 | Grassmann + 秩条件 + Bézout 的精确判定基线 | ✓（规格 + 实现 + 同实例交叉核对）|

### 4.1 三个结构结果

1. **必要条件 $=$ 经典条件不变性**（精确验证 28/28）：记 $\\mathcal K=\\mathcal J+\\mathcal JA$，则
   $$f(\\mathcal U)\\subseteq q_B(\\mathcal U)\\iff\\widetilde{\\mathcal U}A\\subseteq\\widetilde{\\mathcal U}+\\mathcal K .$$
2. **条件不变子空间对交封闭**（44/44）⟹ 含固定行 $W_0=\\pi(\\operatorname{row}L_0)+\\pi(\\operatorname{row}(L_0A))$ 的条件不变子空间
   有**最小元**（标准闭包迭代）。
3. **提升条件是自动的**：$(N)$ + $\\beta$ 满射 ⟹ 存在 $j_i\\in\\mathcal J$ 使 $\\pi((s(u_i)+j_i)A)\\in\\mathcal U$。
   于是 $(5a)$ 可实现 $\\iff(N)$，**不需要**单独的提升条件。

### 4.2 第 4 步的交叉核对（一个实例）

$\\mathbb F_3$、$n=6$、$p_{\\text{rows}}=1$、$j=2$、$d=4$、$\\dim B=1$、$\\dim W_0=2$：

| 路线 | 枚举量 | 结论 |
|---|---|---|
| 判定链（枚举 $\\mathcal U$ + C.2/C.3）| 108 个 3 维子空间，10 个满足 $(N)$ | **INFEASIBLE** |
| 直接枚举（$\\mathcal V$ + 堆叠判据）| 19 个 $(3,1)\\wedge(5a)$ 候选 | **INFEASIBLE** |

两条**独立**路线结论一致。局限：一个实例的 proof of concept；$\\mathcal V$ 的枚举量随 $n$ 增长很快（$n\\ge8$ 不现实）。

---

## 5. 两个缺口（这就是 $q1$ 的难度）

$$\\text{层可行}\\iff\\exists\\,\\mathcal U\\ (3\\text{ 维},\\ \\supseteq W_0,\\ (N)):\\ \\exists\\,\\mathcal H\\ (\\beta(\\mathcal H)\\subseteq\\mathcal U,\\ w\\ne0)\\wedge\\text{C.2/C.3 判据}$$

第三步（$\\exists\\mathcal U$）里，"$(N)$ 且含 $W_0$ 的 3 维子空间"**可判**（$\\dim$ 闭包 $\\le3$）；
但**谱判据随 $\\mathcal U$ 变**，而候选集

$$\\mathfrak C=\\{\\mathcal U:\\dim3,\\ C_{\\min}\\subseteq\\mathcal U,\\ (N)\\}$$

**一般无穷**。所以最后一步是"在 $\\mathfrak C$ 上判 $\\exists$ 使谱判据成立"：

| 缺口 | 内容 |
|---|---|
| **A** | 给 $\\mathfrak C$ 上的"$\\exists$ 谱判据"一个多项式判据（或证明它一般不可能）|
| **B** | 或给出归约/硬度：$\\mathfrak C$ 的搜索是难的 |

两条都没有解决 ✗。**$q1$ 仍开放** ✗。

---

## 6. 复现命令

```bash
# 商空间实现的自检（必须 5 条全 100%）
python proof/rho1_layer/quotient_selfcheck.py

# 格子级判据：抽象模型
python proof/rho1_layer/verify_spectral_criterion.py     # 引理 1 / 推论 2
python proof/rho1_layer/verify_mu2_criterion.py          # C.3：三分法
python proof/rho1_layer/verify_mu0_always_fails.py       # C.4
python proof/rho1_layer/verify_checkpoint.py             # 二次式 + 维数计数

# 格子级判据：真实实例 + 端到端
python proof/rho1_layer/verify_cell_criteria_genuine.py  # C.2
python proof/rho1_layer/verify_cell_mu23_genuine.py      # C.3
python proof/rho1_layer/verify_mu3_genuine.py            # C.1
python proof/rho1_layer/verify_end2end_genuine.py        # 端到端（μ=1）

# 结构结果
python proof/rho1_layer/verify_classical_ci.py           # (N) = 条件不变性
python proof/rho1_layer/verify_ci_intersection.py        # 交封闭

# 第 4 步
python proof/rho1_layer/decide_layer_fp.py 3             # 判定链（F_3）
python proof/rho1_layer/crosscheck_layer_fp.py           # 直接枚举（F_3）

# Lean（30+ 条；WSL）
cd ~/WorkSpace/lean4/MyProof && export PATH="$HOME/.elan/bin:$PATH"
lake env lean MyProof/Perturbation.lean
lake env lean MyProof/Theorem12.lean
lake env lean MyProof/QuadraticMu2.lean
```

---

## 7. 一句话

$$\\boxed{\\ (3,1)\\ \\text{层}\\textbf{格子级} \\text{已完整（四条判据 + 三层验证）};\\quad \\textbf{层级别}\\ \\text{只剩"在无穷候选集上判 }\\exists\\text{"} = q1 }$$
