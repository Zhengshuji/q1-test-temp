# 等号情形 $h=q+r_1$：新增 B.19（顶层与等号互斥，已证），等号排除仍开放

## 目标

按专家 §Direction A 攻等号情形：判断 $h=q+r_1$ 是否必然导致 $(5b)$ 失败；若不然，构造反例。

## 设想与理由

$(5b)$ 自动成立的唯一"平凡"途径是 $V\subseteq\mathcal Z$（此时 $V/S=0$，商铅笔定义域为零）。所以
"等号必失败"最可能被这种候选推翻。于是先查"顶层"能否落在等号上。

关键链条：$V\subseteq\mathcal Z$ ⟹ $\mathcal L$ 在 $V$ 上为零 ⟹ $R=\operatorname{row}\mathcal L\subseteq V^\perp=\operatorname{row}[C;CA]=W$
⟹ $R\cap W=R\ne0$ ⟹（B.11c 的 Type I 判据 $h\ge q+r_1\iff R\cap W=0$）$h<q+r_1$。

## 做法

1. 证明上述链条（B.19）；
2. 数值查"顶层 ∧ 等号"是否可能：先筛 $V\subseteq K$（$V\subseteq\mathcal Z$ 的必要条件），
   再在 $d\ge\dim V$ 的阶上构造含 $V$ 的 $\mathcal Z\subseteq K$；
3. 另做一次**大范围**等号扫描（含终阶 $d=0$）。

## 进展

| 项 | 结果 |
|---|---|
| **B.19（已证）** | $V\subseteq\mathcal Z\Rightarrow h<q+r_1$：顶层与等号**互斥** |
| 大范围等号扫描 | $h=q+r_1$ 的 **3945** 个可容许样本，$(5b)$ **全部失败**（0 例外）；此前另有 22 877 个样本同理 |
| $h>q+r_1$ 的样本 | 0 个（与"行数界直接排除"一致）|
| $h<q+r_1$ 的样本 | 1727 个，其中 1720 个 $(5b)$ 成立（7 个是 Type III）|
| 顶层搜索（修正版）| $V\subseteq K$ 仅 9/4903；其中可容许顶层候选全部 $h<q+r_1$，**无**等号样本 |

**一个被抓住的构造 bug**：第一版 `top_stratum.py` 把 $V$ 的列直接拼进 $Z$，于是 $Z\not\subseteq K$，
它不可能是 $\ker[C;\mathcal L]$；那些"样本"其实是 $\mathcal L=L_0$ 的普通候选。修正后（`top_stratum2.py`
先验 $V\subseteq K$、再验 $Z\subseteq K$）结论完全改变。教训：**构造完 $\mathcal Z$ 必须验证它就是核**。

## 最终结论

1. **B.19 排除了等号情形的"平凡可行"路线**：$V\subseteq\mathcal Z$ 时 $h$ 严格小于 $q+r_1$；
2. 因此"等号 $\Rightarrow$ 失败"**不能**被顶层候选推翻；剩下的缺口只有"$V\not\subseteq\mathcal Z$ 的等号情形"；
3. 该缺口目前**仍是未证**：共 26 822 个等号样本全部失败（精确验证），但不是定理；
4. 专家给的两条修法仍然适用：(i) 把"$h=q+r_1\Rightarrow$ 失败"并入 CSS 假设；(ii) 直接证明它。

## 放弃原因

不适用（等号排除仍未证；B.19 是通往它的必要条件）。

## 残留价值

* **B.19**：一条短证明，把等号情形的"平凡反例"路线彻底关掉；
* 三次扫描的完整数据（26822 个等号样本、0 例外）；
* 一个**方法论教训**（构造 $\mathcal Z$ 后必须验证它就是核）——已写进 `attempts/89`。

## 相关文件

- `docs/02` B.19、B.9（等号未证）、B.11d（等号注）
- `tools/verification/equality_case.py`、`equality_search.py`、`top_stratum2.py`
- 专家答复：`workspace/for_expert/archive/17_paper_layer-answer.md` §Direction A

## 再进一步：B.20（等号情形的结构记账，已证）

对等号情形把 Kronecker 记账落到可用锚点上：

1. **常值右零空间恰是 $S=V\cap\mathcal Z$**：$Q_{\mathcal L}(\lambda)v=0\ \forall\lambda$ $\iff$ $v\in S$。
   证明：$CAv=Cv=0$ ⟹ $v\in V$；$\lambda$-系数与常数项分别给 $\mathcal Lv=0$、$\mathcal LAv=0$；反向用 B.16b。
   故**零次右最小指标个数 $=s$**。
2. **$W\cap\mathcal Z^\perp=C$**：由 $h=\dim(\mathcal Z^\perp+W)=p+q+r_1-\dim(\mathcal Z^\perp\cap W)$ 与 $h=q+r_1$
   得 $\dim(\mathcal Z^\perp\cap W)=p$；而 $C\subseteq W\cap\mathcal Z^\perp$ 且 $\dim C=p$ ⟹ 相等。

于是等号时 $d_{\rm fin}+d_\infty=q+r_1-\sum_j\eta_j$，**等号排除定理等价于**
$$\sum_j\eta_j+d_\infty<q+r_1 .$$
这就是现在还缺的那一步（只有 26 822 个样本的精确证据，没有证明）。

**已知的计数**：左指标个数 $=2p-r_1$（等号时全为零次）；右指标个数 $=n-h$，其中 $s$ 个零次；
$h=q+r_1$。若能把"$\sum\eta_j$ 的上界"与"$d_\infty=r_1$"（后者待确认）结合，就能得到 $d_{\rm fin}=q-\sum\eta_j>0$。

## 再进一步：B.21（右零空间与指标，已证）——等号排除归结为 $d_\infty<h$

**B.21（已证）**：
1. **$s=n-h$**（对偶：$S=W^\perp\cap\mathcal Z$ ⟹ $S^\perp=W+\mathcal Z^\perp$ ⟹ $s=n-\dim(W+\mathcal Z^\perp)=n-h$）。
   **精确验证 650/650**。
2. **右零空间 $=S[\lambda]$**：$Q_{\mathcal L}(\lambda)x(\lambda)=0\iff x(\lambda)\in S[\lambda]$。
   证明：$C$、$CA$ 块逐系数给 $x_i\in V$；$\mathcal L$ 块在 $V$ 上化为 $(\lambda I-\Lambda)\mathcal Lx(\lambda)=0$，
   而 $\lambda I-\Lambda$ 在 $\mathbb C(\lambda)$ 上可逆 ⟹ $\mathcal Lx(\lambda)=0$ ⟹ $x_i\in S$。
3. 推论：右指标共 $n-h=s$ 个且**全为零次**，故 $\sum_j\eta_j=0$。

于是等号时恒等式退化为
$$d_{\rm fin}+d_\infty=h=q+r_1,$$
**等号排除定理 $\iff d_\infty<h$**（铅笔必有非平凡有限初等因子）。

**一条错误路线被否掉**：曾猜 $d_\infty=h-\operatorname{rank}A_1$；反例
$P(\lambda)=\begin{pmatrix}1&\lambda\\0&1\end{pmatrix}$：$h=2$、$\operatorname{rank}A_1=1$，但 $\det\equiv1$ 故 $d_\infty=2$。
所以 $d_\infty$ 不能用 $\operatorname{rank}A_1$ 直接算，这一步需要 Kronecker 理论里关于无穷部分的真正公式。

**当前缺口的一句话形式**：等号排除 $\iff$ "$Q_{\mathcal L}$ 在无穷处的结构不满秩"$\iff$ $d_\infty<h$。
