# B.28 · 子空间归约与分层参数

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `B.28` 条目（§0.1 归并表）。

## 命题

**B.28（a）〔原 B.26〕（Class I：$\mathcal V=\mathcal Z^\perp$ 决定一切）**
*约定*：$\mathcal Z^\perp$ 指**代数零化子**（$\{y: y^{\mathsf T}z=0\ \forall z\in\mathcal Z\}$），不是 Hermite 正交补；行空间恒等式在该约定下成立（专家 2026-11-05 §1.1）。
 设 $p=r=1$、$\mathcal L$ 可容许、$\mathcal Z=\ker[C;\mathcal L]$、$\mathcal V:=\mathcal Z^\perp$。
则

1. **$\mathcal V=\operatorname{row}[\mathcal L;c]$**（故 $\dim\mathcal V=q+1$，且 $\mathcal V$ **只依赖 $\mathcal Z$**）；
2. **$h=\dim(\mathcal V+\langle cA\rangle)$**（同理只依赖 $\mathcal Z$），故 $h\in\{q+1,q+2\}$，且
   $$h=q+2\iff cA\notin\mathcal V ;$$
3. **$(5a)\iff \mathcal VA\subseteq\mathcal V+\langle cA\rangle$**；
4. 特别地：若 $cA\in\mathcal V$（即 $h=q+1$），则 $(5a)\iff\mathcal V$ 是 $A$-不变子空间。

## 纸面证明

*证明*：1. $\mathcal L$ 的行与 $c$ 都零化 $\mathcal Z$，故都在 $\mathcal Z^\perp$ 里；又
$\operatorname{rank}[C;\mathcal L]=1+q$ 给出 $\dim\operatorname{row}[\mathcal L;c]=q+1=\dim\mathcal V$ ✓。
2. $h=\dim(\operatorname{row}[\mathcal L;c]+\langle cA\rangle)$（$[CA;C]$ 的行空间 $=\operatorname{row}[cA;c]$，$c\in\operatorname{row}[\mathcal L;c]$），
   代入 1 即得；$cA\in\mathcal V$ 与否只改变一维。
3. $(5a)\iff\mathcal VA\subseteq\mathcal V+\langle cA\rangle$：由 1 与可容许性，$\mathcal V=\operatorname{row}\mathcal L\oplus\langle c\rangle$（直和），
   故 $\mathcal VA=\operatorname{row}(\mathcal LA)+\langle cA\rangle$；而 $(5a)$ 恰为 $\operatorname{row}(\mathcal LA)\subseteq\mathcal V+\langle cA\rangle$，两者合并即得 ✓
   （这是专家 2026-11-05 §1.3 给出的更简证明）。
4. 由 3 与 $cA\in\mathcal V$ 即得。$\square$

*意义*：Class I 的全部信息都压到 $\mathcal Z$（或 $\mathcal V$）上——$(5a)$、$h$、$(5b)$（B.13c）都只依赖它。
这既解释了为什么"整族不可行"（同一 $\mathcal Z$ 的所有 $\mathcal L$ 行为一致），也给出 $h$ 只能取两个值的二分。


**B.28（b）〔原 B.28〕（一般 $(p,r)$ 的子空间归约与"不变子空间排除"；专家 2026-11-05 §2 给出）** 设 $\mathcal L$ 可容许
（$\operatorname{rank}[C;\mathcal L]=p+q$）、$\mathcal Z=\ker[C;\mathcal L]$、$\mathcal V:=\mathcal Z^\perp$（代数零化子）。
记 $R=\operatorname{row}C$、$W_0=\operatorname{row}[CA;C]$、$r_1=\dim W_0$。则

1. **子空间归约（对任意 $(p,r)$）**：
$$\mathcal V=\operatorname{row}[\mathcal L;C]=U\oplus R\quad(U=\operatorname{row}\mathcal L),\qquad \dim\mathcal V=q+p ;$$
$$(5a)\iff\mathcal VA\subseteq\mathcal V+W_0\ (=\mathcal V+\operatorname{row}(CA)),$$
即 **$(5a)$ 只依赖于 $\mathcal V$**（从而只依赖 $\mathcal Z$），与 $\mathcal L$ 在补空间里的选取无关。
2. **维数公式**：$h=\dim(\mathcal V+W_0)=q+p+r_1-\dim(\mathcal V\cap W_0)$，故
$$q+p\le h\le q+r_1 .$$
3. **不变子空间排除定理**：若 $\operatorname{row}(CA)\subseteq\mathcal V$，则 $\mathcal VA\subseteq\mathcal V$（由 1），于是由 $R\subseteq\mathcal V$ 归纳得
$\operatorname{row}(CA^k)\subseteq\mathcal V$ 对一切 $k$；若 $(C,A)$ 可观测则 $\operatorname{span}\{\operatorname{row}(CA^k)\}=\mathbb C^{1\times n}$，故 $\mathcal V=\mathbb C^{1\times n}$，
$q+p\ge n$。即
$$\boxed{q+p<n\ \text{且}\ \mathcal L\ \text{可容许}\ \Longrightarrow\ \operatorname{row}(CA)\not\subseteq\mathcal V .}$$

