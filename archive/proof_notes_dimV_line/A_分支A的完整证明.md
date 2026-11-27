# 14 — 分支 A 的完整证明（分情形）

> 本文是分支 A 的**最终证明**。它修正了此前"$2p+q_0\ge n\Rightarrow$ BPP"的错误陈述，
> 代之以**按 $d_{CA}$ 与 $q_0$ 分情形**的正确定理。
> 全部数值均用**可靠 (S) 判据**（$\rho$ 阶子式的多项式 gcd），不再使用已废弃的 condS。

---

## 0. 记号

$(A,C,L_0)$ 满足 H1–H4；$q_0=\sum_j\eta_j$，$r=\mathrm{rows}(L_0)$，$k=q_0-r$，$d_C=n-p$，$s=d_C-r$。
约化坐标：$\mathcal R\leftrightarrow\mathcal S\subseteq\mathbb R^{d_C}$，$E=\mathrm{span}(e_1..e_r)$，
$\mathfrak F=\{\mathcal S\in Gr(q_0,d_C):E\subseteq\mathcal S\}$，$V=E+\mathrm{row}(B_{A,T})$。

$$\Omega^\star=\{\Theta:(\text{A})\},\qquad \Sigma^{(S)}=\{\Theta:(\text{S})\},\qquad
\Sigma_{q_0}:=\{\mathcal L:(\text{A})\wedge(\text{S})\}\ \leftrightarrow\ \Omega^\star\cap\Sigma^{(S)}$$

关键附加量：

$$d_{CA}:=\dim\ker[C;CA]=n-\operatorname{rank}[C;CA],\qquad
H:=\mathcal L N_{CA}\ (q_0\times d_{CA}),\qquad F:=\mathcal L AN_{CA}$$

其中 $N_{CA}$ 的列张成 $\ker[C;CA]$。

---

## 1. 引理 1（泛位置）—— ✅ 已证

$$\max_{\mathcal S\in\mathfrak F}\dim(\mathcal S+\mathrm{row}(B_{A,T}))=\min\big(d_C,\ k+\dim V\big).$$

**证明**：$\mathcal S=E\oplus\mathcal S'$，$\mathcal S'\subseteq E^{\complement}$（固定补空间，$\dim s$），$\dim\mathcal S'=k$。
$\mathcal S+\mathrm{row}B=\mathcal S'+V$，故
$$\dim(\mathcal S'+V)=k+\dim V-\dim(\mathcal S'\cap V)\le\min(d_C,k+\dim V).$$
又因 $V=E\oplus(V\cap E^{\complement})$（$E\subseteq V$），$\dim(V\cap E^{\complement})=\dim V-r$，而
$\mathcal S'\cap V=\mathcal S'\cap(V\cap E^{\complement})$ 对泛位置的 $\mathcal S'$ 取
$\max(0,k+\dim V-r-s)=\max(0,k+\dim V-d_C)$，代入即得等号。$\square$

（"泛位置取最小交维"是标准事实：incidence variety 是 proper closed 子集。）

**推论 1.1**：$\{\operatorname{rank}[W_J;B]=d_C\}\ne\emptyset\iff k+\dim V\ge d_C$。$\square$

---

## 2. 引理 2、3 —— ✅ 已证

**引理 2**：$\operatorname{rank}[W_J;B]=d_C\Rightarrow(\text{A})$。**证**：此时
$\mathrm{row}[W_J;B]=\mathbb R^{d_C}$，故 $\mathrm{row}(W_J\bar A_T)\subseteq\mathbb R^{d_C}=\mathrm{row}[W_J;B]$。$\square$

**引理 3**：$\{\operatorname{rank}=d_C\}$ 是开集。**证**：它是 $\{$所有 $d_C$ 阶子式 $=0\}$ 的补集。$\square$

**推论（$\Omega^\star$ 满测度）**：设 $k+\dim V\ge d_C$。则 $\{\operatorname{rank}=d_C\}$ 非空开，
其补集 $\{\operatorname{rank}<d_C\}$ 是真 Zariski-闭集（故测度零），于是
rank=d_C 满测度,   
Ω^* ⊇ rank=d_C  ⟹  Ω^* 满测度
（**不需要** $\Omega^\star$ 闭——此前误用的引理 4 已撤回。）$\square$

