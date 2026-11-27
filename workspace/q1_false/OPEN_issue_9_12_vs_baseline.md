
> ## ✅ 已定案（同日晚）：**不是矛盾**
>
> 精确算出本实例 $j=\dim\mathcal J=2$、$\operatorname{rank}[\mathcal L;CA;C]=3$，故
> $$\rho=\operatorname{rank}[\mathcal L;CA;C]-j=1,$$
> 这是 $(\rho,c)=(1,1)$ 层，**不是** $(2,1)$ ⟹ **定理 9.12 不适用**，`cond_5b_orig` 也没错 ✓。
>
> **我的错误**：把"$\dim(\mathcal L\cap\mathcal J)=1$"当成 $\rho=2$，而没有算
> $\rho=\operatorname{rank}[\mathcal L;CA;C]-j$ ✗（纪律 14 的同类错误：先断言维数、不核算）。
>
> 教训入库：**层号 $\rho$ 必须由 $\operatorname{rank}[\mathcal L;CA;C]-j$ 算出**，不能用 $\dim\mathcal L$ 或 $\dim(\mathcal L\cap\mathcal J)$ 推 ✗。

# ~~待解决的矛盾~~（已定案：不是矛盾）：定理 9.12 与 `cond_5b_orig` 在一个实例上冲突

> 记录日期 2026-10-28。**尚未定案**，任何依赖 9.12 或 `cond_5b_orig` 的结论都应暂缓。

## 实例

$$A=\begin{pmatrix}0&1&1&1\\0&1&-1&-1\\1&-1&0&0\\1&-1&-1&0\end{pmatrix},\quad
C=(0,0,-1,0),\quad
\mathcal L=\begin{pmatrix}1&-1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}$$

## 两边各说什么

| 来源 | 计算 | 结论 |
|---|---|---|
| `AI.cond_5b_orig(A,C,L)` | $\operatorname{rank}[\mathcal L;CA;C]=3$，全部 3 阶子式的 gcd $=1$（18 个非零子式，gcd 次数 0）| $(5b)$ **成立** |
| 定理 9.12 的论证 | $\mathcal J=\operatorname{row}[C;CA]$（$\dim=1$）、$h=\mathcal L_1\in\mathcal J$ 且 $hA\in\mathcal J$（故 $w=\pi(hA)=0$）、$\rho=2,c=1$；把两行写在 $\mathcal U=\pi(\mathcal V)=\langle u_1,u_2\rangle$ 的坐标里得**首一二次** $\lambda^2-(a_1+b_2)\lambda+(a_1b_2-a_2b_1)=0$，在 $\mathbb C$ 上必有根 $\lambda_0$ ⟹ 两行在 $\lambda_0$ 处成比例 ⟹ $(5b)$ **失败** | $(5b)$ **失败** |

## 为什么必须解决

- 若 9.12 对 ⟹ `cond_5b_orig` 有 bug ⟹ 项目所有"可信基线"结论（含 625/625、1605/1605）都要重审 ✗；
- 若 `cond_5b_orig` 对 ⟹ **定理 9.12 被反驳** ⟹ $(2,1)$ 层的"完整判定"（9.10/9.12/10.1）需要重做 ✗；
- 两种后果都很严重，因此**必须先定案**，不能继续往上堆结论。

## 最可能的定位（待验证）

9.12 的论证默认"两行在 $\mathcal U$ 里成比例 ⟹ 商里的秩降"。但商秩是 $\operatorname{rank}[\lambda\mathcal L-\mathcal LA;CA;C]-j$，
而**成比例是在 $\mathcal U=\pi(\mathcal V)$ 内部**判定的；如果两行的 $\mathcal U$-坐标成比例，商秩确实 $\le1$ ✓ —— 这一步看起来没问题 ✗，
所以嫌疑落在：**(a)** $r_i=\pi(\ell_iA)\in\mathcal U$ 是否真的成立（依赖 $(5a)$ 的商形式 $T(\mathcal U)\subseteq\mathcal U$）；
**(b)** `_det_poly` / 子式 gcd 的实现；**(c)** 我对 $j$ 与 $\rho$ 的辨识（本实例 $\operatorname{rank}[\mathcal L;CA;C]=3$，若 $j=1$ 则 $\rho=2$ ✓；若 $j=2$ 则 $\rho=1$，那就**不是** $(2,1)$ 层，9.12 不适用）。

## 下一步（明确）

1. 精确算出本实例的 $j=\dim\mathcal J$（一行 `AI.rank`），确定层号；
2. 用独立实现（手写展式或用 `sympy`-free 的插值）重算 3 阶子式 gcd，与 `cond_5b_orig` 对拍；
3. 若 `cond_5b_orig` 有 bug，修它并重跑历史验证；若 9.12 错，按 `proof/refuted/` 规范处理。