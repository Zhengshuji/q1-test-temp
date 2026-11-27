# $(5a)$ ⟹ 观测器铅笔的右最小指标全为 $0$

> **等级**：**[已证-纸面]**（本文）+ **[精确验证 150/150]**（[verify.py](verify.py)，$n=6,7,8$ 各 50 个）。
> 陈述只用 $(5a)$，**不需要** $(5b)$。

## 记号

$A\in\mathbb C^{n\times n}$、$C\in\mathbb C^{p\times n}$、$L\in\mathbb C^{q\times n}$；
$$Q_L(\lambda)=\begin{bmatrix}\lambda L-LA\\ CA\\ C\end{bmatrix}\in\mathbb C[\lambda]^{(q+2p)\times n}.$$
$(5a)$：$\operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C]$，等价地
$$\operatorname{row}(LA)\subseteq\operatorname{row}(L;CA;C). \tag{5a'}$$

常值右零空间
$$N=\{w\in\mathbb C^n:\ Lw=0,\ LAw=0,\ Cw=0,\ CAw=0\}.$$

## 定理

若 $(5a)$ 成立，则对任何满足 $Q_L(\lambda)v(\lambda)\equiv0$ 的多项式向量
$v(\lambda)=\sum_{k=0}^{d}\lambda^kv_k$（$v_k\in\mathbb C^n$，$v_d\ne0$），**每个系数 $v_k$ 都属于 $N$**。
因此右零模 $=N\otimes\mathbb C[\lambda]$，有**常值基**，从而 $Q_L$ 的**右最小指标全为 $0$**。

## 证明

把 $Q_L(\lambda)v(\lambda)\equiv0$ 按 $\lambda$ 的幂展开（$v_{d+1}:=0$）：

* $\lambda^0$ 项：$LA\,v_0=0$；
* $\lambda^{k+1}$ 项（$0\le k\le d$）：$L\,v_k-LA\,v_{k+1}=0$，特别地 $L\,v_d=0$；
* 常值行：$CA\,v_k=0$，$C\,v_k=0$ 对所有 $k$。

**关键一步**：$v_d$ 满足 $Lv_d=0,\ CAv_d=0,\ Cv_d=0$。由 $(5a')$，$LA$ 的每一行都是
$L,CA,C$ 的行的线性组合，故 $LA\,v_d=0$。于是 $v_d\in N$ ✓。

**归纳**：$v_d\in N$ ⟹ $\lambda^dv_d$ 也是零向量（$Q_L(\lambda)(\lambda^dw)= \lambda^dQ_L(\lambda)w=0$）
⟹ $v(\lambda)-\lambda^dv_d$ 是次数 $<d$ 的零向量 ⟹ 由归纳假设，其全部系数属于 $N$；
$v_d$ 也属于 $N$ ⟹ 全部系数属于 $N$ ✓。

**推论**：$N$ 中的常值向量张成整个右零模 ⟹ 右最小指标全为 $0$ ✓。$\square$

## 备注

1. **与 $(5b)$ 无关**：证明只用了 $(5a')$。所以**不可行**的观测器铅笔也满足本定理
   （验证脚本覆盖了不可行的候选，150/150 全部通过）。
2. **不矛盾于**"常数秩不蕴含右指标为 0"：那条针对**一般**铅笔（反例 $[\lambda\ 1]$）；
   这里用的是 $Q_L$ 的**分块结构**（$CA,C$ 行 + $(5a')$）。
3. **本定理不是"观测器特有"的强结论**：它是 $(5a)$ 的直接推论。剩下的猜想是
   $d_\infty$ 的界（T4-b）与左侧下界（T4-c），见
   [workspace/kronecker/TARGET_FORM_T.md](../../workspace/kronecker/TARGET_FORM_T.md)。

## 复现

```bash
python proof/kron_null_module/verify.py
```

输出形如：`满足 (5a) 的铅笔：150 个（n=6,7,8）`、`右最小指标全为 0：150 / 150`。
