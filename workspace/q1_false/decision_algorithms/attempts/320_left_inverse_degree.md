# 320 左逆证书次数 $\omega-1$ 猜想 与 固定 $q$ 的变量账本

> 本轮只做两件"能当天闭环"的小事，服务于两个战略问题：
> (i) 固定 $q$ 的编码能否压到 $O(q)$ 个变量（若能，$q$ 的 W[1]-hard 就被堵死）；
> (ii) $r=0$ 判定所用的 Bézout 次数界 $\deg S\le2\omega-2$ 是否紧。
> 验证脚本：[c330](../../../../tools/verification/c330_certificate_degree.py)。
> 送审件：[93](../../../for_expert/archive/93_left_inverse_degree_and_directions.md)。

## 目标

1. 把固定 $q$ 编码的**变量账本**算清，并判定"是否存在 $O(q)$ 变量的编码"。
2. 用精确搜索检验：$\lambda X-G$ 的多项式左逆最小次数 $d_{\min}$ 能否达到 Bézout 界 $2\omega-2$。

## 设想与理由

**(1) 账本。** attempts/312 的引理链量化的是 $G=FX$、$X$（各 $q\times\omega$）与谱证书 $x$（$2\omega$ 维），
共 $2q\omega+2\omega$。若有人能把变量数压到 $O(q)$，那么"固定 $q$ 的 XP"就能升级为 FPT，
而 W[1]-hard in $q$ 立刻被排除。所以这个问题不只是记账：它决定参数化下界值不值得做。
另有一个常见直觉——"用 $GL_\omega$ 规范把 $X,G$ 的 $\omega^2$ 维冗余商掉"——需要核对是否真的省得下来。

**(2) 次数界。** 已知界 $2\omega-2$ 是两条放缩的复合：Bézout 乘子 $\deg u_I<\omega$ 与伴随 $\deg\operatorname{adj}=\omega-1$。
两条都各自松，所以真界很可能更小。若真界是 $\omega-1$，则 $r=0$ 的线性系统未知量从 $(2\omega-1)q\omega$ 降到 $\omega^2 q$，
$\exists\mathbb R$ 的左逆证书也同比变短——这是一条**只赚不赔**的改进。

## 做法

**c330 三段。**

- **(A) 账本**：对若干 $(q,\omega)$ 断言 $2q\omega+2\omega$、$\omega=q$ 时 $=2q^2+2q$、枢轴数 $\binom{k}{\omega}\le k^\omega$；
  并对 $r=0$ 断言 $(2\omega-1)q\omega$ 未知量与 $2\omega^3$ 方程（与 c318 的输出一致）。
- **(B) 搜索 $d_{\min}$**：$Q(\lambda)=\lambda X-G$ 满列秩 ⟹ 规范形 $X=[I_\omega;0]$；
  用 (R0.1)–(R0.3) 的整数线性系统判 $d$ 是否可行（与 c318 同一构造）；只检验 $d\le\omega-1$，
  超出者单独算真值。族：$(3,2)$ 穷举 $\{-1,0,1\}^6$、$(3,2),(4,2),(5,2)$ 随机、$(4,3),(5,3)$ 随机。
- **(C) 规范形合法性**：左乘/右乘可逆常数矩阵与 $X=[I;0]$ 规范化都不改变 $d_{\min}$；168 个可行实例对照。

**一个初等下界（可写成小命题）**：$X=[I;0]$ 时 $S_dX=0$ 迫使 $S_d=[0\mid C_d]$，秩 $\le q-\omega$；
$d=0$ 需 $S_0G=-I_\omega$，故 $q-\omega\ge\omega$ 是常数左逆存在的必要条件。
于是 $q=\omega+1$（$\omega\ge2$）时必有 $d_{\min}\ge1$；配上搜索即 $d_{\min}=1=\omega-1$。

## 进展

**账本（A）**

