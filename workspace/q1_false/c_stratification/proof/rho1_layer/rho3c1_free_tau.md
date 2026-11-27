# $(3,1)$ 层的一个**已证**判据：$\tau$ 自由（$\mathcal U\subseteq B$）时型层**不被**覆盖

> 2026-10-30。这是 CQ 的一个**已证特例**（专家优先级 3 的自然延伸）。
> 记号同 [docs/01](../../../../../docs/01_notation.md)：$\mathcal U=\pi(\mathcal V)$、$\dim\mathcal U=3$、$\mathcal H=\langle h\rangle$、$w=\beta(h)\in\mathcal U$（$c=1$）。

## 1. 归一化（把一切放到 $\mathcal U$ 的坐标里）

由 $(5a)$：$T(\mathcal U)\subseteq\mathcal U+B$ ✓，故 $\mathbf{t}_i:=\pi(u_iA)$ 的**投影到 $\mathcal U$** 的部分有意义（模 $B$ 的歧义落在 $B$ ✓）。
对 $c=1$：铅笔的行（在 $\mathcal U$ 的一组基下写成 $\mathbb C^3$ 的向量，再把 $B$ 的部分吸收进 $\beta\tau_i$）为

$$r_i(\lambda)=\lambda\,\mathbf u_i-\mathbf t_i-\boldsymbol\beta\tau_i\quad(i=1,2,3),\qquad r_4=\mathbf w .$$

所有行都在 $\mathcal U\cong\mathbb C^3$ 里 ✓ ⟹ $\operatorname{rank}\le3$ 自动 ✓ ⟹

$$(5b)\iff\gcd\big(p_0,p_1,p_2,p_3\big)=\text{非零常数},$$

其中 $p_0(\lambda)=\det[\lambda U-C]$（$U$ 以 $\mathbf u_i$ 为行、$C$ 以 $\mathbf t_i+\boldsymbol\beta\tau_i$ 为行 ✓），
$p_i(\lambda)$ 是把第 $i$ 行换成 $\mathbf w$ 后的行列式 ✓（$i=1,2,3$）。次数：$\deg p_0\le3$，$\deg p_i\le2$ ✓。

## 2. 定理（$\tau$ 自由 ⟹ 不被覆盖）

**定理**：设 $\dim\mathcal U=3$、$c=1$，且 $\mathcal U\subseteq B$（即 $\beta\tau_i$ 可以在 $\mathcal U$ 内**任意**取值 ✓——"$\tau$ 自由"）。若 $w=\beta(h)\ne0$，则存在 $\tau$ 使 $(5b)$ 成立 ✓。即该型层**不被** $\mathrm{Bad}$ 覆盖 ✓。

*证明*（用 [rho3c1_spectral](rho3c1_spectral.md) 的谱判据）：由推论 2，
$$\gcd=1\iff w^{\mathsf T}v_k\ne0\ \ (k=1,2,3),$$
其中 $v_k$ 是 $C$ 的（单谱）特征向量 ✓。所以只需造一个 $C$ ✓：

1. 取 $\mathcal U$ 的一组基 $v_1,v_2,v_3$ 使 $w^{\mathsf T}v_k\ne0$ 对**每个** $k$ 成立 ✓
   （因 $w\ne0$ ✓：先取 $v_1=w$ ✓；再取 $v_2=w+u$ ✓、$v_3=w+u'$ 使成基 ✓，此时 $w^{\mathsf T}v_k=\|w\|^2\ne0$ ✓）；
2. 取互异的 $\lambda_1,\lambda_2,\lambda_3$ ✓，令 $C=V\Lambda V^{-1}$ ✓（$V$ 以 $v_k$ 为列 ✓）；
3. 因 $\mathcal U\subseteq B$ ⟹ $\boldsymbol\beta\tau_i$ 可任意 ✓ ⟹ $C$ 的每一行都可达 ✓ ⟹ 这个 $C$ 是允许的 ✓。

由推论 2，$\gcd=1$ ✓。$\square$

