# 技术债：商空间 $X=\mathbb C^n/\mathcal J$ 的实现（前置条件）

> 2026-10-29。这份文档说明**为什么**需要一套商空间实现、**需要什么**、**怎么自检**、
> 以及我**失败过的四次**及原因（最重要的部分）。
> 状态：**已实现并通过 5 条自检** ✓（2026-10-29，[quotient_selfcheck.py](../../proof/rho1_layer/quotient_selfcheck.py)）。

---

## 1. 为什么需要它

本项目把 $q_{\min}$ 归约为"逐个 $(\rho,c)$ 判定层是否可行"，而层判定的对象在**商空间**
$X=\mathbb C^n/\mathcal J$ 里（$\mathcal J=\operatorname{row}[C_0;C_0A]$）。已证的四条**格子级**判据
（定理 2、5、11、12）都是在 $X$ 的坐标里叙述的，但**没有任何机器/数值验证**是在真正的商空间上做的 ——
现有验证都停留在"手工设定的 $(\mathcal U,B,\beta,T)$ 数据"上。

要用真实实例 $(A,C_0,L_0)$ 验证任何层级别结论，就必须实现：

$$\pi:\mathbb C^n\twoheadrightarrow X,\qquad B=\pi(\mathcal J A),\qquad
\bar T:X\longrightarrow X/B,\ \bar T(\pi x):=\pi(xA)\bmod B .$$

---

## 2. 需要实现的对象（精确清单）

| 对象 | 定义 | 注意 |
|---|---|---|
| $\mathcal J$ | 行空间 $\operatorname{row}[C_0;C_0A]$ | 用行堆叠 ✓ |
| $\pi$ 的坐标 | 取 $\mathcal J$ 的基 + 补基；$x\mapsto$ 补基坐标 | 补基必须显式构造 ✓ |
| $X$ | $\cong\mathbb C^{d}$，$d=n-\dim\mathcal J$ | |
| $B\subseteq X$ | $\pi(\mathcal J A)$ | **不是** $\pi(\mathcal J)\cap\cdots$ ✗ |
| 子空间 $\mathcal U\subseteq X$ | 3 维（$(3,1)$ 层） | 要能与 $\mathcal V\subseteq\mathbb C^n$ 互相转换 |
| $\bar T:X\to X/B$ | $\bar T(\pi x)=\pi(xA)\bmod B$ | **良定义** ✓；**不**下降到 $X/B$ ✗ |
| $\overline{\mathcal U}$ | $(\mathcal U+B)/B\subseteq X/B$ | |
| $\mathfrak L$ | $\{\mathcal U:\bar T(\mathcal U)\subseteq\overline{\mathcal U}\}$ | 对和封闭 ✓（引理 14）|
| 极小元/极大元 | Krylov 闭包 / supremal | 见 §22–§23 |

---

## 3. 自检协议（**必须先过**，否则后面全是假数据）

**自检 1（$\pi$ 的坐标）**：对随机 $x$，验证 $x-\text{（用坐标重建的 }x\text{）}\in\mathcal J$ ✓。

**自检 2（$\pi$ 与 $A$ 的不交换性）**：随机取 $x$ 与 $j\in\mathcal J$，验证
$$\pi(xA)-\pi((x+j)A)\in B$$
（应当**总成立** ✓；若你的实现给出"$=0$"✗，说明你把 $\pi(xA)$ 当成了良定义 ✗ —— 这正是陷阱）。

