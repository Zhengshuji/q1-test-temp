# 谱障碍只发生在 $\\Lambda$ 的特征值上

> **对应 docs 条目**：B.13（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

**状态**：**[已证-纸面]**（两步恒等式）+ **[精确验证 3/3 候选]**（[type3_spectrum.py](../../tools/verification/type3_spectrum.py)）。

## 记号

$\\mathcal L$ 满足 $(5a)$，取 $\\Lambda,G_0,G_1$ 使 $\\mathcal LA=\\Lambda\\mathcal L+G_0C+G_1CA$，记
$$H=[\\mathcal L;CA;C],\\qquad D(\\lambda)=\\begin{pmatrix}\\lambda I-\\Lambda&-G_1&-G_0\\\\0&I&0\\\\0&0&I\\end{pmatrix}.$$
于是 $Q_{\\mathcal L}(\\lambda)=D(\\lambda)H$。

## 命题

若 $\\lambda\\notin\\operatorname{spec}(\\Lambda)$，则 $\\operatorname{rank}Q_{\\mathcal L}(\\lambda)=\\operatorname{rank}H=h$。

*证明*：$\\lambda\\notin\\operatorname{spec}\\Lambda$ 时 $\\lambda I-\\Lambda$ 可逆，故 $D(\\lambda)$ 可逆
（分块上三角，对角块为 $\\lambda I-\\Lambda$ 与 $I$）。可逆矩阵左乘不改变秩，故
$\\operatorname{rank}(D H)=\\operatorname{rank}H=h$。$\\square$

**推论**：$(5b)\\iff$ 对每个 $\\lambda\\in\\operatorname{spec}(\\Lambda)$ 都有
$\\operatorname{rank}Q_{\\mathcal L}(\\lambda)=h$。

即：**有限初等因子的根必在 $\\operatorname{spec}\\Lambda$ 内**；谱障碍只可能出现在 $\\Lambda$ 的特征值处。

## 验证

对 [C4](../refuted/C4_type3_counterexample.md) 的三个反例候选（$n=6$、Jordan 块 $A$、$q_0=3$）：

| 候选 | $\\Lambda$ 的有理谱 | 直接扫到的坏 $\\lambda$ | 坏 $\\lambda\\subseteq\\operatorname{spec}\\Lambda$ |
|---|---|---|---|
| #1 | $\\{4/3\\}$ | 无（坏根为 $\\lambda^2-5\\lambda+7$ 的**复根**）| ✓ |
| #2 | $\\{4/3,5/3,3\\}$ | $\\{3,5/3\\}$（$3$ 记多重）| ✓ |
| #3 | $\\{1,4/3,17/5\\}$ | $\\{1\\}$（多重）| ✓ |

候选 #1 说明了**有理 $\\lambda$ 扫描会漏掉障碍**：它的坏根是复的。因此"扫有理 $\\lambda$"只能作为
快速定位，不能作为判据；判据仍应用极大子式 gcd（或 Toeplitz 判据）。

## 意义

* 把 $(5b)$ 的检查范围从"所有 $\\lambda\\in\\mathbb C$"缩到 **$\\operatorname{spec}\\Lambda$**（$q$ 个点，
  计重数），且 $\\Lambda$ 由一个线性系统解出；
* 与 $(\\star)$（$\\operatorname{im}H\\cap J\\ker(\\lambda I-\\Lambda)=0$）配合，
  获得"在哪里、以什么方式掉秩"的完整描述；
* 但注意：$\\Lambda$ **依赖 $\\mathcal L$**，所以这不能直接把"存在可行 $\\mathcal L$"变成整数条件。

## 复现

```bash
python tools/verification/type3_spectrum.py
```