| $(q,\omega)$ | $2q\omega+2\omega$ | 说明 |
|---|---|---|
| $(3,2)$ | 16 | |
| $(6,3)$ | 42 | |
| $(10,10)$ | 220 | $\omega=q$，$=2q^2+2q$，约为 $q^2$ 的 2.2 倍 |

- 冗余：公式对 $(X,G)\mapsto(XS,GS)$（$S\in GL_\omega$）不变（$B\mapsto S^{-1}B$），故有 $\omega^2$ 维自由作用。
  商掉它之后是 $2q\omega-\omega^2$ 个变量——在 $\omega=\Theta(q)$ 时仍是 $\Theta(q^2)$。
  另一条路是**规范固定**（把 $X$ 的某 $\omega$ 行钉成 $I$），代价是 $\binom{q}{\omega}$ 个图表；
  但它**不减少变量数**（固定后仍有 $2q\omega-\omega^2$），只是把自由作用消掉。
- 结论：本编码形状下 $2q\omega-\omega^2=\Theta(q^2)$ 是下不去的；$\binom{q}{\omega}$ 的图表代价对 XP 无害（它是 $q$ 的函数），
  真正的障碍是**量词消去的变量数**。FPT($q$) 若要成立，必须来自**非量词消去**的论证。

**搜索（B）**（可行 = 极大子式 gcd 为 1）

| $(q,\omega)$ | 扫描 | 可行 | $d_{\min}$ 直方图 | 用时 |
|---|---|---|---|---|
| $(3,2)$ 穷举 $\{-1,0,1\}^6$ | 729 | 464 | $\{1:464\}$ | 3.8 s |
| $(3,2)$ 随机 box 2 | 1500 | 1267 | $\{1:1267\}$ | 18.3 s |
| $(4,2)$ 随机 box 2 | 1500 | 1453 | $\{0:1173,\ 1:280\}$ | 12.5 s |
| $(5,2)$ 随机 box 2 | 800 | 797 | $\{0:774,\ 1:23\}$ | 5.0 s |
| $(4,3)$ 随机 box 1 | 600 | 374 | $\{2:374\}$ | 50.7 s |
| $(5,3)$ 随机 box 1 | 300 | 270 | $\{1:236,\ 2:34\}$ | 21.7 s |
| $(5,4)$ 随机 box 1 | 60 | 46 | $\{3:46\}$ | 28.3 s |
| $(6,4)$ 随机 box 1 | 40 | 37 | $\{1:31,\ 2:4,\ 3:2\}$ | 11.9 s |
| $(6,5)$ 随机 box 1 | 20 | 16 | $\{4:16\}$ | 60.3 s |

- **从未出现 $d_{\min}=2\omega-2$**（$\omega=2$：界 2、$d_{\min}\le1$；$\omega=3$：界 4、$d_{\min}\le2$；
  $\omega=4$：界 6、$d_{\min}\le3$；$\omega=5$：界 8、$d_{\min}\le4$）。
- $q=\omega+1$ 的五族 $(3,2),(4,3),(5,4),(6,5)$ **直方图只有一个桶**，恰为 $\omega-1$。
- $q\ge2\omega$（$(4,2)$、$(5,2)$）允许 $d_{\min}=0$，符合"常数左逆需 $q-\omega\ge\omega$"。
- $(6,4)$（$q=\omega+2$）出现 $\{1,2,3\}$ 三个值，最大仍 $=\omega-1$：说明 $\omega-1$ 不是只有 $q=\omega+1$ 才达到。
- (C) 168/168 一致。

## 最终结论

> **注（321）**：下面第 2 条的猜想已解决——由 93 号提示（Hautus + 可观测性指标）得到
> $d_{\min}=\nu-1$（[321](321_expert93_verdict_and_degree_theorem.md) 定理 1），故 $\le\omega-1$ 成立且被锐化。

1. **账本**：固定 $q$ 的编码是 $\Theta(q^2)$ 变量；$GL_\omega$ 商掉后 $2q\omega-\omega^2$ 仍是 $\Theta(q^2)$，
   规范固定的图表代价 $\binom{q}{\omega}$ 对 XP 无害但不减变量。
   因此"把固定 $q$ 升级成 FPT($q$)"不是记账问题，而是需要新算法思想的问题（送审问题之一）。