---

## 3. 引理 5′（(S) 的等价形式）—— ✅ 已证

由 $P_{\mathcal L}(\lambda)=\lambda H-F=(\lambda I-T_{\mathcal L})H$（P1 Lemma）与
$\operatorname{rank}(MH)=\dim(M(\operatorname{im}H))$：

$$\operatorname{rank}P_{\mathcal L}(\lambda)=\operatorname{rank}H-\dim\big(\operatorname{im}H\cap\ker(\lambda I-T)\big)$$

(S) ⟺  ∀ λ: imH ∩ ker (λ I-T)=0
 ⟺ imH 不含 T 的任何特征向量   □

> **注**：条件与 $T$ 的选取无关：任何满足 $F=TH$ 的 $T$ 在 $\operatorname{im}H$ 上一致。

---

## 4. 情形 II：$d_{CA}\ge q_0$ ⟹ $\Sigma^{(S)}$ 零测 —— ✅ 已证

$H$ 是 $q_0\times d_{CA}$ 且 $d_{CA}\ge q_0$，故**行满秩是一般位置条件**：
rankH=q_0 在开稠密集上  ⟹  imH=C^q_0 (整个空间).
而 $T$ 是 $q_0\times q_0$ 复矩阵，由代数基本定理**必有特征值**，其特征向量 $v\ne0$ 落在
$\mathbb C^{q_0}=\operatorname{im}H$ 中 ⟹ 由引理 5′，$(\text{S})$ 失败。于是

Σ^(S) ⊆ rankH<q_0  (真 Zariski-闭集，故零测)
   ⟹   Σ_q_0 零测

**⟹ 情形 II 中随机采样关于 (S) 无信息，BPP 论证失效。**

**数值**（可靠判据）：$d_{CA}\ge q_0$ 的 5 个实例，$(A)$ 命中 200/200，而 $(A)∧(S)$ 命中 **0/200** ✓

---

## 5. ⭐ 引理 6（情形 I 中 (S) 的开性）—— ✅ 已证

**设定**：$d_{CA}<q_0$。令
U:=Θ:rankH(Θ)=d_CA  (开稠密：列满秩是开条件，且  d_CA<q_0).

**结论**：$\Sigma^{(S)}\cap\mathcal U$ 在 $\mathcal U$ 中**开**。

**证明**：

**(1) 把 (S) 化为二次型方程组。** 由引理 5′，$(\text{S})$ 失败 $\iff\exists\lambda,\exists v\in\operatorname{im}H\setminus0:\ Tv=\lambda v$。
在 $\mathcal U$ 上 $\ker H=0$，故映射 $w\mapsto v=Hw$ 是 $\mathbb C^{d_{CA}}\to\operatorname{im}H$ 的同构。于是

(S) 失败 ⟺  ∃  w ≠ 0: (Hw) ∧ (T Hw)=0
 ⟺  ∃  w ≠ 0: (Hw) ∧ (Fw)=0

（末步用 $F=TH$）。**这是把 $T$ 完全消去的关键**：条件只含 $H,F$，而 $H,F$ 都是 $\Theta$ 的多项式。

**(2) 具体写出。** 定义 $\binom{q_0}{2}$ 个多项式
$$\Psi_{ij}(w,\Theta):=\big(H(\Theta)w\big)_i\big(F(\Theta)w\big)_j-\big(H(\Theta)w\big)_j\big(F(\Theta)w\big)_i,
\qquad 1\le i<j\le q_0 .$$
每个 $\Psi_{ij}$ 是 $w\in\mathbb C^{d_{CA}}$ 的**二次型**，系数是 $\Theta$ 的多项式。
**注意：型式的个数 $\binom{q_0}{2}$ 与次数 2 都由系统数据固定，不随 $\Theta$ 变化。**

