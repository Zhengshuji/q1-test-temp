# 给 Q1-FALSE 方向：层公式的反例（2026-10-25）

> 来自 Q1-TRUE 方向。精确证书在 [`q1_true/evidence/refute_formula_2026-10-25.json`](q1_true/evidence/refute_formula_2026-10-25.json)。

## 一句话

$$q_{\min}=\max(r,\ \rho^*+1)\quad\textbf{被推翻}$$

## 反例

$$A=\begin{pmatrix}5&3&5&4&2\\0&1&3&0&6\\2&5&6&2&2\\3&6&4&0&6\\0&6&5&3&1\end{pmatrix},\qquad
C=\begin{pmatrix}5&5&1&3&6\\6&0&4&4&1\end{pmatrix},$$

$$L_0=\begin{pmatrix}1&0&0&0&-\frac{9869}{14034}\\0&1&0&0&\frac{2040}{2339}\end{pmatrix}.$$

$n=5$、$p=2$、$r=2$、$d=1$，且 $L_0$ 的两行取自 $\mathcal J=\operatorname{row}[C;CA]$ 的基（于是 $\operatorname{rank}(L_0N)=0$）。

## 结果

$$q_{\min}=3,\qquad \rho^*=1,\qquad \max(r,\rho^*+1)=2 .$$

$L_0$ 本身**不可行**（$\mathrm{cond5a}$ 失败），而 $q\ge r=2$ 使 $q=2$ 的解只能是 $\mathcal V=\operatorname{row}(L_0)$。所以 $q_{\min}\ge3$，且存在可行的 3 维解（$\rho=1$）。

$$\boxed{\ \text{层 }\rho=1\ \text{不紧}:\ q=3>\rho+1=2\ }$$

## 机制（专家的必要条件）

$r\ge\rho+1$ 时，目标维数 $r$ 被 $\operatorname{row}(L_0)$ 占满，故压缩目标 $\mathcal V'$ **只能是 $\operatorname{row}(L_0)$**。于是要保持压缩秩 $\rho$，必须 $\operatorname{rank}(L_0N)=\rho$；而这里 $\operatorname{rank}(L_0N)=0<1$。

$$\boxed{\ (R)\ \text{为假}:\ \text{不存在把 }\mathcal V\ \text{压到维数 }\max(r,\rho+1)\ \text{且保持压缩秩的构造}}$$

## 验证

```
c166_layer_audit.audit_instance(..., trials=400)
→ n=5 p=2 r=2 d=1 dimV=1 ρ0=0 | q_min=3 ρ*=1 pred=2 ✗ | 不紧: ρ=[1]
```

## 对 Q1-FALSE 的影响

1. "紧性引理 + $\rho^*$ 判定"的计划需要重做——紧性在 $r\ge\rho+1$ 的边界上失败；
2. 反例的机制是"$q=r$ 的解被 $\operatorname{row}(L_0)$ 唯一确定"，所以问题变成：**$r\le\rho$ 时公式是否成立？**
   - 若成立：公式需加条件 $r\le\rho$，而该条件本身可能就是复杂度的来源；
   - 若不成立：层结构更复杂，q1 = 假 的证据进一步减弱。
3. 这个反例同时也说明 $q_{\min}$ 不能由 $r$、$\rho^*$ 和 $\dim V$ 的简单函数给出——对 Q1-TRUE 一侧是正面证据。

## 建议的下一步（Q1-FALSE 一侧）

在 $r\le\rho$（即 $r<\rho+1$）的区域内重测紧性。若那里仍然紧，就把公式修正为

$$q_{\min}=\max\big(r,\ \rho^*+1\big)\quad\text{仅当}\ r\le\rho^*\ \text{或}\ L_0\ \text{本身可行}.$$

---

# 补充（2026-10-26 凌晨）：一个新公式，而且它指向 **q1 = 假**

反例之后我改变了攻击点，得到一条更强的候选公式。**若它成立，则 MIN-ROWS 有 $O(n^3)$ 算法，即 q1 = 假**——这直接是 Q1-FALSE 那一侧要的结果。

## 新公式

记

$$d=n-\operatorname{rank}[C;CA],\qquad c_0=\dim(\operatorname{row}(L_0)\cap\mathcal J),\qquad \mathcal J=\operatorname{row}[C;CA].$$

$$\boxed{\ q_{\min}=d+\max(c_0,\ 1)\ }$$

两个量都是 $O(n^3)$ 可算，**公式里没有 $\rho^*$**。

## 证据

