# $\mathrm{DEC}(q)\in\exists\mathbb R$：直接对原铅笔 $Q(\lambda)$ 的证书（专家 58 号）

> 2026-11-08。专家 58 号给出一个更直接的 $\exists\mathbb R$ 上界证明：把多项式广义逆定理
> 直接用在**原铅笔** $Q(\lambda)=[\lambda L-LA;\ CA;\ C]$ 上，不需要 $K_0$、$N$、$H,H_A$。
> 本文件把该证明写全（含 normal rank 条件、逆命题、编码规模）。状态：**M2（纸面）**。

## 目标

证明：对有理输入 $(A,C,L_0)$ 与整数 $q$，$\mathrm{DEC}(q)\in\exists\mathbb R$，用原铅笔证书。

## 设想与理由

令
$$s=\operatorname{rank}\begin{bmatrix}L\\CA\\C\end{bmatrix}.$$
由 $(5a)$，$LA$ 的行在 $\operatorname{row}[L;CA;C]$ 中，故 $\operatorname{rank}Q(\lambda)\le s$ 对所有 $\lambda$；
$(5b)$ 等价于 $\operatorname{rank}Q(\lambda)=s$ 对所有 $\lambda$。

**多项式广义逆定理**：若 $Q\in\mathbb C[\lambda]^{m\times n}$ 的 normal rank 为 $s$，且
$\operatorname{rank}Q(\lambda)=s$ 对所有 $\lambda$，则存在 $Y\in\mathbb C[\lambda]^{n\times m}$，
$\deg Y\le2s-2$，使 $QYQ=Q$（141 的 Bézout-adjugate 构造）。

## 做法

### 定理（直接证书）

设 $Q(\lambda)=[\lambda L-LA;CA;C]$。则 $(5b)$ 成立 $\iff$ 存在多项式 $Y$ 使
$$QYQ=Q,\qquad \deg Y\le2s-2,$$
**且** $Q$ 的 normal rank 为 $s$。

*证明*：
* $(\Rightarrow)$：$(5b)$ 给 normal rank $s$（因为 $Q$ 在一般 $\lambda$ 处秩 $s$）与处处秩 $s$；由定理得 $Y$。
* $(\Leftarrow)$：设 $QYQ=Q$ 且 normal rank $s$。固定 $\lambda_0$，在局部环 $\mathbb C[\lambda]_{(\lambda-\lambda_0)}$
  取 Smith 形 $UQV=\operatorname{diag}(d_1,\dots,d_s,0,\dots)$；由 $QYQ=Q$ 得 $d_i^2\tilde y_{ii}=d_i$，
  故 $d_i$ 是单位，$\operatorname{rank}Q(\lambda_0)=s$。$\lambda_0$ 任意，故 $(5b)$。$\square$

**normal rank 的编码**：存在 $\lambda_0$ 与一个 $s\times s$ 子式使 $\det Q_{I,J}(\lambda_0)\ne0$；
这是一个存在量词 + 多项式非零（复数为 $x^2+y^2>0$）。

### 编码

变量：$L$ 的未知行（$q$ 行，含 $L_0$ 固定）、$\lambda_0$、$Y_0,\dots,Y_D$（$D=2s-2$，每个
$n\times(q+2p)$）。
约束：
1. $(5a)$：$\operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C]=s$（用子式）；
2. $QYQ=Q$ 的系数匹配（$Q$ 次数 1、$Y$ 次数 $D$，左边次数 $\le2D+2=4s-2$）；
3. normal rank：某个 $s\times s$ 子式在 $\lambda_0$ 非零；
4. 满行秩（或 $[C;L]$ 满行秩，按约定）用子式编码；
5. $L_0$ 固定用等式约束。

**规模**：$Y$ 的系数个数 $O(s\cdot n\cdot(q+2p))=O(n^3)$；方程个数 $O(n^3)$；次数 $\le4s-2=O(n)$；
系数比特长由输入比特长与构造中的算术运算控制（有理 Gauss 消元）。故公式规模多项式。

**$s=0$**：$[L;CA;C]=0$，即 $L=0$、$CA=0$、$C=0$；单独处理（$Q\equiv0$，$(5b)$ 自动成立）。

**推论**：$\mathrm{DEC}(q)\in\exists\mathbb R$；$\mathrm{MIN}(k)=\bigvee_{q=r}^{\min(k,n)}\mathrm{DEC}(q)\in\exists\mathbb R$。

## 进展

* 直接原铅笔证书的证明已写全（定理 + 逆命题 + 编码 + 规模）；
* 与 141 的压缩铅笔证书相比：不需要 $K_0,N,H,H_A$，但 $s$ 可能比 $\omega$ 大（$s=h$ 是目标秩，
  $\omega=\operatorname{rank}H$）；次数 $2s-2$ 可能更大，但仍是多项式；
* 与 G.1（chart-free 编码）互补：G.1 用压缩变量，本文件用原变量。

## 最终结论

* $\mathrm{DEC}(q)\in\exists\mathbb R$ 有一个**独立于压缩几何**的直接证明；
* 它不依赖 $c=2/c=3$ 的不可约性，可作为复杂度部分的独立定理；
* 证书的次数界是 $2s-2$（$s$ 为目标秩），编码多项式规模。

## 放弃原因

* 未写 normal rank 条件的完整多项式编码（只给了存在 $\lambda_0$ 的形式）；
* 未处理 $s=0$ 的边界（已说明单独处理，未细写）；
* 未 Lean 化。

## 残留价值

* 一个更短、更独立的 $\exists\mathbb R$ 成员证明；
* 与 G.1 的编码互为校验。

## 相关文件

* [attempts/141](../../c_stratification/attempts/141_polynomial_certificate.md)（压缩铅笔证书）
* [proof/dec_q_existsR](../../../../proof/dec_q_existsR/README.md)（G.1 编码）
* [attempts/157](157_existsR_checklist_audit.md)（审计）

## 状态

* 定理/编码：**[已证-纸面，M2]**。
* 精确验证/Lean：**[未做]**。