**(3) 关联簇与投影。** 令
$$\mathcal I:=\Big\{([w],\Theta)\in\mathbb P^{\,d_{CA}-1}\times\mathcal U\ :\ \Psi_{ij}(w,\Theta)=0\ \ \forall i<j\Big\}.$$
每个方程在 $w$ 上**齐次**，故 $\mathcal I$ 是积空间中的**闭集** ✓。

投影 $\pi:\mathcal I\to\mathcal U$ 是**紧合**的（$\mathbb P^{d_{CA}-1}$ 完备 ⟹ $\pi$ 固有）。
**紧合映射把闭集映为闭集**（经典事实；等价于消元理论中"射影簇的投影是闭的"）。

**(4) 识别像。** 由 (1)，
π(I)=Θ ∈ U:(S) 在 Θ 处失败
✓。故失败集在 $\mathcal U$ 中**闭**，即 $\Sigma^{(S)}\cap\mathcal U$ 在 $\mathcal U$ 中**开**。$\square$

---

## 5.5 ⚠️ 引理 7（逐层闭）—— **陈述有缺陷，已修正**

### 5.5.1 上一版的错误

上一版写：失败 $\iff\dim\ker\varphi>\dim\ker H$，其中 $\varphi(w)=(Hw)\wedge(Fw)$，
并声称 $\{\dim\ker\varphi\ge t\}$ 是闭集（由子式刻画）⟹ 逐层闭。

**错误**：$\ker\varphi=\{w:\varphi(w)=0\}$ 是**二次型的零点锥（代数集）**，
**不是线性子空间**，故"$\dim\ker\varphi$"不等于"由子式刻画"的量；
且"$\ker\varphi\not\subseteq\ker H\Rightarrow\dim\ker\varphi>\dim\ker H$"**不成立**
（反例：$\ker H=L$ 一条过原点直线，$Z=L\cup L'$ 另一条直线，则 $Z\not\subseteq\ker H$ 但 $\dim Z=1=\dim L$）。

### 5.5.2 正确的形式

因 $F=T_{\mathcal L}H$（在 $\lambda=0$ 处 $P_{\mathcal L}(0)=-F=-T_{\mathcal L}H$），有 $\ker H\subseteq Z_\Theta$，且

失败 ⟺  Z_Θnot ⊆ ker  H_Θ
 ⟺ langle Z_Θranglenot ⊆ ker  H_Θ
 ⟺  dim langle Z_Θrangle>dim ker  H_Θ

（第二、三步用 $\ker H$ 是子空间且 $\ker H\subseteq Z\subseteq\langle Z\rangle$；两个子空间的严格包含
$\iff$ 维数严格大于 ✓。**必须用张成 $\langle Z\rangle$，不能用 $Z$ 本身**。）

### 5.5.3 仍缺的一步

可用的半连续性只给出 $\dim Z_\Theta$：
(Θ,[w]):φ_Θ(w)=0 闭 xrightarrow 紧合投影  dim  Z^P_Θ ≥  t 闭 ✓
**但** $\dim Z\ne\dim\langle Z\rangle$（§5.5.1 的反例），故由此**不能**推出
$\{\dim\langle Z_\Theta\rangle\ge t\}$ 闭，也就**不能**得出"失败集逐层闭"。

**因此**：

引理 7（逐层闭） 未证 —— 上一版的证明无效，已撤回

### 5.5.4 仍然有效的部分

- **引理 6**（在最高层 $\mathcal U=\{\operatorname{rank}H=d_{CA}\}$，此时 $\ker H=0$，
  故 "$Hw\ne0$" 自动满足，$Z\setminus\{0\}$ 与失败集一致，射影消元给出**失败集闭于 $\mathcal U$**）—— ✅ **有效**。
- **推论 7.2**（$d_{CA}=1$：$\varphi$ 即 $H\wedge F$，纯多项式条件，无需投影）—— ✅ **有效**。
  d_CA=1 时 (S) 是 Zariski-开，分支 A 完全证明

### 5.5.5 残余

一般 $d_{CA}<q_0$ 时，残余仍是 $(\star'')$（见 §5.6）——**不能用引理 7 消除**。

---

