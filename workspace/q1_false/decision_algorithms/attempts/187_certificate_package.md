# 不可行证书包：seeds 16/21（专家 61 号建议）

> 2026-11-08。按专家 61 号的要求，把 16/21 的全 $q$ 不可行性做成**可复现的精确证书包**：
> $K_0,N$、$W_L$ 基、$W_L\subseteq D$ 的 $w$、$c=2$ 的 $\mathrm{Des}/\alpha$、$c=1$ 的特征线二次式与 $\varphi$。
> 证书文件：[certificates/seed16.md](../../feasibility_geometry/certificates/seed16.md)、
> [certificates/seed21.md](../../feasibility_geometry/certificates/seed21.md)。
> 状态：**精确验证（自动生成）**。

## 目标

把 185 的结构性论证变成一份**逐项可核对**的精确数据，供专家审计。

## 设想与理由

专家建议证书包含：
1. 精确的 $K_0$ 与 $N$；
2. $W_L$ 的定义矩阵与基；
3. $W_L\subseteq D$ 的见证（$Av=Nw$ 的 $w$）；
4. $c=2$ 的 $\mathrm{Des}_i$ 与 $\alpha$（$\alpha^{\mathsf T}\mathrm{Des}_i=e_b$）；
5. $c=1$ 的特征线多项式与每条线的非零 $\varphi$；
6. $c=0$ 的 $\det$ 首项。

## 做法

工具：[tools/verification/infeasibility_certificate.py](../../../../tools/verification/infeasibility_certificate.py)
```bash
python tools/verification/infeasibility_certificate.py 16 > workspace/feasibility_geometry/certificates/seed16.md
python tools/verification/infeasibility_certificate.py 21 > workspace/feasibility_geometry/certificates/seed21.md
```
输出为 markdown，所有数都是精确有理数（`Fraction`）。

## 结果（摘要）

### seed 16

- $K_0$ 基 $N$：$7\times4$（见证书）；
- $W_L$ 基（$K_0$ 坐标）：$(1,-1,1,0)$、$(1,0,0,1)$；
- $W_L\subseteq D$：$Aw_0=N(-1,2,1,2)$、$Aw_1=N(0,-1,-1,-1)$；
- $c=2$：两行的 $\mathrm{Des}$ 均为 $\begin{bmatrix}0&-1&0&0&0\\0&0&0&0&0\end{bmatrix}$，$\alpha=(-1,0)$，$\alpha^{\mathsf T}\mathrm{Des}=(0,1,0,0,0)=e_b$；
- $c=1$：$2a^2-2ab+b^2=0$，判别式 $-4$，两条复共轭特征线；$\mathbb Q(i)$ 上算得 $\varphi=(1,0)\ne0$（见 183）。

### seed 21

- $W_L$ 基：$(0,0,0,1)$、$(0,0,1,1)$；
- $W_L\subseteq D$：$w_0=(1,0,0,-1)$、$w_1=(0,0,0,-1)$；
- $c=2$：$\mathrm{Des}$ 同行，$\alpha=(-1,0)$；
- $c=1$：$a^2-ab=a(a-b)=0$，两条有理特征线：
  - $L_1=\mathbb Cw_1$：$\varphi=(1,0)\ne0$；
  - $L_2=\mathbb C(w_0+w_1)$：$\varphi=(0,-1)\ne0$。

## 进展

* 两个 seed 的证书已生成（精确有理）；
* $c=2$、$c=1$ 的数据与 165/183 一致；
* $c=0$ 的行列式论证是纸面一般结论（184），不需要实例数据。

## 最终结论

* 16/21 的全 $q$ 不可行性现在有**逐项数据**支撑；
* 证书包可直接附在论文附录或回信；
* $c=0$ 的一般论证（$\det P$ 次数 $k$、首项 $\det H\ne0$）已单独证明。

## 放弃原因

* 未把 $c=0$ 的样例 $\det H$ 写进证书（一般论证已足够）；
* 未把证书改成 Lean；
* 未覆盖 $W_L\not\subseteq D$ 的实例（本证书只针对这两个 seed）。

## 残留价值

* 一份可复现、精确的不可行证书；
* 工具可对任意 $(A,C,L_0)$ 生成同类证书。

## 相关文件

* [attempts/185](../../c_stratification/attempts/185_seeds_infeasible_all_q.md)（全 $q$ 结论）
* [attempts/182](../../c_stratification/attempts/182_c1_infeasibility_lemma.md)、[183](../../c_stratification/attempts/183_c1_eigenlines.md)（$c=1$）
* [attempts/184](../../c_stratification/attempts/184_q4_excluded.md)（$c=0$）
* [certificates/seed16.md](../../feasibility_geometry/certificates/seed16.md)、[seed21.md](../../feasibility_geometry/certificates/seed21.md)

## 状态

* 证书：**[精确验证（自动生成）]**。
* Lean/一般实例：**[未做]**。
