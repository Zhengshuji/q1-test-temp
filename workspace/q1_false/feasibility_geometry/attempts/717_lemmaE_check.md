# 717 引理 E：小例检验与修正建议

> 2026-11-27。对 716 的引理 E 做数值检验，并指出其证明中“维数”的可修正版本。
> 状态：**[精确验证]**（小例）+ **[M2 提案]**。

## 检验

合成例：$k=3$、$d=2$、$q=3$、$T=\operatorname{span}\{e_1\}$（$a=1$），
$$X=\begin{bmatrix}1&0\\0&1\\0&0\end{bmatrix},\quad V=\begin{bmatrix}1&0&0\\0&1&0\end{bmatrix},\quad H=XV=\operatorname{diag}(1,1,0),$$
$Z'=0$、$G=\begin{bmatrix}1&0&0\\0&0&0\\0&0&0\end{bmatrix}$（行在 $T$）。解 $ZH=G$ 得 $Z$，取 $R=\begin{bmatrix}1&0&0\\0&1&0\end{bmatrix}$（$RX=I$）、$A=RZX$，计算
$$\operatorname{rank}(ZX-XA)=0\le a=1 .$$

## 修正建议

716 的证明有两处需要修正：

1. **商空间良定义**：$Z'$ 在 $\mathbb C^k/T$ 上的诱导作用需要 $(U\cap T)Z'\subseteq T$（716 已记录该陷阱）；
2. **左零空间维数**：$\overline V$ 行满秩 $d-a$（$d\times k$），故
   $$\dim\ker(\overline V^{\mathsf T})=k-d+a,$$
   不是 $a$。因此由 $(ZX-XA)\overline V=0$ 只能得到
   $$\operatorname{rank}(ZX-XA)\le k-d+a,$$
   这是一个**正确但更弱**的界；引理 E 想要的 $\le a$ 需要额外论证。

## 结论

- 把引理 E 的**可证版本**写成
  $$\boxed{\operatorname{rank}(ZX-XA)\le k-d+a}$$
  （在商空间良定义的假设下）；
- $\le a$ 的强形式仍是 **[M2 提案]**，需新证明或反例；
- 例中 $\operatorname{rank}=0$ 同时满足两个界，不能区分。

## 下一步

1. 寻找 $\operatorname{rank}(ZX-XA)>a$ 的反例（若存在，716 的强形式被推翻）；
2. 若找不到，尝试用 $X$ 的列结构（不只是 $\overline V$）改进维数论证；
3. 与 ChatGPT 核对 $k-d+a$ 的推导。

## 状态

- 小例检验：**[精确验证]**；
- 弱版本：**[已证-纸面]**（待商空间假设）；
- 强版本：**[M2 提案]**。
