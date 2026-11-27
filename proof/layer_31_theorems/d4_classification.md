# $d=4$ 的层可行性：结构化分类（充要）

> **命名注（2026-10-30，采纳 HANDOVER2 Q6）**：标题里的"充要"是**等价**意义 ——
> 定理 6.1 说"层可行 $\iff$ 四条条件同时成立"，两个方向都证了 ✓。
> 它**不是**"可判"意义 ✗：谱步在 $\dim\Phi\ge2$ 时只化成消元问题、未做成判定 ✓（§5、§8）。
> 若读者会混淆，可改称"结构分类（谱步在 $\dim\Phi\ge2$ 开放）" ✓。

> 目标：专家 QA8 第 2 优先级 —— 把 $d=4$（即 $\dim X=4$）的超平面分析做成**充要定理**，
> 按他给的五段组织：结构参数化 / 交维分类 / 提升相容 / 谱判定 / 完备性。
> 标注：[已证] = 纸面证明在本文件；[精确验证 n/N] = 有理算术实例复核；[开放] = 未解决。

**约定**：$X=\mathbb C^n/\mathcal J$、$d=\dim X=4$、$B=\pi(\mathcal J A)$、
$W_0=\pi(\operatorname{row}L_0)+\pi(\operatorname{row}(L_0A))$、$f(x)=\pi(\widehat xA)$、$\mathcal K=\mathcal J+\mathcal J A$。
层是 $(3,1)$：$\mathcal V\subseteq\mathbb C^n$ 满足 $\dim\mathcal V=4$、$\pi(\mathcal V)$ 3 维、$\dim(\mathcal V\cap\mathcal J)=1$。

---

## 1. 结构参数化 [已证]

> **引理 1.1**：$d=4$ 时，每个 3 维子空间 $\mathcal U\subseteq X$ 都是超平面
> $\mathcal U=\ker\phi=\phi^{\perp}$，其中 $[\phi]\in\mathbb P^3$；对应是一一的。

*证明*：$\dim\mathcal U=3=4-1$ ⟹ 余维 1 ⟹ 由线性泛函存在性，$\mathcal U$ 是某个非零 $\phi\in X^*$ 的核 ✓。
$[\phi]$ 与 $\mathcal U$ 一一对应（超平面确定唯一的正规化核泛函 ✓）。$\square$

于是"3 维子空间"这个**无穷**族被压成 $\mathbb P^3$ 上的 4 个齐次参数 ✓ —— 这是 $d=4$ 唯一的特殊性 ✓。

**固定行约束（A2、A3）**：$W_0\subseteq\mathcal U$ ⟺ $\phi(u_0)=0$ 且 $\phi(u_0A)=0$ ✓，其中
$u_0=\pi(\ell_0)$、$u_0A=\pi(\ell_0A)$ ✓。这是 $\phi$ 的**两个齐次线性方程** ✓ ⟹ 解集是
$$\Phi\;=\;\{[\phi]\in\mathbb P^3:\ \phi(u_0)=\phi(u_0A)=0\}$$
一个**射影子空间** ✓（可能是 $\mathbb P^3$、$\mathbb P^2$、$\mathbb P^1$ 或空）✓。

---

## 2. 交维分类 [已证]

> **引理 2.1**：设 $\mathcal U=\ker\phi$、$d=4$。则
> $$\dim(B+\mathcal U)=\begin{cases}3,& B\subseteq\mathcal U\ (\iff\phi\perp B),\\ 4,& B\not\subseteq\mathcal U.\end{cases}$$
> 于是
> $$\mu=\dim(B\cap\mathcal U)=\dim B+3-\dim(B+\mathcal U)=\begin{cases}\dim B,& \phi\perp B,\\ \dim B-1,& \phi\not\perp B.\end{cases}$$

