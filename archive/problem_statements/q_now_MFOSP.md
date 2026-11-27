下面把论文中“在完整最小条件-$(A)$ 族中，找一个同时满足谱条件 $(S)$ 的 $R$”这一核心步骤，**完全抽离成一个独立的抽象判定问题**，并给出完整、准确的数学描述。不讨论复杂度或 NP-hard，只定义问题本身。

---

## 问题名称：最小阶功能观测器谱可行性判定问题（MFOSP）

### 1. 输入

给定连续时间线性时不变系统与功能矩阵：

$$
\dot x=Ax+Bu,\qquad y=Cx,\qquad z=Lx,
$$

其中

$$
A\in\mathbb R^{n\times n},\quad C\in\mathbb R^{p\times n},\quad L\in\mathbb R^{r\times n},
$$

并满足以下基本假设：

1. $C$ 与 $L$ 均行满秩；
2. $\operatorname{rank}\begin{pmatrix}L\\ C\end{pmatrix}=r+p$；
3. 三元组 $(A,C,L)$ 功能可观测。

此外，输入中已经包含由论文方法预先计算出的以下派生量：

- 功能可观测指数 $\eta_1,\dots,\eta_r$；
- 最小功能维数  
  $$
  q_0=\sum_{j=1}^r\eta_j;
  $$
- 额外功能行数  
  $$
  k=q_0-r=\sum_{j=1}^r(\eta_j-1);
  $$
- 约化维数  
  $$
  s=n-p-r;
  $$
- 核空间基 $N_C\in\mathbb R^{n\times d_C}$，其中  
  $$
  d_C=n-p,\qquad CN_C=0,\qquad \operatorname{rank}N_C=d_C;
  $$
- 左逆 $M_C\in\mathbb R^{d_C\times n}$，满足  
  $$
  M_CN_C=I_{d_C};
  $$
- 坐标变换 $T\in\mathbb R^{d_C\times d_C}$，使得  
  $$
  LN_CT=(I_r\quad 0);
  $$
- 约化矩阵  
  $$
  \bar A=M_CAN_C,\qquad B_A=CAN_C,
  $$
  以及变换后的矩阵  
  $$
  \bar A_T=T^{-1}\bar A T,\qquad B_{A,T}=B_A T;
  $$
- 核空间基 $N_{CA}\in\mathbb R^{n\times d_{CA}}$，其中  
  $$
  d_{CA}=n-\operatorname{rank}\begin{pmatrix}C\\ CA\end{pmatrix},
  $$
  且其列构成  
  $$
  \ker\begin{pmatrix}C\\ CA\end{pmatrix}
  $$
  的基，即  
  $$
  CN_{CA}=0,\qquad CAN_{CA}=0.
  $$

---

### 2. 输出

输出为“存在”或“不存在”，并在存在时给出一个具体选择：

- 一个指标集  
  $$
  J\subseteq\{1,\dots,s\},\qquad |J|=k;
  $$
- 一个参数矩阵  
  $$
  \Theta\in\mathbb R^{k\times(s-k)};
  $$
- 可选地，一个矩阵  
  $$
  K\in\mathbb R^{k\times p}.
  $$

使得由这些参数构造出的增广功能矩阵

$$
\mathcal L=\begin{pmatrix}L\\ R\end{pmatrix}
$$

同时满足条件 $(A)$ 和谱条件 $(S)$。若不存在这样的 $(J,\Theta)$，则输出“不存在”。

---

### 3. 参数化：完整最小条件-$(A)$ 族

固定 $J$ 与 $\Theta$ 后，定义矩阵

$$
Y_J(\Theta)\in\mathbb R^{k\times s}
$$

如下：令 $\Pi_J$ 为置换矩阵，使得

$$
Y_J(\Theta)=(I_k\quad \Theta)\Pi_J^T,
$$

其中 $I_k$ 的列对应指标集 $J$，$\Theta$ 的列对应剩余的 $s-k$ 个指标。于是

$$
\operatorname{rank}Y_J(\Theta)=k
$$

对任意 $\Theta$ 成立。

在变换后的约化坐标中，定义

$$
W_J(\Theta)=
\begin{pmatrix}
I_r & 0\\
0 & Y_J(\Theta)
\end{pmatrix}
\in\mathbb R^{(r+k)\times d_C}.
$$

这里 $W_J(\Theta)$ 是约化坐标下的增广行空间表示，其前 $r$ 行对应 $LN_CT=(I_r\quad 0)$，后 $k$ 行对应额外功能方向。

---

### 4. 条件 $(A)$ 的约化形式

条件 $(A)$ 在约化坐标下等价于：

$$
\operatorname{row}\big((\mathcal L N_C)\bar A\big)
\subseteq
\operatorname{row}\begin{pmatrix}\mathcal L N_C\\ B_A\end{pmatrix}.
$$

对候选 $W_J(\Theta)$，条件 $(A)$ 等价于如下**三块**秩等式（P1 式 (20)）：

