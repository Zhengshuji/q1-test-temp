# 零左最小指标的计数，与 $(5b)$ 的必要条件 $h<q+r_1$

**状态**：**[已证-纸面]**（本文件）$+$ **[精确验证 56/56]**（[verify.py](verify.py)）。

## 记号

$\mathcal L$ 为 $q\times n$、**行满秩**、含 $L_0$（$L_0\ne0$）的增广；
$Q_{\mathcal L}(\lambda)=[\lambda\mathcal L-\mathcal LA;\;CA;\;C]$（$(q+2p)\times n$）；
$h=\operatorname{rank}Q_{\mathcal L}$（正规秩）；
$r_1=\operatorname{rank}[C;CA]$；左最小指标 $\varepsilon_1\ge\cdots\ge\varepsilon_m\ge0$，$m=q+2p-h$；
$d_{\rm fin}$ = 有限初等因子的总次数；$s=\operatorname{rank}\mathcal L$。

## 引理 1（常值左零向量）

$Q_{\mathcal L}$ 的常值左零向量空间维数 $=2p-r_1$。
即：$\varphi Q_{\mathcal L}(\lambda)\equiv0$ 的解空间维数为 $2p-r_1$。

*证明.* 写 $\varphi=(\varphi_1,\varphi_2,\varphi_3)$，$\varphi_1\in\mathbb C^{q}$、$\varphi_2,\varphi_3\in\mathbb C^{p}$。
$\lambda$ 的系数给出 $\varphi_1\mathcal L=0$；$\mathcal L$ 行满秩 ⟹ $\varphi_1=0$。
常值项给出 $\varphi_2CA+\varphi_3C=0$，即 $(\varphi_2,\varphi_3)\in\ker_{\rm left}[CA;C]$，维数 $2p-r_1$。$\square$

## 引理 2（零指标恰为常值零向量的维数）

$\#\{j:\varepsilon_j=0\}=2p-r_1$，从而 $\#\{j:\varepsilon_j>0\}=q+r_1-h$。

*证明.* 取左最小基 $\ell_1(\lambda),\dots,\ell_m(\lambda)$，其次数即左最小指标（最小基的 standard theory）。
次数为 $0$ 的基元张成恰是常值左零向量空间（否则可用最小性消去低次项），故零指标个数等于引理 1 的维数。
再由 $m=q+2p-h$ 得非零个数 $=m-(2p-r_1)=q+r_1-h$。$\square$

## 推论 B.9（$(5b)$ 的必要条件）

$$\boxed{\ (5b)\ \Longrightarrow\ h<q+r_1\ }$$

等价地：**若 $h\ge q+r_1$，则 $(5b)$ 必失败**。

*证明.* $h\ge q+r_1$ ⟹ 引理 2 给出非零左指标个数 $=0$ ⟹ 所有 $\varepsilon_j=0$ ⟹ $\sum_j\varepsilon_j=0$。
由 B.6+B.8 的恒等式 $\sum_j\varepsilon_j=s-d_{\rm fin}$ 得 $d_{\rm fin}=s=\operatorname{rank}\mathcal L\ge1$
（$L_0\ne0$）。而 $(5b)\iff d_{\rm fin}=0$（B.8），故 $(5b)$ 失败。$\square$

**注**：$q+r_1-h$ 是**非零**左指标的个数——它只依赖 $(q,r_1,h)$ 三个整数，
所以 B.9 是一个"廉价"的必要条件：先算这三个数，若 $h\ge q+r_1$ 就不必再判 $(5b)$。

## 与已知结果的关系

* B.6（$(5a)\Rightarrow$ 右指标全为 $0$）与 B.8（$(5b)\iff\sum\varepsilon=s$）是本推论的两个输入；
* 与 `h_bound` 的互补障碍不同：后者是**充分**失败条件（$\ker C=\mathcal V\oplus Z$ 且 $h=n-p$），
  只可能在 $q=n-r_1$ 触发；B.9 是**一般阶**上的必要条件。
* 数据上：56 个功能可观测实例中，闭包处 $(5b)$ 失败的 **16 个全部**满足 $h\ge q+r_1$（见 verify.py），
  即 B.9 解释了样本里**所有**的失败。

## 复现

```bash
python proof/left_index_count/verify.py
```

预期：`不通过的断言：0`，`B.9 的触发次数 16；其中 d_fin=0 的（反例）：0`。
