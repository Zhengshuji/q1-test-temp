# 分支 4（E-1）总结：文献 + adapted basis + A-1 前置

> 2026-11-01。任务：E-1「Smith/Hermite 标准形与 adapted basis（Wilkening–Yu、Forney、Zhou）」。
> **结论：可做部分已全部完成并机器验证；剩余项需要新资源或单独立项。**

---

## 1. 交付物清单

| # | 交付物 | 位置 | 状态 |
|---|---|---|---|
| 1 | 文献笔记（Smith/Hermite/Forney/Zhou/adapted basis）| [literature/notes/LIT_SMITH_HERMITE_2026-11-01.md](../../literature/notes/LIT_SMITH_HERMITE_2026-11-01.md) | ✅ |
| 2 | adapted basis 实现 + 验证 | `tools/verification/coeff_of_S.py`（`adapted_basis`）+ [scripts/verify_adapted_basis.py](scripts/verify_adapted_basis.py) | ✅ |
| 3 | **适用条件钉死** | [A2 §39–§40](../../../trash/README.md) | ✅ |
| 4 | **行列式恒等式**（$r=1,2,3$）| [A2 §41](../../../trash/README.md) + 三个 `verify_det_identity*.py` | ✅ |
| 5 | 给分支 1 的交接清单 | [CHECKLIST_A1.md](CHECKLIST_A1.md) | ✅ |
| 6 | **判据验证**（方阵 $r=1$，含 True 点）| `scripts/verify_criterion_square_r1.py`（trial60：24 个可容许、4 可行、**0 不一致**）| ✅ |

---

## 2. 最重要的四个结论

### (1) 适用条件：$q=t$

$$[U\mid P(\lambda)]\ \text{是}\ (w-s)\times(r+t);\qquad r+t=w-s\iff q=t .$$

- **不是** $r+t=\dim(H/S)=m$（这是之前误用的）；
- **不是** $q\le t$。

### (2) 判据的两种形态

| 情形 | 判据 |
|---|---|
| $q=t$（方阵）| $\det[U\mid P(\lambda)]$ 是非零常数 |
| $q\ne t$（非方阵）| **全部** $(r+t)$-子式的 gcd 是常数 |
| $r+t>w-s$ | 恒不可行 |

### (3) 行列式恒等式（A-1 核心）

$$\det[U\mid P(\lambda)]=\sum_j\lambda^j\Big(\sum_{|I|=r}s_I\,a_j[I]\,p_U[I]\Big),\qquad s_I=\pm1 .$$

$s_I$ 是**逐坐标**符号（由坐标子空间 $U=\operatorname{span}(e_I)$ 定出）；因 $s$ 可逆对角，
"$a_0\notin\operatorname{span}\{a_j\}$" 与符号约定无关 ✓

**机器验证**：

| $r$ | 实例 | 结果 |
|---|---|---|
| 1 | 第二实例 $q=2$、$q=3$ | **8/8**、**8/8** |
| 2 | R17 $q=2,s=2$ | **8/8** |
| 3 | $p=3$ 的两个随机实例 | **8/8**、**8/8** |

### (4) 结构观察：$r\le p$

$$r=d-s=w-q-s\le w-v\le p,\qquad w=n-p,\ v\ge n-2p .$$
故 $r=3$ 必须有 $p\ge3$；与 A2 §22 的 $r\le p-1$ 同源。
（**2026-11-01 更正**：原文"$r=w-v$"不是恒等式，c282 上 $r=1$ 而 $w-v=2$。）

---

## 3. 被证伪的（不要再犯）

| 做法 | 结果 |
|---|---|
| "只用 $P$ 的前 $m$ 行"（截断）| **0/6** ✗ |
| "换基是必需的" | 不需要（$s_I$ 自动吸收）|
| "符号是整体常数" | 是**逐坐标**的 |

---

## 4. 剩余项（本分支不继续的原因）

| 项 | 为什么不做 |
|---|---|
| $r\ge4$ | 需要 $p\ge4$ 的实例；项目现有实例都是 $p\le3$ |
| Lean 化（D-1）| 单独立项：需 Grassmannian/Plücker 形式化，工作量大 |
| Forney 原文、Zhou 论文 | 需要 PDF；当前结论不依赖它们 |
| Smith 形乘子（Wilkening–Yu）| 备用；判据已不需要多项式标架 |

---

## 5. 给分支 1 的三条硬性提醒

1. **先查 $q=t$**；不满足就切到"全部子式的 gcd"；
2. **不要截断、不要换基**；直接用完整的 $\det[U\mid P(\lambda)]$；
3. $a_0\notin\operatorname{span}\{a_j\}$ 只是**充分**条件（缺可分解性 = G3，QA25）——
   必须另外做 A-4（$D(K_S)$ vs $K_S$ 的维数比较）。

---

## 6. 一句话

> 分支 4 把 A-1 的**代数前置**做完了：恒等式成立（$r\le3$，机器验证）、适用条件钉死（$q=t$）、
> 错误做法被证伪。**剩下的瓶颈是可分解性（G3）与 Lean 化**，都不属于本分支的范围。