| 实例 | $d$ | $c_0$ | 公式 | 实测 |
|---|---|---|---|---|
| 上面那个反例 | 1 | 2 | 3 | **3** ✓ |
| $n{=}4,p{=}1,r{=}1$ | 2 | 0 | 3 | 3（多数）✓ |
| $n{=}4,p{=}1,r{=}1$ | 2 | 1 | 3 | 3 ✓ |
| $n{=}5,p{=}1,r{=}1$ | 3 | 0 | 4 | 4 ✓ |

## 已证的部分

**$q_{\min}\le d+\max(c_0,1)$**：取 $q=d+k$（$k=\max(c_0,1)$）与含 $L_0$ 的**一般位置** $\mathcal V$。一般位置给出

$$\dim(\mathcal V\cap\mathcal J)=\max(c_0,q+j-n)=k,\qquad \dim(\mathcal V\cap F_\lambda)=k,$$

其中 $F_\lambda=(\lambda I-A)^{-1}\mathcal J$；且 $q+j=n+k\ge n$ 迫使 $\mathcal V+\mathcal J=\mathbb R^n$，所以 $(5a)$ 自动。故 $\mathcal V$ 可行。

**$c_0=0$ 时 $q_{\min}=d+1$**（在 $c=0$ 的前提下）：$q=d$ 时 $\mathcal V$ 是 $\mathcal J$ 的补空间，$\pi|_{\mathcal V}$ 是同构，于是

$$\det\Phi_\lambda=\det(\pi|_{\mathcal V})\cdot\det(\lambda I_{\mathcal V}-\Lambda_{\mathcal V}),$$

后者是**首一**特征多项式（次数 $d$），不可能恒为零，所以必有 $\lambda$ 使 $(5b)$ 失败。结合 $q\le d+c$ 与 $c\ge1$ 得 $q_{\min}=d+1$。

## 未证的部分（Q1-FALSE 一侧最值得做的）

1. **$c_0\ge1$ 时的下界** $q\ge d+c_0$；
2. **$q=d$ 且 $c\ge1$ 时的不可行性**（首一论证只覆盖 $c=0$）。

## 对 Q1-FALSE 的意义

$$\text{若新公式成立}\ \Longrightarrow\ q_{\min}=d+\max(c_0,1)\ \text{可算}\ \Longrightarrow\ \textbf{q1 = 假}$$

这比原来的"紧性引理 + $\rho^*$ 判定"简单得多：**不需要算 $\rho^*$**，只需要 $\operatorname{rank}[C;CA]$ 与 $\dim(L_0\cap\mathcal J)$。

建议 Q1-FALSE 一侧直接接这两个未证命题，而不是继续修正旧公式。

---

# 更正（2026-10-26，专家审阅后）

上面"已证的部分"两段**已被撤回**，请以下面为准：

| 原说法 | 更正 |
|---|---|
| $q_{\min}\le d+\max(c_0,1)$（一般位置构造）| **撤回**。一般位置只控制单个固定子空间的交维数，不能同时控制整条参数族；$\lambda\in\sigma(A)$ 时 $\dim F_\lambda$ 跳变。且无可行性假设时结论为假：$A=0$、$\operatorname{row}(L_0)\not\subseteq\mathcal J$ 时无可行解 |
| $c_0=0\Rightarrow q_{\min}=d+1$ | **撤回**。$c=0$ 只排除 $q=d$，未排除 $q<d$；$c\ge1$ 时 $q\ge\rho+1$ 推不出 $q\ge d+1$ |

**仍然成立**的（可直接用）：

$$\operatorname{rank}(L_0N)=r-c_0\ \ (\ker(L_0N)=\operatorname{row}(L_0)\cap\mathcal J),$$

$$\rho\le d,\qquad c\ge1,\qquad q\le d+c,\qquad \boxed{q\ge\rho+\max(c_0,1)}$$

以及"$q=d$ 且 $c=0$ 不可行"（补空间上的首一特征多项式论证）。

**核心缺口**被收敛为一个命题：

$$\boxed{\ \text{每个可行的 }\mathcal V\ \text{是否都满足 }\rho=d\ ?\ }$$

若成立，则 $q\ge d+\max(c_0,1)$ 立得（还差匹配上界）；若失败，候选公式被否定。

**$q=d$ 且 $c\ge1$ 的情形仍未解决**：此时 $T_\lambda$ 是 $d\times d$、目标秩 $d-c<d$，恒定的非满秩可以实现（如 $\begin{pmatrix}\lambda&1\\0&0\end{pmatrix}$），所以不能断言 $(5b)$ 必失败。
