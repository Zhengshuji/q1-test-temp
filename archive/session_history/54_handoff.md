> # 🔴 **2026-10-19 重大更正**
> $$\rho\ge\mathrm{obs}\ \textbf{已被反例推翻}\ (n{=}7,\rho{=}1,\mathrm{obs}{=}3)\ \Longrightarrow\ \textbf{"q1 为假"撤回，q1 开放}$$
> $$\text{被推翻：A23（正确版：}\ q{=}1\Rightarrow M{=}0\ \text{）、}\ |R|_{\min}=\mathrm{obs}+1-r$$
> $$\text{仍然成立：判据（两侧）、可行性}\in\mathrm{P}\text{、A19（}\rho\le\mathrm{obs}\text{）、}\rho{=}0\ \text{刻画}$$
> 详见 `OPEN_PROBLEM.md` 顶部。
# 54 — 交接单（Handoff）

> 只回答：**已确证什么**、**还缺什么**、**下一步做什么**。
> 权威结论：[`FINAL.md`](../FINAL.md) §7.5；论文：[`PAPER.md`](../PAPER.md)；审计：[`PROOF_AUDIT.md`](../PROOF_AUDIT.md)
> 完整推导：[`52`](52_session_conclusion.md)（4800+ 行）

---

## A. 已严格证明（23 条）

| # | 结论 | 证据 |
|---|---|---|
| **A1** | $(A)\iff$ 分解 $\iff$ 核条件 | **Lean 73 定理** |
| **A2** | $K\subseteq\ker(CA^2)\Rightarrow(5b)$ 恒失败 | **Lean** |
| **A3** | 六步化简：只依赖 $(\mathcal LN,\mathcal LAN)$ | E1–E4 各 400/400 |
| **A4** | $q\le d_{CA}\wedge\rho{=}q\Rightarrow(5b)$ 不可能 | 引理 |
| **A5** | $\rho=\operatorname{rank}A_0$ 由 (5b) 强制 | 秩半连续性 |
| **A6** | **充分性**：$\alpha_0\in V\Rightarrow$ YES | 构造 + pole placement |
| **A7** | 单调性（补零行）| 初等 |
| **A8** | $\rho>\mathrm{obs}\Rightarrow U\cap V^\perp\ne0$ | **Lean**（`DimCount.lean`）|
| **A9** | $\Lambda M=F$ 通解 $=\Lambda_0+\varphi c^{\mathsf T}$（$q$ 参数）| 初等 |
| **A10** | $F^{\mathsf T}(\ker M^{\mathsf T})\subseteq\operatorname{row}R_0$ | 初等 |
| **A11** | $(\text{5b})\iff\forall\lambda:\varphi\notin\operatorname{im}(\Lambda^{\mathsf T}-\lambda I)$ | 2 行 |
| **A11′** | 一般形式：$(\text{5b})\iff\operatorname{rank}[\Lambda^{\mathsf T}-\lambda I\mid\mathcal N]=q\ \forall\lambda$ | 2 行 |
| **A12** | 形式 I（$F^{\mathsf T}u_k$ 无关）$\iff$ Krylov 维数 $=q$ | 交替形式 |
| **A13** | Krylov $=q\Rightarrow(5b)$ | 2 行 |
| **A14** | $(5b)\Rightarrow$ Krylov $=q$ | ⚠️ 经 $\chi_\Lambda$ squarefree（实证 40/40）|
| **A15** | $\rho=d\wedge\mathrm{obs}<d\Rightarrow(5b)$ 败 | A13+A14 |
| **A16** | $\exists0\ne w\in U:wA'\in\operatorname{span}(w)+W_0$ | 严格 |
| **A17** | $(\text{5b})\Rightarrow\dim\ker(\Lambda-\lambda I)\le q-\rho$ | 严格 |
| **A18** | $\rho=1\Rightarrow\rho\le\mathrm{obs}$ | 平凡 |
| **A19** | $\boxed{\rho\le\mathrm{obs}}$（PBH + Krylov 递推）| **严格** |
| **A20** | $\boxed{(\text{5a})\wedge(\text{5b})\Rightarrow\alpha_0=L_0N\in V}$ | **严格** |
| **A21** | $(\text{5a})\Rightarrow U$ 是 $A'^{\mathsf T}$-不变 | ⚠️ **证明有 gap**；实证 4113/4113 |
| **A22** | $\boxed{N^{\mathsf T}R_0=0}$（正交残差）| **2 行** |
| ~~A23~~ | ~~$\rho=1\Rightarrow\mathrm{obs}\le1$~~ ❌ **已推翻**（2026-10-19 反例：$n{=}7,\rho{=}1,\mathrm{obs}{=}3$）| **正确版**：$q=1\wedge(5a)\wedge(5b)\Rightarrow M=0$ ✓ |
| — | **几乎不变性**：$A'^{\mathsf T}U\subseteq U+\tilde V$（lift-无关）| 严格 |

### 主结果（两侧均已证）

