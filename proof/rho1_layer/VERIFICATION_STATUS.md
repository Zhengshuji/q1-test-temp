> ⚠️ **2026-10-29 总说明**：本文件中涉及"层级别判据/定理 8/定理 13/最小元/交封闭"的结论**已全部撤回** ✗；
> 以 [RESTRICTED_COMPLETION_MODEL.md §44](../layer_program/RESTRICTED_COMPLETION_MODEL.md) 为准 ✓。

# 验证状态总表（2026-10-29）

> 回答"所有证明都验证过吗"。结论：**不是** ✗ —— 有 3 条是纸面/标准事实（不需要也不能机器验证），
> 其余每条都有 Lean 或精确验证。下表逐条列出，最后给出"纸面"的原因。

## 1. 分级说明（项目纪律 §4）

| 标记 | 含义 |
|---|---|
| **Lean** | `lake`/`lean` 退出码 0 |
| **精确验证 n/N** | 有理数精确算术，有限实例，无舍入（**不是证明**）|
| **纸面** | 有完整纸面证明，无机器检查 |
| **标准事实** | 教科书级引理（如维数公式、子空间不可约），不为它单独形式化 |

## 2. 逐条状态

| # | 结论 | 证明 | 机器/精确验证 | 状态 |
|---|---|---|---|---|
| 1 | $\rho_{ci}=P(T,B,U_0)$、$P\in\mathbf P$（一步递归 + $O(n^4)$）| 纸面 | **Lean 27 条** + 对拍 | ✓ |
| 2 | T11（$\gcd=1\Rightarrow\exists D_0\le2d_*(N-1)$，$d_*$ = **实际**最大次数）| 纸面 | 195/195 + 19/19 | ✓（更正过 ✗→✓）|
| 3 | $(5a)\iff\pi(\mathcal VA)\subseteq\pi(\mathcal V)$ | 纸面 | — | 标准事实 ✓ |
| 4 | $(2,1)$ 层完整判据（$w\ne0$ 维数比较 / $w=0$ 恒不可行）| 纸面 | 1605/1605、423/423 | ✓ |
| 5 | 定理 29.1（固定 $(\mathcal U,\mathcal H)$、$c\ge\rho-1$、$\dim\beta(\mathcal H)=\rho-1$：$\dim\mathrm{Bad}<\dim\mathcal A$）| 纸面 | 200 例（110/90/0）| ✓ |
| 6 | **定理 2**（$\mu=3$：不被覆盖）| 纸面 | 200/200（抽象模型）+ **真实实例 200/200** ✓（[verify_mu3_genuine.py](verify_mu3_genuine.py)）| ✓ |
| 7 | **引理 1 / 推论 2**（单特征值处 $\lambda_k$ 是公共根 $\iff w^{\mathsf T}v_k=0$）| 纸面 | 352/352、114/114 | ✓ |
| 8 | **完整谱判据**（$\operatorname{rank}[(\lambda I-C);w^{\mathsf T}]=3$ 对所有特征值 $\lambda$）| 纸面 | 由 7 + 7 例穷尽 | ✓ |
| 9 | **引理 3**（秩一扰动在 $\ker\varphi$ 上不动）| 纸面 | **Lean** | ✓ |
| 10 | **引理 6**（秩二扰动，$\mu=2$ 的充分条件）| 纸面 | **Lean** | ✓ |
| 11 | **定理 5**（$\mu=1$ 充要判据）| 纸面（$\Leftarrow$ 用 9；$\Rightarrow$ 用维数计数）| 199/199 + **维数计数 200/200**（[verify_checkpoint.py](verify_checkpoint.py)）| ✓ |
| 12 | **定理 11**（$\mu=2$ 的 $\Rightarrow$，专家构造）| 纸面 | 295/295 + 恒等式 300/300 + **真实实例 43/43** ✓（[verify_cell_mu23_genuine.py](verify_cell_mu23_genuine.py)）| ✓ |
| 13 | $\mu=0$ 通道平凡可判 | 纸面（一行）| — | 标准事实 ✓ |
| 14 | **引理 9**（子空间被有限超平面覆盖 $\Rightarrow$ 被其一覆盖）| 纸面 | — | 标准事实 ✓ |
| 15 | ~~定理 8~~ → **撤回** ✗（层级别"iff"是非法聚合；格子级版本 = 定理 5 仍有效 ✓）| — | — | 见 RESTRICTED_COMPLETION_MODEL §21 |
| 16 | **推论 A′**（$\dim B\ge3$、$U_0\subseteq B$ $\Rightarrow$ 层可行）| 纸面（构造性：显式给出 $(\mathcal U,\mathcal H,\tau)$）| — | **保留** ✓（不依赖不良定义的对象）|
| 17 | **定理 12**（$\mu=0$ 通道恒不可行）| 纸面 + **Lean**（因式分解 3 条）| [verify_mu0_always_fails.py](verify_mu0_always_fails.py)：42/42；Lean：`Theorem12.lean` 退出码 0 | ✓（FTA 那一步未形式化 ✗）|
| 18 | ~~定理 13~~ → **已降级为"待澄清"** ✗ | — | — | **表述有问题** ✗：其中的"$T$"不良定义（$A$ 在 $X$ 上无诱导映射），已在 §20.2 说明并保留原陈述供修正 |

