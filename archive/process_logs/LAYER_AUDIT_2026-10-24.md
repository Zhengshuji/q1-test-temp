# 层公式审计：D33 的「1/70」到底是什么

> 2026-10-24 19:xx。执行上一轮计划里的「第 1 步」：把 D33 的紧性实验变成可复现的，并分类那个失败点。
> 结论：**失败点是数学必然，不是搜索深度；且它恰好发生在公式不受影响的那一层。**

---

## 0. 缺口：D33 没有脚本

`ATTACK_LOG` D33 写「70 个可达 $(\text{实例},\rho)$ 对，紧性 69/70」，但 `scripts/` 里
10-24 只有 `c164_trusted_baseline.py`、`c165_recheck.py` 两个文件，**没有产生这张表的脚本**。
所以那 1 个失败无法复核，D33 的「很可能是搜索深度不足」只是猜测。

新增两个脚本：

| 脚本 | 作用 |
|---|---|
| [`scripts/core/c166_layer_audit.py`](../scripts/core/c166_layer_audit.py) | 可复现审计：逐实例算 $q_{\min}$、$\rho^*$、每个可达 $\rho$ 的紧性；失败案例存 JSON |
| [`scripts/core/c167_probe_tightness.py`](../scripts/core/c167_probe_tightness.py) | 对单个小实例做**穷举**（$n{=}5$ 时 $q{=}2$ 只有 5 个自由坐标） |

方法要点（吸取项目纪律）：
- $(5b)$ 用精确子式 gcd；随机 $\lambda$ 只当**必要条件快速拒绝器**（真解必过所有 $\lambda$，不会误杀）。
- $L=[L_0;R]$ 用字面前缀；由行变换不变性，这等价于 $\operatorname{row}(L_0)\subseteq\operatorname{row}(L)$。
- 每个失败都记 trials 数，便于区分「搜索深度」与「真缺口」。

---

## 1. 第一个不紧点：`counterexample_refute_dimV1`

首跑（`--certs`）就复现出 D33 同型的现象：

```
counterexample_refute_dimV1  n=5 p=2 r=1 d=1 dimV=1 ρ0=0
  | q_min=1 ρ*=0 pred=1 ✓ | 不紧: ρ=[1]
```

即在 $\rho{=}1$ 层，$q$ 只搜到 3，而层下界 $\max(r,\rho+1)=2$。

### 1.1 穷举

$n{=}5$、$q{=}2$ 时 $R$ 只有 5 个坐标，`c167 --box 2` 穷举 $[-2,2]^5$：

```
q=2: 枚举 3125 个整数矩阵 -> 解 92 个, ρ 取值 [0]
```

外加 3000 次随机（$\pm2$）抽样：**83 个解，全部 $\rho=0$，$\rho=1$ 一个都没有**。

### 1.2 证明：$\rho{=}1$ 时 $q{=}2$ 不可能

记 $K=\ker[C;CA]$，$d=1$，$K=\langle\nu\rangle$，$L_0\nu=0$。

关键恒等式（对任意 $L$）：

$$(5b)\iff \ker\big((\lambda L-LA)\big|_K\big)=\ker(L|_K)\quad\forall\lambda .$$

*理由*：$\ker[\lambda L-LA;CA;C]=\{x\in K:(\lambda L-LA)x=0\}$，而 $V_0=\ker[L;CA;C]=\{x\in K:Lx=0\}$。

现在取 $q=2$、$\rho=\operatorname{rank}(LN)=1$（$d=1$ 故 $\rho\in\{0,1\}$）。此时 $\ker(L|_K)=0$，所以 $(5b)$ 等价于

$$(\lambda L-LA)\nu\neq0\quad\forall\lambda\iff L\nu,\ LA\nu\ \text{线性无关}.$$

但 $L=[L_0;R]$，逐块写出：

$$L\nu=\begin{pmatrix}L_0\nu\\ R\nu\end{pmatrix}=\begin{pmatrix}0\\ R\nu\end{pmatrix},\qquad
LA\nu=\begin{pmatrix}L_0A\nu\\ RA\nu\end{pmatrix}.$$

若 $L_0A\nu=0$，则 $LA\nu=(0,\,RA\nu)$，两个向量都落在 $\{0\}\times\mathbb R\subset\mathbb R^2$ 里，
**必然线性相关** $\Longrightarrow$ 存在 $\lambda$ 使 $(5b)$ 降秩。$\blacksquare$

### 1.3 为什么恰好是「无害」的

$L_0A\nu=0$ 还有另一个等价身份。由 $K^\perp=\operatorname{row}[C;CA]=:\mathcal J$：

$$L_0A\nu=0\iff L_0A\in\mathcal J\iff \operatorname{row}(L_0)A\subseteq \operatorname{row}(L_0)+\mathcal J
\iff (5a)\ \text{对}\ L_0\ \text{成立}.$$

而 $L_0N=0$（退化）时 $(5a)\Longrightarrow(5b)$ 自动成立
（因 $L_0\subseteq\mathcal J$，$(5a)$ 给 $L_0A\in\mathcal J$，于是 $\lambda L_0-L_0A\in\mathcal J$、
$[\lambda L_0-L_0A;CA;C]$ 的行空间就是 $\mathcal J$，秩恒为 $\dim\mathcal J$）。

