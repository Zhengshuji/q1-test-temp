> **开发日志摘要**（2026-10-27 整理）
> - **目标**：在"混合情形"（$E\cap K\ne0$ 且 $E\not\subseteq K$）上找 $d_{\max}$ 的组合结构。
> - **结果**：**死**。代数部分有谱结构、谱部分有代数结构，但没有形成可用于归约的组合对象。
> - **残留价值**：混合情形的分类（见原文）。
# D1：代数部分与谱部分的分离（含一次失败的化简）

> **记号提示**：本文用的是**旧框架**记号（$\alpha_0=L_0N_{CA}$、$d_{CA}$、$V=\langle S\rangle_{A'}$），
> 其结论 $\alpha_0\in V$ 在**新框架下已废**（$\dim V+1$ 被 $n{=}5$ 反例推翻）。
> 新旧对照见 [archive/framework_map/README.md](../../../archive/framework_map/README.md)。


## 目标
在"混合情形"（$E\cap K
e0$ 且 $E
ot\subseteq K$）上找 $d_{\max}$ 的组合结构，作为归约入口。

## 最终结论
**死**。代数部分有谱结构、谱部分有代数结构，但没有形成可用于归约的组合对象。

## 相关文件
- `archive/old_scripts/q1_true_routes/spectral_gap.py`、`c169_family_scan.py`
- [01_matroid_tap.md](01_matroid_tap.md)


> 2026-10-24。目标 D1：在"混合态"（$E\cap K\neq0$ 且 $E\not\subseteq K$）上看 $d_{\max}$ 是否有组合结构。
> 结果：**代数部分有闭式**；**谱条件 (8c) 是真正的约束**，可以把 $d$ 从 $3$ 砍到 $1$。
> 这**修正**了 Q1-TRUE README §2.1 的启发式（"硬度只能来自闭条件"）。

---

## 1. 代数部分（忽略 (8c)）

$(Z\text{-FORM})$ 的两条约束是 $Z\subseteq E:=\ker C\cap L_0^{\perp}$ 与 $A(Z\cap K)\subseteq Z$。

令 $L=Z\cap K$。则 $L\subseteq E\cap K$，且 $A(L)\subseteq Z\subseteq E$。反过来：

- 给定 $L\subseteq E\cap K$ 满足 $A(L)\subseteq E$ 与 $A(L)\cap K\subseteq L$，
- $Z$ 可以取成 $L+A(L)$ 在 $E$ 内、模 $K$ 的任意补，
- 最大维数 $\dim Z=\dim L+\dim E-\dim(E\cap K)$。

$$\boxed{\ d_{\text{alg}}=\dim E-\dim(E\cap K)+\max_{L}\dim L\ }$$

$$\text{于是}\quad q_{\text{alg}}=n-p-d_{\text{alg}}=r+\big(\dim(E\cap K)-\max_L\dim L\big).$$

**特例**：若 $L=E\cap K$ 本身可行（$A(E\cap K)\subseteq E$ 且 $A(E\cap K)\cap K\subseteq E\cap K$），则 $d_{\text{alg}}=\dim E$、$q_{\text{alg}}=r$。

$$\Longrightarrow\ \textbf{代数部分总是给出下界 } r\ \textbf{（当 }E\cap K\text{ 可行时）}$$

---

## 2. 数值：代数 vs 真实

$d_{\text{true}}=n-p-q_{\min}$（$q_{\min}$ 取自已验证的解）。

| 实例 | $n,p,r$ | $\dim E$ | $\dim(E\cap K)$ | $E\cap K$ 可行？ | $d_{\text{alg}}$ | $d_{\text{true}}$ |
|---|---|---|---|---|---|---|
| `refute_dimV1` | 5,2,1 | 2 | 1 | 是 | 2 | **2** ✓ |
| `middle_layer` | 6,2,1 | 3 | 2 | 否（$A(E\cap K)\not\subseteq E$）| 2（$L_{\max}=1$）| **2** ✓ |
| `candidate` | 5,1,1 | 3 | 2 | 是 | **3** | **1** ✗ |

$$\boxed{\ \text{`candidate`：代数部分说 }d=3\ (q=1)，\text{真实 }d=1\ (q=3)\ \text{—— 谱条件砍掉 2 维}}$$

---

## 3. 为什么 (8c) 能砍这么多

$$(8c)\iff\dim\big((\lambda I-A)K\cap Z\big)=\dim(K\cap Z)\quad\forall\lambda .$$

当 $d=\dim E$ 时，$Z\subseteq E$ 且 $\dim Z=\dim E$ **强制** $Z=E$ —— 代数族只有一个点。
若这个点不满足 $(8c)$，就只能降维。降一维后代数族才有正维数，$(8c)$ 才可能"一般位置成立"。

$$\Longrightarrow\ \text{顶部维数总是单点解 ⟹ 顶部经常被 (8c) 排除 ⟹ } q_{\min}>r\ \text{很常见}.$$

---

## 4. 一次失败的化简（记录，避免重走）

我曾猜 $(8c)\iff AK\subseteq K+Z$。**这是错的**：

- 它只是**充分**条件（若 $AK\subseteq K+Z$，则 $(\lambda I-A)K\subseteq K+Z$）；
- 但等式 $\dim((\lambda I-A)K+Z)=\dim(K+Z)$ **不**要求 $(\lambda I-A)K\subseteq K+Z$，
  因为左边这个和**不一定包含 $K$**。

数值反例：`candidate` 的真实解满足 $(8c)$，但 $AK\not\subseteq K+Z$。

$$\boxed{\ \text{不要把"秩相等"偷换成"包含"—— 这是本项目踩过多次的同类错误。}}$$

---

## 5. 对 q1 的意义（修正后的判断）

| 旧启发式 | 修正 |
|---|---|
| "硬度只能来自闭条件（(5a)/ci 结构）" | **(8c) 虽然在 $L$ 中是开条件，但在 $Z$ 的代数族上经常是紧约束**；它排除顶部维数的单点解，直接把 $q$ 抬到 $r+1,r+2$ |

$$\text{真实图景}:\quad q_{\min}=r+\Big(\text{为满足 }(8c)\text{ 必须\textbf{降多少维}}\Big)\ \text{（在代数族内）}$$

**新靶子**：对每个维数 $d$，判定"代数族 $\{Z:\dim Z=d,\ Z\subseteq E,\ A(Z\cap K)\subseteq Z\}$ 是否与谱集相交"。
这是"簇是否被除子包含"的问题 —— 既可能多项式（用一般位置点），也可能是难度的来源。

---

## 6. 复现

```bash
# 计算 d_alg 所需的量（dimE, dim(E∩K), 可行性）
python -c "..."   # 见本轮会话记录；数据表在 §2
```

> 这一步是**分析 + 小规模精确计算**，没有跑大规模搜索。

---

## 7. 统计（28 个实例）：总量可靠，分解不可靠

脚本：[`scripts/spectral_gap.py`](../../../archive/old_scripts/q1_true_routes/spectral_gap.py)。

$$q_{\min}-r=\underbrace{\big(\dim(E\cap K)-L_{\max}\big)}_{\text{alg\_gap}}+\underbrace{\text{spec\_cut}}_{\text{谱条件}}$$

| 量 | 分布（28 实例）|
|---|---|
| $q_{\min}-r$ | $\{0{:}4,\ 1{:}6,\ 2{:}9,\ 3{:}3,\ 4{:}6\}$ |
| alg_gap | $\{0{:}10,\ 1{:}12,\ 2{:}5,\ 3{:}1\}$ |
| spec_cut | $\{0{:}5,\ 1{:}15,\ 2{:}7,\ 3{:}1\}$ |

### 7.1 一个诚实的警告

上表的 **alg_gap / spec_cut 不可信**：$L_{\max}$ 是用随机采样估的下界，换一个种子就会变
（例如三个 $q_{\min}=5$ 的实例，$(\text{alg\_gap},\text{spec\_cut})$ 分别是 $(2,2),(1,3),(3,1)$，
而总量恒为 $4$）。

$$\boxed{\ \text{可靠的是总量 }q_{\min}-r\text{；把总量拆成"代数/谱"两部分需要\textbf{精确的 }L_{\max}}\ }$$

### 7.2 精确 $L_{\max}$ 是一个独立的小问题

$$L_{\max}=\max\{\dim L:\ L\subseteq E\cap K,\ A(L)\subseteq E,\ A(L)\cap K\subseteq L\}.$$

已知：
- 条件 $A(L)\subseteq E$ 是线性的（$L\subseteq A^{-1}(E)$）；
- $A(L)\cap K\subseteq L$ **不是**格条件（与 §4.1 的非格现象同源）；
- 曾猜它等价于 "$L$ 是某个线性映射的不变子空间"，**但这是错的**（只约束 $Av\in K$ 的那些 $v$）。

这个问题本身已经足够小、可以单独攻；它可能是 q1 的一个缩影。

### 7.3 对 q1 的判断（本轮结束时的位置）

- $q_{\min}-r$ 在样本里随 $n$ 增长（最大到 4），与 $q_{\min}\approx\dim V+1$ 一致；
- 没有看到"组合爆炸"的证据，也没有归约；
- **Q1-TRUE 仍未找到任何硬度来源**，但已把问题压到两个明确的小问题上：
  (a) 精确 $L_{\max}$；(b) 谱集与代数族的相交判定。

---

## 8. R-族的维度扫描（c169）

脚本：[`scripts/c169_family_scan.py`](../../../archive/old_scripts/q1_true_routes/c169_family_scan.py)。

把 `../../archive/process_logs/COUNTEREXAMPLE_2026-10-22.md` 的 R-族（Krylov 维数 2）推广到一般 $d$：

| $d$ | $n$ | $\dim K$ | $\dim V$ | $\rho_0$ | $\rho^*$ | $q_{\min}$ |
|---|---|---|---|---|---|---|
| 3 | 5 | 3 | 2 | 1 | 2 | **3** |
| 4 | 6 | 4 | 2 | 1 | 2 | **3** |
| 5 | 7 | 5 | 2 | 1 | — | 搜索未命中 |

$$\boxed{\ q_{\min}=3\ \text{对 }d=3,4\ \text{成立，且}\ \dim V=2\ \text{不随 }d\ \text{增长}}$$

**构造中踩到的坑（记下）**：$u$ 必须**不在** $K$ 里（取 $u=e_{d+1}$），否则 $R_0=u\otimes r$
的列全在 $K$ 内，会被压缩 $A'$ 吸收，导致 $S=0$、$\dim V=0$、$R_0$ 实际为 0。

**解读**：这又是一个"平"的族——最小阶不随维数增长。它对 q1 = 真 **不提供支持**。

### 8.1 幂零 Jordan 族（2026-10-24 补测）

把 $A'$ 换成单个幂零 Jordan 块（$A' e_i=e_{i+1}$），其余同 c169：

| $d$ | $\dim V$ | $\rho_0$ | $\rho^*$ | $q_{\min}$ |
|---|---|---|---|---|
| 3 | 3 | 1 | 3 | **4** $=\dim V+1$ |
| 4 | 4 | 1 | 4 | **5** $=\dim V+1$ |

$$\boxed{\ \text{幂零（唯一特征值 }\lambda=0\text{）也只给默认情形 }q_{\min}=\dim V+1\ }$$

**注**：随机的幂零 $A$ 几乎全部**不可行**（$\alpha_0\in V$ 是余维条件）；能构造出来的可行幂零实例都落在默认分支。
这是"$\rho^*=\dim V$ 默认"的又一类结构。至此试过的结构（对角、交换块、幂零 Jordan）**全部给默认情形**。