**自检 3（$\bar T$ 良定义）**：同上，随机 $x,x'$ 满足 $\pi x=\pi x'$，验证 $\bar T(\pi x)=\bar T(\pi x')$ ✓。

**自检 4（与堆叠判据对齐 —— 最关键）**：对随机 $\mathcal V\subseteq\mathbb C^n$，比较

$$\underbrace{\operatorname{rank}[\mathcal VA;\mathcal V;C_0A;C_0]=\operatorname{rank}[\mathcal V;C_0A;C_0]}_{(5a)\ \text{的直接判据}}$$
与
$$\underbrace{\pi(\mathcal VA)\subseteq\pi(\mathcal V)}_{\text{商空间版本}}$$

两者必须**逐例一致** ✓（一致率 100%，不是 297/298 ✗）。

**自检 5（维数）**：$\dim\mathcal U=\dim\mathcal V-\dim(\mathcal V\cap\mathcal J)$ ✓，逐例核对 ✓。

**验收标准**：自检 1–5 全部 100% ✓，且至少覆盖 200 个随机实例 ✓。

---

## 4. 我失败过的四次（**请先把这些坑避开**）

| # | 做法 | 错在哪 |
|---|---|---|
| 1 | 把 $A$ 在 $X$ 上的映射直接当成矩阵 $T$（"$T(\pi x)=\pi(xA)$"）| **不良定义** ✗：$A(\mathcal J)\not\subseteq\mathcal J$，偏差是 $B$。自检 4 会立刻暴露（当时是 297/298 ✗）|
| 2 | 于是用 $T(\mathcal U)\subseteq\mathcal U$ 当 $(5a)$ | 错误 ✗：正确是 $\pi(\mathcal VA)\subseteq\mathcal U$，且**依赖提升** ✗ |
| 3 | 用 $\ker g(T)$ 枚举 $T$-不变子空间来穷尽型层 | 因为 (1)(2) 全错 ✗；而且即使 $T$ 正确，$(5a)$ 也不只依赖 $\mathcal U$ ✗ |
| 4 | 在 $X$ 里枚举 $3$ 维 $\mathcal U$ 时忘了 $B\subseteq\mathcal U$ 之类的对齐 | 得到"$0$ 个合法 $\mathcal V$"，与已知反例矛盾 ✗ |

**共同模式**（写进 CLAUDE §10.1）：**把"差一个 $B$"的量当成良定义的量** ✗。
凡是出现 $\pi(xA)$，都必须问：**模掉 $B$ 了吗？** ✓

---

## 5. 做对之后能立刻解锁什么

| 解锁项 | 说明 |
|---|---|
| **已完成**：真实实例上的四条格子判据 | $\mu=1$ 17/17、$\mu=2$ 43/43、$\mu=3$ 200/200、$\mu=0$ 42/42 ✓ |
| 定理 13 / 定理 8 的**重述** | 在 $\bar T$ 语言下重写并验证（现在已撤回 ✗）|
| 引理 14 / 推论 15 的**验证** | $\mathfrak L$ 的求和封闭、Krylov 极小元、supremal，都需要实现 ✓ |
| 层级别的**独立复核** | 例如"$\dim B\le2$ 时层可行 $\iff\cdots$"这类陈述 |
| $(\rho,c)$ 扫描 | 把 $q_{\min}$ 的层扫描真正跑起来（现在是手工数据 ✗）|

---

## 6. 参考实现要点（伪代码）

```
def quotient_data(A, C0):
    J   = row_basis(vstack(C0, C0@A))            # (j, n)
    comp= complement_basis(J)                     # (d, n), d = n - j
    Pinv= inverse(vstack(J, comp))                # 坐标
    def pi(x):  return coords(x)[j:]              # X 坐标（d 维）
    def lift(u): return coords_to_x([0]*j + u)    # X 坐标 -> C^n 的代表
    def Tbar(x):                                   # 返回 X/B 里的类（用商坐标表示）
        y = pi(x @ A)                              # 注意：x 必须是 C^n 里的向量
        return coset_mod_B(y)
    return dict(J=J, comp=comp, pi=pi, lift=lift, Tbar=Tbar, B=row_basis([pi(j@A) for j in J]))
```

**关键断言（每个函数入口都写）**：
- `pi(x)` 只在 $x\in\mathbb C^n$ 上有意义 ✓，**不要**对 $X$ 坐标调用 ✗；
- `Tbar` 的返回值是 **$X/B$ 的类** ✓，不是 $X$ 的元素 ✗；
- 任何"$\bar T(u)$ 与 $u$ 比较"的式子，必须先把两者送到**同一个空间**（$X/B$）✓。

---

## 7. 登记

| 项 | 值 |
|---|---|
| 状态 | **已实现** ✓（`proof/rho1_layer/quotient_selfcheck.py`）|
| 自检结果 | S1 60/60、S2 60/60、S3 60/60、**S4 120/120**、S5 60/60 ✓ |
| 相关文档 | §21（撤回 8/13）、§22（$\bar T$ 语言）、§23（引理 14/推论 15）|

### 7.1 自检结果（2026-10-29）

| 自检 | 内容 | 结果 |
|---|---|---|
| S1 | 坐标往返 $x=\mathrm{to\_x}(\mathrm{coords}(x))$ | **60/60** ✓ |
| S2 | $\pi(xA)-\pi((x+j)A)\in B$ | **60/60** ✓ |
| S3 | $\bar T$ 良定义（不同 lift 给同一类）| **60/60** ✓ |
| **S4** | 堆叠判据 $\iff\pi(\mathcal VA)\subseteq\pi(\mathcal V)$ | **120/120** ✓ |
| S5 | $\dim\pi(\mathcal V)=\dim\mathcal V-\dim(\mathcal V\cap\mathcal J)$ | **60/60** ✓ |

$$\boxed{\ \text{商空间实现已可用 ✓（含最关键的 S4 100\%）\ }$$