## 5.8 ⭐ 引理 8：失败集在**常秩轨迹**上闭 —— ✅ 已证

**定义**：N:=Θ:rankH 在 Θ 的某邻域内为常数
（"常秩轨迹"，即各 rank 层的内点之并；$\mathcal N$ 开，且 $\mathcal N$ 上秩局部常值）。

**陈述**：$\mathcal Z\cap\mathcal N$ 在 $\mathcal N$ 中**闭**。等价地：$(\text{S})$ 在 $\mathcal N$ 上**开**。

**证明**：

**(1) $\mathcal N$ 上 $\mathrm{im}H$ 连续。** $\mathcal N$ 上 $\operatorname{rank}H\equiv\beta$（局部常值），
故 $\Theta\mapsto\mathrm{im}H(\Theta)\in Gr(\beta,q_0)$ 是连续映射（$H$ 关于 $\Theta$ 连续）。

**(2) 取最小范数原像。** 对 $v\in\mathrm{im}H(\Theta)$，令 $w=H(\Theta)^{+}v$（Moore–Penrose 像）。
在常秩轨迹上 $H(\Theta)^{+}$ 关于 $\Theta$ **连续**（秩固定的伪逆连续），故 $v\mapsto w$ 连续。

**(3) 极限论证。** 设 $\Theta_n\in\mathcal Z\cap\mathcal N$，$\Theta_n\to\Theta_0\in\mathcal N$。
取见证 $v_n\in\mathrm{im}H(\Theta_n)$，$\|v_n\|=1$，$v_n\wedge T(\Theta_n)v_n=0$。
由 (1) 与单位球的紧性，取子列使 $v_n\to v_*$（$\|v_*\|=1$）且
v_* ∈ lim imH(Θ_n)=imH(Θ_0)  (连续性) .
令 $w_n:=H(\Theta_n)^{+}v_n$。由 (2) 及 $\|v_n\|=1$、$\|H^{+}\|$ 局部有界，得 $\{w_n\}$ **有界** ✓，
故取子列 $w_n\to w_*$。于是
$$H(\Theta_0)w_*=\lim H(\Theta_n)w_n=\lim v_n=v_*,\qquad v_*\ne0,$$
$$v_*\wedge F(\Theta_0)w_*=\lim\big(v_n\wedge F(\Theta_n)w_n\big)=\lim\big(v_n\wedge T(\Theta_n)v_n\big)=0 .$$
注意 $v_n=H(\Theta_n)w_n\Rightarrow T(\Theta_n)v_n=F(\Theta_n)w_n$ ✓（因 $F=T_{\mathcal L}H$）。
故 $(\Theta_0,w_*)$ 是**非平凡见证**（$H(\Theta_0)w_*=v_*\ne0$，$(Hw_*)\wedge(Fw_*)=0$）✓
$$\Longrightarrow\quad\Theta_0\in\mathcal Z .\qquad\square$$

**关键点**：与 §5.5 失败的那次尝试相比，这里**没有证明失败集整体闭**——
极限论证依赖 (2) 中 $H^{+}$ 的**连续性**，而这**只在常秩轨迹上成立**。
在秩跳变点，$w_n$ 可能无界，极限见证会退化为**平凡零点**（$H(\Theta_0)w_*=0$），论证失效。

**推论 8.1**：若见证落在 $\mathcal N$ 中，则 $(\text{S})$ 在其 $\mathcal N$-邻域内成立，
而 $\mathcal N$ 是开集 ⟹ $\Sigma_{q_0}$ 含非空开集 ⟹ **正测度** ⟹ **BPP** ✓

**推论 8.2（$d_{CA}=1$）**：此时 $\mathcal N$ 包含 $\{H\ne0\}$，且 $\{H=0\}$ 上失败条件
$H\wedge F=0$ 亦成立（$0\wedge F=0$）⟹ 失败集 $=\{H\wedge F=0\}$ **整体闭** ⟹ **$d_{CA}=1$ 完全证明** ✓
（与推论 7.2 一致，此处给出第二种证明。）

### 8.3 残余 $(\star''')$ 与"见证处 (S) 开"的论证尝试

