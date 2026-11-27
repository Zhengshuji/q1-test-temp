# Toeplitz 判据：用**一个矩阵的零度**判 $(5b)$

> **等级**：**[已证-纸面]**（本文，依赖 B.6/B.7/B.8 与最小基标准理论）$+$ **[精确验证 66/66]**
> （[verify.py](verify.py)）。判据由专家 2026-11-02 答复 §9 提出；本文把它的陈述与证明写完整。

## 记号

$L$ 满足 $(5a)$，$H=[L;CA;C]$，$h=\operatorname{rank}H$，$s=\operatorname{rank}L$，
$m=q+2p-h$（左最小指标的个数）。由 $(5a)$ 取常值 $\Lambda$ 使 $LA=\Lambda L+G_0C+G_1CA$。

取 $J$ 满行秩、$\ker J=\ker H^{\mathsf T}$（即 $J$ 的行是 $H^{\mathsf T}$ 的行的基），按 $(q,p,p)$ 分块
$J=[J_1\ J_2\ J_3]$，令 $E=J_1$、$B=[J_2\ J_3]$、$F=E\Lambda^{\mathsf T}$。**约化铅笔**
$$R(\lambda)=[\lambda E-F\ \ B]\quad(h\times(q+2p)),\qquad [E\ B]=J\ \text{满行秩 }h .$$

对 $d\ge0$，$T_d$ 是方程 $R(\lambda)y(\lambda)=0$（$y=(x,u)$、$\deg y\le d$）的**块 Toeplitz 矩阵**：
第 $k$ 块行（$0\le k\le d+1$）为
$$k=0:\ -Fx_0+Bu_0;\qquad 1\le k\le d:\ Ex_{k-1}-Fx_k+Bu_k;\qquad k=d+1:\ Ex_d .$$
它是 $h(d+2)\times(q+2p)(d+1)$ 的矩阵；$\nu_d:=\dim\ker T_d$。

## 引理 1（多项式零空间维数）

设 $R$ 的右最小指标为 $\varepsilon_1\ge\cdots\ge\varepsilon_m\ge0$。则
$$\nu_d=\sum_{i=1}^{m}\max\{0,\ d-\varepsilon_i+1\} .$$
*依据*：铅笔的右零模是 $\mathbb C[\lambda]$ 上的自由模，秩 $m$，其**最小基**的次数正是右最小指标
（最小多项式基的 standard theory；Forney 1975 的 predictable degree 性质）。按最小基把次数 $\le d$ 的元素写开，
第 $i$ 个生成元给出 $d-\varepsilon_i+1$（当 $d\ge\varepsilon_i$）个自由系数，其余为 $0$。∎

**推论**：$d\ge\max_i\varepsilon_i$ 时 $\nu_d=(d+1)m-\sum_i\varepsilon_i$；且
$$\#\{i:\varepsilon_i=d\}=\nu_d-2\nu_{d-1}+\nu_{d-2}\qquad(\nu_{-1}=\nu_{-2}=0).$$

## 定理（单 Toeplitz 矩阵判据）

$$\boxed{\ (5b)\iff \nu_s=(s+1)m-s\ }\qquad\Longleftrightarrow\qquad
\boxed{\ \operatorname{rank}T_s=(q+2p)(s+1)-((s+1)m-s)\ }$$

### 证明

1. 由 B.6，$\sum_i\eta_i=0$（右最小指标全为 $0$）；由 B.7，$d_\infty=h-s$；由全局恒等式
   $\sum\eta+\sum\varepsilon+d_{\rm fin}+d_\infty=h$ 得
   $$\sum_i\varepsilon_i=s-d_{\rm fin}. \tag{B.8}$$
   特别地 $\max_i\varepsilon_i\le\sum_i\varepsilon_i\le s$，故引理 1 的推论在 $d=s$ 可用。
2. 于是 $\nu_s=(s+1)m-\sum\varepsilon_i=(s+1)m-s+d_{\rm fin}$。
3. 因此 $\nu_s=(s+1)m-s\iff d_{\rm fin}=0\iff(5b)$（最后一步是 B.8 的等价）。
   $\square$

**注**：判据只用一个 $h(s+2)\times(q+2p)(s+1)$ 的常数矩阵的秩，**不需要 Smith 形**、
也不需要逐个算最小指标。

## 与 Smith 路径的独立交叉验证

[verify.py](verify.py)：$n=6,7,8$ 的 66 个满足 $(5a)$ 的铅笔上，
$\nu_d$ 的差分恢复出的 $\varepsilon$ 与 Smith 路径（[tools/verification/kronecker_pencil.py](../../tools/verification/kronecker_pencil.py)）
**逐个相等（66/66）**；判据 $(5b)\iff\nu_s=(s+1)m-s$ 也 **66/66** 一致。

## 用途

* **WP1（专家建议的最高优先）**：给 $(5b)$ 一个不依赖 Smith 形的判定；
* **G-4**：把"在增广族上搜索"变成"对每个成员算一个矩阵的秩"，且该矩阵的条目是参数的**显式多项式/有理函数**；
* **G-3**：整条指标序列可由 $\nu_0,\dots,\nu_s$ 恢复，便于比较不同成员。

## 复现

```bash
python proof/toeplitz_criterion/verify.py
```
