# Gram 证书的精确实例（244 铅笔）

> 2026-11-09。为 277 的 Gram 引理给出一个可机器检查的实例：
> 用 244 的 $3\times3$ 铅笔 $P$ 验证 $(5b)$ 的 $2\omega$ 维证书与 Cauchy–Binet 压缩；
> 用 244 的 $H,H_A$ 验证 $(5a)$ 的 $e_\omega(G_H)>0$、$e_{\omega+1}(G_S)=0$。
> `c278_gram_certificate.py` PASS。状态：**M2 + 精确验证**。

## 目标

把 277 的两个 Gram 引理落成可复现的精确计算。

## 设想与理由

244 的 $P$ 是 $3\times3$、秩 2，极大子式是 $2\times2$，且 gcd $=1$；
正好是 $\omega=2$ 的 Gram 证书测试用例。

## 做法

### 1. $(5b)$ 证书

$P$ 的 9 个 $2\times2$ 子式 $f_i$，gcd $=1$。
取 $B$ 的行为 $f_i$ 与 $\lambda f_i$ 的系数向量（次数 $0..3$），$B$ 是 $18\times4$。
计算：
- $\operatorname{rank}B=4$；
- $e_0=(1,0,0,0)^{\mathsf T}\in\operatorname{row}B$（$\operatorname{rank}[B;e_0]=4$）；
- $B^{\mathsf T}Bx=e_0$ 有精确解。

### 2. Cauchy–Binet 压缩

$$K(\lambda,\mu)=\sum_i f_i(\lambda)f_i(\mu)
=\sum_{|J|=2}\det(P_{:,J}(\lambda)^{\mathsf T}P_{:,J}(\mu)).$$
精确验证两边相等；并验证
$$(B^{\mathsf T}B)_{d,e}=\operatorname{coeff}_{\lambda^d\mu^e}\big((1+\lambda\mu)K\big).$$

### 3. $(5a)$ 证书

244 的
$$H=\begin{bmatrix}0&0&1\\1&2&0\\3&6&1\end{bmatrix},\qquad
H_A=\begin{bmatrix}0&0&0\\3&6&1\\3&6&3\end{bmatrix}.$$
- $\operatorname{rank}H=\operatorname{rank}[H;H_A]=2$；
- $e_2(G_H)=55>0$，$e_3(G_S)=0$；
- 扰动 $H_A$ 使 $\operatorname{rank}[H;H_A]=3$，则 $e_3(G_S)=444\ne0$。

## 输出

```
number of 2x2 minors = 9
gcd of minors = 1
B shape = (18, 4) rank B = 4
rank[B;e0] = 4
B^T B x = [[1],[0],[0],[0]]
Cauchy-Binet difference = 0
B^T B coefficient formula: OK
rank H = 2 rank[H;HA] = 2
e2(GH) = 55 ; e3(GS) = 0
perturbed rank[H;HA] = 3 ; e3(GS_bad) = 444
PASS
```

## 进展

* 两个 Gram 引理在 244 上精确验证；
* Cauchy–Binet 压缩公式验证；
* $(5a)$ 的正/负例（扰动后 $e_3>0$）。

## 最终结论

* 277 的证书不是纯形式论证：至少在一个非平凡实例上精确成立；
* 剩余是比特复杂度、$\omega=0$、以及完整 FPT 实现。

## 放弃原因

* 未测更大/随机实例；
* 未做比特复杂度；
* 未实现 FPT。

## 残留价值

* 可复用的证书脚本；
* 对 277 的机器支持；
* 244 数据的双重用途（门 + Gram 测试）。

## 相关文件

* [attempts/277](277_gram_fpt.md)
* [attempts/244](../../../q1_true/multiplication_gate/attempts/244_q3_feasible_absorbed.md)
* `tools/verification/c278_gram_certificate.py`

## 状态

* 实例验证：**[M2 + 精确验证]**。
* 比特复杂度/实现：**[未做]**。