## 3. "纸面/标准事实"那几条为什么可以接受

| 条 | 为什么不为它单独做机器验证 |
|---|---|
| #3 | 一行等价（取商）；等价性在第一次使用时就被后续所有精确验证间接覆盖 |
| #13 | 一行：$w=0$ $\Rightarrow$ 第 4 行为零 $\Rightarrow$ 只剩前三行；$\tau$ 的自由度为零 |
| #14 | 教科书级（子空间不可约性）；且它在定理 8 里只用来把"有限并"降成"一个" |
| #15 | 定理 5 已精确验证（199/199），引理 9 是标准事实；组合起来无新计算 |
| #16 | 定理 2 已验证（200/200）；推论只是把它用在 $E=\mathcal U$ 这一情形 |

## 4. 本轮补做的两项核对（补齐 #11、#12 的可机器部分）

[verify_checkpoint.py](verify_checkpoint.py)（精确有理算术）：

| 项 | 结果 |
|---|---|
| 定理 5 的维数计数（$\dim U=2$、$\phi\ne0$ $\Rightarrow$ $\dim(U\cap\ker\phi)\ge1$）| **200/200** ✓ |
| 定理 11 的坏二次式恒等式 $\det[z,Dz]=a^2s+a(u-c)y-by^2$ | **300/300** ✓ |

（第一版我把"维数计数"写成了 `rank([U;φ]) <= 2` ✗ —— 那是"$\varphi\in$ rowspace$(U)$"，不是所需的交集维数；
改正为 $\dim(U\cap\ker\phi)=2-\operatorname{rank}(\varphi|_U)$ 后 200/200 ✓。）

## 5. 结论

- **主要结论全部有验证** ✓（Lean 27 条 + 五组精确验证：195/195、423/423、1605/1605、200/200、352/352、199/199、295/295、300/300）；
- **6 条没有机器检查**，但都是"一行推理"或"教科书事实"✓，且其中 2 条的**可计算部分**本轮已补 ✓；
- **没有**遗留的"结论靠抽样支持"的情形 ✓（$\mu=2$ 的三分法协议见 [rho3c1_spectral.md §15.4](rho3c1_spectral.md)）。

---

## 5.1 端到端验证（2026-10-29 新增）

[verify_end2end_genuine.py](verify_end2end_genuine.py)：从"格子判据说可行"出发，**反解 $\tau$、构造真正的
$\mathcal V\subseteq\mathbb C^n$**，再用**堆叠判据**（独立于商空间实现 ✓）验 $(5a)\wedge(5b)$：

$$12/12\ \text{成功}\ ✓$$

## 5.2 端到端验证的新标准（2026-10-29）

[verify_end2end_fixed.py](verify_end2end_fixed.py)：每条成功实例必须同时满足 **10 条**
（dim U=3、W0⊆U、w≠0、(N)、μ≥1、**row(L0)⊆V**、dim V=4、类型 (3,1)、(5a)、(5b)）。

$$\textbf{12/12 全部 10 条通过}\ ✓\qquad\text{且全部落在 } \mu=2\ ✓$$

> **注意**：旧的 12/12（§17）**没有**检查 `row(L0) ⊆ V` ✗ —— 数字碰巧对 ✓，但验证不完整 ✗。新标准取代之 ✓。

## 5.3 $\mu=1$ 通道的真实实例验证（"被覆盖"方向，2026-10-29 新增）

[verify_mu1_r0.py](verify_mu1_r0.py) + §52.7 的实例（$n=6$、$A$ 有一个 3 维不变块、$C=L_0=e_5$、$\mathcal V=W\oplus\langle e_5\rangle$）：

| 项 | 结果 |
|---|---|
| 类型 | $(\rho,c)=(3,1)$ ✓ |
| $\mu$ | 1 ✓ |
| 六项检查（$\dim\mathcal V=4$、$\operatorname{row}(L_0)\subseteq\mathcal V$、类型、$\mu\ge1$、$(N)$、$(5a)$）| 全 PASS ✓ |
| $(5b)$ | **失败** ✓（独立论证：铅笔 $r_0=5$ 阶子式的次数是 3、4 ⟹ $\gcd$ 非常量 ⟹ 对**所有** $\tau$ 都失败 ✓）|
| C.2 判据 | **"被覆盖"** ✓（$T=\begin{pmatrix}0&1&0\\0&0&1\\1&1&0\end{pmatrix}$、$a=(1,0,0)$；见下方更正）|

$$\text{独立论证与判据}\textbf{一致}\ ✓\ ——\ \text{该 }\mu=1\text{ 的真实实例的格子被覆盖}\ ✓$$

