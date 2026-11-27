# Paper I 证明审计（2026-11-17，三个只读子代理的产出）

判据：(a) 重复已生效的记号/条件；(b) 该实例化已有引理却在重推；(c) 中间步骤占用编号；
(d) 长证明缺策略句；(e) 多步证明缺结构标记。

## MATH 级问题（必须先修）

| # | 位置 | 问题 | 修法 |
|---|---|---|---|
| M1 | `lem:W-conditions` 证明 | 引用 `lem:compression`(iii)，但 (iii) **假设 (5a)**；而本引理的第二半是无条件的 | 把 `eq:5b-1`（在假设 (5a) 之前就已推出）提升为节内带编号的显示公式，本引理直接引它 |
| M2 | `lem:zero` (iii)⇒(iv) | `lem:bezout` 只给**实**系数 $g_I$，但 (iv) 断言 $S\in\mathbb{Q}[\lambda]$ | 补一句：有理线性系统的实解蕴含有理解，或直接在 $\mathbb{Q}[\lambda]$ 里做 Bézout |
| M3 | `lem:zero` (v)⇒(i) | 直接"在 $\lambda_0$ 取值"预设了恒等式 $S(\lambda)Q(\lambda)=I_\omega$ | 补半句：恒等式由 (R0) 的系数逐项消失得到 |
| M4 | `lem:zero` (iii)⇒(iv) | "这是附录的伴随构造"是**前向循环**（附录说"该构造不在此重复"） | 删掉该句，构造就在本证明里 |
| M5 | `lem:rationalbasis` vs `eq:B2` | **$D$ 的定义冲突**：引理给的是左零空间 $D$（$(m-r)\times m$，行作用），而 (B.2) 要 $\ker D=\mathcal T$（$(2k-d_0)\times 2k$）。两者不是同一个矩阵 | 统一为一个定义（按需要改引理的陈述），并修 `lem:coeff`(i) 里相应的用法 |
| M6 | `lem:rationalbasis` 证明 | "公分母是至多 $r$ 个枢轴子式之积，只加 $O(r\log r)$ 位"——实为 $O(r^2(\tau+\log n))$ | 改成 Bareiss 只带**一个** $r\times r$ 行列式，位长恰为所宣布的界 |
| M7 | `lem:rationalbasis` 陈述 | $\tau_M=O(\cdot)$ 却在结论里写"≤ τ_M"，含隐藏常数 | 用显式常数定义 $\tau_M$ |
| M8 | `lem:coeff`(i) | "$\operatorname{bits}(H=LN)\le\dots$" 把 $L$ 当输入；但 $r\ge1$ 时自由行是**未知量**，界不成立 | 限定在枢轴分解给出的有理代表（$H=XB$）或只对 $L_0N,L_0AN$ 断言 |
| M9 | `lem:coeff`(ii) | "对系数矩阵用 Hadamard"——不存在这样的 $\omega\times\omega$ 系数矩阵 | 用 Laplace 展开 + 对两个子式用 Hadamard（结论不变） |
| M10 | `lem:coeff`(iii) | 数错了求和项数（把 Cauchy–Binet 的列集数与 $Z^TZ$ 的项数混为一谈）；且界 $f(\ell)\operatorname{poly}$ 与 `tab:bitlen` 的 $\operatorname{poly}$ **自相矛盾** | 引 `item:coef`，用正确的项数，并与表统一 |
| M11 | `cor:time` 证明 | "$\text{for }r=0$ 第二个界是 $\operatorname{poly}(\mathcal L)$"——**假**：$\ell$ 与 $r$ 无关，指数因子仍在 | 改为"$r=0$ 时 Section VII 给另一个 $\operatorname{poly}(\mathcal L)$ 算法，故最小值是多项式" |
| M12 | `thm:existsr` 证明 | 变量计数 4 项，附录是 6 项（漏了 $U,V$）；且 $q=r_0,\dots,Q$ 应为 $\min(Q,n)$ | 引附录的计数 |
| M13 | `lem:struct` 证明 | 开头 "$\operatorname{row}(L_0M)\subseteq W$ 给出 $W_0\subseteq\mathcal T$" 与上界无关且推理不成立；下界缺 $\dim W\ge\dim\pi_1(W)$ | 删该句；补一句 |
| M14 | `lem:monotone` | 未限定 $q$：$q=n$ 时 $\mathrm{DEC}(n+1)$ 无定义 | 改为"for $q<n$" |
| M15 | `lem:sandwich` | 逆命题给出的是 $r_0+t$ 阶而非 $q$ 阶 | 补"(and then at order $q$ by Lemma monotone)" |

## 编辑级问题（(a)(b)(c)）

- `lem:compression`（65 行）：删 l.320 与 l.350 的重复 "N 是 K0 的基"；(iii) 的第二次秩恒等式未说明代换（应为 $M=\lambda L-LA$、$M=L$，而**不是** $M(\lambda)$）；`eq:5a-1`、`eq:5a-2`、`eq:5b-2` → equation*；项 (iv) 全文未被引用（是 (iii) 在 $\lambda=0$ 的推论）→ 并入 (iii)。目标 65→38。
- `lem:attainable`（11 行）：证明几乎全在复述正文定义，唯一实质是 $k\le d_0$。目标 11→5。
- `prop:zero`（46 行）：Step 4 的"$B$ 满行秩"秩转移可在 §IV 找到（重复）；(5b)→铅笔 未注明引自 `eq:5b-1`；结尾两处复述（1277–1281、1293）。目标 46→33。
- `thm:existsr`（18 行）→ 10；`cor:time`（13 行）→ 7。
- `lem:coeff`（61 行）：17 行前奏在重推 `lem:rationalbasis` 的 Cramer 估计且后续**从未使用**（$m,\beta_0$）→ 删；两处显示与相邻句子重复。目标 61→40。
- `lem:zero`（35 行）：前 8 行在重推 `lem:compression`(iii) 的等价形式 → 改为引用。目标 35→26。
- `eq:struct` 全文无 `\eqref`（但它是关键不等式，按用户规则保留编号）。
- `lem3-1`、`lem3-2` 标签名以 `lem3-` 开头但其实是公式，应改 `eq:` 前缀。

## 未决

- `diag-iv`（§IV 证书 + 两个算法定理）的备忘录待收。
- 修复顺序建议：M1–M15 先（影响正确性）、再 (c) 编号、再 (b) 重推消除、最后 (d)(e) 策略句。
