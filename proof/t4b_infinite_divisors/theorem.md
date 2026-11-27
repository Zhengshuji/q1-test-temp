# T4-b：观测器铅笔的无穷初等因子全是 1 次

> **等级**：**[已证-纸面]**（本文）+ **[精确验证 151/151]**（[verify.py](verify.py)，$n=6,7,8,9,10$）。
> **注意**：定理**只用 $(5a)$**，不需要 $(5b)$。

## 记号

$A\in\mathbb C^{n\times n}$、$C\in\mathbb C^{p\times n}$、$L\in\mathbb C^{q\times n}$；
$$Q_L(\lambda)=\begin{bmatrix}\lambda L-LA\\ CA\\ C\end{bmatrix},\qquad
H=\begin{bmatrix}L\\CA\\C\end{bmatrix},\qquad h=\operatorname{rank}H=\operatorname{rank}[L;CA;C].$$
$(5a)$：$\operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C]$，等价地
$$\operatorname{row}(LA)\subseteq\operatorname{row}(L;CA;C). \tag{5a'}$$

## 定理（T4-b）

若 $(5a)$ 成立，则 $Q_L$ 的**无穷初等因子全是 1 次**，个数为 $h-\operatorname{rank}L$。于是
$$d_\infty:=\sum_{\text{无穷因子}}(\text{次数})=h-\operatorname{rank}L .$$

## 证明

### 第 1 步：分解

由 $(5a')$，$LA$ 的每一行是 $L,CA,C$ 的行的线性组合，故存在**常值**矩阵 $X\in\mathbb C^{q\times q}$、
$Y_1,Y_2\in\mathbb C^{q\times p}$ 使
$$LA=XL+Y_1CA+Y_2C .$$

于是
$$Q_L(\lambda)=\begin{bmatrix}\lambda L-XL-Y_1CA-Y_2C\\CA\\C\end{bmatrix}
=\underbrace{\begin{bmatrix}\lambda I_q-X&-Y_1&-Y_2\\0&I_p&0\\0&0&I_p\end{bmatrix}}_{=:P(\lambda)}
\underbrace{\begin{bmatrix}L\\CA\\C\end{bmatrix}}_{=:H}.$$

而
$$P(\lambda)=\underbrace{\begin{bmatrix}I_q&-Y_1&-Y_2\\0&I_p&0\\0&0&I_p\end{bmatrix}}_{=:U\ \text{常值可逆}}
\operatorname{diag}(\lambda I_q-X,\ I_{2p}).$$

### 第 2 步：严格等价

左乘常值可逆的 $U^{-1}$ 是**严格等价**（保持全部 Kronecker 不变量，含无穷因子），故 $Q_L$ 与
$$M(\lambda):=\operatorname{diag}(\lambda I_q-X,\ I_{2p})H=\begin{bmatrix}(\lambda I_q-X)L\\CA\\C\end{bmatrix}$$
有相同的 Kronecker 数据。**下面只算 $M$。**

### 第 3 步：反转铅笔

写 $M(\lambda)=M_0+\lambda M_1$，则
$$M_1=\begin{bmatrix}I_q&0\\0&0\end{bmatrix}H=\begin{bmatrix}L\\0\\0\end{bmatrix},\qquad
M_0=\begin{bmatrix}-X&0\\0&I_{2p}\end{bmatrix}H=\begin{bmatrix}-XL\\CA\\C\end{bmatrix}.$$
$M$ 的无穷初等因子 = 反转铅笔
$$\widehat M(\mu):=M_1+\mu M_0=\begin{bmatrix}(I_q-\mu X)L\\ \mu CA\\ \mu C\end{bmatrix}$$
在 $\mu=0$ 处的初等因子（按定义：$\lambda=1/\mu$）。

### 第 4 步：在 $\mu=0$ 处做局部等价

$\det(I_q-\mu X)|_{\mu=0}=1\ne0$，故 $I_q-\mu X$ 在局部环 $\mathbb C[\mu]_{(\mu)}$ 里**可逆**，
$S(\mu):=\operatorname{diag}\bigl((I_q-\mu X)^{-1},I_p,I_p\bigr)$ 是该局部环上的可逆矩阵。于是
$$S(\mu)\widehat M(\mu)=\begin{bmatrix}L\\ \mu CA\\ \mu C\end{bmatrix}=:\widetilde M(\mu).$$
局部等价（左右乘局部环上的可逆矩阵）**保持** $\mu=0$ 处的局部 Smith 形 ⟹
$\widehat M$ 与 $\widetilde M$ 在 $\mu=0$ 处的初等因子相同。

### 第 5 步：$\widetilde M$ 的行列式因子

记 $r_1=\operatorname{rank}L$，$\Delta_k$ 为 $\widetilde M$ 的全部 $k\times k$ 子式的 gcd（$\mu$ 的多项式）。

* $k\le r_1$：取 $k$ 行全来自 $L$ 块且行列式非零 ⟹ $\Delta_k$ 是**非零常数** ✓（$\mu$ 赋值 $0$）。
* $r_1<k\le h$：
 * **下界**：任何非零 $k\times k$ 子式用了 $j$ 个 $\mu$ 块的行、$k-j$ 个 $L$ 块的行；
   由 $\operatorname{rank}L=r_1$，非零要求 $k-j\le r_1$，即 $j\ge k-r_1$ ⟹ 子式被 $\mu^{k-r_1}$ 整除。
 * **达到**：取 $r_1$ 个线性无关的 $L$ 行，再取 $k-r_1$ 个 $[CA;C]$ 的行，使合起来在 $[L;CA;C]$ 中
   秩为 $k$（可能，因为 $h=\operatorname{rank}[L;CA;C]\ge k$）；对应子式 $=\mu^{k-r_1}\cdot\det(\text{非零常数})$。
 ⟹ $\Delta_k=c_k\,\mu^{k-r_1}$，$c_k\ne0$ 常数。
* $k>h$：全为 $0$（normal rank 是 $h$）。

### 第 6 步：不变因子与结论

不变因子 $d_k=\Delta_k/\Delta_{k-1}$：
* $k\le r_1$：$d_k=c_k/c_{k-1}$ 是**单位**；
* $r_1<k\le h$：$d_k=(c_k/c_{k-1})\,\mu$ —— 恰好 $\mu$ 的一次幂。

所以 $\mu=0$ 处的初等因子恰是 $h-r_1$ 个 $\mu$，每个**次数 1** ✓。于是
$$d_\infty=h-\operatorname{rank}L . \qquad\blacksquare$$

## 推论（**更正版**，专家 2026-11-02 §2）

由 B.6（$\sum\eta=0$）、B.7（$d_\infty=h-\operatorname{rank}L$）与全局恒等式
$$\sum\eta+\sum\varepsilon+d_{\rm fin}+d_\infty=h$$
（$d_{\rm fin}$ = 全部**有限**初等因子的总次数）得

$$\boxed{\ \sum_j\varepsilon_j=\operatorname{rank}L-d_{\rm fin}\ }\qquad(\text{只用 }(5a))$$

只有在 $(5a)+(5b)$（即 $d_{\rm fin}=0$）时才有
$$\sum_j\varepsilon_j=\operatorname{rank}L .$$

**注意**：本文件早先的版本把后者写成"$(5a)$ 的推论"，**那是错的**（见
[proof/refuted R21](../refuted/README.md)）；151 个验证样本里有 43 个不满足 $(5b)$，
它们的 $d_{\rm fin}$ 从 $1$ 到 $7$ 不等，$\sum\varepsilon$ 因此**小于** $\operatorname{rank}L$。

**两条立即的推论**：

1. $d_{\rm fin}\le\operatorname{rank}L$（因为 $\sum\varepsilon\ge0$）；
2. 若 $(5a)+(5b)$ 同时成立，左指标个数为 $q+2p-h$ 且非负，故
$$\boxed{\ \operatorname{rank}L\le q+2p-h\ }$$
——一条**谱可行性的必要条件**（专家建议收进秩/维数屏障清单）。

## 与数据的对照

* [verify.py](verify.py)：$n=6,7,8,9,10$ 共 **151 个满足 $(5a)$ 的铅笔**（其中 108 个可行），
  **反例 0 个**；所有无穷因子的 $\mu$-赋值都是 $1$，形态分布只有 `()`、`(1,)`、`(1,1)`。
* **注意量**：$d_\infty$ 必须用反转铅笔不变因子在 $\mu=0$ 处的**阶（$\mu$-adic 赋值）**，
  **不是**多项式总次数——用总次数会得到假的"反例"（见 [proof/refuted R20](../refuted/README.md)）。

## 复现

```bash
python proof/t4b_infinite_divisors/verify.py
```

预期：`满足 (5a) 的铅笔：151 个`、`反例：0 个`、`✓ 全部通过`。