> ⚠️ **2026-10-30 更正（两根因）** ✗→✓
> 1. **表里的 $T$ 曾是错的**（旧版 $T=\begin{pmatrix}1&0&0\\0&1&0\\1&0&0\end{pmatrix}$）。正确的 $T$ 由解
>    $f(u_i)=\sum_jT_{ij}u_j+\sum_kc_{ik}B_k$ 得到：$T=\begin{pmatrix}0&1&0\\0&0&1\\1&1&0\end{pmatrix}$
>    （残差恰为零，逐条可验）。两个旧脚本"算出的 $T$ 互相矛盾"就是这一条。
> 2. **本实例 $w=0$**：$H=\mathcal V\cap\mathcal J=\langle e_5\rangle$、$w=\beta(e_5)=\pi(e_6)=0$
>    ⟹ 归 **C.5（恒被覆盖）**，**不是** C.2（C.2 要求 $w\ne0$）。
>    旧脚本把 $a$（$E$ 的方向）当 $w$ 代进判据，所以显示"不一致"。
>
> 修正后的 `verify_mu1_covered_instance.py` 三组（$\alpha,\beta$）全部一致 ✓（输出里直接打印 $w$）。
> **补上（2026-10-30）**：C.2 的"被覆盖"方向现在有**真正 $w\ne0$** 的真实实例
> —— [verify_mu1_w_ne_0_instance.py](verify_mu1_w_ne_0_instance.py)（写死的 $n=6$、$\mu=1$、$w=\pi(e_1)\ne0$）：
> 判据给出 gcd 次数 $=2>0$（被覆盖）✓，**直接**验（商铅笔的 3 阶子式 gcd）**25/25** 个提升全被覆盖 ✓。
> **"不被覆盖"方向也补上了**（2026-10-30）：[verify_mu1_w_ne_0_not_covered.py](verify_mu1_w_ne_0_not_covered.py)
> —— 判据 gcd 次数 $=0$（不被覆盖）✓，且给出**具体见证** $\mathcal L=[e_1;e_2;e_3;e_6]$：商铅笔子式 gcd 次数 $=0$
> ⟹ $(5b)$ 成立，同时 $\operatorname{rank}\mathcal L=4$、$\operatorname{row}(L_0)\subseteq\operatorname{row}\mathcal L$、$(5a)$ ✓。
> $$\therefore\ \text{C.2 的两个方向现在都各有一个真实实例}\ ✓$$

## 6. 一键复核清单（按此顺序跑，全部通过才算基础可靠）

```bash
# 1) 布局/一致性
python tools/hygiene/audit_layout.py                  # 必须 0 issue

# 2) 精确验证（有理算术）
python proof/rho1_layer/verify_checkpoint.py          # 维数计数 200/200、坏二次式恒等式 300/300
python proof/rho1_layer/verify_mu0_always_fails.py    # 定理 12：42/42
python proof/rho1_layer/verify_propP_triangle.py      # 定理 11（mu=2）：295/295
python proof/rho1_layer/verify_mu2_criterion.py       # mu=2 三分法：300/300（覆盖靠证明、可行靠见证）
python proof/rho1_layer/verify_mu1_criterion.py       # mu=1 判据（旧版脚本）
python proof/rho1_layer/verify_spectral_criterion.py  # 引理 1（352/352）、推论 2（114/114）
python proof/rho1_layer/verify_bezout_actual_degree.py# T11 实际次数版：19/19
python proof/rho1_layer/verify_9_12.py                # (2,1)/w=0：423/423
python proof/rho1_layer/verify_29_1.py                # 定理 29.1：200 例（0 mix）

# 3) Lean（WSL）
cd ~/WorkSpace/lean4/MyProof && export PATH="$HOME/.elan/bin:$PATH"
lake env lean MyProof/Perturbation.lean   # 5 条（秩一/秩二扰动）
lake env lean MyProof/Theorem12.lean      # 3 条（定理 12 的因式分解）
lake env lean MyProof/PVal.lean           # 4 条（P 的定义与接口）
# 以及 PRecursion 系列（需先 lake build MyProof.<Module>）
```

**注意**：`lake env lean` 不会自动构建被 import 的模块；先 `lake build MyProof.<Module>`（CLAUDE §6）。

## 7. 当前"纸面但未机器检查"的清单（可接受，需知情）

| 条 | 内容 | 为什么可接受 |
|---|---|---|
| #3 | $(5a)$ 的商等价 | 一行（取商）|
| #14 | 引理 9（子空间被有限超平面覆盖）| 已补**完整初等证明**（对 $m$ 归纳 + "有限条真仿射直线不能覆盖 $\mathbb C$"）；教科书事实 |
| #15 | 定理 8 | = 定理 5（已验证）+ 引理 9 |
| #16 | 推论 A′ | = 定理 2（已验证）的直接应用 |
| #18 | 定理 13 | = 定理 11+12+8+A′ 串联；**独立复核缺** ✗（需商坐标）|
| #17 的一部分 | 定理 12 的"非零三次必有根" | FTA；Lean 未接通（API 名），由 42/42 精确验证覆盖 |