2. **次数界（M1 实验 + 一条初等下界）**：
   - 猜想：$\deg S\le\omega-1$ 恒成立（Bézout 的 $2\omega-2$ 松了一倍）；
   - 已证小命题：$q=\omega+1,\ \omega\ge2$ 时 $d_{\min}\ge1$；搜索给出该族（$\omega=2,3,4,5$）恒 $=\omega-1$；
   - 若猜想成立：$r=0$ 系统未知量 $(2\omega-1)q\omega\to\omega^2q$。
3. 两条都不改变 $q1$ 的开放状态，但**都直接改写可送审的陈述**（前者决定 $q$-W[1]-hard 是否值得做，后者是引理强度）。

## 文献检索（按纪律 §19，按"问题的形状"检索）

- 检索式：`polynomial matrix full column rank left inverse degree bound`；
  `minimal degree polynomial left inverse linear pencil matrix`；
  `degree of polynomial left inverse of a full column rank polynomial matrix bound`。
- 命中：Fabiano–Struppa, *Bounds for the degrees of the entries of left inverses of polynomial
  matrices*, Multidim. Syst. Signal Process. 1(1):67–74, 1990（Zbl 0715.93017）。
  **论文已引用该文**，但只作背景（"经典界"），未用其显式公式；我们用的是初等的
  伴随–Bézout 界 $2d\omega-d-1$。
- 未命中：$d=1$ 情形的更紧界（线性于 $\omega$），也没有以 $q-\omega$ 表述的界。
- 判断：$\omega-1$ 可能已隐含在经典界的证明里，也可能是一条未被陈述的锐化；
  两种可能都已写进送审件 Q5。

## 放弃原因

- **未证明** $d_{\min}\le\omega-1$：只做了 $\omega\le5$ 的随机搜索（$q\le\omega+2$），$\omega\ge6$ 未测；也没有构造性证明思路。
- 未处理实数/复数差异：gcd 判定按"公根在 $\mathbb C$ 上取"，而系统在 $\mathbb Q$ 上解。
- 未把账本结论升级为"FPT($q$) 不可能"：只证了"本类编码不行"，不是一般不可能性。

## 残留价值

- `c330` 可复跑，含规范形合法性对照（避免"换坐标改变了 $d_{\min}$"这类错误）；
- 一条初等下界（$q=\omega+1\Rightarrow d_{\min}\ge1$）与一条族级恒取上界的观察；
- 澄清"固定 $q$ 是 XP 而非 FPT"是**编码形状所限**，而不是懒；
- 三个可直接送审的问题（次数界、$O(q)$ 变量编码、$q$-W[1]-hard 的价值）。

## 相关文件

- [c330](../../../../tools/verification/c330_certificate_degree.py)（本轮新增，PASS）
- [attempts/312](312_fixed_q_proof_sketch.md)（变量账本的出处）
- [attempts/317](317_85_verdict_r0.md)（$\deg S\le2\omega-2$ 与 $r=0$ 系统）
- [c318](../../../../tools/verification/c318_r0_linear_system.py)（同一线性系统构造）
- 送审件：[93](../../../for_expert/archive/93_left_inverse_degree_and_directions.md)

## 状态

- 账本：**[已证-纸面]**（计数）+ **[精确验证]**（c330 (A)）。
- 次数界：**[已证-纸面]**（[321](321_expert93_verdict_and_degree_theorem.md) 定理 1：$d_{\min}=\nu-1$）
  + **[精确验证]**（c330 (B)(C) 与 c331 255/255 + 构造 8/8）。本文件的猜想部分已被锐化为等式。
  **注意**：该定理新颖性待核（倾向为经典结果的重新发现），影响仅限 $r=0$ 与证书规模，
  见 [321 §重要性评估](321_expert93_verdict_and_degree_theorem.md)。