$$\boxed{\ \exists R\ \text{使}\ (\text{5a})\wedge(\text{5b})\iff\alpha_0=L_0N\in V=\big\langle\operatorname{row}(AN-NA')\big\rangle_{A'}\ }$$

$$\Longrightarrow\ \textbf{可行性判定}\in\mathrm{P}\ (O(n^3))$$

**注**：只需 H1–H3；**H4 未被使用** ✓（结论对更大的类成立）

### 机器验证

$$\textbf{Lean}\ \mathbf{73}\ \text{定理};\quad \texttt{lake build}\ \to\ \textbf{18134 jobs 零 error}$$
$$\texttt{verify\_all}\ \to\ 0;\quad \texttt{verify\_equivalences}\ \to\ 0;\quad \texttt{exact\_gcd}\ \to\ 0$$

---

## B. 唯一缺口

$$\boxed{\ (\text{5a})\wedge(\text{5b})\ \Longrightarrow\ \rho\ge\mathrm{obs}\ }$$

**等价形式**（4 个）：
$$\rho\ge\mathrm{obs}\iff\dim U\ge\dim\tilde V\iff W\subseteq U\iff\ker M\subseteq\ker R_0$$

### 证据（六条独立线，约 48 万样本，零反例）

| # | 证据 | 规模 |
|---|---|---|
| 1 | 随机解 $p=1$ | 472,177 全 $\rho=\mathrm{obs}$ |
| 2 | 随机解 $p=2$ | 2,793 全 ✓ |
| 3 | 定向搜寻反例 | 523,447 候选，反例 0 |
| 4 | 抽象构造反例 | 19,091 **全不可实现** |
| 5 | 交集维数 | 193,382 组，**恒 $\le1$** |
| 6 | 薄集穷尽（$\gamma_0\parallel\alpha_0$）| 8×729，**4,048 解全 $\rho=\mathrm{obs}$** |

### 缺口在经典理论中的位置

$$\text{缺口}\iff\mathcal L\ \text{必消去}\ sN-NA\ \text{的无穷初等因子（i.e.d.）}$$
$$\text{经典文献（Jaffe–Karcanias 1981；TSH Thm 7.10）只处理 restriction pencil 本身，未覆盖"投影后"的情形}$$

**已排除的路线（9 条）**：商的谱、$\forall y$ 平行、$\alpha_0A'\notin$ 某空间、$\Lambda$ 算子化、
$H(V)$ 不变、$S_0$ 迭代、$w\cdot\gamma_0$、只用 $\ker M^{\mathsf T}$ 的像、逐 $\lambda$ 维数不等式。

---

## C. 下一步

| 序 | 动作 | 可行性 |
|---|---|---|
| **1** ⭐⭐⭐⭐ | 求助于懂 Jaffe–Karcanias 铅笔机器的人：$\mathcal L$ 投影后 i.e.d. 的条件 | 需外部 |
| **2** ⭐⭐⭐ | 显式算 Kronecker 形（$d\le4$），直接看投影后的秩 | 中等 |
| **3** ⭐⭐ | A19/A20 的剩余 Lean 形式化（递推已有 `krylov_image_le`）| 可行 |
| **4** ⭐ | 补 A21 的 gap（$\mathrm{row}(MA')\subseteq\mathrm{row}M$）| 与缺口同源 |
| ❌ | 继续随机/定向搜索 $\rho<\mathrm{obs}$ | 已 48 万样本，无意义 |
| ❌ | $d=5$ 采样 | 参数 ~50 维，不可行 |

---

## D. 纪律（47 处更正换来）

1. **"已实证"与"已证明"必须分开写**
2. obs 是**闭包**维数（不是 $\dim\operatorname{row}R$）
3. **转置索引必须写清**（本项目已犯 5 次）
4. **$\ker\mathcal L$ 依赖 lift** —— 不能用它做 lift-无关的目标（第 42 处）
5. **子式 gcd 必须先过滤零多项式**（第 40 处，见 `exact_gcd.py`）
6. **sympy 的 `rank()` 算泛型秩，不能判"秩恒定"**（第 34 处）
7. 中文文件用 `write` 工具；**Lean 不接受花体字符**（`𝒩`）作标识符
8. `finrank K (p ⊔ q)` 要写 `↥(p ⊔ q : Submodule K E)`
9. **恒等式冒充推论**是最隐蔽的错误（第 43 处）
10. **未证的不等式要写清是哪一半**（第 46 处：是 $\rho\ge\mathrm{obs}$，不是整个等式）

---

## E. 一键复现

```
cd scripts/core
python verify_all.py            # exit 0
python verify_equivalences.py   # exit 0（E1–E4 各 400/400）
python exact_gcd.py             # 自检 exit 0
```
```
wsl -e bash -lc 'export PATH="$HOME/.elan/bin:$PATH" && cd ~/WorkSpace/lean4/MyProof && lake build'
# → Build completed successfully (18134 jobs)
```

**文献**：`lit/willems1981.txt`（Jaffe–Karcanias 1981）、`lit/tsh.txt`（Trentelman–Stoorvogel–Hautus）