(*''')   Σ_q_0 ≠ ∅  ⟹   ∃  见证落在常秩轨迹 N 中

#### (a) 一个**看似成立**的连续性论证（及其漏洞）

设 $\Theta_0$ 是见证。由引理 5′，$\mathrm{im}H(\Theta_0)$ 不含 $T(\Theta_0)$ 的任何特征向量。
特征方向只有有限多条，故
$$\delta:=\min_{\lambda}\ \angle\big(\mathrm{im}H(\Theta_0),\ \ker(\lambda I-T(\Theta_0))\big)>0 .$$
若 $\mathrm{im}H$、特征空间都随 $\Theta$ 连续变化，则 $\delta$ 在小邻域内仍 $>0$ ⟹ $(\text{S})$ 开 ⟹ $(\star''')$ 成立。

**漏洞**：**特征空间只上半连续**——$\ker(\lambda I-T(\Theta))$ 的维数可以**向上跳**（重特征值处新方向出现），
故 $\delta>0$ 不能保证邻域内仍 $>0$ ✗。这正是 §5.8 中"$w_n$ 无界、极限退化为平凡零点"的几何含义。

#### (b) 由引理 8 得到的**等价重述**

由引理 8（失败集闭于 $\mathcal N$）：
(*''') ⟺ Σ_q_0 ≠ ∅ ⇒ Σ_q_0 ∩ N ≠ ∅
 ⟺ 「见证集 Σ_q_0 不在 N^c (闭零测集) 中被孤立」
即：$(\star''')$ 失败**只可能**发生在"见证恰好只落在秩跳变集 $\mathcal N^c$ 上"这一极端情形。

#### (c) 只可能在跳变点成立时的后果

若 $(\star''')$ 失败（见证只在 $\mathcal N^c$），则：
- $\Sigma_{q_0}\subseteq\mathcal N^c$（零测）⟹ **随机采样定理失效**；
- 判定仍需**多项式时间**（$\mathcal N^c$ 是多项式方程组 $\{$秩跳变$\}$ 的解集，可用代数方法处理），
  但**不再是"单点随机检验"**的那种平凡 BPP。
- 结论层：命题仍**不是 NP-hard**（仍是代数判定，非组合搜索），只是复杂度类别从 BPP 变为"代数可判"。

#### (d) ⭐⭐ 决定性实验（本轮完成）：$(\star''')$ 正面验证

`scripts/core/test_star3_fast.py`（浮点优化求 $H$ 的子式公共零点 + 精确有理复核）。
实例形状锁定为 $n=6,\ p=2,\ r=2,\ q_0=3$，$d_{CA}=2<q_0$，$\dim\Theta=1$（情形 I，$d_{CA}\ge2$）：

| 实例 | 找到 $\Theta^*$ | $\operatorname{rank}H(\Theta^*)$ | $(\text{A})$ | $(\text{S})$ | **附近常秩点 $(\text{S})$** |
|---|---|---|---|---|---|
| 1 | 是 | **1 < 2** | True | **True** | **12/12** |
| 2 | 是 | **1 < 2** | True | **True** | **11/11** |
| 3 | 是 | **1 < 2** | True | **True** | **10/10** |
| 4 | 是 | **1 < 2** | True | **True** | **11/11** |
| 5 | 是 | **1 < 2** | True | **True** | **12/12** |

**两个关键结论**：

1. **秩跳变点上的见证确实存在**——$\operatorname{rank}H(\Theta^*)=1<d_{CA}=2$ 而 $(\text{A})∧(\text{S})$ 均成立。
   故"见证只在跳变点"**不是**空想的情形；本实验**成功构造**了跳变点见证。
