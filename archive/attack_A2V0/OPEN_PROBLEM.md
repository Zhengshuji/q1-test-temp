# 开放问题（2026-10-23 收盘）


> # 2026-10-24 状态（两次修正）
>
> **① 原猜想被推翻**（02:20）：精确反例 $n{=}5,\ p{=}2,\ q{=}1,\ \dim V{=}1$，$(5a)\wedge(5b)$ 成立但 $q=1<\dim V+1=2$。
> 证书 `lit/counterexample_refute_dimV1.json`；崩点 Gap A（$S\not\subseteq\mathcal A$）。
>
> **② 双层公式不完整**：$\min(\dim V+1,\ q_{\deg})$ 在修好穷举工具的 bug 后只有 **97/100**。
>
> **③ 正确的结构**：按 $\rho=\dim\operatorname{row}(\mathcal LN)$ 分层
> $$q_{\min}=\min_{\rho=0}^{\dim V}q(\rho)$$
> | 层 | 含义 | 状态 |
> |---|---|---|
> | $\rho=0$ | 退化解 = conditioned invariant | ✅ 1935/1935 验证 |
> | $\rho=\dim V$ | 非退化（原定理）| 🟡 有退化解时被击败 |
> | $0<\rho<\dim V$ | **中间层** | ✅ **证书存在**（`certificate_middle_layer.json`）|
>
> **四个验证工具 bug 已修**：采样 $\lambda$、带过滤搜索、`row_basis` 丢 $L_0$、$\rho^*$ 搜索漏 $\supseteq\operatorname{row}(L_0)$。
>
> **共同模式**：搜索约束写漏，然后结论看起来是对的（见纪律 8–10）。
>
> **q1 仍开放。**

> ## 🏁 最终判断（2026-10-24 18:20）
>
> $$q_{\min}=\max\big(r,\ \rho^*+1\big)$$
>
> - 8 个已证命题 + 5 个精确验证 + 8 个精确证书
> - 中间层（$\rho^*<\dim V$）存在但**不能非平凡放大**（D38）：简单块扩展破坏它，只有"不可见块"能放大（不增难度）
> - $$\Longrightarrow\quad \boxed{\ \textbf{q1 很可能为假（多项式）}\ }\quad\text{—— 启发式判断，非证明}$$

> ## 🎯 修正后最重要的结果：多项式可算的夹逼（2026-10-24 04:00）
>
> $$\boxed{\ \dim\big(\mathcal V^{\mathrm{ci}}_{\min}\big)\ \le\ q_{\min}\ \le\ \dim V+1\ }$$
>
> - 两端都可用 $O(n^3)$ 算出（conditioned invariant 迭代 / Kleiman–Krener 闭包）
> - 下界可取等（中间层证书：$2=2$）
> - **但夹逼可以不闭合**（57/59 取端点，2 个实例严格在中间）
>
> $$\textbf{q1}\iff\text{能否在夹逼内部精确判定 }q_{\min}$$





> **只有一个**：一条子空间不变性引理。其余全部已证或已大规模验证。

---

## 0. 一句话

$$\boxed{\ \text{设}\ (5b)\ \text{成立},\ V_0:=\ker\begin{pmatrix}L\\CA\\C\end{pmatrix}.\ \text{证明}:\quad A^2V_0\subseteq V_0\ }$$

---

## 1. 为什么它重要

它是定理 $q_{\min}=\dim V+1$ 证明链里**唯一未证**的一步：

$$\underbrace{q\ge\rho+1}_{\text{已证}}\ +\ \underbrace{\rho\ge\dim V}_{\Longleftarrow\ A^2V_0\subseteq V_0}\ +\ \underbrace{\text{其余四步}}_{\text{已证}}\ \Longrightarrow\ q_{\min}=\dim V+1$$

**若它成立** ⟹ $q_{\min}$ 可 $O(n^3)$ 算出 ⟹ **q1 = 假**（且改进 Fernando et al. 2010 的指数算法）。

