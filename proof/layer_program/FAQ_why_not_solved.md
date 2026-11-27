# FAQ：文献已给出满足 $(5a)$ 的"通式"，为什么 $(5b)$ 的判定仍不知复杂度？

> 这是接手时最容易产生的误解，必须一次说清。

## 1. 文献给的是"解集的刻画"，不是"搜索算法"

无论"通式"以哪种形式出现（行空间的参数化、线性组合、子空间格、$(A,B)$-不变子空间的分类），
它回答的是：

$$\text{"哪些 }\mathcal L\text{ 满足 }(5a)\text{"}$$

也就是**解集**（对固定 $q$，它是 $\mathrm{Gr}(q,\mathbb C^n)$ 里的一个子簇）✓。
而 $q_{\min}$ 要的是：

$$\text{"在解集里，哪一个（若有）成员还满足 }(5b)\text{"}$$

——这是**在子簇上做存在性搜索** ✗，不是"读通式" ✗。

## 2. 关键区分：**验证**是多项式的，**搜索**不是

- **给定** $\mathcal L$ 时，验证 $(5b)$ 是多项式的 ✓ —— 就是"全部 $\rho\times\rho$ 子式的 $\gcd$ 是否非零常数"；
  更进一步，"$\exists\tau$ 使 $\gcd=1$"等价于"某个极大子式在仿射集 $\mathcal A$ 上不恒为零"（**有限**代数判据）✓。
  **但注意（2026-10-29 专家指出、已核实）**：子式个数 $N=\binom{\rho+c}{\rho}\binom{d}{\rho}$ 与 Bézout 矩阵规模在 $\rho$ 随 $n$ 增长时是**指数级** ✗，
  所以这一步是"**有限判定程序**"，只有在 $\rho$ **固定**（如 $\rho=2$）时才是多项式 ✗✓。
- **搜索** $\mathcal L$（或 $(\mathcal U,\mathcal H)$）时，参数族是：

$$\{\mathcal V:\ \pi(\mathcal V)\ \text{是 }T\text{-不变},\ \dim\pi(\mathcal V)=\rho,\ \dim(\mathcal V\cap\mathcal J)=c,\ \mathcal V\supseteq\operatorname{row}L_0\}$$

——一般情形下这是 $\mathrm{Gr}$ 上的**正维数子簇** ✗，不能枚举 ✗。

**例子**：若 $T=\mu I$（标量），则 $T(\mathcal U)=\mu\mathcal U\subseteq\mathcal U$ 对**任意** $\mathcal U$ 成立 ⟹
$(5a)$ 完全不构成约束 ⟹ 参数族就是整个 $\mathrm{Gr}(\rho,d)$ ✗。此时"通式"就是"任意子空间"，
对搜索没有任何帮助 ✗。

## 3. $(5b)$ 是**开**条件，所以难度在"失败集是否覆盖整个族"

$(5b)$ 失效集
$$\mathrm{Bad}=\{\tau:\ \exists\lambda:\ \operatorname{rank}Q_{\mathcal V}(\lambda)\le\rho-1\}$$
是"$\exists\lambda$ 秩降"的集合 = 某个代数簇的**投影** ✗（不是闭的条件那么简单，而是投影型）。

于是层判定 $=\exists(\mathcal U,\mathcal H):\ \mathcal A_{(\mathcal U,\mathcal H)}\not\subseteq\mathrm{Bad}$，
即一个 $\forall\exists$ 型问题：

$$\forall\tau\in\mathcal A\ \exists\lambda:\ \text{秩降}\quad ?$$

- 对 $(2,1)$（$\rho=2$）：**容器唯一** ⟹ $\mathrm{Bad}$ 是**仿射**的 ⟹ 退化成维数比较 ⟹ 可判 ✓（定理 9.10/10.1）；
- 对 $\rho\ge3$ 或 $c\ge2$：容器不唯一（$(\le\rho-1)$ 维、含 $\beta(\mathcal H)$ 的子空间有多个）⟹
  $\mathrm{Bad}$ 是"仿射集的并" ⟹ 投影型 ✗ ⟹ 无判据 ✗。

## 4. 不能靠"数维数"绕过搜索（已证否）

曾以为可以用秩型不变量判定。**已被精确反例否定** ✗：

| 判据 | 否证 |
|---|---|
| 层可行 $\iff\dim K\ge\rho$（$K=\{b\in B:T(b)\in B\}$）| $n=4,\rho=2,c=1$：$\dim K=0$ 却可行 |
| 只依赖 $(\rho,c,\mu,\nu)$ | $(3,1,1,0)$ 下 354 可行 / 160 不可行 |
| 只依赖 $(\rho,\mu,\nu,\kappa)$ | 4 个组合**每一个**都同时出现两种结论 |

⟹ 可行性依赖子空间的**方向几何** ✓，不是任何有限秩签名 ✗ ⟹ 必须真的做几何搜索 ✗。

## 5. 所以"复杂度未知"的准确含义

$$\text{未知的不是"能否判定"（可判定 ✓，Chevalley–Tarski），而是"能否}\textbf{多项式}\text{判定}\ ✗$$

"只需进一步验证 $(5b)$"这句话漏掉了两个量词的**交替**：
外层 $\exists(\mathcal U,\mathcal H)$（Grassmannian 搜索）+ 内层 $\forall\lambda$（常秩），
而中间那个"验证"本身是多项式的 ✓ —— 难点在**搜索** ✗。