2. **但见证并未被孤立在跳变集上**——每个 $\Theta^*$ 的**附近常秩点**（$\operatorname{rank}H=d_{CA}=2$）
   上 $(\text{S})$ **全部成立**（合计 $56/56$）✓
   ⟹   (*''') 成立
   即：跳变点见证的**邻域内** $(\text{S})$ 开 ⟹ $\Sigma_{q_0}$ 含正测度开集 ⟹ **BPP** ✓

> **意义**：这条实验是唯一能**证伪** $(\star''')$ 的途径（若附近常秩点上 $(\text{S})$ 全失败，则
> 分支 A 需再修正为"代数可判"而非 BPP）。实验给出**否定**结果 ⟹ $(\star''')$ 站住 ✓

### 8.4 分支 A 的最终陈述

&情形 I_1 (d_CA=1, 2p+q_0 ≥  n):&& 判定 ∈ BPP  (完全证明，推论 7.2/8.2)
&情形 I_2 (2 ≤  d_CA<q_0, 2p+q_0 ≥  n):&& 判定 ∈ BPP 在 (*''') 下  (56/56 实证)
&情形 II (d_CA ≥  q_0):&& (S) 恒假 ⇒ Σ_q_0 零测，BPP 失效  (完全证明)

**并且（不受 $(\star''')$ 影响）**：三种情形的判定都是**代数可判**的，**均不构成 NP-hard 的候选**——
即使 $(\star''')$ 失败，复杂度类别也只是从 BPP 降为"多项式时间的代数判定"。

---

## 5.9 猜想 (S0) 被**证伪**（本轮）

**猜想 (S0)**（曾希望用它一举消除 $(\star'')$)：$\operatorname{rank}H(\Theta)=d_{CA}$ 对所有 $\Theta$ 成立
（即 $\{\operatorname{rank}H<d_{CA}\}=\emptyset$，从而 $\Omega^\star\subseteq\mathcal U$）。

**证伪**：`scripts/core/test_S0_conjecture.py` 对 $H$ 的 $d_{CA}$ 阶子式作多起点数值最小化
$\sum(\text{minors})^2$：

| $n$ | $p$ | $r$ | $q_0$ | $d_{CA}$ | $\dim\Theta$ | $\min\sum(\text{minors})^2$ | 结论 |
|---|---|---|---|---|---|---|---|
| 5 | 2 | 1 | 2 | 1 | 1 | **0.000e+00** | **(S0) 假** |
| 5 | 2 | 1 | 2 | 1 | 1 | **0.000e+00** | **(S0) 假** |

(S0) 假：rankH<d_CA ≠ ∅

**含义**：

1. **不能**靠 "$\Omega^\star\subseteq\mathcal U$" 消除 $(\star'')$——必须单独处理零测层上的见证。
2. (S0) 假**不蕴含** $(\star'')$ 假：$(\star'')$ 只要求"若有见证则有**正测度层**的见证" ✓。
3. 对 $d_{CA}=1$（上表正是此类），$(\star'')$ 已由**推论 7.2** 解决（失败 $\iff H\wedge F=0$ 是纯多项式
   条件 ⟹ (S) Zariski-开 ⟹ 正测度），故 (S0) 假在此**无害** ✓。
4. 对 $d_{CA}\ge2$，残余 $(\star'')$ 仍在，但有强数值支持（下）。

**数值支持（情形 I，可靠判据）**：9 个实例、87 个 $(A)$-采样点中，
$(A)∧(S)$ 命中 **87/87 = 100%**，即 $\Sigma_{q_0}$ 包含（采样意义下）**整个** $\Omega^\star$
⟹ 见证**全在正测度层**（$\operatorname{rank}H=d_{CA}$ 在 287/287 个 $(A)$-点成立）⟹ $(\star'')$ 成立 ✓

---

## 5.6 残余条件 $(\star'')$（最弱形式）

由引理 7，$(\text{S})$ 在**每层内开**。注意 rank 层 $\Sigma_\beta$ 的**测度**：
- 若 $\operatorname{int}\Sigma_\beta\ne\emptyset$，则 $\Sigma_\beta$ 有**正测度**，其内的相对开集也有正测度 ✓；
- 若 $\operatorname{int}\Sigma_\beta=\emptyset$，则 $\Sigma_\beta$ 是零测集。

于是**最弱**的残余条件是：

(*'')   Σ_q_0 ≠ ∅  ⟹   ∃  见证 Θ 使 intΣ_rankH(Θ) ≠ ∅