*证明*：$\dim\mathcal U=3$ 且 $B\subseteq\mathcal U$ ⟹ $B+\mathcal U=\mathcal U$ ✓（3 维 ✓）；
$B\not\subseteq\mathcal U$ ⟹ $B+\mathcal U\supsetneq\mathcal U$ ⟹ 4 维 ✓。维数公式给 $\mu$ ✓。$\square$

**推论 2.2**：$d=4$ 时
$$\mu\ge1\iff\begin{cases}\dim B\ge1,\ \phi\not\perp B &(\text{此时 }\mu=\dim B-1),\\ \dim B\ge1,\ \phi\perp B &(\text{此时 }\mu=\dim B).\end{cases}$$

**特例**：$\dim B=1$ 时 $\phi\not\perp B$ 给 $\mu=0$ ⟹ **只有 $\phi\perp B$（即 $B\subseteq\mathcal U$）可行** ✓ ——
这与 §63/§72 的"$d=5$、$\dim B=1$ 要 $B\subseteq\mathcal U$"一致 ✓。

---

## 3. $(N)$ 的分类 [已证]

> **引理 3.1**：$d=4$、$\mathcal U=\ker\phi$。
> - 若 $\phi\not\perp B$：$(N)$ **自动成立** ✓；
> - 若 $\phi\perp B$：$(N)$ ⟺ $f(\mathcal U)\subseteq\mathcal U/B$（即 $\mathcal U$ 关于 $f$ 是**条件不变**的 ✓）。

*证明*：$(N)$ 是 $f(\mathcal U)\subseteq(\mathcal U+B)/B$ ✓。
- $\phi\not\perp B$ ⟹ $B+\mathcal U=X$ ⟹ $(\mathcal U+B)/B=X/B$ ⟹ 右端是全空间 ⟹ 恒成立 ✓。
- $\phi\perp B$ ⟹ $B\subseteq\mathcal U$ ⟹ $(\mathcal U+B)/B=\mathcal U/B$ ⟹ $(N)\iff f(\mathcal U)\subseteq\mathcal U/B$ ✓。$\square$

**注 3.2**：第二种情形是**真正的约束** ✓，而且它**不是** $\mathcal U$ 不变（$f$ 的靶是 $X/B$ ✓）——
"条件不变"这个名字在这里是字面意义：$\mathcal U$ 在 $f$ 下**模 $B$** 不变 ✓。

---

## 4. 提升相容性（A4、A5、A7）[已证]

提升就是选 $\mathcal V$（$\dim4$、$\pi(\mathcal V)=\mathcal U$、$\dim(\mathcal V\cap\mathcal J)=1$、$\operatorname{row}(L_0)\subseteq\mathcal V$）。

> **引理 4.1**：设 $W_0\subseteq\mathcal U$（即 A2∧A3 成立）。则这样的 $\mathcal V$ **存在** ✓；
> 且其 $\mathcal J$-方向的直线**被 $L_0$ 唯一确定** ✓。

*证明*：
**存在性**：取 $\mathcal U$ 的任一截面 $s:\mathcal U\to\mathbb C^n$（$s$ 是线性的、$\pi\circ s=\mathrm{id}$ ✓）。
$\ell_0\in\mathbb C^n$ 满足 $\pi(\ell_0)=u_0\in\mathcal U$ ✓ ⟹ $j_0:=\ell_0-s(u_0)\in\mathcal J$ ✓ ✓。
令 $\mathcal V=s(\mathcal U)\oplus\langle j_0\rangle$ ✓：$\dim=3+1=4$ ✓、$\pi(\mathcal V)=\mathcal U$ ✓、
$\operatorname{row}(L_0)=\langle\ell_0\rangle\subseteq\mathcal V$ ✓（因为 $\ell_0=s(u_0)+j_0$ ✓）、
$\dim(\mathcal V\cap\mathcal J)=1$ ✓（$s(\mathcal U)\cap\mathcal J=0$ ✓ 且 $\langle j_0\rangle\subseteq\mathcal J$ ✓）。
**唯一性**：$\mathcal V$ 里落在 $\mathcal J$ 的部分由 $\ell_0-s(\mathcal U\text{-part})$ 决定 ✓ ⟹ 给定 $L_0$ 与截面，直线固定 ✓。$\square$