$$\boxed{\ \text{所以：}\rho=1\ \text{层不紧}\iff L_0\ \text{本身就是解}\iff\rho^*=0.\ }$$

而 $\rho^*=0$ 时公式给 $q_{\min}=\max(r,1)=r$，恰由 $L_0$ 本身达到。

$$\boxed{\ \textbf{这个不紧点不是反例，而是公式在退化层的自洽性。}\ }$$

---

## 2. 对最终公式的意义

$$q_{\min}=\max(r,\rho^*+1)$$

- $\rho^*=0$ 层：**成立**（就是上面的论证；与 $L_0$ 是否是解完全锁定）。
- $\rho^*=\rho_0>0$ 层：24/24 验证，但没有独立证明。
- $\rho^*=\dim V$ 层：已证（构造）。
- **真正的风险**：$\rho^*>\rho_0$ 且该层不紧。目前没有任何证据，也没有反例。

---

## 3. 附带得到的干净重述

对任意解 $L$，令 $M=LN$（$q\times d$）、$N'=LR_0$、$A'$ 为 $A$ 在 $K$ 上的压缩。则

$$(5b)\iff \ker\big(\lambda M-MA'-N'\big)=\ker M\quad\forall\lambda .$$

**紧层 $q=\rho+1$ 的判据**（$d=1$ 时就是 §1.2）：

$$\forall\xi:\ M\xi\neq0\ \Longrightarrow\ N'\xi\notin\{M(\lambda\xi-A'\xi):\lambda\in\mathbb R\}.$$

这条把「层紧性」化成一个关于 $(M,N',A')$ 的线性代数条件，可能是证明
$q(\rho)=\max(r,\rho+1)$（当 $\rho$ 可达）的正确入口。

---

## 4. 复现

```bash
python scripts/core/c166_layer_audit.py --certs --trials 100
python scripts/core/c167_probe_tightness.py --inst refute --box 2 --qs 2
```

---

## 5. 批量审计结果

| 批次 | 可行实例 | 公式一致 | 逐层紧性 | 备注 |
|---|---|---|---|---|
| `--certs` | 6 | **5/5**（p2 未搜到解）| 7/8 | 唯一不紧 = refute 的 $\rho{=}1$（已证）|
| `--random 10 --seed 5` | 10 | **10/10** | **10/10** | 含 1 个 $d{=}0$、1 个 $\dim V{=}0$ |
| `--random 8 --seed 3` | 7 | **7/7** | **7/7** | 1 个不可行 |
| `--random 8 --seed 9` | 8 | **8/8** | **8/8** | 含 1 个 $d{=}0$ |

$$\boxed{\ \text{30 个可行实例：公式 30/30；可达 (实例,}\rho\text{) 对 32/33 紧（唯一不紧已证）}}$$

分布观察（与 D34/D35 一致）：这批实例里 $\rho^*=\dim V$ 占绝大多数，$\rho^*=\rho_0$ 出现 2 次，
**没有出现 $\rho_0<\rho^*<\dim V$ 的中间层** —— 那类实例随机撞不到，只能靠定向构造。

### 5.1 一个被排除的假象

首轮（代码未修）时 `rand_s5_8` 曾报「$\rho{=}\dim V$ 不紧、$q_{\min}$ 搜不到」，看似反例。
但 $\rho=\dim V$ 层有已证构造保证 $q\le\dim V+1$，矛盾说明是**搜索深度**。把关键层的 trials ×4 后，
该实例变成 $q_{\min}=4=\dim V+1$、$\rho^*=3$，完全正常。

$$\text{教训（与纪律 8–12 同类）：搜不到 }\ne\text{ 不存在；任何"反例"先与已证上界对照。}$$

## 6. 现在的结论与剩余风险

| 层 | 状态 |
|---|---|
| $\rho^*=0$ | ✅ 成立（§1.3 的等价论证）|
| $\rho^*=\rho_0>0$ | 🟡 24/24 + 本次审计，无独立证明 |
| $\rho^*=\dim V$ | ✅ 已证（构造）|
| $\rho_0<\rho^*<\dim V$ | ❌ 稀有，未审计到；紧性未知 |

**真正的风险只剩一个**：$\rho^*$ 严格落在中间时，$q(\rho^*)=\rho^*+1$ 是否成立。
这需要定向构造中间层实例（随机撞不到），或用 §3 的判据证明。

## 7. 下一步（具体）

1. 用 `certificate_middle_layer` / `certificate_rhostar_lt_dimV` 作种子，做**参数化变形**，
   看能否造出 $\rho_0<\rho^*<\dim V$ 且该层不紧的实例（若有 $\Rightarrow$ 公式被推翻）。
2. 从 §3 的判据出发：证明 $\rho$ 可达 $\Rightarrow$ 存在紧解，或找出反例。
3. 若都失败，可考虑把「层紧性」作为一个独立引理写进论文（它已是干净陈述）。