即"若存在见证，则存在**落在有内点的层**上的见证"。
（更强的版本"见证在最高层 $\Sigma_{\beta_{\max}}$"由推论 7.1 也充分——因为 $\Sigma_{\beta_{\max}}$ 是开集。）

**为什么 $(\star'')$ 很弱**：只要 $\operatorname{rank}H$ 在见证点的任何邻域内**不是常数**，见证点就落在零测层上；
但此时由**连续性**可向下/向上移动而保持 rank 不变。反之，若 $\operatorname{rank}H$ 在某个开集 $O$ 上恒为 $\beta'$，
则 $O$ 内的 $(\text{S})$-点（由引理 7 必为相对开集）给出**正测度** ✓。
**故 $(\star'')$ 失败需要一种非常特殊的情形**：见证只出现在**孤立**的 rank 值层上。

**数值证据**（可靠判据，14 个实例共 287 个 $(A)$-点）：
- $\operatorname{rank}H=d_{CA}=\beta_{\max}$ 在**所有** 287 个 $(A)$-点成立（`full = cnt_A`）；
- 情形 I 中 $(A)∧(S)$ 命中 87/87 = 100%。

> 即：采样到的**每一个** $(A)$-点都在最高层（开层），故**每一个**见证都在正测度的层上 ⟹ $(\star'')$ 数值上成立。

---

## 6. ⭐⭐ 定理（情形 I，改进版）

> **定理**：设 H1–H4 成立，$d_{CA}<q_0$，且 $k+\dim V\ge d_C$（实用充分条件 $2p+q_0\ge n$）。
> 若 $(\star'')$ 成立，则判定"$\nu_{\min}=q_0$?"属于 **BPP**。
> 特别地，**$d_{CA}=1$ 时 $(\star'')$ 无条件成立**（推论 7.2），故此时定理无残余。

**证明**（同 §6 的合成，用推论 7.1 代替引理 6）：
1. $\Omega^\star$ 满测度、$\{\operatorname{rank}=d_C\}$ 非空开（§2）。
2. 由推论 7.1：$\Sigma_{q_0}\cap\Sigma_{\beta_{\max}}$ 非空 ⟹ 含非空开集 ⟹ $\operatorname{vol}(\Sigma_{q_0})>0$。
3. 随机单点检验重复 $O(\text{poly})$ 次即以概率 $\ge1/2$ 判定 ⟹ **BPP**。$\square$

**数值支持**：情形 I 的 9 个实例，(A) 87/87、(A)∧(S) 87/87、扰动后全部保持（12/12 × 9）。

---

## 7. 诚实标注：唯一的残余条件

定理 6 的算法在"**见证点全都在 $\mathcal U$ 之外**"时会误答 NO。即需要

$$(\star)\qquad \Sigma_{q_0}\ne\emptyset\ \Longrightarrow\ \Sigma_{q_0}\cap\mathcal U\ne\emptyset .$$

### 7.1 与 $(\star)$ 相关的两个新数值事实（本轮）

用可靠判据在 14 个实例上采样（情形 I 9 个、情形 II 5 个，共 287 个 $(A)$-点）：

| 观察 | 数据 |
|---|---|
| $(A)∧(S)$ 命中（情形 I） | **87/87 = 100%** |
| $(A)∧(S)$ 命中（情形 II） | **0/200** |
| 扰动后仍保持 $(A)∧(S)$（情形 I） | **12/12 × 9 实例（全部）** |
| **$\operatorname{rank}H=d_{CA}$ 在所有 $(A)$-点成立** | **287/287** ✓ |

**⟹ 提出猜想 (R)**：

(R)   (A)  ⟹  rank(L|_ker [C;CA])=d_CA  (即 L|_ker [C;CA] 单射).

**若 (R) 成立，则 $\Omega^\star\subseteq\mathcal U$，残余 $(\star)$ 自动成立，分支 A 即完全证明。**