**注 4.2**：$c=1$ 是**自动的** ✓ —— 因为 $\dim\mathcal V=\dim\pi(\mathcal V)+c$ 与 $\dim\mathcal V=4$、$\dim\pi(\mathcal V)=3$ 给出 $c=1$ ✓。
所以"类型 $(3,1)$"不是额外约束 ✓。

> **引理 4.3**：$(5a)$ 是**唯一**还需要检查的提升条件，且它等价于
> $$\widetilde{\mathcal U}A\subseteq\widetilde{\mathcal U}+\mathcal K$$
> （$\widetilde{\mathcal U}$ 是 $\mathcal V$ 所对应的 $X$ 的子空间 ✓，$\mathcal K=\mathcal J+\mathcal J A$ ✓）。

*证明*：这是 §36 的经典识别（条件不变性 ⟺ $(5a)$），在本项目已 [精确验证 28/28] ✓。$\square$

---

## 5. 谱判定 [已证 + 可判]

判据（与坐标无关的**秩**形式 ✓，见 RCP §80 顶部与 QA8）：
$$\text{格子被覆盖}\iff\exists\lambda:\ \operatorname{rank}\big[\lambda I-T;\ w^{\mathsf T}\big]<\rho .$$
等价地（简单特征值 ✓）：存在右特征向量 $v$ 使 $Tv=\lambda v$ 且 $w^{\mathsf T}v=0$ ✓。

**可判性**：$\Phi\subseteq\mathbb P^3$ 是射影子空间 ✓ ⟹ 两种情形：
- $\dim\Phi=0$（单点 ✓）：直接算一次 ✓；
- $\dim\Phi=1$（一条射影直线 ✓）：$\phi(t)=p+tq$ ✓ ⟹ 铅笔的子式对 $t$ 是**一次**的 ✓ ⟹ 「所有子式有公共根」是**一次方程组的相容性** ✓ ⟹ **两次取值即可判定** ✓（RCP §65/§67 用过的办法 ✓）；
- $\dim\Phi\ge2$：子式对参数是**高次**多项式 ✗ ⟹ 需要消元/incidence ✓（RCP §73 的 incidence variety ✓），本轮不做 ✓。

> **2026-10-30 补（两个结构性观察 + 一个有限性命题，见 [../layer_program/SPECTRAL_STEP_DESIGN.md](../layer_program/SPECTRAL_STEP_DESIGN.md)）**：
> ① **"被覆盖"是闭条件**（incidence variety 的 proper 像）⟹"不被覆盖"是开条件 ⟹ 找到一个不被覆盖的点就**可证**层可行。
> ② $d=4$、$\dim B=1$ 时 $\{\mu\ge1\}=B^{\perp}\cong\mathbb P^2$。
> ③ **可行 $\varphi$ 至多 2 个**：$(N)\iff\Phi(\varphi)\in\operatorname{span}\{\varphi\}$（转移映射），而 $\varphi$ 还要满足一条**线性**约束 $\ker c\subseteq B^{\perp}\cong\mathbb P^1$，
>    在 $\mathbb P^1$ 上"$\Phi_1(\varphi)\parallel\varphi$"是三个二次型的公共零点 ⟹ 至多 2 个方向（退化时整条线）。
>    ⟹ **$\dim\Phi\ge2$ 的担心可以去掉**：$d=4,\ \dim B=1$ 的谱步是**有限**计算 ✓（实现：[../layer_program/c204_d4_finite_phi.py](../layer_program/c204_d4_finite_phi.py)）。

---

## 6. 定理（$d=4$ 的充要判据）[已证，谱步见 §5 的边界]

