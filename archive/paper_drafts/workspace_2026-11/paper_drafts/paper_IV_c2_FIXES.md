# Paper IV：作者答复（页数决定 + 六处矛盾的精确修补）

> 针对 `paper/current/paper_IV_c2.tex`（7 页，0/0/0/0）的转换反馈。
> 每处给 **old → new 的 LaTeX 片段**，可直接替换；编号前缀 `F1…F9` 便于回话。

## 一、页数：**接受 7 页，按 IEEE TAC Technical Note 投**

理由：

1. 内容自洽：结构（层参数 → 两种纤维 → 像约化 → 底 → 算法 → 复杂度）在 7 页内是完整的，没有半截定理。
2. 缺的那 4–5 页材料（十类测试集、带常数的高度链、worked example）**正是专家要求"在宣称完整之前必须补"的东西**——
   在它们没做出来之前扩页，只能靠加叙述，那是灌水；把它们真做出来再扩，才是完整论文。
3. TAC Technical Note 的上限是 8 页，7 页正好；先占位发表，扩版作为后续投稿（含测试集与常数）。

**不要**换单栏凑页数：单栏 13–15 页会让审稿人以为是完整论文，从而按完整论文的标准要求那 4–5 页材料。

**扩版需要我先补的三块**（我可以写，但要按顺序）：

| 块 | 内容 | 估计页数 |
|---|---|---|
| (a) 十类精确测试集 | 每类一条实例 + 期望结论 + 证书格式（规格见 attempts/415） | 2–3 |
| (b) 高度链的显式常数 | Appendix A 每一步给界（Kronecker、Mahler、Cramer、subresultant） | 1–2 |
| (c) 一个完整 worked example | $n=8,k=4$：从 $A,C$ 到 $D$、$\Phi$、gcd、结论 | 1 |

## 二、六处矛盾的裁决与修补

### #1 $\dim D^\circ$：**是 $\omega$，不是 $c$**（影响摘要与贡献 3）

正确事实（卷宗 [416](../augmentation_family/attempts/416_dim_dual_annihilator_fix.md)）：
$$\dim D^\circ=k-\dim D=k-c=\omega .$$
**正文已正确**（Theorem 6 第 3 项、Remark 9 都写对了）；错在**摘要**与**贡献 3**还留着旧措辞。
真正小的是**像**：$\Phi(W)\subseteq\varphi(T_D)$，$\dim\varphi(T_D)\le n-k\le 2p$。

**F1（摘要）** 把
```latex
$\Phi(W)\subseteq D^\circ$, a subspace of $D^\circ$ of dimension at most $c=2$. Consequently the search
over a Grassmannian of arbitrary dimension collapses to a search over subspaces of the image
$\varphi(T_D)$, whose dimension is at most the codimension of $K_0$ (hence at most $2p$).
```
改为
```latex
$\Phi(W)\subseteq D^\circ$; the pencil's whole row space lies in $D^\circ$, of dimension $\omega$, but
$\Phi(W)$ itself lies in the image $\varphi(T_D)$, whose dimension is at most $n-k$ (at most twice the
number of output rows). Consequently the search over a Grassmannian of arbitrary dimension collapses to
a search over subspaces of $\varphi(T_D)$.
```
（要点：**别再说 $D^\circ$ 的维数是 $c$**；$D^\circ$ 是 $\omega$ 维，只有 $\varphi(T_D)$ 小。）

**F2（贡献 3）**
```latex
space of its $D$-part plus $\Phi(W)\subseteq D^\circ$, so the fibre acts only through a subspace of a
$c$-dimensional space.
```
改为
```latex
space of its $D$-part plus $\Phi(W)\subseteq D^\circ$; since the whole pencil lies in $D^\circ$ (of
dimension $\omega$) while $\Phi(W)$ lies in $\varphi(T_D)$ (of dimension at most $n-k$), the fibre acts
only through a subspace of the low-dimensional image $\varphi(T_D)$.
```

### #2 $P_D$ 在 Theorem 6 里就用了，但到 Theorem 8 才定义