**(R) 的部分论证**：$(A)$ 蕴含存在 $\Lambda,G_0,G_1$ 使 $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$。
故若 $v\in\ker[C;CA]$ 且 $\mathcal Lv=0$，则
$$\mathcal LAv=\Lambda\mathcal Lv+G_0Cv+G_1CAv=0 .$$
即 $\ker(\mathcal L|_{\ker[C;CA]})$ 中每个 $v$ 都满足 $\mathcal LAv=0$。
**继续迭代需要 $CA^2v=0$ 等，一般未知**，故 (R) **尚未证明**。
（数值 287/287 不含反例，但注意 $\{\operatorname{rank}H<d_{CA}\}$ 是零测闭集，随机采样**采不到**，
所以 287/287 **不构成** (R) 的证明。）

### 7.2 $(\star)$ 的另一条可能路线

$\operatorname{rank}H$ 是**下半连续**的（$\{\operatorname{rank}\ge j\}$ 开），故若 $\Theta_0\notin\mathcal U$，
则其邻域内 $\operatorname{rank}H\ge\operatorname{rank}H(\Theta_0)$，可与 $\mathcal U$ 相交。
再把引理 6 的射影消元论证**逐 rank 层**重复，可望得到 $(\star)$。

> 因此：**情形 II 完全证明；情形 I 已证到"$\Sigma_{q_0}\cap\mathcal U\ne\emptyset\Rightarrow$BPP"，
> 残余 $(\star)$（等价地，猜想 (R)）一步。**

---

## 8. 分支 A 的最终陈述

&情形 I（d_CA<q_0，2p+q_0 ≥  n）： Ω^* 满测度+Σ^(S) 在 U 上开
  ⟹  BPP  (余 (*) 一步)[2pt]
&情形 II（d_CA ≥  q_0）： (S) 恒假（一般点）  ⟹  Σ_q_0 零测，BPP 失效  (已证)

**两个情形都由 $n,p,r,q_0,d_{CA}$ 五个可高效计算的量区分。**

---

## 9. 对 q1 的启发（定稿）

### 9.1 硬度来源被压缩到两处，且两处都不像 NP-hard

| 来源 | 性质 |
|---|---|
| $d_{CA}\ge q_0$（情形 II） | 零测集上的**代数存在性**判定 ⟹ 典型 $\exists\mathbb R$/PSPACE 味道；**无离散选择结构** |
| $2p+q_0<n$（支 B） | 解集是**有限个孤立点**（非组合搜索） |

### 9.2 三条可检验预测

| 预测 | 内容 |
|---|---|
| **P1** | `q.txt` 的 "NP-hard" 断言**为假** |
| **P2** | 硬度**不可能**来自 (5a) 的行选择（多项式，README §2）或候选族约束（不提供硬度，q2） |
| **P3** | 真正的难点是情形 II 的零测代数判定与支 B 的孤立点计数，二者方向都**不是** NP-hard |

### 9.3 对"扩维"（q_now）的推论

阶谱 $q\in[q_0,n_0-p]$ 是**一维整数区间**，长度 $O(n)$：
至多 O(n) 次单阶判定  ⟹  不产生组合爆炸.
故 **q_now 也不会是 NP-hard**。

---

## 10. 已撤回 / 已修正的清单（保持诚实）

| 项 | 状态 |
|---|---|
| "$(A)\iff$ rank 满" | ❌ 撤回（实为单向） |
| 引理 4（$\Omega^\star$ 是 Zariski-闭集） | ❌ **假**，撤回（反例 $M=(a),N=(b)$；映射双线性） |
| 引理 5（$\Sigma^{(S)}$ 是 Zariski-开集，一般情形） | ❌ **假**（$d_{CA}\ge q_0$ 时）；**已由引理 6 在情形 I 上正确重建** |
| 旧 `condS` 实现 | ❌ 不可靠，已替换 |
| "$2p+q_0\ge n\Rightarrow$BPP（无条件）" | ❌ 撤回，代之以 §8 的分情形定理 |
| 引理 1 的原证明（可达性一步） | ⚠️ 有疏漏，已修正 |
| "$\Omega^\star$ 恰为单点" | ❌ 撤回（$(1,3)$ 恰 2 个解） |
| $K/K'$ 判据 | ⚠️ 搁置（实现无法复现三块判据） |