> **定理 6.1**：设 $d=4$。层可行 **当且仅当** 存在 $[\phi]\in\Phi$ 使
> 1. **（交维）** $\mu\ge1$，其中 $\mu$ 由引理 2.1 给出；
> 2. **（$(N)$）** 引理 3.1 的相应条件成立；
> 3. **（提升）** 存在 $\mathcal V$ 如引理 4.1，且 $(5a)$（引理 4.3）成立；
> 4. **（谱）** 该格子**不被覆盖**（§5 的判据）。

*证明*：
**(⟸)** 给定满足 1–4 的 $\phi$：由引理 1.1 得 $\mathcal U$；由 1 得 $\rho+\mu\ge1$ 的层号合法；
由 2 得 A6；由引理 4.1 得 $\mathcal V$（A4/A5/A7 的长度与类型 ✓），由 3 得 $(5a)$；
由 4 得 $(5b)$ 在某 $\tau$ 处成立 ✓ ⟹ $(\mathcal L,V)$ 是原问题的合法见证 ✓ ⟹ 层可行 ✓。
**(⟹)** 若层可行，取任一合法见证 $(\mathcal L=[L_0;R],V)$：令 $\mathcal U=\pi(V)$ ✓ ⟹ 3 维 ✓ ⟹ $\phi$ 存在 ✓；
A2/A3 给 $[\phi]\in\Phi$ ✓；$\mu\ge1$ 由层的定义 ✓；A6 给条件 2 ✓（引理 3.1 是等价的 ✓）；
$\mathcal V$ 本身就是条件 3 的见证 ✓；$(5b)$ 给 4 ✓。$\square$

**完备性说明**：两个方向都在**同一组条件**上，没有遗漏的中间情形 ✓ —— 因为引理 2.1、3.1、4.1 都是**穷尽二分** ✓（$B\subseteq\mathcal U$ 与否 ✓）。

---

## 7. 与既有的 $d=4$ 结果的关系

| 已有 | 位置 | 与本文件的关系 |
|---|---|---|
| $d=4$ 的 $\mu$ 公式（$1/1$ 与 $476/476$）| RCP §63.2 | 就是引理 2.1 ✓ |
| $d=4,\dim B=1$ 的 P2 = YES 实例 | RCP §64 | 满足引理 2.1 的第二种情形（$\phi\perp B$）✓ |
| 二分猜想的反例（$d=3$）| RCP §81–§82 | $d=3$ 不在本定理范围内（$\mathcal U$ 唯一 ✓），但它说明**谱步不能省** ✓ |

---

## 8. 诚实的边界

1. ~~**谱步在 $\dim\Phi\ge2$ 时未做成判定**~~ —— **2026-10-30 更正**：$d=4$、$\dim B=1$ 时可行的 $\varphi$ 由**转移映射**定：
   $$\Phi(\varphi)(u)=\varphi(\pi(uA)),\qquad (N)\iff c(\varphi)=0\ \text{且}\ \Phi_1(\varphi)\parallel\varphi,$$
   $\ker c\subseteq B^{\perp}\cong\mathbb P^1$、$\Phi_1|_{\ker c}$ 是 2 维 ⟹ **可行 $\varphi$ 至多 2 个**（退化时整条 $\mathbb P^1$，用两次取值）✓。
   见 [../layer_program/SPECTRAL_STEP_DESIGN.md](../layer_program/SPECTRAL_STEP_DESIGN.md) §3.1；
   实现 [c204](../layer_program/c204_d4_finite_phi.py)、批量 [c205](../layer_program/c205_d4_batch.py)
   （12 个随机实例：11 个层不可行、1 个可行、无中间情形）。
   **仍缺** ✗：候选在**二次域**（判别式非有理平方）时的 `covered` 判定未实现。
2. **本文件的"判定"是结构性的** ✓：它把层问题化成"$\mathbb P^3$ 上一个射影子空间上的有限个多项式条件" ✓，
   而不是一个多项式时间算法 ✗。
3. **未做 Lean 形式化** ✗ —— 本轮无 Lean（按用户 2026-10-29 指示"A 确认无误则暂不使用 Lean" ✓）。
4. 引理 4.3 依赖 §36 的经典识别，那条是 [精确验证 28/28] 而非纸面 ✓ —— 这里引用它，标注清楚 ✓。

