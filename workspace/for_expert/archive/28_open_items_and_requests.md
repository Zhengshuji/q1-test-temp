# 六条未完成命题的缺口清单，以及四问

本份回答你上一轮的三条裁决（已全部落实），并列出**尚未完成**的条目与确切缺口，
最后请你判断四件事：两处 Lean 路线、一处纸面缺口、以及等级判定的口径。

---

# Part I. 记号（沿用前几份报告）

$A\in\mathbb C^{n\times n}$、$C\in\mathbb C^{p\times n}$、$\mathcal L$ 为 $q\times n$ 的增广行块，
$\mathcal J=\operatorname{row}[C;CA]$、$\mathcal V=\operatorname{row}[\mathcal L;C]$、
$\mathcal Z=\ker[C;\mathcal L]$、$K=\ker[C;CA]$、$S=\mathcal V\cap\mathcal Z$、
$\rho=\dim(\mathcal V/\mathcal J)$、$c=\dim S$、$h=\operatorname{rank}[\mathcal L;CA;C]$。
$(5a)/(5b)$ 与 $q_{\min}$ 的定义不变。

**验收规则（本轮新增）**：只有下面两档算"完成证明"——
**L4**：Lean 覆盖命题的**字面陈述**；**L3**：纸面经复核或来自可信文献，且非平凡部分有 Lean 内核。
其余（**L2** 可接受纸面但无 Lean、**L1** 仅自检）不算完成；**实验证据**（精确算术、随机实例）**不计入证明**。

---

# Part II. 当前状态：23 / 29 完成，6 条未完成

## II.1 已完成的 23 条

**L4（Lean 字面，8 条）**：A.1（$(5a)$ 的商形式）、B.1（商铅笔等价）、B.3（$\rho=0$ 层）、
B.9（边界与等号结构，含矩阵级）、B.12（可观性归约三段等价）、B.25（矩形铅笔的二元 gcd 判据）、
C.1（$S=\mathcal J$ 闭包族）、H.1（商等价 Theorem Q）。

**L3（可接受纸面 + Lean 内核，15 条）**：B.2、B.6、B.11、B.15、B.17（统一商铅笔定理，含原 B.16/B.21）、
B.18、B.22、B.23、B.28、B.31、B.32、D.1（下界 + $\sigma$ 三分段）、F.1、G.1、K.1。

## II.2 六条未完成

| # | 条目 | 等级 | 确切缺口 |
|---|---|---|---|
| 1 | **B.4** | L2 | (P) 版 Lean 内核缺。已尝试并定位三处障碍：$J\le E^*$ 的零化子要用 `dualCoannihilator`（`dualAnnihilator` 落在 $E^{**}$）；需要 $(\operatorname{range}M^*)^{\perp}=\ker M$（Mathlib 只给反方向）；维数计算要避开 $E$ 与 $E^{**}$ 混用 |
| 2 | **B.10** | L2 | 定域性（$\lambda\notin\operatorname{spec}\Lambda\Rightarrow D(\lambda)$ 可逆）无 Lean |
| 3 | **B.14** | L2 | 投影铅笔构造无 Lean |
| 4 | **B.24** | L2 | 偏算子 $\Phi$ 的良定义与"特征向量等价"无 Lean |
| 5 | **B.8** | L2 | Smith/Kronecker 结构（极大子式 $\gcd$ = 不变因子之积）——Mathlib 无多项式矩阵 Smith 形与极大子式 $\gcd$；已有的 `Submodule.smithNormalForm` 只覆盖列满秩/包含情形 |
| 6 | **B.13** | L3 但未完成 | **覆盖定理**：从 $\dim\mathfrak I\le\max\{v,\dim\mathcal B+k-1\}$ 到"整族不可行"的那一步（B.13a 本身已完整证明）|

## II.3 上一轮两处请确认（尚未收到回复）

* **D.1**：$\gamma$-方程 $\widehat\pi\Phi(\gamma c)=c$、$\beta$-方程 $U'.\mathrm{mkQ}(\beta u)=U'.\mathrm{mkQ}(\widehat\pi\Phi(su))$、
  $\sigma=-\gamma\circ\beta$，以及 $U=\operatorname{span}(T\cup\{su+\sigma(u)\})$、$\dim U\le\dim T+\dim U'$。
* **B.13a**：$\mathfrak I$ 闭、$\mathcal B$ 外纤维 $\le0$、$\mathcal B$ 上纤维 $=\mathbb P(K)$、
  $\dim\mathfrak I\le\max\{v,\dim\mathcal B+k-1\}$、以及"$\mathcal B=\varnothing\Rightarrow\dim\mathfrak I\le v$"。

---

# Part III. 请求

## III.1 Lean 侧：对偶搬运的标准做法

B.4 的 (P) 形式是
$$J\sqcup\operatorname{range}M^*=\top\iff\ker M\cap J^{\perp}=0,\qquad M=\lambda I-A,\ J\le E^* .$$
证明只需 $(J+\operatorname{range}M^*)^{\perp}=J^{\perp}\cap\ker M$ 与有限维对偶维数。
我们的困难是 $J\le E^*$、$J^{\perp}\le E$、而 $\operatorname{range}M^*\le E^*$ 三者不同空间。

**问**：这类"双对偶搬运"在形式化里是否有标准路径（例如先固定一组基把 $E^{**}\cong E$ 变成等式，
或改在矩阵层面把 $J$ 写成具体的行矩阵）？若你倾向矩阵层面，我们就把 B.4 重写成矩阵陈述。

## III.2 库缺口：极大子式 $\gcd$ 与 Smith 形

B.8 需要：$Q(\lambda)$ 为 $a\times b$ 多项式矩阵、正规秩 $h$ 时
$$\operatorname{rank}Q(\lambda)=h\ \forall\lambda\iff\Delta_h(\lambda)=\gcd\{\text{全部 } h\times h\text{ 极大子式}\}\in\mathbb Q^\times .$$
Mathlib 里没有"多项式矩阵的 Smith 形"与"极大子式的 gcd"。

**问**：是否有已知的形式化路径（例如先把 $\Delta_h$ 通过子式插值构造为多项式，再证明"$\Delta_h$ 常数 $\iff$ 秩处处满"，
只用单变量多项式的根与整除性，不引入 Smith 形）？或者你认为这条应当留在纸面（L2）？

## III.3 纸面缺口：B.13 的覆盖定理

B.13a 给出 $\dim\mathfrak I\le\max\{v,\ \dim\mathcal B+k-1\}$。我们想把它变成：
若 $\dim\mathfrak I<\dim\mathbb P(K)=k-1$，则投影 $\mathfrak I\to\mathbb P(K)$ 不满，于是存在 $[z]$ 使
"对所有 $x\in V$ 与所有 $[\alpha:\beta]$，$z\wedge(\alpha x-\beta Ax)\ne0$"。

**问**：这个推论是否成立？若成立，是否就是你说的"覆盖判据"；若不成立，正确形式是什么？
我们更希望得到**纸面证明**（哪怕是 sketch），因为这一条我们判断是研究性的。

## III.4 口径

在 L4（Lean 字面）/ L3（可接受纸面 + 部分 Lean）/ L2（可接受纸面无 Lean）这三档里，
**B.4、B.10、B.14、B.24** 都只是"缺 Lean"，数学内容已由你复核或已由你更正。
**问**：这四条在你看来是否可以直接按 L3 记账（只要你认为纸面证明可接受），
还是必须等到有 Lean 内核才允许称"完成"？你的口径我们照办。