$$
\operatorname{rank}
\begin{pmatrix}
W_J(\Theta)\\
B_{A,T}\\
W_J(\Theta)\bar A_T
\end{pmatrix}
=
\operatorname{rank}
\begin{pmatrix}
W_J(\Theta)\\
B_{A,T}
\end{pmatrix}.
\tag{A}
$$

> ⚠️ **更正（2026-xx）**：左端是**三块**，含 $W_J(\Theta)$ **本身**。
> 曾误写为两块 $\begin{pmatrix}W_J(\Theta)\bar A_T\\ B_{A,T}\end{pmatrix}$——
> 该两块版本对**所有** $\Theta$ 都成立，**与 (A) 不等价**（数值验证：17/17 恒成立）。
> 出处：P1 `data/p1.txt` L949–953（式 20）。

定义集合

Ω_A,J^*=
 ≤ ft
Θ ∈ R^k × (s-k)
 middle| 
秩等式 (A) 成立
.

因此，**满足条件 $(A)$ 的所有最小维数增广**，在约化坐标下恰好由

$$
W_J(\Theta),\qquad 
J\subseteq\{1,\dots,s\},\ |J|=k,\ 
\Theta\in\Omega_{A,J}^*
$$

给出。

---

### 5. 从 $(J,\Theta)$ 恢复原始增广矩阵 $R$

对固定的 $(J,\Theta)\in\Omega_{A,J}^*$，由

$$
W_J(\Theta)T^{-1}
=
\begin{pmatrix}
LN_C\\
X_J(\Theta)
\end{pmatrix}
$$

定义 $X_J(\Theta)\in\mathbb R^{k\times d_C}$。然后解方程

$$
RN_C=X_J(\Theta).
$$

其通解为

$$
R=X_J(\Theta)M_C+KC,\qquad K\in\mathbb R^{k\times p}.
$$

因此对应的增广功能矩阵为

$$
\mathcal L=
\begin{pmatrix}
L\\
X_J(\Theta)M_C+KC
\end{pmatrix}.
\tag{$\mathcal L$}
$$

注意：$K$ 只添加测量行空间方向，不影响谱条件，因为

$$
KCN_{CA}=0,\qquad KCAN_{CA}=0.
$$

所以谱可行性只取决于 $(J,\Theta)$，与 $K$ 无关。

---

### 6. 谱条件 $(S)$ 的约化形式

对候选 $\mathcal L$，定义

$$
H=\mathcal L N_{CA},\qquad F=\mathcal L A N_{CA},
$$

以及矩阵束

$$
P_{\mathcal L}(\lambda)=\lambda H-F.
$$

谱条件 $(S)$ 要求

$$
\operatorname{rank}P_{\mathcal L}(\lambda)=\operatorname{rank}H,
\qquad \forall\lambda\in\mathbb C.
\tag{S}
$$

令

$$
h=\operatorname{rank}H.
$$

- 若 $h=0$，则条件 $(S)$ 自动满足。
- 若 $h>0$，令

  $$
  \Delta_1(\lambda),\dots,\Delta_{N_h}(\lambda)
  $$

  为 $P_{\mathcal L}(\lambda)$ 的所有 $h\times h$ 子式。则条件 $(S)$ 等价于

  $$
  \gcd\big(\Delta_1(\lambda),\dots,\Delta_{N_h}(\lambda)\big)=1.
  \tag{S'}
  $$

---

### 7. 抽象问题的形式化陈述

**MFOSP（最小阶功能观测器谱可行性判定问题）**

> **给定**  
> $A,C,L$ 及上述所有派生量  
> $n,p,r,\eta_1,\dots,\eta_r,q_0,k,s,N_C,M_C,T,\bar A_T,B_{A,T},N_{CA}$，  
> **判定**是否存在  
> $$
> J\subseteq\{1,\dots,s\},\quad |J|=k,
> $$
> 以及  
> $$
> \Theta\in\mathbb R^{k\times(s-k)}
> $$
> 使得：
>
> 1. $\Theta\in\Omega_{A,J}^*$，即满足条件 $(A)$ 的秩等式；
> 2. 由 $(J,\Theta)$ 按第 5 节构造出的增广矩阵  
>    $$
>    \mathcal L=
>    \begin{pmatrix}
>    L\\
>    X_J(\Theta)M_C+KC
>    \end{pmatrix}
>    $$
>    （$K$ 任取）满足谱条件 $(S)$，即  
>    $$
>    \operatorname{rank}P_{\mathcal L}(\lambda)=\operatorname{rank}H,
>    \qquad \forall\lambda\in\mathbb C.
>    $$
>
> 若存在，则输出这样的 $(J,\Theta)$（以及可选的 $K$）；否则输出不存在。

---

### 8. 一句话概括

**MFOSP 就是在论文给出的完整最小条件-$(A)$ 增广族中，联合搜索一个离散指标集 $J$ 和一个连续参数矩阵 $\Theta$，使得对应的增广功能矩阵既满足代数条件 $(A)$，又满足全局谱条件 $(S)$。**  
这是整个最小阶功能观测器构造中唯一需要联合处理组合选择与连续参数谱约束的步骤。