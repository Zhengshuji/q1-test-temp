# C2 —— "$h<q+r_1$ 充分"被推翻（2026-11-02）

## 背景

[B.9](../left_index_count/README.md) 证明：$(5b)\Longrightarrow h<q+r_1$
（$r_1=\operatorname{rank}[C;CA]$、$h$ = 铅笔正规秩、$q$ = $\mathcal L$ 的行数）。
上一轮在 56 个闭包样本里，$h<q+r_1$ 的 40 个**全部**可行，于是提出：

**C2（猜想，已推翻）**：$h<q+r_1$ 也是 $(5b)$ 的**充分**条件。

## 反例

在 912 个 $(5a)$-可行的铅笔（56 个功能可观测实例 × 闭包/闭包$+1$/闭包$+2$，
每阶由 [omega_construct.sample_chains](../../tools/verification/omega_construct.py) 生成）中，
满足 $h<q+r_1$ 但 $(5b)$ **失败**的有 **415 个**。

最干净的一个：$n=5,p=1,r=1$（[qmin_scan_pr.make_instance](../../tools/verification/qmin_scan_pr.py)
的 seed 参数取 $3000\cdot17+1\cdot7+1=51008$），$q=4$：

| 量 | 值 |
|---|---|
| $h=\operatorname{rank}[\mathcal L;CA;C]$ | $5$ |
| $r_1=\operatorname{rank}[C;CA]$ | $2$ |
| $q+r_1$ | $6$ |
| 左指标 $\varepsilon$ | $[3]$（非零个数 $=q+r_1-h=1$ ✓ 与 B.9 的计数一致）|
| $\sum\varepsilon$ | $3$ |
| $s=\operatorname{rank}\mathcal L$ | $4$ |
| $d_{\rm fin}=s-\sum\varepsilon$ | $1>0$ ⟹ **$(5b)$ 失败** |

即：**非零左指标存在**（个数 $=1$），但它的**值太小**（$\sum\varepsilon=3<s=4$），所以仍有有限初等因子。

## 教训

B.9 的"非零左指标个数"只给出**计数**，而 $(5b)$（由 B.8）要求的是**和** $\sum\varepsilon=s$。
计数为 1 不等于和等于 $s$。B.9 仍是有效的**必要**条件，但**不能**当作判据。

## 幸存的问题

$(5b)$ 在固定 $\mathcal L$ 处的判据已经是 $d_{\rm fin}=0$（B.8）；真正要问的是：
**在 $q=\mathrm{cl}$（唯一候选）处，能否用比"算 Kronecker 数据"更便宜的量判断 $d_{\rm fin}=0$？**
目前只知道 $h\ge q+r_1$ 必失败；$h<q+r_1$ 时两种情形都可能（本文件的 415 个 vs 样本里的 40 个）。

## 证书

```bash
python -u tools/verification/closure_feasibility.py   # 交叉表
# 反例的直接复现（在 tools/verification 下的生成器 + omega_construct.sample_chains）
```

## 相关

- [B.9](../left_index_count/README.md)（必要条件）
- [C1](C1_closure_plus_one.md)（另一个被推翻的猜想）
