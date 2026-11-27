# 668 Bézout 秩判据的数值验证

> 2026-11-27。用 [668_bezout_rank.py](668_bezout_rank.py) 验证 667 的判据
> $(5b)\iff\operatorname{rank}[M(H)\mid e_0]=\operatorname{rank}M(H)$。
> 状态：**[精确验证]**。

## 结果

| 实例 | $d$ | 子式数 $m$ | $\operatorname{rank}M$ | $\operatorname{rank}[M\mid e_0]$ | 可解 | 已知 |
|---|---|---|---|---|---|---|
| 638 | 2 | 3 | 4 | 4 | **是** | 可行 ✓ |
| 641B | 2 | 4 | 2 | 3 | **否** | 不可行 ✓ |

（$M$ 的规模为 $2d\times md$：638 为 $4\times6$，641B 为 $4\times8$。）

## 说明

- 对 638：$d=2$，$H=\operatorname{diag}(1,1,0)$、$Z$ 循环；2-子式为 $\lambda^2,-\lambda,1$，gcd=1 ⇒ Bézout 可解；
- 对 641B：gcd $=\lambda(\lambda-1)$ ⇒ 不可解；
- 判据与直接 gcd 计算一致。

## 意义

- 667 的“统一 Bézout 系统”不依赖 $d$ 的具体值，可直接编码；
- 下一步应研究 $M(H)$ 的结构（尤其在 $d=2$ 时 $M$ 为 $4\times md$），看秩条件能否化为更简单的线性代数/结式条件，而不是逐 $d$ 分类。

## 状态

- 验证：**[精确验证]**；
- $M$ 的结构化简：**[未做]**。