---

## 9. 精确验证 [精确验证 40/40 × 3]

脚本：`proof/layer_program/verify_d4_classification.py`（固定种子 987654、$n=6$、$p=1$、随机 $A$ 与随机 $\phi$）。

| 引理 | 结果 |
|---|---|
| 引理 2.1（$\mu$ 二分：$\phi\perp B$ 给 $\dim B$，否则 $\dim B-1$）| **40/40** ✓ |
| 引理 3.1（$(N)$：$\phi\not\perp B$ 恒成立；$\phi\perp B$ 时等价于 $f(\mathcal U)\subseteq\mathcal U/B$）| **40/40** ✓ |
| 引理 4.1（$W_0\subseteq\mathcal U$ ⟹ 提升存在，且 $\dim\mathcal V=4$、$\pi(\mathcal V)$ 3 维、$\dim(\mathcal V\cap\mathcal J)=1$、$\mathrm{row}(L_0)\subseteq\mathcal V$）| **40/40** ✓ |

**覆盖范围（重要 ✗）**：40 个随机 $\phi$ 里 **$\phi\perp B$ 的 0 例** ✗ ——
因为 $\phi\perp B$ 是一个**多项式方程** ✓，随机 $\phi$ 命中的概率为 0 ✗ ✓（本会话第 5 次撞上"余维 $\ge1$ 条件不能随机命中"✓）。
所以：

| 引理 | 被覆盖的分支 | **未**覆盖的分支 |
|---|---|---|
| 2.1 | $\phi\not\perp B$（$\mu=\dim B-1$）✓ 40/40 | $\phi\perp B$（$\mu=\dim B$）✗ |
| 3.1 | $\phi\not\perp B$（$(N)$ 恒成立）✓ 40/40 | $\phi\perp B$（$(N)\iff f(\mathcal U)\subseteq\mathcal U/B$）✗ |
| 4.1 | $W_0\subseteq\mathcal U$ 的情形 ✓ 40/40 | — |

$\phi\perp B$ 分支的**唯一**验证是 §63.2 的 $1/1$ ✓（那次是**构造**的 $\phi$ ✓，不是随机 ✓）——
也与"构造而非采样"的结论一致 ✓ ✓。

**未验证的部分** ✗：定理 6.1 的**谱步**（§5）与 §36 的经典识别（引理 4.3）——
前者需要 $(5b)$ 的完整计算（在 $\dim\Phi\ge2$ 时未做成判定 ✓），后者是 [精确验证 28/28] 而非纸面 ✓。


---

## 10. 补上 $\phi\perp B$ 分支（**构造法**，60/60）[精确验证]

§9 指出随机抽样**命中不了** $\phi\perp B$ ✗（那是多项式方程 ✓）。补法：**构造** ✓ ——
把 $\phi$ 限定在
$$\Phi_{\perp}:=\{b^{\mathsf T}=0\ \forall b\in B\}\cap\{u_0^{\mathsf T}=0\}\cap\{(u_0A)^{\mathsf T}=0\}$$
里取非零元素 ✓（在 60 个实例上这个空间都非零 ✓），再验证两条引理 ✓：

| 引理 | 结果 |
|---|---|
| 2.1 的 $\phi\perp B$ 分支（$\mu=\dim B$）| **60/60** ✓ |
| 3.1 的 $\phi\perp B$ 分支（$(N)\iff f(\mathcal U)\subseteq\mathcal U/B$）| **60/60** ✓ |

脚本：`proof/layer_program/verify_d4_perp_branch.py`（固定种子 13579 ✓）。

$$\therefore\ \text{§9 的覆盖缺口已补}\ ✓\ \text{（两条分支现在都有验证 ✓）}$$

**仍缺** ✗：谱步在 $\dim\Phi\ge2$ 时未做成判定 ✓（§5 ✓）。