---

## 2. 已知的全部信息

### 2.1 设定

- $N$：$K=\ker[C;CA]$ 的基（$n\times d$，列满秩）
- $A'=(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN$，$R_0=AN-NA'$
- $\mathcal L$ 满足 $(5a)$ 与 $(5b)$
- $V_0=\ker[L;CA;C]$

### 2.2 已证的三个事实

$$\textbf{(i)}\quad N^{\mathsf T}R_0=0\qquad\textbf{(ii)}\quad S'=S\qquad\textbf{(iii)}\quad q\ge\rho+1$$

$$\textbf{(iv)}\quad (5b)\iff\ker[\lambda L-LA;CA;C]=V_0\ \forall\lambda$$

$$\textbf{(v)}\quad\text{由 (iv)}:\ A(V_0)\subseteq\ker L$$

### 2.3 已验证（2293 个解，0 违例）

$$A(V_0)\subseteq\ker(CA)\qquad A^2(V_0)\subseteq V_0\qquad A(V_0)\subseteq\ker L$$

### 2.4 已排除的错误路线

| 路线 | 反例 |
|---|---|
| $A(\operatorname{col}N)\subseteq\operatorname{col}N$ | 1/3、1/4、2/4 违例 ✗ |
| $A(\ker L\cap\ker C)\subseteq\ker(CA)$ | 2160 解中 2579 违例 ✗ |
| 封闭性递推（$v\mapsto Av\mapsto A^2v$ 逐步）| 同 ✗ |

$$\boxed{\ \text{关键：必须用}\ \textbf{完整堆叠}\ \ker[L;CA;C]\ \text{（不是}\ \ker L\cap\ker C\text{）}}$$

---

## 3. 文献地位

| 来源 | 结果 |
|---|---|
| Wonham（geometric approach）| 有 pencil 与 invariant subspace 的通用理论，**无此引理** |
| Basile–Marro | conditioned invariant 的定义，**无此引理** |
| **Trentelman–Stoorvogel–Hautus (2002)**（403 页，全文已提取）| "no zeros" 20 处**全指传递矩阵零点**；**无此引理** ✗ |
| Web 搜索（2 轮）| 只有相邻概念（conditioned invariant、coasting subspace）✗ |

$$\boxed{\ \text{若它确实不在文献中}\ \Longrightarrow\ \textbf{它是本项目的新贡献}\ ✓}$$

---

## 4. 三条可能的攻法

| # | 思路 | 评估 |
|---|---|---|
| **A** | 用 $(5b)$ 的"多项式版"（所有 $\rho$ 阶子式 gcd $=1$）做代数消元 | 需要计算量，但可能可行 |
| **B** | 用 Rosenbrock/Wonham 的"无零点铅笔"理论的标准论证 | 需要找到正确的定理编号 |
| **C** | 反例搜索：构造 $A^2V_0\not\subseteq V_0$ 的实例 | 2293 次未找到 ⟹ 很可能不存在 |

---

## 5. 陷阱（已踩过，不要再踩）

| 陷阱 | 教训 |
|---|---|
| 用 $\ker L\cap\ker C$ 代替 $\ker[L;CA;C]$ | 差一个 $CA$，导致 2579/2160 违例 ✗ |
| 认为 $A$ 保持 $\operatorname{col}(N)$ | 假 ✗ |
| 以为 $(5b)$ 的一阶用法就够了 | 只给 $LAv=0$，不够 ✗ |
| 把"开集非空"当"处处成立" | 薄实例解集是薄集 ✗ |

---

## 6. 复现

```bash
python scripts/core/c162_dimV_formula.py      # 主验证器（6 实例）
python scripts/core/c163_construct_algorithm.py --random 25   # 构造算法
```

```bash
wsl -e bash -lc 'cd ~/WorkSpace/lean4/MyProof && export PATH="$HOME/.elan/bin:$PATH" && lake build'
```
