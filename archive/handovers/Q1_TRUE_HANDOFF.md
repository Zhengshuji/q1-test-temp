# 给 Q1-FALSE 方向的交接（来自 Q1-TRUE 的尝试）

> 2026-10-24。我在尝试证明 q1 = 真（NP-hard）的过程中，得到了一些**对证 q1 = 假更有用**的结论。
> 这个文件把它们集中起来，附上"别踩"的坑，避免重复劳动。

---

## 1. 一个等价形式：Z-FORM（可直接用于算法设计）

用 2026 文献（Fernando，见 [`q1_true/LITERATURE_2026.md`](q1_true/LITERATURE_2026.md)）的 nullspace 判据，
把"最小化 $\dim\mathcal V$"翻译成"最大化 $\dim Z$"：

$$\boxed{\ q_{\min}=n-p-d_{\max}\ }$$

$$d_{\max}=\max\Big\{\dim Z:\ Z\subseteq E,\ A(Z\cap K)\subseteq Z,\
\dim\big((\lambda I-A)K\cap Z\big)=\dim(K\cap Z)\ \forall\lambda\Big\},\quad E=\ker C\cap L_0^{\perp}.$$

**对算法设计的价值**：变量落在固定维数的环境 $E$ 里；目标变成"最大化"；两条约束都写成秩条件。

---

## 2. 代数部分有闭式，谱部分是唯一难点

$$\boxed{\ q_{\min}=r+\underbrace{\big(\dim(E\cap K)-\max_L\dim L\big)}_{\text{alg\_gap}}+\underbrace{\text{spec\_cut}}_{\text{谱条件}}\ }$$

$$L\subseteq E\cap K,\quad A(L)\subseteq E,\quad A(L)\cap K\subseteq L .$$

- **alg_gap**：纯代数（$(5a)$ 部分）。$\max_L$ 就是"最小动态 cover"的补维数；
- **spec_cut**：为了满足 $(8c)$ 必须额外降的维数。

**关键事实（已数值验证）**：当 $d=\dim E$ 时，代数族只有单点 $Z=E$；若 $E$ 不满足 $(8c)$，就必须降维。
所以 **spec_cut 经常是 1**，这正是 $q_{\min}=\dim V+1$ 常见的来源。

---

## 3. 文献：$(5a)$ 部分是低复杂度的

| 文献 | 结论 | 对本方向 |
|---|---|---|
| **Varga 2003, CDC**（[DLR](https://elib.dlr.de/12000/)）| 最小动态 cover 有 **low computational complexity** 的算法，直接服务于"minimum order functional observers" | $(5a)$ 部分多项式 |
| Karcanias–Vafiadis 1993 | 提出最小维数 cover 问题，无复杂度结论 | 无阻碍 |
| Fernando 2026（两篇）| 完整 order spectrum + chart 参数化；**无复杂度结论**；$\Theta$ 搜索未指定 | 算法空间存在，未被堵死 |
| 其他（almost invariant / 共不变子空间 / Tarski）| 几何、算子、可判定性 | 无 NP-hard 结论 |

$$\boxed{\ \text{文献里}\textbf{没有任何 NP-hard 结论}\ \Longrightarrow\ \text{证 q1 = 假 没有文献障碍}\ }$$

---

## 4. 要补的两个缺口（按优先级）

### 缺口 A：精确计算 $L_{\max}$

$$L_{\max}=\max\{\dim L:\ L\subseteq E\cap K,\ A(L)\subseteq E,\ A(L)\cap K\subseteq L\}.$$

- $A(L)\subseteq E$ 线性；
- $A(L)\cap K\subseteq L$ **不是格条件**（我构造了反例：两个可行 $L$ 的并不可行，见 [`q1_true/Z_FORMULATION.md`](q1_true/Z_FORMULATION.md) §4.1）；
- **警告**：它**不**等价于任何线性映射的不变子空间（我试过，错了，见 [`q1_true/D1_MIXED_CASE.md`](q1_true/D1_MIXED_CASE.md) §4）。

若能精确算 $L_{\max}$ 且它是多项式，则 alg_gap 多项式。

### 缺口 B：谱集与代数族的相交判定

$$\text{对每个维数 }d:\quad \mathcal A_d=\{Z:\dim Z=d,\ Z\subseteq E,\ A(Z\cap K)\subseteq Z\}\ \text{是否与谱集相交？}$$

这是"簇是否被除子包含"的问题。若可多项式判定 ⟹ q1 = 假。

---

## 5. 已验证的数据（可直接引用）

- **50 个可行实例**：公式 $q_{\min}=\max(r,\rho^*+1)$ **50/50**；可达 $(\text{实例},\rho)$ 对 **52/53 紧**，唯一例外已证（`refute_dimV1` 的 $\rho=1$ 层，见 ATTACK_LOG D42）。
- 45 个实例里**可达 $\rho$ 集合全是区间**（无跳跃）。
- 对已知解做小扰动：`middle_layer` 只有 **1.5%** 扰动仍合法、`candidate` **9.5%** —— 解集是薄集但非孤立。

---

## 6. 别踩的坑（我踩过，已验证是错的）

| 猜想 | 反例/原因 |
|---|---|
| $(8c)\iff AK\subseteq K+Z$ | 秩相等不蕴含包含；`candidate` 的真实解满足 $(8c)$ 但 $AK\not\subseteq K+Z$ |
| $A(L)\cap K\subseteq L$ 等价于某线性映射不变 | 只约束 $Av\in K$ 的那些 $v$；随机反例 |
| "$(5b)$ 是开条件 ⟹ 硬度只能来自闭条件" | $d=\dim E$ 时代数族是单点，$(5b)$ 反而把 $d$ 从 3 砍到 1（`candidate`）|
| 审计报的 $q=k$ 就是 $q_{\min}=k$ | 审计是搜索上界；`middle_layer` 自身 $t=0$ 处就漏解（`q1_false/tests/PROTOCOL.md` §已知限制）|

---

## 7. 文件指针

| 内容 | 位置 |
|---|---|
| 2026 文献（Fernando）| [`q1_true/LITERATURE_2026.md`](q1_true/LITERATURE_2026.md)、`q1_true/papers/` |
| cover 线文献（Varga / Karcanias）| [`q1_true/LITERATURE_COVER.md`](q1_true/LITERATURE_COVER.md) |
| Z-FORM 完整推导 + 非格反例 | [`q1_true/Z_FORMULATION.md`](q1_true/Z_FORMULATION.md) |
| 代数/谱分离 + 失败化简 | [`q1_true/D1_MIXED_CASE.md`](q1_true/D1_MIXED_CASE.md) |
| 9 条归约路线的失败点 | [`q1_true/ATTEMPTS_AND_BARRIERS.md`](q1_true/ATTEMPTS_AND_BARRIERS.md) |
| 审计数据 | `record/layer_audit_seed{3,5,9,21}.json` |

---

## 8. 一句话

$$\boxed{\ \text{证 q1 = 真：9 条路全部失败；证 q1 = 假：只剩"精确 }L_{\max}\text{"与"谱集∩代数族"两个具体缺口}\ }$$