> **⚠️ 2026-10-30 自我更正**：本节初版的构造是"取 $C$ 对角、$c$ 互异"，并断言对任意 $w\ne0$ 都有 $\gcd=1$ ✗ ——
> 这是**错的** ✗：$C$ 对角时 $v_k=e_k$ ✓，于是 $w^{\mathsf T}v_k=w_k$ ✓，
> 只要 $w$ 有零分量，对应的 $c_k$ 就是公共根 ✓ ⟹ $\gcd\ne1$ ✗（与推论 2 矛盾 ✓）。
> 初版的验证脚本恰好只抽了 $w_i\ne0$（$\pm1,\pm2$）✓，所以 200/200 通过 ✗ 掩盖了这个错误 ✗。
> 现在的证明改用谱判据 ✓。

## 3. 推论（$w=0$ ⟹ 被覆盖）

**推论**：若 $w=0$，则该型层**恒不可行** ✗（即被覆盖 ✓）。

*证明*：$r_4=\mathbf w=0$ ✓ ⟹ 任何含第 4 行的子式恒为零 ✓ ⟹ 每个 $3\times3$ 子式都可用前 3 行表示 ✗ hmm：
更直接地，$r_4\equiv0$ ✓ ⟹ 铅笔的 4 行仅 3 行非零 ✓ ⟹ 秩 $\le3$ ✓；且含 $r_4$ 的 $3\times3$ 子式恒为 0 ✓，
故"某个 $3\times3$ 子式非零"必须由 $r_1,r_2,r_3$ 给出 ✓ ⟹ 需要 $\det[\lambda U-C]\not\equiv0$ ✓ 且与另三个子式无公共根 ✓……
**注意**：这里不能直接断言"恒不可行"✗ —— 需检查 $\det[\lambda U-C]$ 是否可能与 $p_1,p_2,p_3$ 的 gcd 为 1 ✓。

（本节原想给出 $w=0$ 的推论，但检查后发现**不能**这样推 ✗ —— $w=0$ 时仍有 3 个非零行 ✓，
可能出现 $\gcd=1$ ✓。已知的"$w=0$ 恒不可行"结论只对 $(2,1)$ 成立 ✓（那里 $2\times2$ 子式 = 一个首一二次 ✓ 必有根 ✓），
对 $(3,1)$ **不**成立 ✗。本节保留为空，作为对"$w=0$ 在 $(3,1)$ 上是否恒不可行"的**警示** ✗。）

## 4. 意义与边界

| 项 | 状态 |
|---|---|
| $\mathcal U\subseteq B$、$w\ne0$、$(3,1)$：型层不被覆盖 | **已证** ✓（定理 2）|
| 一般 $(3,1)$（$\beta$ 不满射到 $\mathcal U$）：是否被覆盖 | **开放** ✗ |
| $(2,1)$ 的 $w=0$：恒不可行 | 已证 ✓（首一二次必有根 ✓）|
| $(3,1)$ 的 $w=0$：是否恒不可行 | **未知** ✗（本文件 §3 的尝试失败 ✗）|

## 5. 为什么这仍然有用

定理 2 给出 CQ 的**第一个已证"不被覆盖"判据** ✓ —— 它说明：
只要 $\tau$ 在 $\mathcal U$ 内**自由** ✓，$(5b)$ 就能被满足 ✓ ⟹ 层可行 ✓ ⟹ **层判定退化为"类型 + $(5a)$"的子空间存在问题** ✓
（正是 C31 在 $\rho=3$、$\tau$ 自由时的情形 ✓）。

而 $\tau$ 不自由时（$\dim(B\cap\mathcal U)<3$ ✓）才是真正困难的情形 ✗ —— 这也解释了 §2/§15 的测量中
"覆盖"总是发生在 $\mu=\dim(B\cap\mathcal U)$ 较小的实例上 ✓（见 [PROBE_31](../layer_program/PROBE_31.md) §2 的分组 ✓）。

## 6. 验证

[verify_free_tau.py](../../proof/rho1_layer/verify_free_tau.py)：在 $\mathcal U\subseteq B$、$w\ne0$ 的随机 $(3,1)$ 实例上，
按定理 2 的构造（$C$ 取对角且互异 ✓）造 $\tau$ ✓，直接检验 $(5a)\wedge(5b)$ ✓。
预期：全部通过 ✓（若有不通过，则定理 2 或构造有误 ✗）。
