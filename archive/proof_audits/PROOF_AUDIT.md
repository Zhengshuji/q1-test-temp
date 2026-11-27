# 证明审计（Proof Audit）

> 目的：对本会话声称的**核心定理**做逐条自查，找出可能的漏洞。
> 审计对象：
> · **A19**：$(\text{5a})\wedge(\text{5b})\Rightarrow\rho\le\text{obs}$
> · **A20**：$(\text{5a})\wedge(\text{5b})\Rightarrow\alpha_0\in V$
> · **判据**：$\text{YES at }q\iff\alpha_0\in V$（两侧）

---

## 0. 记号（严格定义）

| 记号 | 定义 | 尺寸 |
|---|---|---|
| $A\in\mathbb{Q}^{n\times n}$ | 系统矩阵 | $n\times n$ |
| $C$ | 输出行 | $1\times n$（一般 $p\times n$）|
| $N$ | $\ker[C;CA]$ 的基 | $n\times d$，$d=d_{CA}$ |
| $A'$ | $(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN$ | $d\times d$ |
| $R$ | $AN-NA'$ | $n\times d$ |
| $\mathcal L$ | $q\times n$（含固定首行 $L_0$）| $q\times n$ |
| $M$ | $\mathcal LN$ | $q\times d$ |
| $F$ | $\mathcal LAN$ | $q\times d$ |
| $A_0,A_1$ | $=M,\,F$（**同一矩阵**）| $q\times d$ |
| $\rho$ | $\operatorname{rank}M=\operatorname{rank}A_0$ | 标量 |
| $\mathcal N$ | $\ker M^{\mathsf T}\subseteq\mathbb{R}^q$ | $\dim=q-\rho$ |
| $\tilde V$ | $\sum_{t\ge0}(A'^{\mathsf T})^t\operatorname{im}(R^{\mathsf T})$ | $\subseteq\mathbb{R}^d$ |
| $\text{obs}$ | $\dim\tilde V=\dim V$ | 标量 |
| $\alpha_0$ | $L_0N$（$M$ 的首行）| $1\times d$ |

**(5a)**：$\ker A_0\subseteq\ker A_1$ ⟺ $\exists\Lambda\in\mathbb{Q}^{q\times q}:\ F=\Lambda M$
**(5b)**：$\operatorname{rank}(\lambda M-F)=\rho\ \ \forall\lambda\in\mathbb{C}$

---

## 1. 关键恒等式（先核对，全部为算术）

$$\textbf{(I)}\quad AN=NA'+R\qquad\text{(R 的定义)}$$
$$\textbf{(II)}\quad F=\mathcal LAN=\mathcal L(NA'+R)=\underbrace{\mathcal LN}_{M}A'+\mathcal LR=MA'+\mathcal LR\ \checkmark$$
$$\textbf{(III)}\quad F^{\mathsf T}=A'^{\mathsf T}M^{\mathsf T}+R^{\mathsf T}\mathcal L^{\mathsf T}\ \checkmark$$
$$\textbf{(IV)}\quad\text{(5a)}\Rightarrow F=\Lambda M\Rightarrow F^{\mathsf T}=M^{\mathsf T}\Lambda^{\mathsf T}\ \checkmark$$
$$\textbf{(V)}\quad\tilde V\ \text{是}\ A'^{\mathsf T}\text{-不变的（按定义取闭包）}\ \checkmark$$

---

## 2. A19 的逐步审计

### 步 1：$(\text{5b})\iff\operatorname{rank}\big[\,\Lambda^{\mathsf T}-\lambda I\ \big|\ \mathcal N\,\big]=q\ \forall\lambda$

**推导**：
$$\lambda M-F=\lambda M-\Lambda M=(\lambda I-\Lambda)M$$
$$\operatorname{rank}(AB)=\dim\operatorname{im}B-\dim(\operatorname{im}B\cap\ker A)$$
$$\operatorname{rank}\big((\lambda I-\Lambda)M\big)=\rho=\dim\operatorname{im}M\iff\operatorname{im}M\cap\ker(\lambda I-\Lambda)=0$$
取正交补：
$$\big(\operatorname{im}M\cap\ker(\lambda I-\Lambda)\big)^\perp=(\operatorname{im}M)^\perp+\big(\ker(\lambda I-\Lambda)\big)^\perp=\mathcal N+\operatorname{im}(\Lambda^{\mathsf T}-\lambda I)$$
$$\Longrightarrow\ \text{条件}\iff\mathcal N+\operatorname{im}(\Lambda^{\mathsf T}-\lambda I)=\mathbb{R}^q\iff\operatorname{rank}\big[\Lambda^{\mathsf T}-\lambda I\mid\mathcal N\big]=q\ \checkmark$$

**状态**：✅ **正确**（纯线性代数，无隐藏假设）

### 步 2：⟺ $(\Lambda^{\mathsf T},\mathcal N)$ 可控（**PBH 测试**）

**PBH（标准形式）**：$(A,B)$ 可控 $\iff\operatorname{rank}[\lambda I-A,\ B]=n\ \forall\lambda\in\mathbb{C}$
取 $A=\Lambda^{\mathsf T}$、$B$ = 列空间为 $\mathcal N$ 的矩阵 ⟹ 即步 1 的式子 ✓

**状态**：✅ **正确**（经典定理；$\lambda$ 量词为 $\mathbb{C}$ ✓，与本项目一致）

### 步 3：可控 ⟹ $K:=\sum_{k\ge0}(\Lambda^{\mathsf T})^k\mathcal N=\mathbb{R}^q$

**依据**：可控性定义 = 可控子空间为全空间 ✓（PBH ⟺ 可控子空间为全空间，经典 ✓）

**状态**：✅ **正确**

### 步 4：$F^{\mathsf T}(K)\subseteq\tilde V$

**归纳**（对 $u_0\in\mathcal N$ 及迭代）：
- 基础：$M^{\mathsf T}u_0=0$ ⟹ $F^{\mathsf T}u_0\overset{(III)}{=}R^{\mathsf T}\mathcal L^{\mathsf T}u_0\in\operatorname{im}R^{\mathsf T}\subseteq\tilde V$ ✓
- 归纳：设 $F^{\mathsf T}u_{k-1}\in\tilde V$，取 $u_k=\Lambda^{\mathsf T}u_{k-1}$：
  $$M^{\mathsf T}u_k=M^{\mathsf T}\Lambda^{\mathsf T}u_{k-1}\overset{(IV)}{=}F^{\mathsf T}u_{k-1}\in\tilde V$$
  $$F^{\mathsf T}u_k\overset{(III)}{=}\underbrace{A'^{\mathsf T}(M^{\mathsf T}u_k)}_{\in A'^{\mathsf T}\tilde V=\tilde V}+\underbrace{R^{\mathsf T}\mathcal L^{\mathsf T}u_k}_{\in\operatorname{im}R^{\mathsf T}\subseteq\tilde V}\in\tilde V\ \checkmark$$

**状态**：✅ **正确**（关键：$M^{\mathsf T}\Lambda^{\mathsf T}=F^{\mathsf T}$ 是 (5a) 的直接后果 ✓）

### 步 5：$K=\mathbb{R}^q$ ⟹ $\operatorname{im}F^{\mathsf T}=F^{\mathsf T}(\mathbb{R}^q)\subseteq\tilde V$

**状态**：✅ **正确**

### 步 6：$\dim\operatorname{im}F^{\mathsf T}=\rho$

$(5b)$ 在 $\lambda=0$：$\operatorname{rank}(-F)=\rho$ ⟹ $\operatorname{rank}F=\rho=\dim\operatorname{im}F^{\mathsf T}$ ✓

**状态**：✅ **正确**

### 结论

$$\rho=\dim\operatorname{im}F^{\mathsf T}\le\dim\tilde V=\text{obs}\qquad\checkmark$$

$$\boxed{\ \textbf{A19 审计通过}\ }$$

---

## 3. A20 的逐步审计

### 步 1：$(\text{5a})\Rightarrow\operatorname{im}F^{\mathsf T}\subseteq\operatorname{im}M^{\mathsf T}$

$F^{\mathsf T}=M^{\mathsf T}\Lambda^{\mathsf T}$ ⟹ $\operatorname{im}F^{\mathsf T}\subseteq\operatorname{im}M^{\mathsf T}$ ✓

**状态**：✅ **正确**

### 步 2：$(\text{5b})\Rightarrow\operatorname{im}F^{\mathsf T}\subseteq\tilde V$

即 A19 的步 1–5 ✓

**状态**：✅ **正确**（依赖 A19 ✓）

### 步 3：$\dim\operatorname{im}M^{\mathsf T}=\rho$

$\dim\operatorname{im}M^{\mathsf T}=\operatorname{rank}M^{\mathsf T}=\operatorname{rank}M=\rho$ ✓

**状态**：✅ **正确**

### 步 4：$\operatorname{im}M^{\mathsf T}\subseteq\tilde V$

$$\operatorname{im}F^{\mathsf T}\subseteq\operatorname{im}M^{\mathsf T}\cap\tilde V,\qquad \dim\operatorname{im}F^{\mathsf T}=\rho$$
$$\Longrightarrow\ \rho\le\dim(\operatorname{im}M^{\mathsf T}\cap\tilde V)\le\dim\operatorname{im}M^{\mathsf T}=\rho$$
$$\Longrightarrow\ \dim(\operatorname{im}M^{\mathsf T}\cap\tilde V)=\dim\operatorname{im}M^{\mathsf T}$$
$$\Longrightarrow\ \operatorname{im}M^{\mathsf T}\subseteq\tilde V\quad(\text{同维包含即相等})\ \checkmark$$

**状态**：✅ **正确**（这条已用 Lean 形式化于 `CriterionCore.lean`：
`le_trans_of_le_of_finrank_eq` ✓）

### 步 5：$\alpha_0^{\mathsf T}=M^{\mathsf T}e_1\in\operatorname{im}M^{\mathsf T}\subseteq\tilde V$

$M^{\mathsf T}e_1$ = $M^{\mathsf T}$ 的首列 = $M$ 首行的转置 = $\alpha_0^{\mathsf T}$ ✓

**状态**：✅ **正确**（注意转置方向 ✓）

### 结论

$$\alpha_0\in V\qquad\checkmark$$

$$\boxed{\ \textbf{A20 审计通过}\ }$$

---

## 4. 审计中发现的**两个需要强调的点**

### 4.1 ⚠️ A20 **对任意 $q$ 都成立**（不限于 $q=d+1$）

A20 的证明只用到 $(5a)$、$(5b)$、以及 $M,F,N,A',R$ 的定义 —— **与行数 $q$ 无关** ✓

$$\boxed{\ \textbf{故：}\alpha_0\notin V\ \Longrightarrow\ \textbf{NO for ALL}\ q\ \text{（非仅}\ q\le d{+}1\text{）}\ }$$

$$\text{这比我此前的表述更强，且与实证一致（}q{=}d{+}1,d{+}2,d{+}3\ \text{全 NO}\ ✓\text{）}$$

### 4.2 ⚠️ 充分性的 $q$ 必须是 $\text{obs}+1$，再由单调性到 $d+1$

充分性构造（§7.5.3）在**压缩问题**上做，规模是 $\text{obs}$，给出 YES at $q=\text{obs}+1$；
由单调性（A7）⟹ YES at 所有 $q\ge\text{obs}+1$；而 $\text{obs}\le d$ ⟹ $d+1\ge\text{obs}+1$ ⟹ **YES at $d+1$** ✓

**状态**：✅ 逻辑闭合（此处曾是我表述含糊之处，现已澄清 ✓）

---

## 5. 审计中**未发现**的问题（逐项排除）

| 可能的漏洞 | 检查结果 |
|---|---|
| $\Lambda$ 的存在性是否被滥用？ | (5a) ⟺ $\exists\Lambda:F=\Lambda M$ ✓ 已证（Lean）|
| $F$ 与 $M$ 的行数/列数是否一致？ | 都是 $q\times d$ ✓ |
| $\mathcal N$ 与 $\operatorname{im}M^{\mathsf T}$ 是否混淆？ | $\mathcal N=\ker M^{\mathsf T}$（左零），$\operatorname{im}M^{\mathsf T}$（列空间）—— 集合不同，**维度都是 $q-\rho$ 与 $\rho$** ✓ 审计中已区分 ✓ |
| $\tilde V$ 与 $V$ 是否混淆？ | $\tilde V\subseteq\mathbb{R}^d$（列侧），$V\subseteq(\mathbb{R}^d)^*$（行侧），**同维**，转置等同 ✓ |
| PBH 的 $\lambda$ 量词范围？ | $\mathbb{C}$ ✓ 与 (5b) 一致 ✓ |
| $\rho=0$ 退化情形？ | $\alpha_0=0\in V$ 平凡 ✓；(5b) 自动 ⟺ $\mathcal LR=0$ ✓ 一致 ✓ |
| $d=0$（$N$ 空）？ | $\text{obs}=0,\rho=0$ ✓ 平凡 ✓ |
| 是否需要 $A'$ 有理性/可对角化？ | **不需要** ✓ —— A19/A20 的证明**完全没用到** squarefreeness ✓（那只用于 A14 的旧路线）|

---

## 6. 审计结论

$$\boxed{\ \textbf{A19、A20 与判据的证明均无逻辑漏洞（逐步自查通过）}\ }$$

**但必须诚实标注三点**：

1. **PBH 测试是引用的经典定理** ✓ —— 若要求完全自足，需补一句：
   "$(\Lambda^{\mathsf T},\mathcal N)$ 可控 $\iff$ 可控子空间 $=\mathbb{R}^q$" 是定义级的 ✓
2. **充分性依赖 pole placement** ✓ —— 经典结果（$(A'^{\mathsf T},R^{\mathsf T})$ 可控 ⟺ 可任意配置特征多项式）✓
3. **以上均未用 Lean 完整形式化**（只形式化了 A20 第 4 步）⚠️ ——
   完整形式化需要 $(5a)/(5b)$ 的矩阵形式定义与 PBH，工作量较大

---

## 7. 🔴🔴 **审计发现的代码 bug（第 40 处更正）**

### 7.1 bug 内容

```python
ps = [所有 ρ 阶子式]              # ps[0] 可能是零多项式 ['0','0']
g = ps[0]                         # ⟹ g = 0
for x in ps[1:]:
    g = Pg(g, x)
    if len(g) == 1: break         # g=['0'] 时也被当作"已互素" ✗
```

**触发条件**：开头**至少两个** ρ 阶子式同时为零多项式
$$\Longrightarrow\ g=\text{Pg}(0,0)=0,\quad \texttt{len}(g)=1\ \Longrightarrow\ \text{误判为互素}\ ✗$$
$$\Longrightarrow\ \texttt{const\_nz}\ \text{返回 False}\ \Longrightarrow\ \textbf{(5b) 被误报为失败（假阴性）}\ ✗$$

**影响方向**：假阴性 ⟹ **漏报解** ⟹ 可能把"其实有解"的实例判成 **NO** ⚠️

### 7.2 修复

```python
def gcd_fixed(ps):
    nz = [p for p in ps if not is_zero(p)]     # 跳过零多项式 ✓
    if not nz: return ZERO
    g = nz[0]
    for x in nz[1:]:
        g = Pg(g, x)
        if is_nz_const(g): break               # 只在非零常数时退出 ✓
    return g
```

### 7.3 重查结果（`c86_RECHECK.py`）

| 实例 | $\alpha_0\in V$ | 旧判解数 | 新判解数 |
|---|---|---|---|
| 6 个（Y）| Y | 72–624 | **完全相同** ✓ |
| **2 个（N）** | N | **0** | **0** ✓ |

$$\text{翻转实例：}\mathbf{0}\qquad\Longrightarrow\ \text{判据必要性}\ (\alpha_0\notin V\Rightarrow\text{NO})\ \textbf{仍成立}\ ✓$$

### 7.4 ⚠️ **另一条重要教训：sympy 的 `rank()` 不能当裁判**

$$\text{sympy }\texttt{Matrix.rank()}\ \text{算的是}\ \textbf{泛型秩}\ (\text{over}\ \mathbb{Q}(\lambda))\ ✗$$
$$\text{而 (5b) 要求}\ \operatorname{rank}=\rho\ \textbf{在每个具体}\ \lambda\in\mathbb{C}\ \text{处}\ (\text{不允许秩降})\ ✓$$

**例**（`c84` trial 3）：子式 $=(\lambda+1)^2$ 与 $0$ ⟹ sympy 判 rank 2（泛型）；
但 $\lambda=-1$ 时实际秩降为 1 ⟹ **(5b) 确实失败** ✓ ⟹ **我的 gcd 判据正确，sympy 裁判错误** ✗

$$\Longrightarrow\ \textbf{教训}：\text{"秩恒定"必须用}\ \textbf{子式 gcd}\ \text{判，不能用泛型秩}\ ✗$$

---

## 8. 最终审计裁定

| 项 | 裁定 |
|---|---|
| **A19 的数学证明** | ✅ **无漏洞**（6 步全部核验）|
| **A19 步 1–2（PBH 等价）** | ✅ **数值验证 60/60**（$\rho=d$）+ **60/60**（$\rho<d$，修正版）|
| **A20 的数学证明** | ✅ **无漏洞**（5 步全部核验；第 4 步已 Lean 形式化）|
| **判据（两侧）** | ✅ **成立** |
| **代码实现** | ⚠️ 发现 1 个 bug（假阴性），**已修复并建回归测试** ✓ |
| **sympy 作为裁判** | ✗ **不可用于"秩恒定"判定**（泛型秩 ≠ 恒定秩）|

$$\boxed{\ \textbf{结论}：\text{数学证明通过审计};\ \text{实现 bug 已修复};\ \text{核心结论保持不变}\ }$$

---

## 9. 改进措施（已实施）

### 9.1 新增共享修正模块 `scripts/core/exact_gcd.py`

$$\text{提供}\ \texttt{cond\_5b}\ /\ \texttt{cond\_5b\_verbose}\ /\ \texttt{gcd\_list}\ /\ \texttt{Pdet}\ \text{等，全部修正}$$

**关键修正**：
```python
def gcd_list(ps):
    nz = [p for p in ps if not is_zero(p)]     # 跳过零多项式 ✓
    if not nz: return ZERO
    g = nz[0]
    for x in nz[1:]:
        g = Pg(g, x)
        if is_nonzero_const(g): break           # 只在非零常数时退出 ✓
    return g
```

### 9.2 回归测试（内置于 `exact_gcd.py` 的自检）

| 用例 | 内容 | 期望 |
|---|---|---|
| **1** | 开头两个子式为零（**旧 bug 的触发条件**）| (5b)=True ✓ |
| **2** | $\lambda=-1$ 处真的秩降 | (5b)=False ✓ |

$$\texttt{python}\ \texttt{exact\_gcd.py}\ \Longrightarrow\ \textbf{全部回归通过}\ ✓$$

### 9.3 两个既有验证器**无此 bug**（已核对 ✓）

$$\texttt{verify\_all.py}\ \text{与}\ \texttt{verify\_equivalences.py}\ \text{都先}\ \texttt{if dd != [Fr(0)]: ps.append(dd)}\ ✓$$
$$\Longrightarrow\ \text{它们的历史结论}\ \textbf{不受影响}\ ✓$$

### 9.4 修正版重跑审计（`c87_AUDIT_FIXED.py`）

$$\rho<d\ \text{实例}\ 60\ \text{个：一致}\ \mathbf{60}\ \text{，不一致}\ \mathbf{0}\ ✓$$

| $(d,\rho)$ | 数量 | 一致 |
|---|---|---|
| (2, 1) | 16 | 16 ✓ |
| (3, 1) | 30 | 30 ✓ |
| (3, 2) | 14 | 14 ✓ |

$$\Longrightarrow\ \textbf{A19 步 1–2 的审计完整通过（含}\ \rho<d\text{）}\ ✓$$
$$\text{旧版 2/40 的"不一致"}\ \textbf{确认为 gcd bug（假阴性），修复后消除}\ ✓$$


