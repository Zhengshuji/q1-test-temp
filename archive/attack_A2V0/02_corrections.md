> **归档说明（2026-10-27 重构）**：本文件是从旧文档拆出的归档件，文中链接指向重构前的旧路径；新旧路径映射见根目录 `ATTEMPTS.md` 与 `README.md`。

# 提升引理 §14–§20（拆分自 LEMMA_LIFT_2026-10-23.md）

> 原文：`archive/attack_A2V0/LEMMA_LIFT_2026-10-23.md`。整条链对应已推翻的 $q_{\min}=\dim V+1$。

## 14. ✅ 引理 12.1 的严格版（显式构造，不用"一般位置"）

### 14.1 我们要的其实只是**单射**

由 §12.2：$(b)\iff F\vert_{V^{\perp}}$ **单射**（不要求秩恰好最大，只需 $=d-\rho$）。

所以只需**显式构造**一个 $L$ 使 $F\vert_{V^{\perp}}$ 单射 ✓ —— 不需要"一般位置"的抽象论证。

### 14.2 构造

记 $X:=V^{\perp}$（$\dim=d-\rho$），$F_1:=M\circ(A')_V\vert_X$（**固定**），$F_2:=(L|_S)\circ R_0\vert_X$（**可调**）。

**第 1 步**：分解 $X=\ker F_1\oplus W$（$\dim W=\operatorname{rank}F_1=:r_1\le\rho$）。

**第 2 步**：在 $\ker F_1$ 上要求 $F_2$ 单射。
$$\dim\ker F_1=(d-\rho)-r_1\ \le\ (d-\rho)-\rho\ \le\ p_1\quad(\text{由条件}\ d-\rho\le 2\rho+p_1\ \text{与}\ r_1\le\rho)$$
而 $F_2$ 的像可落在任意 $\le p_1$ 维子空间（$L|_S$ 自由 ✓）⟹ **可取 $F_2\vert_{\ker F_1}$ 单射** ✓

**第 3 步**：在 $W$ 上，$F_1\vert_W$ 单射（$W$ 是 $\ker F_1$ 的补 ✓）。
取 $F_2\vert_W$ 使 $(F_1+F_2)\vert_W$ 仍单射 —— 例如取 $F_2\vert_W$ 的像落在 $F_1(W)$ 的正交补方向 ✓
（$\dim F_1(W)=r_1\le\rho$，而 $q\ge\rho+1$，故 $F_1(W)$ 不充满 $\mathbb R^q$ ✓ 总有可用方向 ✓）

**第 4 步**：合并。$X=\ker F_1\oplus W$ ✓，$F_2$ 在这两块上分别构造 ✓。
$$\text{对}\ v=x+w\ (x\in\ker F_1,\ w\in W):\quad (F_1+F_2)v=\underbrace{F_2x}_{\in\operatorname{im}F_2\ \text{(单射)}}+\underbrace{(F_1+F_2)w}_{\in F_1(W)+\operatorname{im}F_2}$$

取 $\operatorname{im}F_2$ 与 $F_1(W)$ 横截（可能，因 $\dim F_1(W)=r_1\le\rho$、$\dim\operatorname{im}F_2\le p_1$、$r_1+p_1\le q$ ✓）
⟹ 两部分独立 ⟹ $(F_1+F_2)v\ne0$ 对 $v\ne0$ ✓

$$\boxed{\ F\vert_{V^{\perp}}\ \text{单射}\quad\Longrightarrow\quad (b)\ \checkmark\ }$$

### 14.3 条件检查

$$\text{第 2 步用了}\ d-\rho-r_1\le p_1\quad\Longleftarrow\quad d-\rho\le\rho+p_1\ (\text{因}\ r_1\le\rho)\ ✓$$
$$\text{第 4 步用了}\ r_1+p_1\le q=\max(\rho+1,d-\rho)\quad\Longleftarrow\quad r_1\le\rho\le q-1\ \text{且}\ p_1\le q-\rho\ \text{hmm}$$

**第 4 步的条件需再核**：$r_1+p_1\le q$ ✓？

- 若 $q=\rho+1$：$r_1+p_1\le\rho+p_1$ —— 需 $p_1\le1$ hmm ⚠️
- 若 $q=d-\rho$：$r_1+p_1\le\rho+p_1$ —— 需 $\rho+p_1\le d-\rho$ ✓（即条件本身 ✓）

$$\textbf{所以第 4 步在}\ q=\rho+1\ \text{时需额外条件（}p_1\ \text{小）}\ ✗\ \text{——这是残余缺口}$$

### 14.4 结论

$$\boxed{\ \text{上界在}\ q=\max(\rho+1,d-\rho)\ \text{下成立，除了}\ q=\rho+1\ \text{且}\ p_1\ \text{较大时的边界情形}}$$

**已验证**：6/6 实例全部满足 ✓（含 $q=\rho+1$ 的情形 ✓ —— 说明那里的第 4 步实际上更容易 ✓）

### 14.5 残余缺口的准确形式

$$\text{当}\ q=\rho+1\ \text{（即}\ d-\rho\le\rho+1\text{）时，需要}\ r_1+p_1\le\rho+1$$

$$\text{而}\ r_1\le\rho\ \text{且}\ p_1\le p\ \text{——所以只要}\ p_1\le1\ \text{或}\ r_1\le\rho+1-p_1\ \text{即可}$$

**可能总成立**（需再核 $r_1$ 与 $p_1$ 的关系）；**或者**改用更强的第 4 步构造（不要求横截，只要求单射）。

---

## 15. 🔴 关键更正：$p_1=0$ —— §12 的"$L$ 自由度"论证失效

### 15.1 计算

| 实例 | $d$ | $\rho$ | $p$ | $\dim V^{\perp}$ | $p_1=\operatorname{rank}(R_0\vert_{V^{\perp}})$ |
|---|---|---|---|---|---|
| `cand` | 3 | 2 | 1 | 1 | **0** |
| `d4` | 4 | 2 | 1 | 2 | **0** |
| `p2` | 4 | 2 | 2 | 2 | **0** |

$$\Longrightarrow\quad R_0(V^{\perp})=0\ \Longrightarrow\ F_2=(L|_S)\circ R_0\vert_{V^{\perp}}\equiv0\ \textbf{恒零}\ ✗$$

### 15.2 后果

$$\boxed{\ F\vert_{V^{\perp}}=F_1=M\circ(A')_V\vert_{V^{\perp}}\quad\textbf{完全固定};\ L\ \text{的自由度无作用}\ ✗\ }$$

$$\text{所以 (b) 可行}\iff d-\rho\le\operatorname{rank}(A')_V\vert_{V^{\perp}}=\dim\big((A')_V(V^{\perp})\big)$$

**这是一个关于 $(A',V)$ 的结构条件** ✓ —— 不是 $L$ 的构造能解决的 ✓

### 15.3 对我们的实例意味着什么

$$d-\rho=2\le\rho=2\quad\Longrightarrow\quad \text{需要}\ \dim\big((A')_V(V^{\perp})\big)=2$$

即 $(A')_V$ 在 $V^{\perp}$ 上满秩 ✓ —— 已数值验证成立（因为 $q_{\min}$ 确实 $=3$ ✓）

### 15.4 §12 / §14 的地位（诚实标注）

| 节 | 内容 | 状态 |
|---|---|---|
| §12 | "一般位置"论证 | 🔴 **在本批实例上失效**（$p_1=0$ ⟹ $F_2=0$）✗ |
| §14 | 显式构造 | 🔴 同上（构造出的 $F_2$ 是零）✗ |
| **§15** | 真正的条件：$\dim((A')_V(V^{\perp}))=d-\rho$ | ✅ 正确 ✓ |

### 15.5 修正后的判据

$$\boxed{\ \text{(b) 可行}\iff d-\rho\ \le\ \operatorname{rank}\Big((A')_V\big\vert_{V^{\perp}}\Big)\ }$$

$$\text{结合下界}\ \Longrightarrow\quad q_{\min}=\max\Big(\rho+1,\ d-\rho\Big)\quad\text{当上面条件成立}$$

**待做**：
1. 验证 $6/6$ 实例都满足 $\dim((A')_V(V^\perp))=d-\rho$ ✓
2. 找出该条件与 $A',V,S$ 的关系（是否自动？）
3. 若**不自动** ⟹ 存在无解实例 ⟹ 判据就是这些条件 ✓

---

## 16. 🔴🔴 撤回：$(b)$ 的方向写错了

### 16.1 正确的等价

$$(b)\iff\dim\ker(\lambda M-F)=\operatorname{rank}M=\rho\iff\dim\ker(\lambda M-F)=d-\rho$$

$\ker M=V^{\perp}$（$\dim=d-\rho$ ✓），且 $(5a)\iff\ker M\subseteq\ker(\lambda M-F)$ ✓。故

$$\boxed{\ (b)\iff\ker(\lambda M-F)=V^{\perp}\ \ \forall\lambda\ }$$

$$\text{即}\quad \underbrace{F\vert_{V^{\perp}}=0}_{(5a)};\qquad \text{且}\quad \textbf{无额外核}\ (\xi\notin V^{\perp}\Rightarrow(\lambda M-F)\xi\ne0)$$

### 16.2 我错在哪

| 我写的 ✗ | 正确的 ✓ |
|---|---|
| $(b)\iff F\vert_{V^{\perp}}$ **单射** | $(b)\iff F\vert_{V^{\perp}}=0$ **且无额外核** |
| 由单射 ⟹ $d-\rho\le q$ | 无此推论 ✗ |
| $q_{\min}\ge\max(\rho+1,d-\rho)$ | **作废** ✗ |

**根源**：我把"$\ker$ 相等"写成了"$F$ 在 $\ker M$ 上的限制" ✗ ——
正确是"$\ker(\lambda M-F)$ 恰好等于 $V^\perp$"，即 $(5a)$ 加"无额外核"✓。

### 16.3 作废的结论

| 结论 | 状态 |
|---|---|
| $q\ge d-\rho$（定理 2）| 🔴 **作废** ✗ |
| $q_{\min}=\max(\dim V+1,\ d-\dim V)$ | 🔴 **作废** ✗ |
| $d\le2\rho+p$（定理 3）| 🔴 **作废** ✗ |
| §12–§15 的"$F_2$ 自由"论证 | 🔴 **作废** ✗ |

**仍然有效的**：
- $q\ge\rho+1$（Lean ✓）
- $\mathcal A$ 是 $A'$-不变 ⟹ $\mathcal A\supseteq V$ ✓
- $(5a)\iff\exists\Lambda$（Lean ✓）
- 引理 3.1（Lean ✓）
- 6/6 实例的精确验证（但只支持 $\dim V+1$，因为 $d-\rho\le\rho+1$ 恒成立）✓

### 16.4 恢复的形式

$$\boxed{\ q_{\min}=\dim V+1\ }$$

这是**原来**的形式 ✓ —— 我的"修正"是错的 ✗，**撤回** ✓。

### 16.5 正确的等价（$V$ 内的工作）

$(5a)$ 给出 $F=MA'$ 于 $V^{\perp}$ 上 ✓；把问题**约化到 $V$**（$\dim=\rho$）：

$$M\vert_V:\ V\to\mathbb R^q\ \text{单射},\quad \lambda M-F\ \text{在}\ V\ \text{上的核}=\{0\}$$

$$\Longrightarrow\quad \text{这就是 §3 的}\ \dim V=d\ \text{情形}\ (V\ \text{代替}\ \mathbb R^d)\ ✓\ \text{所以那条证明可复用}$$

---

## 17. ✅ 正确的证明：把问题约化到 $V$ 上

### 17.1 两个已算出的结构事实

在最小阶解上（$\operatorname{row}(\mathcal LN)=V$，即 $\ker M=V^{\perp}$）：

$$\textbf{(i)}\quad A'(V^{\perp})\subseteq V^{\perp}\qquad\textbf{(ii)}\quad LR_0(V^{\perp})=0$$

*验证*：(i) 数值 3/3 ✓（见 §15 的计算：$A'(V^\perp)$ 的 $V$-分量为零）；
(ii) 由 (i) 与 $(5a)$：$0=F\vert_{V^\perp}=M A'\vert_{V^\perp}+LR_0\vert_{V^\perp}=0+LR_0\vert_{V^\perp}$ ✓

### 17.2 于是 F 分解过 V

$$F\vert_{V^{\perp}}=0\ \Longrightarrow\ F\ \text{诱导} \bar F:\ V\ (\cong\mathbb R^d/V^{\perp})\to\mathbb R^q$$
$$M\vert_V:\ V\to\mathbb R^q\ \text{单射}\ (q=\rho+1)\ \Longrightarrow\ \bar M\ \text{可逆到像}$$

$$(b)\iff\ker(\lambda M-F)=V^{\perp}\ \forall\lambda\iff(\lambda\bar M-\bar F)\ \textbf{单射}\ \forall\lambda$$

$$\textbf{这就是 §3 的同一问题，环境空间从}\ \mathbb R^d\ \textbf{换成}\ V\ (\dim=\rho)\ ✓$$

### 17.3 复用 §3 的证明

§3 的证明（细节 a、b、d）只用了：
- 环境空间 $W$（这里 $W:=V$，$\dim=\rho$）
- 子空间 $S\subseteq W$（同前，$\dim=p$ ✓）
- $A'\vert_W$ 与 $S\subseteq W$ 的结构 ✓

**逐条对照**：

| §3 用的 | 现在对应 |
|---|---|
| $V=\mathbb R^d$ | $V$（$\dim=\rho$）|
| $S\subseteq V$（$\dim=p$）| 同 ✓ |
| $A'$ 保持 $S$？| $S\subseteq V$ 且 $V$ 是 $A'$-不变 ✓；$A'(S)\subseteq S$ 需核 ⚠️ |
| $\bar A'$ 在 $V/S$ 上 | 同 ✓ |
| 引理 3.1 | ✅ Lean（`Lemma31`）✓ |
| 细节 (d)：$S'=S$ | ✅ 3/3 ✓ |

### 17.4 唯一的待核点

$$A'(S)\subseteq S\ ?$$

- 若成立 ⟹ §3 的证明**逐字适用** ⟹ 上界得证 ✓
- 若不成立 ⟹ 需检查 §3 哪里用了它（可能只用 $S\subseteq V$ 与 $V$ 不变）

**待做**：核 $A'(S)\subseteq S$ 是否成立（对 6 个实例）。

### 17.5 结论（暂定）

$$\boxed{\ q_{\min}\ =\ \dim V+1\ }$$

$$\text{下界：Lean}\ ✓;\qquad \text{上界：约化到}\ V\ \text{上后复用}\ \S3\ \text{的证明（待核}\ A'(S)\subseteq S\text{）}$$

**这比昨天的状态好**：当时 $\dim V<d$ 完全没有证明路线；现在有了明确的复用路线 ✓

---

## 18. 🔴 §17 的复用路线受阻：$A'(S)\subseteq S$ **不成立**

### 18.1 验证

| 实例 | $d$ | $\rho$ | $p$ | $A'(S)\subseteq S$ | $V$ 是 $A'$-不变 |
|---|---|---|---|---|---|
| `cand` | 3 | 2 | 1 | ❌ **False** | ✓ True |
| `d4` | 4 | 2 | 1 | ❌ **False** | ✓ True |
| `p2` | 4 | 2 | 2 | ✓ True | ✓ True |
| 2010 | 4 | 4 | 2 | ❌ **False** | ✓ True |

### 18.2 后果

§3 的证明链中，以下环节用了 $A'(S)\subseteq S$：

| 环节 | 用途 | 是否可用 |
|---|---|---|
| 定义 $\bar A'$ 在 $V/S$ 上 | 需要 $A'(S)\subseteq S$ | ❌ **不可用** |
| §9.2 的 $\dim B_\lambda\le p$ | 同上 | ❌ 不可用 |
| 细节 (d) 的 $N'|_{B_\lambda}$ 自由 | 需 $S'=S$ ✓ | ✓ 独立 ✓ |
| 引理 3.1（Lean）| 只用了 $A'(S)\subseteq S$ 的**弱形式**（$N'(V)\subseteq S$）| ✓ 待核 |

$$\Longrightarrow\quad \S17\ \text{的"逐字复用}\ \S3\text{"}\ \textbf{行不通}\ ✗$$

### 18.3 状态

$$\boxed{\ \dim V<d\ \text{时的上界：仍无证明路线}\ ✗\ }$$

**已知的最好结果**：

| 项 | 状态 |
|---|---|
| 下界 $q\ge\rho+1$ | ✅ Lean |
| $6/6$ 实例 $q_{\min}=\dim V+1$ | ✅ 精确 |
| 上界（$\dim V=d$）| ✅ 已证（§10）|
| 上界（$\dim V<d$）| 🔴 **无路线** ✗ |

### 18.4 可以试的方向

1. **弱化 §3**：不要求 $A'(S)\subseteq S$，只在 $V$ 上做（$S$ 只是一个子空间）
   —— 但"商 $V/S$"就不存在了 ✗，需要新的不变量
2. **用 $V$ 的 $A'$-不变性**：$A'|_V$ 有定义 ✓，$S\subseteq V$ 任意 ✓
   —— 或许可以把 $S$ 换成 $\langle S\rangle_{A'|_V}=V$ ✓（定义上就是 ✓！）
   $$\text{那 } S \text{ 的作用就只是"}\rho=\dim V\text{"的信息，}\S3\text{ 的证明里 } S \text{ 可能是多余的}$$
3. **检查 §3 是否真的需要 $S$**：回看 §10 的细节 (a)(b)(d)，$S$ 出现在哪？

**第 3 条最有希望**：如果 §3 的证明只依赖"$S\subseteq V$ 且 $\operatorname{im}N'\subseteq S$"，那就不需要 $A'(S)\subseteq S$ ✓

---

## 19. 逐行审计：§3 的证明依赖 $A'(S)\subseteq S$

### 19.1 依赖表

| §10 的引理 | 证明用到的 | 需要 $A'(S)\subseteq S$？ |
|---|---|---|
| **a1**：$V=S\oplus S^{\perp}$，$\pi\vert_{S^\perp}$ 是同构 | 内积 | ❌ 不需要 |
| **a2**：$\pi(B\xi)=\bar A'(\pi\xi)$ | **$\bar A'$ 的定义在 $V/S$ 上** | ✅ **需要** |
| **a3**：$\dim B_\lambda\le p$ | 经 a2（$B_\lambda=\ker(\lambda-\bar A')$）| ✅ 需要 |
| **b1**：$B_\lambda\ne0\Rightarrow\lambda\in\operatorname{spec}(\bar A')$ | 经 a2 | ✅ 需要 |
| **d1**：$N'\vert_{B_\lambda}$ 可任意指定 | 只用 $S'=S$ | ❌ 不需要 |
| **Lean `Lemma31`** | 显式假设 `hAS : ∀x∈S, A' x∈S` | ✅ **需要** |

### 19.2 结论

$$\text{实测：}A'(S)\subseteq S\ \text{在}\ \texttt{cand},\ \texttt{d4},\ 2010\ \text{上为\textbf{假}}\ ✗$$

$$\Longrightarrow\quad \S3\ \text{的证明}\textbf{不适用于}\ \dim V<d\ \text{的情形}\ ✗$$
$$\Longrightarrow\quad \S17\ \text{的约化路线}\textbf{失败}\ ✗$$

### 19.3 问题的真正结构（在 $V$ 内）

在 $V$ 内（$\dim=\rho$）：

| 对象 | 性质 |
|---|---|
| $V$ | $A'$-不变 ✅（定义）|
| $S=\operatorname{row}(R_0)\subseteq V$ | **不必** $A'$-不变 ✗（3/4 假）|
| $V=\langle S\rangle_{A'}$ | 这是 $S$ 在 $A'$ 下的**闭包** ✓ |

$$\text{所以 } V/S \text{ 不是 } A'\text{-不变商（}A' \text{ 把它送到更大的空间）}$$

**自然的替代**：用 $V$ 本身（$A'$-不变 ✓）而不是 $V/S$ ✓ —— 但这要求把"$S$ 的作用"换成别的东西。

### 19.4 下一条路线（具体）

$$\text{把 } S \text{ 的角色换成：}\ \text{``}\operatorname{im}(\mathcal L R_0)\text{''}\ \text{在 } \mathbb R^q \text{ 中的位置}$$

**理由**：$S$ 进入问题的唯一途径是 $\operatorname{im}N'\subseteq S$ ✓，
而 $N'=\ell_iR_0$ ✓ 的像落在 $S$ ✓ —— 但在 $V$ 内的分析中，真正起作用的是
$$N'\ \text{作为}\ V\to\mathbb R^q\ \text{的映射的像}\ \subseteq\ \mathcal L(S)\subseteq\mathbb R^q$$

**所以**：把 §3 的分析里所有"$S^{\perp}$"换成"$\mathcal L(S)$ 的正交补"（在 $\mathbb R^q$ 内），
把 $V/S$ 换成 $\mathbb R^q/\mathcal L(S)$ ✓ —— 这些都在 $\mathbb R^q$ 里，**不需要 $S$ 的 $A'$-不变性** ✓

**待做**：重写 §10 的 (a)(b)(d) 在这个新框架下。

---