*证明*：1. $\mathcal L$ 的行与 $C$ 的行都零化 $\mathcal Z$，故 $\subseteq\mathcal Z^\perp$；$\operatorname{rank}[C;\mathcal L]=p+q$ 给出维数相等，
且 $U\cap R=0$（否则堆叠秩 $<p+q$）。
$(5a)\iff\operatorname{row}(\mathcal LA)\subseteq\operatorname{row}[\mathcal L;C;CA]=U+W_0$；$(\impliedby)$ 由 $\mathcal LA\subseteq UA$；
$(\implies)$ 由 $\mathcal V=\operatorname{row}\mathcal L\oplus R$、$RA\subseteq\operatorname{row}(CA)\subseteq W_0$ 得
$\mathcal VA\subseteq\operatorname{row}(\mathcal LA)+W_0\subseteq\mathcal V+W_0$ ✓。
2. $h=\dim(\operatorname{row}[\mathcal L;CA;C])=\dim(\mathcal V+W_0)$（因 $h$ 是 $\mathcal V$ 与 $W_0$ 之和的行空间维数），再用法则
$\dim(X+Y)=\dim X+\dim Y-\dim(X\cap Y)$；$R\subseteq\mathcal V\cap W_0$ 给出下界。
3. 见文中。$\square$



**B.28（c）〔原 B.28b〕（分层参数 $\delta$；专家 2026-11-05 §3.3 的建议）** 在 B.28 的记号下（设 $\operatorname{row}(CA)\cap R=0$，一般位置成立）令
$$\delta(\mathcal V):=\dim\frac{\operatorname{row}(CA)}{\operatorname{row}(CA)\cap\mathcal V}
=(r_1-p)-\dim\bigl(\operatorname{row}(CA)\cap\mathcal V\bigr),$$
即"$\operatorname{row}(CA)$ 中落在 $\mathcal V$ 外的方向数"。则
$$h=q+p+\delta(\mathcal V),\qquad 0\le\delta\le r_1-p .$$
* **等号障碍**对应 $\delta=r_1-p$（此时 $\operatorname{row}(CA)\cap\mathcal V=0$、$h=q+r_1$，**B.22** 给失败）；
* **不变子空间排除**排除 $\delta=0$（当 $q+p<n$，由 B.28 第 3 条）；
* **未决**的恰是中间层 $1\le\delta<r_1-p$。Class I 时 $r_1-p=2-1=1$，故**没有中间层**——这正是它能被一次二分解决的**结构原因**（专家 §2.3 的判断）。



**B.28（d）〔原 B.33〕（分层与约化铅笔尺寸的精确关系；专家 §5.2 给出）** 在 B.28/B.28b 的记号下，
$$\dim(V/S)=\dim V-\dim S=(n-r_1)-(n-h)=h-r_1=q+\delta-\rho ,$$
故商铅笔 $\overline N_{\mathcal Z}:V/S\to X/\mathcal Z$ 的尺寸是
$$\boxed{(p+q)\times(q+\delta-\rho)} .$$
*证明*：$\dim V=n-r_1$、$\dim S=n-h$（B.21）、$h=q+p+\delta$、$r_1=p+\rho$，相减即得。$\square$
*意义*：分层的几何参数 $\delta$ **直接就是**约化铅笔的列数偏移——这把"几何筛选"与"谱检验"接在同一条公式上。

## Lean（2026-11-06 已同步登记）

* 内核：`RowSpaceLayer.map_sup_le_iff`
* 均在 `tools/lean/MyProof/` 下，已登记进 `tools/lean/STATEMENT_MAP.md`；WSL 侧 `lake build MyProof` exit=0。
* 差异：矩阵实例化/行空间翻译与其余分部仍为纸面（详见 `## 状态与历史` 的等级行）。

## 精确验证

* `tools/verification/b26_class_I_only_Z.py`

## 状态与历史

*等级*：**[已证-纸面]** $+$ **[精确验证 2954/2954]**（`tools/verification/b26_class_I_only_Z.py`：1、2、3 与情形判别全部成立）。
*等级*：**[已证-纸面]**（专家给出，本项目复核；Class I 的 $p=1$ 特例即 B.26，已 2954/2954 精确验证）。
*等级*：**[已证-纸面]**（$h=q+p+\delta$ 的推导）+ **[观察]**（"未决=中间层"是问题定位，不是定理）。
*等级*：**[已证-纸面]** $+$ **[Lean-conditional]**（`B33.dim_quotient` 商维数公式、`B33.dim_arith` 算术）。
* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。




## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F2 |
| 导出等级 | **L3** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— Lean 已覆盖（内核） |


## 支撑目录

无（证据全部在本卷宗内）。