**F3** 在 §IV-A 的 "For $w\in K_0^\perp$ define..." 之前加一句：
```latex
Write $H_K,(H_A)_K$ for the rows carried by $D^{\perp_{K_0}}$, and put
$P_D(\lambda):=\lambda H_K-(H_A)_K$, $R_\lambda:=\row P_D(\lambda)$.
```
然后把 Theorem 8 里的 `Write $P_D(\lambda)=\lambda H_K-(H_A)_K$ and ...` 改成
`Recall $P_D(\lambda)=\lambda H_K-(H_A)_K$ and $r_D(\lambda)=\dim R_\lambda$;`。
Theorem 6 第 4 项里的 `where $R_\lambda:=\row P_D(\lambda)$` 可删（已在前文定义）。

### #3 $\mathcal I_c(M)$ 从未定义（影响 Theorem 5 与命题 17 的陈述）

**F4** 在 §II-B（split 假设）里，Definition 之后加：
```latex
For $c\ge0$ put $\mathcal I_c(M):=\{D\le K_0:\ \dim D=c,\ M(D)\subseteq D\}$; in the case $c=2$ we write
$\mathcal I_2(M)=\mathcal I_c(M)$.
```
§V 里那句 "Write $\mathcal I_2(M)=\{D\in\Gr(2,K_0):M(D)\subseteq D\}$" 改成
"Write $\mathcal I_2(M)$ for $\mathcal I_c(M)$ with $c=2$ (Section~\ref{sec:layers})"。

### #4 $p$ 在摘要里先用后定义

**F5（摘要）** 把 `(hence at most $2p$)` 改成 `(at most twice the number of output rows)`（见 F1 已含）；
§I Notation 里的 `$p$ is the number of output rows` 保留即可（位置已合适）。

### #5 "见 Section II" 的交叉引用

你已改指 §VI-A 与 [9]——**正确，无需再动**。

### #6 §VI 里"Definition 2 的三种类型"

你已改成"Definition 2 的某个图卡"——**正确**。但**同一段上游的 Claim 9 还留着旧措辞**，见 F6。

**F6（Claim 9，可容许性）** 现文
```latex
In particular, on a chart parameterising an image line, $H$ does not depend on the parameter and every
real point of the chart is admissible.
```
改为（更强的正确陈述：对**任何** $j$ 的图卡都成立）
```latex
In particular $H$ is independent of all chart parameters, so the $\lambda$-leading coefficient of a
suitable maximal minor is a non-zero constant and every real point of every chart is admissible.
```
证明末句相应改为
```latex
On any chart of $\Gr(j,V_\varphi)$ the rows of $H$ are parameter-free, and the $\lambda$-leading
coefficient of the maximal minor built on those $\omega$ rows is a non-zero constant.
```

## 三、两处笔误（确认是笔误，请一并改）

**F7** $H=LN$, $H_A=LAN$ → **$H=\mathcal L N$, $H_A=\mathcal L AN$**（摘要与 §I Setting 各一处；
因为 $\mathcal L=[L_0;R]$ 才是设计矩阵，$L$ 在文中另有含义）。

**F8** §I Notation 里 `$D^\circ\subseteq K_0^*$ is the annihilator of $D$` 加一句维数备查：
`(so $\dim D^\circ=k-\dim D=\omega$)`。这与 F1 呼应，防止再被误读成 $c$。

## 四、我建议你去核的三处（不需要改，只要确认）

1. **Theorem 14（位复杂度）的 (iv) "$p$ fixed"**：这是修正版的关键假设，别在排版时被优化掉；
2. **Claim 12（度数）的 `$\deg_{\text{param}}\le j\le\min(t,2p)$`**：只在 $j$ 行随参数变时成立，
   若把 $j$ 换成 $1$ 就退化成旧版（旧版只在 $\dim\varphi(T_D)\le2$ 时对）；
3. **§V 的 Remark 6（"what is *not* claimed"）**：一般谱不宣称有理参数化，这条不能删。

## 五、改完之后的预期

- 摘要、贡献 3/4/5、Claim 9、$H$ 记号与 $\mathcal I_c$ 定义统一到 $\dim D^\circ=\omega$ / 参数受 $2p$ 控制这个版本；
- 页数仍应 ≈7（F1–F8 都是等长替换或 +1 行）；
- 若改完出现 1–2 行 overfull，优先压 F1/F2 的从句，不要动定理陈述。
